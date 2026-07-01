"""One-off driver: fixed-C_agamma=8 prior-predictive at 1e5 (parallel), merged
into alp_prior_predictive_result.json alongside the c5 headline config.
Kept as a thin wrapper so multiprocessing workers import a real module file
(macOS spawn re-imports __main__). Set ALP_NPROC to control workers."""
import json
import os
import alp_prior_predictive as m


def main():
    res2 = m.prior_predictive(100000, sample_coupling=False)
    res2["integrator_equiv_max_deg"] = float(m.verify_equivalence(20))
    path = os.path.join(os.path.dirname(__file__),
                        "alp_prior_predictive_result.json")
    d = json.load(open(path))
    d = [r for r in d if not r["config"].startswith("run1_full")]
    d.append(res2)
    json.dump(d, open(path, "w"), indent=2)
    print("=== FIXED-C (run1_full) 1e5 ===")
    print("1sig=%.4f 2sig=%.4f median|beta|=%.4f n=%d failed=%d" % (
        res2["frac_within_1sigma"], res2["frac_within_2sigma"],
        res2["median_abs_beta_deg"], res2["n_draws"], res2["n_failed"]))


if __name__ == "__main__":
    main()
