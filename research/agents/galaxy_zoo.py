"""Galaxy Zoo catalog access and analysis for BigBounce spin-torsion cosmology.

Provides data access to Galaxy Zoo morphological classifications for analyzing
galaxy spin asymmetry — a key observational signature of the BigBounce framework.
The paper claims A₀ ~ 0.003 galaxy spin dipole at (l ~ 52°, b ~ 68°).
"""

import json
import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

# Constants
DIPOLE_DIRECTION = {"l": 52.0, "b": 68.0}  # Galactic coordinates from paper
A0_PAPER = 0.003  # Empirical amplitude at z=0


def query_gz2(target=None, ra=None, dec=None, radius_arcmin=10, max_results=1000) -> list[dict]:
    """Query Galaxy Zoo 2 (GZ2) catalog via VizieR.

    GZ2: 304,122 galaxies with detailed morphological classifications.
    VizieR catalog: J/MNRAS/435/2835
    """
    try:
        from astroquery.vizier import Vizier
    except ImportError:
        raise ImportError("Install astroquery: pip install astroquery")

    v = Vizier(columns=["*"], row_limit=max_results)
    v.catalog = "J/MNRAS/435/2835"

    if target:
        from astropy.coordinates import SkyCoord
        import astropy.units as u
        result = v.query_region(SkyCoord.from_name(target), radius=radius_arcmin * u.arcmin)
    elif ra is not None and dec is not None:
        from astropy.coordinates import SkyCoord
        import astropy.units as u
        coord = SkyCoord(ra=ra, dec=dec, unit="deg")
        result = v.query_region(coord, radius=radius_arcmin * u.arcmin)
    else:
        result = v.query_constraints()

    if not result:
        return []

    table = result[0]
    return [dict(zip(table.colnames, row)) for row in table]


def query_gz_decals(target=None, ra=None, dec=None, radius_arcmin=10, max_results=1000) -> list[dict]:
    """Query Galaxy Zoo DECaLS catalog via VizieR.

    GZ DECaLS: ~314,000 galaxies with Dark Energy Camera Legacy Survey imaging.
    VizieR catalog: J/MNRAS/509/3966
    """
    try:
        from astroquery.vizier import Vizier
    except ImportError:
        raise ImportError("Install astroquery: pip install astroquery")

    v = Vizier(columns=["*"], row_limit=max_results)
    v.catalog = "J/MNRAS/509/3966"

    if target:
        from astropy.coordinates import SkyCoord
        import astropy.units as u
        result = v.query_region(SkyCoord.from_name(target), radius=radius_arcmin * u.arcmin)
    elif ra is not None and dec is not None:
        from astropy.coordinates import SkyCoord
        import astropy.units as u
        coord = SkyCoord(ra=ra, dec=dec, unit="deg")
        result = v.query_region(coord, radius=radius_arcmin * u.arcmin)
    else:
        result = v.query_constraints()

    if not result:
        return []

    table = result[0]
    return [dict(zip(table.colnames, row)) for row in table]


def load_gz_desi(streaming=True, max_samples=None):
    """Load Galaxy Zoo DESI dataset from HuggingFace.

    8.67 million galaxies with morphological classifications including
    spiral arm direction (Z-wise vs S-wise) — directly relevant to
    the paper's galaxy spin dipole asymmetry claim.

    Dataset: mwalmsley/gz_desi
    """
    try:
        from datasets import load_dataset
    except ImportError:
        raise ImportError("Install datasets: pip install datasets")

    ds = load_dataset("mwalmsley/gz_desi", streaming=streaming)

    if max_samples and not streaming:
        ds = ds.select(range(min(max_samples, len(ds))))

    return ds


def load_tng50_ceers(split="train", max_samples=None):
    """Load TNG50-CEERS simulated galaxy images from HuggingFace.

    10,000 simulated galaxy images from the IllustrisTNG cosmological
    simulation, processed to mimic CEERS/JWST observations.

    Dataset: StarThomas1002/TNG50-CEERS
    """
    try:
        from datasets import load_dataset
    except ImportError:
        raise ImportError("Install datasets: pip install datasets")

    ds = load_dataset("StarThomas1002/TNG50-CEERS", split=split)

    if max_samples:
        ds = ds.select(range(min(max_samples, len(ds))))

    return ds


