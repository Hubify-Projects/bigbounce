#!/usr/bin/env python
"""
BigBounce P7 — Mandatory Bias Audits for Galaxy Spin Classifier.

Four tests:
  1. Mirror Test: flip each test image L-R; model should predict opposite class (>90% flip rate)
  2. Rotation Test: rotate 180 deg; prediction should NOT change (<20% flip rate)
  3. PSF Proxy Test: correlate predicted CW fraction with seeing/PSF if available
  4. Balanced Null Test: elliptical galaxies should give ~50/50 CW/CCW (no bias)

Usage:
    python eval_bias_audits.py \\
        --model_path runs/dev/model.pt \\
        --data_dir data/ \\
        --output_dir runs/dev/audits/
"""

from __future__ import print_function, division

import argparse
import json
import logging
import os
import sys
import warnings

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
from scipy import stats as scipy_stats

warnings.filterwarnings("ignore")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("bias_audit")

LABEL_TO_IDX = {"cw": 0, "ccw": 1}
IDX_TO_LABEL = {0: "cw", 1: "ccw"}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run bias audits on trained galaxy spin classifier"
    )
    parser.add_argument("--model_path", type=str, required=True,
                        help="Path to trained model checkpoint (model.pt)")
    parser.add_argument("--data_dir", type=str, default="data/",
                        help="Path to dataset directory")
    parser.add_argument("--output_dir", type=str, default="runs/dev/audits/",
                        help="Output directory for audit results")
    parser.add_argument("--batch_size", type=int, default=64,
                        help="Batch size for inference")
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Model loading
# ---------------------------------------------------------------------------

def load_model(model_path, device):
    """Load trained ResNet-18 model."""
    model = models.resnet18(weights=None)
    model.fc = nn.Linear(model.fc.in_features, 2)

    checkpoint = torch.load(model_path, map_location=device, weights_only=False)
    if "model_state_dict" in checkpoint:
        model.load_state_dict(checkpoint["model_state_dict"])
    else:
        model.load_state_dict(checkpoint)

    model = model.to(device)
    model.eval()
    return model


def get_eval_transform(img_size=128):
    """Standard evaluation transform."""
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
# Inference helpers
# ---------------------------------------------------------------------------

def predict_single_image(model, img, transform, device):
    """
    Run inference on a single PIL image.
    Returns (predicted_class_idx, prob_cw, prob_ccw).
    """
    tensor = transform(img).unsqueeze(0).to(device)
    with torch.no_grad():
        output = model(tensor)
        probs = torch.softmax(output, dim=1).cpu().numpy()[0]
    pred_idx = int(np.argmax(probs))
    return pred_idx, float(probs[0]), float(probs[1])


def load_test_images(catalog, data_dir):
    """Load test split images and their labels."""
    test_df = catalog[catalog["split"] == "test"].reset_index(drop=True)
    images = []
    labels = []
    objids = []
    ras = []
    decs = []
    skipped = 0

    for _, row in test_df.iterrows():
        objid = str(row["objid"])
        label = row["label"]
        img_path = os.path.join(data_dir, "images", label, "{}.jpg".format(objid))

        if not os.path.exists(img_path):
            skipped += 1
            continue

        try:
            img = Image.open(img_path).convert("RGB")
            images.append(img)
            labels.append(LABEL_TO_IDX[label])
            objids.append(objid)
            ras.append(float(row["ra"]))
            decs.append(float(row["dec"]))
        except Exception as e:
            logger.warning("Failed to load %s: %s", img_path, str(e))
            skipped += 1

    if skipped > 0:
        logger.warning("Skipped %d test images (missing/corrupt)", skipped)

    return images, labels, objids, ras, decs


def load_null_images(data_dir):
    """Load null test images (elliptical galaxies)."""
    null_catalog_path = os.path.join(data_dir, "null_catalog.csv")
    null_img_dir = os.path.join(data_dir, "images", "null")

    if not os.path.exists(null_catalog_path):
        logger.warning("No null catalog found at %s", null_catalog_path)
        return [], []

    null_df = pd.read_csv(null_catalog_path)
    images = []
    objids = []

    for _, row in null_df.iterrows():
        objid = str(row["objid"])
        img_path = os.path.join(null_img_dir, "{}.jpg".format(objid))

        if not os.path.exists(img_path):
            continue

        try:
            img = Image.open(img_path).convert("RGB")
            images.append(img)
            objids.append(objid)
        except Exception:
            pass

    return images, objids


