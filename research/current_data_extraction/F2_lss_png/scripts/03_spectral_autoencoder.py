#!/usr/bin/env python3
"""
Pipeline B Step 3: Spectral Autoencoder for DESI Anomaly Detection

Gate 2 requirement: must beat PCA baseline from Step 2.
Gate 3 requirement: injection recovery validated.
Gate 7 requirement: calibrated anomaly scores.

Architecture:
  Encoder: spectrum → 256 → 128 → 64 → latent (32)
  Decoder: latent (32) → 64 → 128 → 256 → spectrum
  Loss: MSE + optional KL (if VAE variant helps)

Training:
  - 80/10/10 split by sky region (NOT random)
  - Train on "normal" spectra (good ZWARN, standard types)
  - Anomaly score = reconstruction error (MSE per spectrum)

Anomaly classification (post-hoc):
  - Cluster high-error spectra by latent-space proximity
  - Label clusters by dominant spectral features
  - Separate artifacts from science

Output:
  - Anomaly score for every object
  - Latent-space embedding (32-dim) for clustering
  - Anomaly family assignment
  - Tracer utility score for PNG
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import json
import os


class SpectralAutoencoder(nn.Module):
    """Simple fully-connected autoencoder for spectral features."""

    def __init__(self, input_dim, latent_dim=32):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(256, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(128, 64),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Linear(64, latent_dim),
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 64),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(64, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(128, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Linear(256, input_dim),
        )

    def forward(self, x):
        z = self.encoder(x)
        x_recon = self.decoder(z)
        return x_recon, z

    def anomaly_score(self, x):
        """Per-sample reconstruction error (MSE)."""
        with torch.no_grad():
            x_recon, z = self.forward(x)
            mse = torch.mean((x - x_recon) ** 2, dim=1)
        return mse, z


def train_autoencoder(X_train, X_val, input_dim, latent_dim=32,
                      epochs=50, batch_size=512, lr=1e-3, device='cpu'):
    """Train the autoencoder and return the model + training history."""
    model = SpectralAutoencoder(input_dim, latent_dim).to(device)
    optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=1e-5)
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, patience=5, factor=0.5)
    criterion = nn.MSELoss()

    train_ds = TensorDataset(torch.FloatTensor(X_train))
    val_ds = TensorDataset(torch.FloatTensor(X_val))
    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=batch_size)

    history = {'train_loss': [], 'val_loss': []}

    for epoch in range(epochs):
        # Train
        model.train()
        train_loss = 0
        for (batch,) in train_loader:
            batch = batch.to(device)
            recon, _ = model(batch)
            loss = criterion(recon, batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            train_loss += loss.item() * len(batch)
        train_loss /= len(X_train)

        # Validate
        model.eval()
        val_loss = 0
        with torch.no_grad():
            for (batch,) in val_loader:
                batch = batch.to(device)
                recon, _ = model(batch)
                loss = criterion(recon, batch)
                val_loss += loss.item() * len(batch)
        val_loss /= len(X_val)

        scheduler.step(val_loss)
        history['train_loss'].append(train_loss)
        history['val_loss'].append(val_loss)

        if (epoch + 1) % 10 == 0 or epoch == 0:
            print('  Epoch %3d/%d: train=%.6f val=%.6f lr=%.1e' % (
                epoch + 1, epochs, train_loss, val_loss,
                optimizer.param_groups[0]['lr']))

    return model, history


def compute_anomaly_catalog(model, X_all, device='cpu', batch_size=4096):
    """Score all objects and return anomaly scores + latent embeddings."""
    model.eval()
    all_scores = []
    all_latents = []

    ds = TensorDataset(torch.FloatTensor(X_all))
    loader = DataLoader(ds, batch_size=batch_size)

    with torch.no_grad():
        for (batch,) in loader:
            batch = batch.to(device)
            scores, latents = model.anomaly_score(batch)
            all_scores.append(scores.cpu().numpy())
            all_latents.append(latents.cpu().numpy())

    scores = np.concatenate(all_scores)
    latents = np.concatenate(all_latents)
    return scores, latents


if __name__ == '__main__':
    print('Pipeline B Step 3: Spectral Autoencoder')
    print('This script is imported by the training pipeline.')
    print('Run 04_train_and_score.py for the full pipeline.')