def load_zoobot_encoder(model_name="convnext_nano"):
    """Load a Zoobot encoder model for galaxy morphology embeddings.

    Zoobot models are trained on 820K+ Galaxy Zoo volunteer classifications.
    Available models range from 4M to 197M parameters.

    Args:
        model_name: One of "convnext_nano" (4M), "convnext_small" (50M),
                   "convnext_base" (89M), "convnext_large" (197M)
    """
    try:
        import timm
    except ImportError:
        raise ImportError("Install timm: pip install timm")

    model_map = {
        "convnext_nano": "mwalmsley/zoobot-encoder-convnext_nano",
        "convnext_small": "mwalmsley/zoobot-encoder-convnext_small",
        "convnext_base": "mwalmsley/zoobot-encoder-convnext_base",
        "convnext_large": "mwalmsley/zoobot-encoder-convnext_large",
    }

    if model_name not in model_map:
        raise ValueError(f"Unknown model: {model_name}. Choose from {list(model_map.keys())}")

    model = timm.create_model(model_map[model_name], pretrained=True)
    model.eval()
    return model


def compute_spin_asymmetry(catalog: list[dict], z_bins: int = 20,
                           cw_key: str = "spiral_cw_fraction",
                           ccw_key: str = "spiral_ccw_fraction",
                           z_key: str = "redshift") -> dict:
    """Compute galaxy spin asymmetry A(z) in redshift bins.

    A(z) = (N_CW - N_CCW) / (N_CW + N_CCW) per bin.
    The paper predicts A(z) = A₀(1+z)^{-p} e^{-qz} with A₀ ~ 0.003.

    Returns dict with keys: z_centers, asymmetry, errors, n_galaxies, model_fit
    """
    import numpy as np

    zs = np.array([g[z_key] for g in catalog if z_key in g and g[z_key] is not None])
    cws = np.array([g.get(cw_key, 0) for g in catalog if z_key in g and g[z_key] is not None])
    ccws = np.array([g.get(ccw_key, 0) for g in catalog if z_key in g and g[z_key] is not None])

    if len(zs) == 0:
        return {"z_centers": [], "asymmetry": [], "errors": [], "n_galaxies": []}

    z_edges = np.linspace(zs.min(), zs.max(), z_bins + 1)
    z_centers = 0.5 * (z_edges[:-1] + z_edges[1:])

    asymmetry = []
    errors = []
    n_galaxies = []

    for i in range(z_bins):
        mask = (zs >= z_edges[i]) & (zs < z_edges[i + 1])
        n = mask.sum()
        n_galaxies.append(int(n))

        if n < 10:
            asymmetry.append(0.0)
            errors.append(1.0)
            continue

        cw_sum = cws[mask].sum()
        ccw_sum = ccws[mask].sum()
        total = cw_sum + ccw_sum

        if total > 0:
            a = (cw_sum - ccw_sum) / total
            err = np.sqrt(4 * cw_sum * ccw_sum / total**3)  # binomial error
        else:
            a = 0.0
            err = 1.0

        asymmetry.append(float(a))
        errors.append(float(err))

    # Model prediction: A(z) = A₀(1+z)^{-p} e^{-qz}
    p, q = 0.5, 0.5  # Paper best-fit values
    model = A0_PAPER * (1 + z_centers)**(-p) * np.exp(-q * z_centers)

    return {
        "z_centers": z_centers.tolist(),
        "asymmetry": asymmetry,
        "errors": errors,
        "n_galaxies": n_galaxies,
        "model_fit": {
            "A0": A0_PAPER,
            "p": p,
            "q": q,
            "predicted": model.tolist()
        }
    }


def compute_spin_dipole(catalog: list[dict], nside: int = 16,
                        ra_key: str = "ra", dec_key: str = "dec",
                        cw_key: str = "spiral_cw_fraction",
                        ccw_key: str = "spiral_ccw_fraction") -> dict:
    """Compute HEALPix sky map of CW-CCW galaxy spin excess.

    Returns dict with keys: nside, npix, pixel_values, dipole_direction, dipole_amplitude
    """
    try:
        import healpy as hp
    except ImportError:
        raise ImportError("Install healpy: pip install healpy")
    import numpy as np

    npix = hp.nside2npix(nside)
    cw_map = np.zeros(npix)
    ccw_map = np.zeros(npix)
    count_map = np.zeros(npix)

    for g in catalog:
        ra = g.get(ra_key)
        dec = g.get(dec_key)
        cw = g.get(cw_key, 0)
        ccw = g.get(ccw_key, 0)

        if ra is None or dec is None:
            continue

        theta = np.radians(90 - dec)  # colatitude
        phi = np.radians(ra)
        pix = hp.ang2pix(nside, theta, phi)

        cw_map[pix] += cw
        ccw_map[pix] += ccw
        count_map[pix] += 1

    # Compute asymmetry per pixel
    total = cw_map + ccw_map
    asymmetry_map = np.where(total > 0, (cw_map - ccw_map) / total, 0)

    # Fit dipole
    dipole = hp.fit_dipole(asymmetry_map, gal_cut=0)
    mono = dipole[0]
    dipole_vec = dipole[1:]

    # Convert to galactic coordinates
    l_dipole = np.degrees(np.arctan2(dipole_vec[1], dipole_vec[0])) % 360
    b_dipole = np.degrees(np.arcsin(dipole_vec[2] / np.linalg.norm(dipole_vec)))
    amplitude = np.linalg.norm(dipole_vec)

    return {
        "nside": nside,
        "npix": npix,
        "pixel_values": asymmetry_map.tolist(),
        "counts_per_pixel": count_map.tolist(),
        "dipole_direction": {"l": float(l_dipole), "b": float(b_dipole)},
        "dipole_amplitude": float(amplitude),
        "monopole": float(mono),
        "paper_dipole": DIPOLE_DIRECTION,
        "paper_A0": A0_PAPER
    }