# ---------------------------------------------------------------------------
# Test 1: Mirror Test
# ---------------------------------------------------------------------------

def run_mirror_test(model, images, labels, transform, device):
    """
    Mirror test: for each test image, also evaluate its left-right mirror.
    The model should predict the opposite class for the mirrored image.
    Reports 'flip rate' = fraction where prediction flips.
    Target: >90%.
    """
    logger.info("=" * 50)
    logger.info("TEST 1: Mirror Test")
    logger.info("=" * 50)

    n = len(images)
    flips = 0
    same = 0
    details = []

    for i in range(n):
        img = images[i]
        mirror = img.transpose(Image.FLIP_LEFT_RIGHT)

        pred_orig, p_cw_orig, p_ccw_orig = predict_single_image(
            model, img, transform, device
        )
        pred_mirror, p_cw_mirror, p_ccw_mirror = predict_single_image(
            model, mirror, transform, device
        )

        flipped = pred_orig != pred_mirror
        if flipped:
            flips += 1
        else:
            same += 1

        details.append({
            "idx": i,
            "pred_orig": IDX_TO_LABEL[pred_orig],
            "pred_mirror": IDX_TO_LABEL[pred_mirror],
            "flipped": bool(flipped),
            "prob_cw_orig": p_cw_orig,
            "prob_cw_mirror": p_cw_mirror,
        })

    flip_rate = flips / max(n, 1)
    passed = flip_rate > 0.90

    logger.info("  Total test images: %d", n)
    logger.info("  Predictions that flipped: %d (%.1f%%)", flips, flip_rate * 100)
    logger.info("  Predictions that stayed: %d (%.1f%%)", same, (1 - flip_rate) * 100)
    logger.info("  PASS (>90%%): %s", "YES" if passed else "NO")

    result = {
        "test_name": "mirror_test",
        "n_images": n,
        "n_flipped": flips,
        "n_same": same,
        "flip_rate": flip_rate,
        "target": 0.90,
        "passed": passed,
    }
    return result, details


# ---------------------------------------------------------------------------
# Test 2: Rotation Test
# ---------------------------------------------------------------------------

def run_rotation_test(model, images, labels, transform, device):
    """
    Rotation test: rotate each image by 180 deg.
    For face-on spirals, 180 deg rotation should NOT change chirality.
    Reports fraction where prediction changes.
    Target: <20% flip rate.
    """
    logger.info("=" * 50)
    logger.info("TEST 2: Rotation Test (180 deg)")
    logger.info("=" * 50)

    n = len(images)
    flips = 0
    same = 0
    details = []

    for i in range(n):
        img = images[i]
        rotated = img.rotate(180, resample=Image.BILINEAR, expand=False)

        pred_orig, p_cw_orig, _ = predict_single_image(
            model, img, transform, device
        )
        pred_rot, p_cw_rot, _ = predict_single_image(
            model, rotated, transform, device
        )

        flipped = pred_orig != pred_rot
        if flipped:
            flips += 1
        else:
            same += 1

        details.append({
            "idx": i,
            "pred_orig": IDX_TO_LABEL[pred_orig],
            "pred_rotated": IDX_TO_LABEL[pred_rot],
            "flipped": bool(flipped),
            "prob_cw_orig": p_cw_orig,
            "prob_cw_rotated": p_cw_rot,
        })

    flip_rate = flips / max(n, 1)
    passed = flip_rate < 0.20

    logger.info("  Total test images: %d", n)
    logger.info("  Predictions that flipped: %d (%.1f%%)", flips, flip_rate * 100)
    logger.info("  Predictions that stayed: %d (%.1f%%)", same, (1 - flip_rate) * 100)
    logger.info("  PASS (<20%%): %s", "YES" if passed else "NO")

    result = {
        "test_name": "rotation_test",
        "n_images": n,
        "n_flipped": flips,
        "n_same": same,
        "flip_rate": flip_rate,
        "target_max": 0.20,
        "passed": passed,
    }
    return result, details


# ---------------------------------------------------------------------------
# Test 3: PSF Proxy Test
# ---------------------------------------------------------------------------

