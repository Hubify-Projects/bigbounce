#!/usr/bin/env python3
r"""Exact-convention P1A NJL and late-density recomputation.

The declared scalar interaction is exactly

    L_int = G_s (psi_bar psi)^2.

The regulator is a hard four-dimensional Euclidean ball, p_E^2 <= Lambda^2.
P1A uses the unreduced Planck mass M_Pl = G_N^(-1/2), hence

    kappa = 8*pi*G_N = 8*pi/M_Pl^2,

not 1/M_Pl^2.  The script derives the gap threshold symbolically, evaluates
all six declared cutoff/multiplicity rows, separates the scalar sign result
from the coefficient-magnitude diagnostic, and recomputes the density bound.
It writes a deterministic JSON artifact beside this file.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import sympy as sp


OUT = Path(__file__).with_name("njl_gap_equation_route1_results.json")


def derive_gap_equation() -> dict[str, object]:
    """Derive G_crit for +G_s(psi_bar psi)^2 with a 4D hard cutoff."""
    M, Gs, Lam, Nf, Nc = sp.symbols(
        "M G_s Lambda N_f N_c", positive=True, finite=True
    )

    # Integral over a four-dimensional Euclidean ball.
    i4 = (
        Lam**2 - M**2 * sp.log(1 + Lam**2 / M**2)
    ) / (16 * sp.pi**2)

    # Dirac trace 4 and N_f N_c degeneracy.
    condensate = -4 * Nf * Nc * M * i4

    # M = -2 G_s <psi_bar psi> in the chiral limit.
    gap_rhs = sp.simplify(-2 * Gs * condensate)
    slope = sp.simplify(sp.limit(gap_rhs / M, M, 0, dir="+"))
    gcrit = sp.simplify(sp.solve(sp.Eq(slope, 1), Gs)[0])
    expected = 2 * sp.pi**2 / (Nf * Nc * Lam**2)
    assert sp.simplify(gcrit - expected) == 0

    return {
        "interaction": "G_s*(psi_bar psi)^2",
        "regulator": "hard four-dimensional Euclidean ball, p_E^2 <= Lambda^2",
        "I4": "[Lambda^2 - M^2*ln(1+Lambda^2/M^2)]/(16*pi^2)",
        "condensate": (
            "-(N_f*N_c*M)/(4*pi^2)"
            "*[Lambda^2-M^2*ln(1+Lambda^2/M^2)]"
        ),
        "gap_equation": (
            "M=(G_s*N_f*N_c*M)/(2*pi^2)"
            "*[Lambda^2-M^2*ln(1+Lambda^2/M^2)]"
        ),
        "G_crit": "2*pi^2/(N_f*N_c*Lambda^2)",
        "symbolic_check": True,
    }


def recompute() -> dict[str, object]:
    gap = derive_gap_equation()

    # Paper conventions and declared scan inputs.
    m_pl_gev = 1.22089e19  # unreduced Planck mass
    m_pl_ev = m_pl_gev * 1.0e9
    gamma_bi = 0.274
    kappa_gev_m2 = 8 * math.pi / m_pl_gev**2
    holst_factor = gamma_bi**2 / (1 + gamma_bi**2)

    # Minimal-EC exchange-channel Fierz coefficients in the paper's declared
    # anticommuting-operator convention.  The axial sign depends on the stated
    # operator ordering and is not used scientifically, so only its magnitude
    # is propagated as a scalar-threshold benchmark.
    g_scalar_over_kappa = -3 / 16
    g_axial_abs_over_kappa = 3 / 32
    assert math.isclose(abs(g_scalar_over_kappa), 2 * g_axial_abs_over_kappa)

    rows: list[dict[str, object]] = []
    expected_scalar = [
        0.238732414637843,
        0.8712861848096462,
        0.716197243913529,
        2.6138585544289384,
        2.148591731740587,
        7.841575663286815,
    ]

    # Interleave the two cutoff choices within each N_f N_c multiplicity.
    for nfnc in (1, 3, 9):
        for cutoff_label, lambda_over_mpl in (
            ("M_Pl", 1.0),
            ("M_Pl/sqrt(gamma_BI)", 1 / math.sqrt(gamma_bi)),
        ):
            # |G_scalar|/G_crit = 3 N_f N_c/(4 pi) * Lambda^2/M_Pl^2.
            scalar_ratio = (
                3 * nfnc * lambda_over_mpl**2 / (4 * math.pi)
            )
            axial_benchmark = scalar_ratio / 2
            rows.append(
                {
                    "N_f_times_N_c": nfnc,
                    "cutoff": cutoff_label,
                    "Lambda_over_M_Pl": lambda_over_mpl,
                    "scalar_abs_G_over_scalar_Gcrit": scalar_ratio,
                    "axial_coefficient_over_scalar_Gcrit": axial_benchmark,
                    "scalar_magnitude_subcritical": scalar_ratio < 1,
                    "axial_benchmark_below_one": axial_benchmark < 1,
                    "Holst_dressed_scalar_ratio_at_gamma_0.274": (
                        scalar_ratio * holst_factor
                    ),
                    "Holst_dressed_axial_benchmark_at_gamma_0.274": (
                        axial_benchmark * holst_factor
                    ),
                }
            )

    assert len(rows) == len(expected_scalar)
    for row, expected in zip(rows, expected_scalar):
        assert math.isclose(
            row["scalar_abs_G_over_scalar_Gcrit"],
            expected,
            rel_tol=2e-14,
            abs_tol=0.0,
        )

    # The sign result is independent of the magnitude diagnostic.  Dividing
    # the nonzero real scalar gap equation by M gives 1 = G_s * positive_factor;
    # therefore G_s < 0 cannot support a nonzero homogeneous scalar-mass root.
    scalar_sign = {
        "G_scalar_over_kappa": "-3/16",
        "G_scalar_GeV^-2": g_scalar_over_kappa * kappa_gev_m2,
        "sign": "negative (repulsive in the declared +G_s convention)",
        "derived_consequence": (
            "no nonzero real homogeneous scalar-mass solution for G_s<0"
        ),
        "scope": (
            "direct-channel standard mean field only; no global-potential, "
            "Fierz-independent, axial-condensation, or beyond-mean-field claim"
        ),
    }

    # Density conversion and conservative coefficient-independent bound.
    hbar_c_ev_cm = 1.973269804e-5
    n_cm3 = 100.0
    n_ev3 = n_cm3 * hbar_c_ev_cm**3
    kappa_ev_m2 = 8 * math.pi / m_pl_ev**2
    rho_bound_ev4 = kappa_ev_m2 * n_ev3**2
    rho_lambda_ev4 = (2.3e-3) ** 4
    rho_ratio = rho_bound_ev4 / rho_lambda_ev4
    contact_rho_ev4 = (3 / 16) * rho_bound_ev4
    contact_ratio = contact_rho_ev4 / rho_lambda_ev4

    density = {
        "hbar_c_eV_cm": hbar_c_ev_cm,
        "n_cm^-3": n_cm3,
        "n_eV^3": n_ev3,
        "M_Pl_eV_unreduced": m_pl_ev,
        "kappa_eV^-2": kappa_ev_m2,
        "rho_4f_conservative_bound_eV^4": rho_bound_ev4,
        "rho_Lambda_eV^4": rho_lambda_ev4,
        "rho_bound_over_rho_Lambda": rho_ratio,
        "orders_below_rho_Lambda": -math.log10(rho_ratio),
        "rho_with_3_over_16_contact_coefficient_eV^4": contact_rho_ev4,
        "contact_rho_over_rho_Lambda": contact_ratio,
        "contact_orders_below_rho_Lambda": -math.log10(contact_ratio),
        "equation_of_state_claim": (
            "none inferred from <J5>=0; composite stress tensor is state-dependent"
        ),
    }

    assert math.isclose(rho_bound_ev4, 9.9542e-80, rel_tol=6e-6)
    assert math.isclose(rho_ratio, 3.5571e-69, rel_tol=6e-6)
    assert math.isclose(-math.log10(rho_ratio), 68.45, abs_tol=0.005)

    return {
        "paper": "P1A",
        "closure": "Fierz operator-convention correction v1A.0.119",
        "planck_convention": {
            "M_Pl_definition": "unreduced M_Pl=G_N^(-1/2)",
            "M_Pl_GeV": m_pl_gev,
            "kappa_definition": "8*pi*G_N=8*pi/M_Pl^2",
            "kappa_GeV^-2": kappa_gev_m2,
        },
        "gap_derivation": gap,
        "fierz_coefficients": {
            "G_scalar_over_kappa": "-3/16",
            "G_axial_abs_over_kappa": "3/32",
            "axial_note": (
                "only |G_A| is reported because its sign depends on the "
                "declared operator ordering; the axial column uses the "
                "scalar-channel G_crit only as a coefficient benchmark and "
                "is not an axial critical threshold"
            ),
        },
        "scan_inputs": {
            "gamma_BI": gamma_bi,
            "N_f_times_N_c": [1, 3, 9],
            "cutoffs": ["M_Pl", "M_Pl/sqrt(gamma_BI)"],
            "Holst_factor_gamma2_over_1_plus_gamma2": holst_factor,
        },
        "ratios": rows,
        "scalar_sign_result": scalar_sign,
        "magnitude_result": {
            "all_scalar_rows_subcritical": all(
                row["scalar_magnitude_subcritical"] for row in rows
            ),
            "scalar_supercritical_rows": sum(
                not row["scalar_magnitude_subcritical"] for row in rows
            ),
            "maximum_scalar_ratio": max(
                row["scalar_abs_G_over_scalar_Gcrit"] for row in rows
            ),
            "maximum_axial_coefficient_benchmark": max(
                row["axial_coefficient_over_scalar_Gcrit"] for row in rows
            ),
            "verdict": (
                "blanket magnitude-subcritical claim is false; the scalar sign "
                "result remains independently valid in the declared model"
            ),
        },
        "density_bound": density,
    }


def main() -> None:
    results = recompute()
    OUT.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2))
    print(f"\nWrote {OUT}")


if __name__ == "__main__":
    main()