def zooniverse_project_stats(project_slug: str = "zookeeper/galaxy-zoo") -> dict:
    """Get basic project statistics from Zooniverse API."""
    import urllib.request

    url = f"https://www.zooniverse.org/api/projects?slug={project_slug}"
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.api+json; version=1",
        "Content-Type": "application/json"
    })

    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode())

    if not data.get("projects"):
        return {"error": f"Project {project_slug} not found"}

    proj = data["projects"][0]
    return {
        "id": proj.get("id"),
        "display_name": proj.get("display_name"),
        "classifications_count": proj.get("classifications_count"),
        "subjects_count": proj.get("subjects_count"),
        "retired_subjects_count": proj.get("retired_subjects_count"),
        "launch_date": proj.get("launch_date"),
    }


def list_gz_datasets() -> dict:
    """List all available Galaxy Zoo datasets with metadata."""
    return {
        "galaxy_zoo_2": {
            "source": "VizieR J/MNRAS/435/2835",
            "galaxies": 304122,
            "description": "GZ2: SDSS DR7 main galaxy sample with detailed morphology",
            "reference": "Willett et al. 2013, MNRAS 435, 2835",
            "access": "query_gz2()"
        },
        "galaxy_zoo_decals": {
            "source": "VizieR J/MNRAS/509/3966",
            "galaxies": 314000,
            "description": "GZ DECaLS: Dark Energy Camera Legacy Survey galaxies",
            "reference": "Walmsley et al. 2022, MNRAS 509, 3966",
            "access": "query_gz_decals()"
        },
        "galaxy_zoo_desi": {
            "source": "HuggingFace mwalmsley/gz_desi",
            "galaxies": 8670000,
            "description": "GZ DESI: 8.67M galaxies with spiral direction classifications",
            "reference": "Walmsley et al. 2023",
            "access": "load_gz_desi()",
            "key_columns": ["spiral_cw_fraction", "spiral_ccw_fraction", "ra", "dec", "redshift"]
        },
        "tng50_ceers": {
            "source": "HuggingFace StarThomas1002/TNG50-CEERS",
            "galaxies": 10000,
            "description": "Simulated galaxy images from IllustrisTNG + CEERS",
            "reference": "TNG Collaboration",
            "access": "load_tng50_ceers()"
        },
        "zoobot_encoders": {
            "source": "HuggingFace mwalmsley/zoobot-encoder-*",
            "models": ["convnext_nano (4M)", "convnext_small (50M)", "convnext_base (89M)", "convnext_large (197M)"],
            "description": "Vision encoders trained on 820K+ Galaxy Zoo classifications",
            "access": "load_zoobot_encoder(model_name)"
        }
    }


def save_gz_data(data: dict, filename: Optional[str] = None) -> str:
    """Save Galaxy Zoo analysis data to JSON file.

    Args:
        data: Dictionary of analysis results
        filename: Output filename (default: auto-generated)

    Returns:
        Path to saved file
    """
    output_dir = Path(__file__).resolve().parents[2] / "public" / "data" / "galaxy_zoo"
    output_dir.mkdir(parents=True, exist_ok=True)

    if filename is None:
        from datetime import datetime
        filename = f"gz_analysis_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"

    filepath = output_dir / filename
    filepath.write_text(json.dumps(data, indent=2), encoding="utf-8")
    logger.info(f"Saved Galaxy Zoo data to {filepath}")
    return str(filepath)