def run_psf_test(model, images, labels, transform, device, catalog, data_dir):
    """
    PSF proxy test: correlate predicted CW fraction with image quality (seeing).
    If SDSS PSF/seeing data is available in catalog, compute Pearson correlation.
    Should show no significant correlation (p > 0.05).
    """
    logger.info("=" * 50)
    logger.info("TEST 3: PSF Proxy Test")
    logger.info("=" * 50)

    # Check if PSF/seeing column exists in catalog
    psf_cols = [c for c in catalog.columns if "psf" in c.lower() or "seeing" in c.lower() or "fwhm" in c.lower()]

    if not psf_cols:
        logger.info("  No PSF/seeing column found in catalog.")
        logger.info("  SKIPPED — PSF proxy test requires seeing metadata.")
        result = {
            "test_name": "psf_proxy_test",
            "status": "skipped",
            "reason": "No PSF/seeing column in catalog",
            "passed": None,
        }
        return result, []

    psf_col = psf_cols[0]
    logger.info("  Using PSF column: %s", psf_col)

    test_df = catalog[catalog["split"] == "test"].reset_index(drop=True)

    # Get predictions and PSF values
    prob_cw_list = []
    psf_list = []

    for idx, (img, label) in enumerate(zip(images, labels)):
        if idx < len(test_df):
            psf_val = test_df.iloc[idx].get(psf_col)
            if psf_val is not None and not np.isnan(float(psf_val)):
                pred_idx, p_cw, p_ccw = predict_single_image(
                    model, img, transform, device
                )
                prob_cw_list.append(p_cw)
                psf_list.append(float(psf_val))

    if len(prob_cw_list) < 10:
        logger.info("  Too few PSF values (%d). SKIPPED.", len(prob_cw_list))
        result = {
            "test_name": "psf_proxy_test",
            "status": "skipped",
            "reason": "Too few PSF values ({})".format(len(prob_cw_list)),
            "passed": None,
        }
        return result, []

    # Pearson correlation
    r, p_val = scipy_stats.pearsonr(psf_list, prob_cw_list)
    passed = p_val > 0.05  # no significant correlation

    logger.info("  N samples: %d", len(prob_cw_list))
    logger.info("  Pearson r: %.4f", r)
    logger.info("  p-value: %.4f", p_val)
    logger.info("  PASS (p>0.05, no significant correlation): %s",
                "YES" if passed else "NO")

    result = {
        "test_name": "psf_proxy_test",
        "status": "completed",
        "n_samples": len(prob_cw_list),
        "pearson_r": float(r),
        "p_value": float(p_val),
        "psf_column": psf_col,
        "passed": passed,
    }
    return result, list(zip(psf_list, prob_cw_list))


# ---------------------------------------------------------------------------
# Test 4: Balanced Null Test
# ---------------------------------------------------------------------------

def run_null_test(model, null_images, null_objids, transform, device):
    """
    Balanced null test: run classifier on elliptical/featureless galaxies.
    Should give ~50/50 CW/CCW (no chirality bias).
    Report CW fraction and binomial 95% CI.
    """
    logger.info("=" * 50)
    logger.info("TEST 4: Balanced Null Test (Elliptical Galaxies)")
    logger.info("=" * 50)

    if len(null_images) == 0:
        logger.info("  No null test images available. SKIPPED.")
        result = {
            "test_name": "balanced_null_test",
            "status": "skipped",
            "reason": "No elliptical galaxy images available",
            "passed": None,
        }
        return result, []

    n = len(null_images)
    n_cw = 0
    n_ccw = 0
    details = []

    for i in range(n):
        pred_idx, p_cw, p_ccw = predict_single_image(
            model, null_images[i], transform, device
        )
        if pred_idx == 0:
            n_cw += 1
        else:
            n_ccw += 1
        details.append({
            "objid": null_objids[i],
            "pred": IDX_TO_LABEL[pred_idx],
            "prob_cw": p_cw,
            "prob_ccw": p_ccw,
        })

    cw_frac = n_cw / max(n, 1)

    # Binomial 95% CI (Clopper-Pearson)
    alpha = 0.05
    ci_low = scipy_stats.beta.ppf(alpha / 2, n_cw, n - n_cw + 1) if n_cw > 0 else 0.0
    ci_high = scipy_stats.beta.ppf(1 - alpha / 2, n_cw + 1, n - n_cw) if n_cw < n else 1.0

    # Pass if 50% is within the 95% CI
    passed = ci_low <= 0.5 <= ci_high

    logger.info("  Total null images: %d", n)
    logger.info("  Predicted CW: %d (%.1f%%)", n_cw, cw_frac * 100)
    logger.info("  Predicted CCW: %d (%.1f%%)", n_ccw, (1 - cw_frac) * 100)
    logger.info("  CW fraction: %.4f", cw_frac)
    logger.info("  95%% CI: [%.4f, %.4f]", ci_low, ci_high)
    logger.info("  PASS (50%% within CI): %s", "YES" if passed else "NO")

    result = {
        "test_name": "balanced_null_test",
        "status": "completed",
        "n_images": n,
        "n_cw": n_cw,
        "n_ccw": n_ccw,
        "cw_fraction": cw_frac,
        "ci_95_low": ci_low,
        "ci_95_high": ci_high,
        "passed": passed,
    }
    return result, details


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------

