#!/usr/bin/env python3
"""
Pipeline B Step 11: Deep Cross-Match + Spectrum Extraction

For each top spectral anomaly:
1. Cross-match against SIMBAD, NED, and VizieR
2. Extract the actual spectrum (wavelength x flux)
3. Identify WHY the autoencoder flagged it (which wavelength region has highest error)
4. Classify the anomaly type (unusual emission, absorption, continuum)
5. Produce a summary for the review page

This is what makes the anomalies ACTIONABLE — not just "high score"
but "here's the spectrum, here's what's unusual about it."
"""

import numpy as np
import json
import os
import urllib.request
import time


def query_simbad(ra, dec, radius_arcsec=5):
    """Query SIMBAD for known objects near this position."""
    url = ('https://simbad.cds.unistra.fr/simbad/sim-coo?Coord=%.5f+%.5f'
           '&CooFrame=FK5&CooEpoch=2000&CooEqui=2000&Radius=%d&Radius.unit=arcsec'
           '&output.format=ASCII' % (ra, dec, radius_arcsec))
    try:
        req = urllib.request.urlopen(url, timeout=10)
        content = req.read().decode()
        if 'No astronomical object found' in content:
            return {'found': False, 'source': 'SIMBAD'}
        else:
            # Extract object name
            lines = content.split('\n')
            name = 'unknown'
            otype = 'unknown'
            for line in lines:
                if 'Object' in line and '---' not in line and 'query' not in line.lower():
                    name = line.strip()[:60]
                    break
            return {'found': True, 'source': 'SIMBAD', 'name': name}
    except Exception as e:
        return {'found': None, 'source': 'SIMBAD', 'error': str(e)[:60]}


def query_ned(ra, dec, radius_arcmin=0.1):
    """Query NED for known objects near this position."""
    url = ('https://ned.ipac.caltech.edu/cgi-bin/objsearch?search_type=Near+Position+Search'
           '&of=ascii_bar&in_csys=Equatorial&in_equinox=J2000.0'
           '&lon=%.5fd&lat=%.5fd&radius=%.1f&hconst=67.8&omegam=0.308&omegav=0.692'
           '&corr_z=1&z_constraint=Unconstrained&z_unit=z'
           '&ot_include=ANY&nmp_op=ANY' % (ra, dec, radius_arcmin))
    try:
        req = urllib.request.urlopen(url, timeout=10)
        content = req.read().decode()
        lines = [l for l in content.split('\n') if l.strip() and not l.startswith('#')]
        if len(lines) > 1:  # header + data
            return {'found': True, 'source': 'NED', 'n_matches': len(lines) - 1}
        return {'found': False, 'source': 'NED'}
    except Exception as e:
        return {'found': None, 'source': 'NED', 'error': str(e)[:60]}


def identify_anomaly_region(spectrum, reconstruction, wavelength_bins):
    """Find which wavelength region has the highest reconstruction error."""
    error = (spectrum - reconstruction) ** 2

    # Split into ~10 wavelength regions
    n_regions = 10
    region_size = len(error) // n_regions
    region_errors = []

    for i in range(n_regions):
        start = i * region_size
        end = min((i + 1) * region_size, len(error))
        region_mean = np.mean(error[start:end])
        # Map to approximate wavelength
        # B: 3600-5800 (172 bins), R: 5760-7620 (145 bins), Z: 7520-9824 (180 bins)
        if start < 172:
            wave_label = 'B arm (3600-5800 A)'
        elif start < 172 + 145:
            wave_label = 'R arm (5760-7620 A)'
        else:
            wave_label = 'Z arm (7520-9824 A)'
        region_errors.append({
            'region': i,
            'wave_label': wave_label,
            'mean_error': float(region_mean),
            'start_bin': start,
            'end_bin': end,
        })

    # Sort by error
    region_errors.sort(key=lambda x: -x['mean_error'])
    return region_errors


def classify_anomaly_type(spectrum, reconstruction):
    """Classify the type of spectral anomaly based on the residual pattern."""
    residual = spectrum - reconstruction

    # Check for localized features vs broad features
    abs_residual = np.abs(residual)
    median_resid = np.median(abs_residual)

    # Localized peak (emission line or absorption)
    max_resid = np.max(abs_residual)
    peak_idx = np.argmax(abs_residual)
    peak_width = np.sum(abs_residual > max_resid * 0.5)  # FWHM in pixels

    if peak_width < 10 and max_resid > 5 * median_resid:
        if residual[peak_idx] > 0:
            return 'EMISSION_LINE', 'Localized emission feature at bin %d' % peak_idx
        else:
            return 'ABSORPTION_LINE', 'Localized absorption feature at bin %d' % peak_idx

    # Broad continuum anomaly
    if np.std(residual) > 2 * median_resid:
        # Check if it's a color anomaly (slope)
        left_mean = np.mean(residual[:len(residual)//3])
        right_mean = np.mean(residual[-len(residual)//3:])
        if abs(left_mean - right_mean) > 3 * median_resid:
            return 'CONTINUUM_SLOPE', 'Unusual spectral slope (color anomaly)'

    # Scattered features
    n_peaks = np.sum(abs_residual > 3 * median_resid)
    if n_peaks > 20:
        return 'NOISY', 'Multiple scattered features (possibly low SNR or complex spectrum)'

    return 'UNUSUAL_SHAPE', 'Broadly unusual spectral shape'


if __name__ == '__main__':
    print('Pipeline B Step 11: Deep cross-match + spectrum analysis')
    print('Run this on RunPod after retraining with 40K+ spectra.')
    print('Requires: trained model, anomaly scores, original spectra.')
