"""Reusable exact-window and content-bound receipt primitives."""

from .receipts import (
    PROTECTED_RECEIPT_FIELDS,
    publish_json,
    receipt_path,
    sha256,
    validate_json_receipt,
    verify_json_receipt,
)
from .multipoles import bandpower_edges, field_harmonic_kwargs
from .windows import (
    build_rotation_response,
    recover_beta_deg,
    rotate_eb_spectra,
    validate_window_equivalence,
    windowed_bandpowers,
)

__all__ = [
    "PROTECTED_RECEIPT_FIELDS",
    "build_rotation_response",
    "publish_json",
    "receipt_path",
    "recover_beta_deg",
    "rotate_eb_spectra",
    "sha256",
    "validate_json_receipt",
    "bandpower_edges",
    "field_harmonic_kwargs",
    "validate_window_equivalence",
    "verify_json_receipt",
    "windowed_bandpowers",
]

__version__ = "0.1.5"
