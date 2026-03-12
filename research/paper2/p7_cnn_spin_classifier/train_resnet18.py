#!/usr/bin/env python
"""
BigBounce P7 — Train ResNet-18 for galaxy spin (CW/CCW) classification.

Uses parity augmentation: with probability 0.5, mirror the image AND flip the
label (CW <-> CCW). This teaches the network that mirror images have opposite
handedness, which is the physically correct equivariance.

Usage:
    python train_resnet18.py --data_dir data/ --output_dir runs/dev/ --epochs 30 --seed 42
"""

from __future__ import print_function, division

import argparse
import json
import logging
import os
import sys
import time
import warnings

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torchvision import models, transforms
from PIL import Image
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay,
)

warnings.filterwarnings("ignore")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("train")

# Try importing sklearn; provide fallback if not available
try:
    from sklearn.metrics import confusion_matrix, classification_report
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False
    logger.warning("scikit-learn not found. Confusion matrix will be basic.")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Train ResNet-18 for galaxy spin classification"
    )
    parser.add_argument("--data_dir", type=str, default="data/",
                        help="Path to dataset directory (with catalog.csv and images/)")
    parser.add_argument("--output_dir", type=str, default="runs/dev/",
                        help="Output directory for model and results")
    parser.add_argument("--epochs", type=int, default=30,
                        help="Number of training epochs (default: 30)")
    parser.add_argument("--batch_size", type=int, default=64,
                        help="Batch size (default: 64)")
    parser.add_argument("--lr", type=float, default=1e-4,
                        help="Learning rate (default: 1e-4)")
    parser.add_argument("--label_smoothing", type=float, default=0.1,
                        help="Label smoothing factor (default: 0.1)")
    parser.add_argument("--parity_aug", action="store_true", default=True,
                        help="Enable parity augmentation (default: True)")
    parser.add_argument("--no_parity_aug", action="store_true", default=False,
                        help="Disable parity augmentation")
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed (default: 42)")
    parser.add_argument("--num_workers", type=int, default=2,
                        help="DataLoader workers (default: 2)")
    parser.add_argument("--weight_decay", type=float, default=1e-4,
                        help="Weight decay for AdamW (default: 1e-4)")
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------------

LABEL_TO_IDX = {"cw": 0, "ccw": 1}
IDX_TO_LABEL = {0: "cw", 1: "ccw"}


class GalaxySpinDataset(Dataset):
    """Dataset for galaxy spin classification with optional parity augmentation."""

    def __init__(self, catalog_df, data_dir, transform=None, parity_aug=False):
        """
        Args:
            catalog_df: DataFrame with columns [objid, ra, dec, label, split, ...]
            data_dir: root data directory containing images/{cw,ccw}/
            transform: torchvision transforms to apply
            parity_aug: if True, with p=0.5 mirror image and flip label
        """
        self.catalog = catalog_df.reset_index(drop=True)
        self.data_dir = data_dir
        self.transform = transform
        self.parity_aug = parity_aug

    def __len__(self):
        return len(self.catalog)

    def __getitem__(self, idx):
        row = self.catalog.iloc[idx]
        objid = str(row["objid"])
        label_str = row["label"]
        label_idx = LABEL_TO_IDX[label_str]

        # Load image
        img_path = os.path.join(
            self.data_dir, "images", label_str, "{}.jpg".format(objid)
        )
        try:
            img = Image.open(img_path).convert("RGB")
        except Exception as e:
            # Return a black image on error
            logger.warning("Failed to load %s: %s", img_path, str(e))
            img = Image.new("RGB", (128, 128), (0, 0, 0))

        # Parity augmentation: mirror image AND flip label
        if self.parity_aug and np.random.random() < 0.5:
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
            label_idx = 1 - label_idx  # CW(0) <-> CCW(1)

        if self.transform:
            img = self.transform(img)

        return img, label_idx