def plot_mirror_histogram(details, output_dir):
    """Histogram of P(CW) for original vs mirrored images."""
    orig_pcw = [d["prob_cw_orig"] for d in details]
    mirror_pcw = [d["prob_cw_mirror"] for d in details]

    fig, ax = plt.subplots(figsize=(8, 5))
    bins = np.linspace(0, 1, 30)
    ax.hist(orig_pcw, bins=bins, alpha=0.6, label="Original", color="steelblue")
    ax.hist(mirror_pcw, bins=bins, alpha=0.6, label="Mirrored", color="coral")
    ax.set_xlabel("P(CW)")
    ax.set_ylabel("Count")
    ax.set_title("Mirror Test: P(CW) Distribution")
    ax.legend()
    ax.grid(True, alpha=0.3)

    path = os.path.join(output_dir, "mirror_test_histogram.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Mirror test histogram saved to %s", path)


def plot_rotation_histogram(details, output_dir):
    """Histogram of P(CW) for original vs 180-deg rotated images."""
    orig_pcw = [d["prob_cw_orig"] for d in details]
    rot_pcw = [d["prob_cw_rotated"] for d in details]

    fig, ax = plt.subplots(figsize=(8, 5))
    bins = np.linspace(0, 1, 30)
    ax.hist(orig_pcw, bins=bins, alpha=0.6, label="Original", color="steelblue")
    ax.hist(rot_pcw, bins=bins, alpha=0.6, label="Rotated 180 deg", color="orange")
    ax.set_xlabel("P(CW)")
    ax.set_ylabel("Count")
    ax.set_title("Rotation Test: P(CW) Distribution")
    ax.legend()
    ax.grid(True, alpha=0.3)

    path = os.path.join(output_dir, "rotation_test_histogram.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Rotation test histogram saved to %s", path)


