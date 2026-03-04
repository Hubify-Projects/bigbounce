"""Galaxy spin dipole analysis pipeline.

Full pipeline: load GZ catalog -> classify ambiguous cases ->
compute dipole -> compare with paper's A₀ ~ 0.003.

This module ties together galaxy_zoo.py (data access) and
galaxy_classifier.py (vision classification) into a single
analysis workflow.
"""

import json
import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

# Paper parameters
PAPER_A0 = 0.003
PAPER_P = 0.5
PAPER_Q = 0.5
PAPER_DIPOLE = {"l": 52.0, "b": 68.0}


def run_spin_analysis(
    sample_size: int = 100000,
    z_bins: int = 20,
    nside: int = 16,
    classify_ambiguous: bool = False,
    classifier_method: str = "zoobot",
    output_dir: Optional[str] = None,
) -> dict:
    """Run the full galaxy spin dipole analysis pipeline.

    Steps:
      1. Load Galaxy Zoo DESI catalog (streaming)
      2. Filter for clear spiral galaxies
      3. Optionally classify ambiguous cases with vision model
      4. Compute spin asymmetry A(z) in redshift bins
      5. Compute HEALPix sky map and fit dipole
      6. Compare with paper predictions

    Args:
        sample_size: Number of galaxies to process
        z_bins: Number of redshift bins for A(z)
        nside: HEALPix resolution for sky map
        classify_ambiguous: Whether to reclassify ambiguous spirals
        classifier_method: "zoobot" or "api" for ambiguous classification
        output_dir: Directory to save results (default: public/data/galaxy_zoo/)

    Returns:
        dict with full analysis results
    """
    from research.agents.galaxy_zoo import (
        load_gz_desi, compute_spin_asymmetry, compute_spin_dipole, save_gz_data
    )

    logger.info(f"Starting spin analysis pipeline (n={sample_size})")

    # Step 1: Load catalog
    logger.info("Step 1/5: Loading GZ DESI catalog...")
    ds = load_gz_desi(streaming=True, max_samples=sample_size)

    # Step 2: Filter for clear spirals
    logger.info("Step 2/5: Filtering for clear spiral galaxies...")
    catalog = []
    n_processed = 0
    n_ambiguous = 0
    ambiguous_indices = []

    for sample in ds["train"] if "train" in ds else ds:
        if n_processed >= sample_size:
            break

        cw = sample.get("spiral_cw_fraction", 0) or 0
        ccw = sample.get("spiral_ccw_fraction", 0) or 0
        z = sample.get("redshift")
        ra = sample.get("ra")
        dec = sample.get("dec")

        if z is not None and z > 0 and ra is not None and dec is not None:
            total_spiral = cw + ccw
            if total_spiral > 0.5:  # Clear spiral
                catalog.append({
                    "ra": ra, "dec": dec, "redshift": z,
                    "spiral_cw_fraction": cw,
                    "spiral_ccw_fraction": ccw,
                    "clarity": "clear"
                })
            elif total_spiral > 0.2:  # Ambiguous spiral
                n_ambiguous += 1
                if classify_ambiguous:
                    ambiguous_indices.append(len(catalog))
                    catalog.append({
                        "ra": ra, "dec": dec, "redshift": z,
                        "spiral_cw_fraction": cw,
                        "spiral_ccw_fraction": ccw,
                        "clarity": "ambiguous"
                    })

        n_processed += 1
        if n_processed % 10000 == 0:
            logger.info(f"  Processed {n_processed}/{sample_size}, spirals: {len(catalog)}")

    logger.info(f"  Found {len(catalog)} spirals ({n_ambiguous} ambiguous)")

    # Step 3: Classify ambiguous cases (optional)
    if classify_ambiguous and ambiguous_indices:
        logger.info(f"Step 3/5: Classifying {len(ambiguous_indices)} ambiguous cases...")
        # This requires images — skip if only catalog data is available
        logger.warning("  Skipping vision classification (requires galaxy images)")
    else:
        logger.info("Step 3/5: Skipping ambiguous classification")

    # Step 4: Compute spin asymmetry
    logger.info("Step 4/5: Computing spin asymmetry A(z)...")
    asymmetry = compute_spin_asymmetry(catalog, z_bins=z_bins)

    # Step 5: Compute sky map and dipole
    logger.info("Step 5/5: Computing sky map and fitting dipole...")
    try:
        sky_map = compute_spin_dipole(catalog, nside=nside)
    except ImportError:
        logger.warning("  healpy not installed — skipping sky map")
        sky_map = {"error": "healpy not installed"}

    # Compare with paper
    comparison = compare_with_paper(asymmetry, sky_map)

    results = {
        "pipeline": "spin_analysis",
        "sample_size": sample_size,
        "n_spirals": len(catalog),
        "n_ambiguous": n_ambiguous,
        "asymmetry": asymmetry,
        "sky_map": sky_map,
        "comparison": comparison,
    }

    # Save results
    if output_dir:
        out = Path(output_dir)
    else:
        out = Path(__file__).resolve().parents[2] / "public" / "data" / "galaxy_zoo"
    out.mkdir(parents=True, exist_ok=True)

    save_gz_data(results, "spin_analysis_results.json")
    logger.info(f"Results saved to {out}/spin_analysis_results.json")

    return results


def compare_with_paper(asymmetry: dict, sky_map: dict) -> dict:
    """Compare analysis results with paper's predictions.

    Returns a comparison summary with consistency assessments.
    """
    import math

    result = {"paper_parameters": {
        "A0": PAPER_A0, "p": PAPER_P, "q": PAPER_Q,
        "dipole_l": PAPER_DIPOLE["l"], "dipole_b": PAPER_DIPOLE["b"]
    }}

    # Check asymmetry amplitude
    if asymmetry.get("asymmetry"):
        measured_values = [a for a in asymmetry["asymmetry"] if abs(a) < 0.1]
        if measured_values:
            mean_a = sum(abs(a) for a in measured_values) / len(measured_values)
            result["measured_mean_asymmetry"] = mean_a
            result["paper_A0"] = PAPER_A0
            result["asymmetry_ratio"] = mean_a / PAPER_A0 if PAPER_A0 > 0 else None
            result["asymmetry_consistent"] = 0.1 < mean_a / PAPER_A0 < 10

    # Check dipole direction
    if isinstance(sky_map, dict) and "dipole_direction" in sky_map:
        measured_l = sky_map["dipole_direction"]["l"]
        measured_b = sky_map["dipole_direction"]["b"]

        # Angular separation
        l1, b1 = math.radians(measured_l), math.radians(measured_b)
        l2, b2 = math.radians(PAPER_DIPOLE["l"]), math.radians(PAPER_DIPOLE["b"])
        cos_sep = (math.sin(b1) * math.sin(b2) +
                   math.cos(b1) * math.cos(b2) * math.cos(l1 - l2))
        cos_sep = max(-1, min(1, cos_sep))
        separation_deg = math.degrees(math.acos(cos_sep))

        result["measured_dipole"] = {"l": measured_l, "b": measured_b}
        result["angular_separation_deg"] = separation_deg
        result["dipole_consistent"] = separation_deg < 30  # Within 30 degrees

    return result


def quick_check(n_galaxies: int = 10000) -> dict:
    """Quick consistency check with a small sample.

    Useful for verifying the pipeline works before running the full analysis.
    """
    logger.info(f"Quick check with {n_galaxies} galaxies...")
    return run_spin_analysis(
        sample_size=n_galaxies,
        z_bins=10,
        nside=8,
        classify_ambiguous=False,
    )
