# RBEXT P3 Gemini — chat: https://gemini.google.com/u/0/app/4d5c72c084a2edd0
VERDICT: MAJOR REVISIONS

Provider: Gemini (Flash regular tier)
PDF: RBEXT_P3.pdf | md5: f6b8d9a5e16fc5f4f3301433c9c556dc
Harvested: 2026-06-29

---

Recommendation: MAJOR REVISIONS

Summary: This manuscript presents a comprehensive multi-survey anomaly detection pipeline using a deterministic symmetric fully connected autoencoder (BIGAE) applied to seven major astronomical archives (DESI DR1, SDSS DR18, LAMOST DR10, eROSITA DR1, Planck CMB, Gaia DR3, NEOWISE) comprising over 37 million sources. The key deliverable is a recommended tier of 269,317 unique anomalies. The paper also explores downstream cosmological applications (fNL constraints and NANOGrav consistency).

General Evaluation: The scale is highly impressive — potentially the largest unified multi-archive autoencoder anomaly detection in astronomy to date. The Path-C Rebuild Protocol and injection-recovery tests provide a robust framework. However, critical issues regarding data reproducibility, missing provenance, and irreproducible score axes must be thoroughly addressed.

Key Major Comments

The eROSITA Score Axis Irreproducibility:
In Section II B, feature scaling statistics were fit over the full sample rather than exclusively on the training split, introducing minor information leakage from validation and extreme tail subsets. Although the author runs a robustness check demonstrating global Spearman correlation (ρ=0.94), extreme-tail membership suffers ~15% churn. The author must add an explicit warning in the user guide section of the catalog manifest so downstream investigators do not misinterpret threshold cutoffs near these boundaries.

Minor / Typographical Comments

- Clarity of "S" vs "z": Ensure the note clarifying S = statistical z-score vs. z = astrophysical redshift is uniformly consistent across all figures and axes.
- Figure 3 Dynamic Range: The right panel shows cross-transfer SDSS scores blowing up to S∼10^11. The text should emphasize earlier in Section III C that this vanishes upon native retraining (S < 14).
- Data Availability: The Hugging Face link and GitHub repository are commended. Ensure the placeholder Zenodo DOI is fully minted upon final acceptance.