def get_transforms(split, img_size=128):
    """Get data transforms for train/val/test splits."""
    if split == "train":
        return transforms.Compose([
            transforms.Resize(144),
            transforms.RandomCrop(img_size),
            transforms.RandomHorizontalFlip(p=0.5),
            transforms.RandomRotation(15),
            transforms.ColorJitter(brightness=0.2, contrast=0.2),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225],
            ),
        ])
    else:
        return transforms.Compose([
            transforms.Resize(img_size),
            transforms.CenterCrop(img_size),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225],
            ),
        ])


# ---------------------------------------------------------------------------
# Model
# ---------------------------------------------------------------------------

def build_model(num_classes=2, pretrained=True):
    """Build ResNet-18 with modified final FC layer."""
    model = models.resnet18(
        weights=models.ResNet18_Weights.DEFAULT if pretrained else None
    )
    num_features = model.fc.in_features
    model.fc = nn.Linear(num_features, num_classes)
    return model


# ---------------------------------------------------------------------------
# Training loop
# ---------------------------------------------------------------------------

def train_one_epoch(model, loader, criterion, optimizer, device):
    """Train for one epoch, return average loss and accuracy."""
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    for images, labels in loader:
        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * images.size(0)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    avg_loss = running_loss / total
    accuracy = correct / total
    return avg_loss, accuracy


def evaluate(model, loader, criterion, device):
    """Evaluate on a dataset, return average loss, accuracy, all predictions."""
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0
    all_preds = []
    all_labels = []
    all_probs = []

    with torch.no_grad():
        for images, labels in loader:
            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)
            loss = criterion(outputs, labels)

            running_loss += loss.item() * images.size(0)
            probs = torch.softmax(outputs, dim=1)
            _, predicted = torch.max(outputs, 1)

            total += labels.size(0)
            correct += (predicted == labels).sum().item()

            all_preds.extend(predicted.cpu().numpy().tolist())
            all_labels.extend(labels.cpu().numpy().tolist())
            all_probs.extend(probs.cpu().numpy().tolist())

    avg_loss = running_loss / total
    accuracy = correct / total
    return avg_loss, accuracy, all_preds, all_labels, all_probs


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------

