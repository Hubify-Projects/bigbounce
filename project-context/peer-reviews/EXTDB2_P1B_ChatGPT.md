# EXTDB2 P1B ChatGPT — chat: https://chatgpt.com/c/6a40f191-d698-83e8-9590-5b1ba5db56b1

Provider: ChatGPT (Instant tier)
PDF md5: dbf1d9d374f4923fd33c7e30cbd36ad5
Harvested: 2026-06-28

---

Referee Report — Paper P1B

1. Recommendation: MINOR REVISIONS

The paper is unusually careful about scope, negative results, and non-claiming. I do not see a blocker or a need for major scientific rework. The main scientific risks are already mostly disclosed by the authors; remaining issues are presentation-control and reproducibility-clarity fixes.

2. BLOCKERS
None.

3. MAJORS
None requiring major revision. The paper's key limitations are explicitly stated: the ΛCDM+∆Neff run is not an ECH Boltzmann-module test; the NaMaster exercise is synthetic-sky pipeline validation, not a sky detection; the ALP result is accommodation, not prediction; and model selection is deferred.

4. MINORS

1. The w0wa material is still too prominent for a caveated cross-check. The paper repeatedly quotes +4.3σ / −3.6σ marginalized-tail distances while also stating that the DES-SN5YR × Pantheon+ product likelihood double-weights overlapping SNe and that these are not detection significances. This is acceptable only if every headline use is visibly labeled as "overlap-uncorrected diagnostic / upper-bound apparent departure."

2. Release-pairing differences should be summarized earlier. The frozen chains mix PR4 CamSpec high-ℓ with 2018 low-ℓ/lensing, while the c15 rerun uses PR4-consistent low-ℓ/lensing. The 0.04σ agreement is reassuring, but readers should see this caveat before the first results table, not mainly in later notes.

3. The NaMaster validation should avoid calling the 0.040° bias a "systematic floor" without qualification. Use "observed synthetic-pipeline bias" consistently.

4. The ALP spectator discussion remains complex and risks over-reading. The paper correctly states that the spectator-safe subset is only 13% posterior mass and that θi tuning plus non-minimal coupling are required. The conclusion should lead with "consistent but tuned and non-distinctive," before mentioning LiteBIRD detectability.

5. Repository/version reproducibility is strong but dense. The manuscript would benefit from a compact "minimum reproduction recipe" table: chain, script/artifact, command, output quantity, expected value.

6. The title may overpromise ECH relevance. Since all three analyses are compatibility or validation checks and none directly tests ECH dynamics, consider adding "proxy" or "consistency" language more prominently in the title/subtitle.

5. Strengths

1. Excellent scope discipline. The manuscript repeatedly distinguishes proxy tests, pipeline validation, and physical model prediction, avoiding several common overclaims.
2. Strong reproducibility posture. The paper gives chain counts, convergence metrics, YAML likelihood blocks, corrected artifact warnings, and explicit repository/HuggingFace locations.
3. Good treatment of negative/null results. The ∆Neff null result is framed correctly as compatibility, not evidence for the spin-torsion model.
4. Transparent handling of known weaknesses. SN-overlap, PR3/PR4 ambiguity, ALP spectator tuning, coupling burden, and lack of Bayes factors are disclosed rather than hidden.
5. Useful methodological validation. The NaMaster MC suite, sky-fraction sweep, sign test, and robustness battery are valuable technical checks even though they are not sky measurements.