def plot_null_bar(result, output_dir):
    """Bar chart of CW/CCW predictions on null test galaxies."""
    if result.get("status") == "skipped":
        return

    fig, ax = plt.subplots(figsize=(6, 5))

    n_cw = result["n_cw"]
    n_ccw = result["n_ccw"]
    total = n_cw + n_ccw

    bars = ax.bar(
        ["CW", "CCW"], [n_cw, n_ccw],
        color=["steelblue", "coral"], edgecolor="black", linewidth=0.5
    )

    # Add count labels
    for bar, count in zip(bars, [n_cw, n_ccw]):
        ax.text(
            bar.get_x() + bar.get_width() / 2, bar.get_height() + total * 0.01,
            str(count), ha="center", va="bottom", fontsize=12,
        )

    # Expected 50% line
    ax.axhline(y=total / 2.0, color="gray", linestyle="--", alpha=0.7, label="Expected 50%")

    ax.set_ylabel("Count")
    ax.set_title(
        "Balanced Null Test: Elliptical Galaxies\n"
        "CW fraction = %.3f [95%% CI: %.3f, %.3f]"
        % (result["cw_fraction"], result["ci_95_low"], result["ci_95_high"])
    )
    ax.legend()
    ax.grid(True, alpha=0.3, axis="y")

    path = os.path.join(output_dir, "null_test_bar.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Null test bar chart saved to %s", path)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logger.info("=" * 60)
    logger.info("BigBounce P7 — Bias Audits")
    logger.info("Model: %s", args.model_path)
    logger.info("Data dir: %s", args.data_dir)
    logger.info("Output dir: %s", args.output_dir)
    logger.info("Device: %s", device)
    logger.info("=" * 60)

    # Load model
    if not os.path.exists(args.model_path):
        logger.error("Model not found: %s", args.model_path)
        sys.exit(1)

    model = load_model(args.model_path, device)
    transform = get_eval_transform()

    # Load catalog and test images
    catalog_path = os.path.join(args.data_dir, "catalog.csv")
    if not os.path.exists(catalog_path):
        logger.error("Catalog not found: %s", catalog_path)
        sys.exit(1)

    catalog = pd.read_csv(catalog_path)
    images, labels, objids, ras, decs = load_test_images(catalog, args.data_dir)
    logger.info("Loaded %d test images", len(images))

    if len(images) == 0:
        logger.error("No test images found. Cannot run audits.")
        sys.exit(1)

    # Load null images
    null_images, null_objids = load_null_images(args.data_dir)
    logger.info("Loaded %d null test images", len(null_images))

    # -----------------------------------------------------------------------
    # Run all 4 tests
    # -----------------------------------------------------------------------

    all_results = {}

    # Test 1: Mirror
    mirror_result, mirror_details = run_mirror_test(
        model, images, labels, transform, device
    )
    all_results["mirror_test"] = mirror_result
    if mirror_details:
        plot_mirror_histogram(mirror_details, args.output_dir)

    # Test 2: Rotation
    rotation_result, rotation_details = run_rotation_test(
        model, images, labels, transform, device
    )
    all_results["rotation_test"] = rotation_result
    if rotation_details:
        plot_rotation_histogram(rotation_details, args.output_dir)

    # Test 3: PSF
    psf_result, psf_details = run_psf_test(
        model, images, labels, transform, device, catalog, args.data_dir
    )
    all_results["psf_proxy_test"] = psf_result

    # Test 4: Null
    null_result, null_details = run_null_test(
        model, null_images, null_objids, transform, device
    )
    all_results["balanced_null_test"] = null_result
    if null_result.get("status") != "skipped":
        plot_null_bar(null_result, args.output_dir)

    # -----------------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------------

    n_passed = sum(
        1 for r in all_results.values()
        if r.get("passed") is True
    )
    n_failed = sum(
        1 for r in all_results.values()
        if r.get("passed") is False
    )
    n_skipped = sum(
        1 for r in all_results.values()
        if r.get("passed") is None
    )

    summary = {
        "total_tests": len(all_results),
        "passed": n_passed,
        "failed": n_failed,
        "skipped": n_skipped,
        "overall_pass": n_failed == 0,
        "tests": all_results,
    }

    # Save JSON report
    json_path = os.path.join(args.output_dir, "bias_audit_report.json")
    with open(json_path, "w") as f:
        json.dump(summary, f, indent=2)
    logger.info("JSON report saved to %s", json_path)

    # Save human-readable report
    txt_path = os.path.join(args.output_dir, "bias_audit_report.txt")
    with open(txt_path, "w") as f:
        f.write("BigBounce P7 — Bias Audit Report\n")
        f.write("=" * 50 + "\n\n")
        f.write("Model: %s\n" % args.model_path)
        f.write("Data: %s\n\n" % args.data_dir)

        f.write("SUMMARY\n")
        f.write("-" * 30 + "\n")
        f.write("Tests passed: %d\n" % n_passed)
        f.write("Tests failed: %d\n" % n_failed)
        f.write("Tests skipped: %d\n" % n_skipped)
        f.write("Overall: %s\n\n" % ("PASS" if n_failed == 0 else "FAIL"))

        for name, result in all_results.items():
            f.write("\n%s\n" % name.upper().replace("_", " "))
            f.write("-" * 30 + "\n")
            for key, val in result.items():
                if key != "test_name":
                    f.write("  %s: %s\n" % (key, str(val)))
            status = result.get("passed")
            if status is True:
                f.write("  --> PASS\n")
            elif status is False:
                f.write("  --> FAIL\n")
            else:
                f.write("  --> SKIPPED\n")
            f.write("\n")

    logger.info("Text report saved to %s", txt_path)

    # Final summary
    logger.info("=" * 60)
    logger.info("BIAS AUDIT SUMMARY")
    logger.info("  Passed: %d / %d", n_passed, len(all_results))
    logger.info("  Failed: %d / %d", n_failed, len(all_results))
    logger.info("  Skipped: %d / %d", n_skipped, len(all_results))
    logger.info("  Overall: %s", "PASS" if n_failed == 0 else "FAIL")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