def plot_training_curves(history, output_dir):
    """Plot training and validation loss/accuracy curves."""
    epochs = range(1, len(history["train_loss"]) + 1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(epochs, history["train_loss"], "b-", label="Train")
    ax1.plot(epochs, history["val_loss"], "r-", label="Val")
    ax1.set_xlabel("Epoch")
    ax1.set_ylabel("Loss")
    ax1.set_title("Loss Curves")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(epochs, history["train_acc"], "b-", label="Train")
    ax2.plot(epochs, history["val_acc"], "r-", label="Val")
    ax2.set_xlabel("Epoch")
    ax2.set_ylabel("Accuracy")
    ax2.set_title("Accuracy Curves")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    path = os.path.join(output_dir, "training_curves.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Training curves saved to %s", path)


def plot_confusion_matrix(y_true, y_pred, output_dir):
    """Plot and save confusion matrix."""
    labels = ["CW", "CCW"]

    if HAS_SKLEARN:
        cm = confusion_matrix(y_true, y_pred)
        fig, ax = plt.subplots(figsize=(6, 5))
        disp = ConfusionMatrixDisplay(cm, display_labels=labels)
        disp.plot(ax=ax, cmap="Blues", colorbar=True)
        ax.set_title("Galaxy Spin Classification — Confusion Matrix")
    else:
        # Manual confusion matrix
        cm = np.zeros((2, 2), dtype=int)
        for t, p in zip(y_true, y_pred):
            cm[t][p] += 1
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.imshow(cm, cmap="Blues")
        for i in range(2):
            for j in range(2):
                ax.text(j, i, str(cm[i][j]), ha="center", va="center", fontsize=16)
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
        ax.set_xticklabels(labels)
        ax.set_yticklabels(labels)
        ax.set_xlabel("Predicted")
        ax.set_ylabel("True")
        ax.set_title("Confusion Matrix")

    path = os.path.join(output_dir, "confusion_matrix.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Confusion matrix saved to %s", path)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = parse_args()

    # Handle parity aug flags
    use_parity = args.parity_aug and not args.no_parity_aug

    # Set seeds
    torch.manual_seed(args.seed)
    np.random.seed(args.seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(args.seed)

    os.makedirs(args.output_dir, exist_ok=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logger.info("=" * 60)
    logger.info("BigBounce P7 — ResNet-18 Galaxy Spin Classifier")
    logger.info("Device: %s", device)
    logger.info("Data dir: %s", args.data_dir)
    logger.info("Output dir: %s", args.output_dir)
    logger.info("Epochs: %d", args.epochs)
    logger.info("Batch size: %d", args.batch_size)
    logger.info("Learning rate: %g", args.lr)
    logger.info("Label smoothing: %g", args.label_smoothing)
    logger.info("Parity augmentation: %s", use_parity)
    logger.info("Seed: %d", args.seed)
    logger.info("=" * 60)

    # Load catalog
    catalog_path = os.path.join(args.data_dir, "catalog.csv")
    if not os.path.exists(catalog_path):
        logger.error("Catalog not found at %s. Run dataset_build_sdss_gz.py first.", catalog_path)
        sys.exit(1)

    catalog = pd.read_csv(catalog_path)
    logger.info("Loaded catalog: %d galaxies", len(catalog))

    # Split datasets
    train_df = catalog[catalog["split"] == "train"]
    val_df = catalog[catalog["split"] == "val"]
    test_df = catalog[catalog["split"] == "test"]

    logger.info("Train: %d, Val: %d, Test: %d", len(train_df), len(val_df), len(test_df))

    # Create datasets
    train_dataset = GalaxySpinDataset(
        train_df, args.data_dir,
        transform=get_transforms("train"),
        parity_aug=use_parity,
    )
    val_dataset = GalaxySpinDataset(
        val_df, args.data_dir,
        transform=get_transforms("val"),
        parity_aug=False,
    )
    test_dataset = GalaxySpinDataset(
        test_df, args.data_dir,
        transform=get_transforms("test"),
        parity_aug=False,
    )

    # Create data loaders
    train_loader = DataLoader(
        train_dataset, batch_size=args.batch_size, shuffle=True,
        num_workers=args.num_workers, pin_memory=True,
    )
    val_loader = DataLoader(
        val_dataset, batch_size=args.batch_size, shuffle=False,
        num_workers=args.num_workers, pin_memory=True,
    )
    test_loader = DataLoader(
        test_dataset, batch_size=args.batch_size, shuffle=False,
        num_workers=args.num_workers, pin_memory=True,
    )

    # Build model
    model = build_model(num_classes=2, pretrained=True)
    model = model.to(device)
    logger.info("Model: ResNet-18 (pretrained ImageNet, FC -> 2 classes)")

    # Loss, optimizer, scheduler
    criterion = nn.CrossEntropyLoss(label_smoothing=args.label_smoothing)
    optimizer = optim.AdamW(
        model.parameters(), lr=args.lr, weight_decay=args.weight_decay
    )
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)

    # Training loop
    history = {
        "train_loss": [],
        "train_acc": [],
        "val_loss": [],
        "val_acc": [],
    }
    best_val_acc = 0.0
    best_epoch = 0

    logger.info("Starting training...")
    t_start = time.time()

    for epoch in range(1, args.epochs + 1):
        t_epoch = time.time()

        train_loss, train_acc = train_one_epoch(
            model, train_loader, criterion, optimizer, device
        )
        val_loss, val_acc, _, _, _ = evaluate(
            model, val_loader, criterion, device
        )
        scheduler.step()

        history["train_loss"].append(train_loss)
        history["train_acc"].append(train_acc)
        history["val_loss"].append(val_loss)
        history["val_acc"].append(val_acc)

        elapsed = time.time() - t_epoch
        lr_current = optimizer.param_groups[0]["lr"]

        logger.info(
            "Epoch %d/%d — train_loss=%.4f train_acc=%.4f "
            "val_loss=%.4f val_acc=%.4f lr=%.6f (%.1fs)",
            epoch, args.epochs, train_loss, train_acc,
            val_loss, val_acc, lr_current, elapsed,
        )

        # Save best model
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            best_epoch = epoch
            model_path = os.path.join(args.output_dir, "model.pt")
            torch.save({
                "epoch": epoch,
                "model_state_dict": model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
                "val_acc": val_acc,
                "val_loss": val_loss,
            }, model_path)
            logger.info("  -> New best model saved (val_acc=%.4f)", val_acc)

    total_time = time.time() - t_start
    logger.info("Training complete in %.1f seconds", total_time)
    logger.info("Best val accuracy: %.4f at epoch %d", best_val_acc, best_epoch)

    # Load best model for final evaluation
    checkpoint = torch.load(
        os.path.join(args.output_dir, "model.pt"),
        map_location=device,
        weights_only=False,
    )
    model.load_state_dict(checkpoint["model_state_dict"])

    # Evaluate on test set
    test_loss, test_acc, test_preds, test_labels, test_probs = evaluate(
        model, test_loader, criterion, device
    )
    logger.info("Test accuracy: %.4f", test_acc)
    logger.info("Test loss: %.4f", test_loss)

    # Classification report
    if HAS_SKLEARN:
        report = classification_report(
            test_labels, test_preds,
            target_names=["CW", "CCW"],
        )
        logger.info("Classification Report:\n%s", report)
        report_path = os.path.join(args.output_dir, "classification_report.txt")
        with open(report_path, "w") as f:
            f.write("BigBounce P7 — Galaxy Spin Classification Report\n")
            f.write("=" * 50 + "\n\n")
            f.write("Test accuracy: %.4f\n" % test_acc)
            f.write("Test loss: %.4f\n\n" % test_loss)
            f.write(report)
            f.write("\n")
        logger.info("Classification report saved to %s", report_path)

    # Confusion matrix plot
    plot_confusion_matrix(test_labels, test_preds, args.output_dir)

    # Training curves plot
    plot_training_curves(history, args.output_dir)

    # Save training curves as JSON
    curves_path = os.path.join(args.output_dir, "training_curves.json")
    with open(curves_path, "w") as f:
        json.dump(history, f, indent=2)
    logger.info("Training curves saved to %s", curves_path)

    # Save hyperparameters
    hyperparams = {
        "model": "resnet18",
        "pretrained": True,
        "num_classes": 2,
        "epochs": args.epochs,
        "batch_size": args.batch_size,
        "lr": args.lr,
        "weight_decay": args.weight_decay,
        "label_smoothing": args.label_smoothing,
        "parity_aug": use_parity,
        "seed": args.seed,
        "optimizer": "AdamW",
        "scheduler": "CosineAnnealingLR",
        "img_size": 128,
        "device": str(device),
        "best_epoch": best_epoch,
        "best_val_acc": best_val_acc,
        "test_acc": test_acc,
        "test_loss": test_loss,
        "total_train_time_sec": total_time,
        "n_train": len(train_df),
        "n_val": len(val_df),
        "n_test": len(test_df),
    }
    hyper_path = os.path.join(args.output_dir, "hyperparams.json")
    with open(hyper_path, "w") as f:
        json.dump(hyperparams, f, indent=2)
    logger.info("Hyperparameters saved to %s", hyper_path)

    # Save test predictions for downstream use
    test_results = []
    test_df_reset = test_df.reset_index(drop=True)
    for i in range(len(test_preds)):
        row = test_df_reset.iloc[i]
        test_results.append({
            "objid": str(row["objid"]),
            "ra": float(row["ra"]),
            "dec": float(row["dec"]),
            "true_label": IDX_TO_LABEL[test_labels[i]],
            "pred_label": IDX_TO_LABEL[test_preds[i]],
            "prob_cw": float(test_probs[i][0]),
            "prob_ccw": float(test_probs[i][1]),
        })
    test_results_path = os.path.join(args.output_dir, "test_predictions.json")
    with open(test_results_path, "w") as f:
        json.dump(test_results, f, indent=2)
    logger.info("Test predictions saved to %s", test_results_path)

    logger.info("=" * 60)
    logger.info("All outputs saved to %s", args.output_dir)
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
