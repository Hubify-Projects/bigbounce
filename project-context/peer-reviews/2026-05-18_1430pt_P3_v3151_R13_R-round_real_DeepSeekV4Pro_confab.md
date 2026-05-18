# P3_v3151_R13 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1430pt
**Wall time**: 264.2s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=61726, completion=9036, reasoning=7772, total=70762

---

# Adversarial Peer Review — Numbers Provenance Audit

## PAPER-DEE-B1 — BLOCKER: Headline unique-anomaly count 378,280 unverifiable and internally contradictory

**Location:** Abstract, title, Sec. 4.3 (Cross‑Survey Matches), Sec. 6.4 deferral (a), data‑availability statement, Table 1 footnote.

**Issue:** The paper’s most load‑bearing number — the catalog size of 378,280 unique anomalies — is acknowledged to be a “frozen” placeholder pending a union‑find recompute (deferral (a)). The text states: “The published headline of 378,280 unique physical objects remains frozen at the previously‑reported value pending a full intra‑survey duplicate recompute (the residual 9,576‑object shortfall …)”. The only deduplication evidence provided is 637 inter‑survey coincidences, which implies at most 387,856 unique objects, not 378,280. Simultaneously, the data‑availability appendix claims `pathc_unique_objects_no_act.parquet` already exists with 378,280 rows, contradicting the statement that the value is frozen and not yet recomputed. No script, cluster manifest, or artifact on disk is cited that actually produces 378,280 from the 388,493 detections; the arithmetic required to close the 9,576 gap is absent.

**Fix:** Remove 378,280 from title, abstract, and conclusions until the union‑find recompute is executed and the on‑disk artifact is published and internally consistent with the described deduplication steps. Alternatively, if the number is an artifact of a previous run, provide the exact script and input data that produced it and reconcile the gap explicitly.

---

## PAPER-DEE-M1 — MAJOR: Genuine novelty fraction 17.8 % lacks a traceable on‑disk artifact

**Location:** Abstract, Sec. 4.2 (“Archival cross‑match and genuine novelty fraction”), Sec. 6.3 Limitations, Conclusions item 2.

**Issue:** The paper prominently quotes “a genuine novelty fraction of ∼17.8 % (178/1,000)” for DESI top‑1,000 anomalies cross‑matched against 20 all‑sky catalogs via CDS X‑Match. No JSON, CSV, or parquet file is named that contains the per‑object cross‑match verdicts; the text merely defers to “the deeper NED+VizieR sweep detailed in the companion data release.” Given that this is a primary discovery‑rate figure, its provenance must be auditable.

**Fix:** Add a specific artifact path (e.g., `crossmatch/dr1_top1000_cds_xmatch.parquet`) to the paper and ensure the file is deposited with the data release. The text must explicitly state which file contains the 178/1,000 determination so a reader can reproduce it.

---

## PAPER-DEE-M2 — MAJOR: Scale‑comparison multipliers (141×, 73×) depend on the unverifiable 378,280 count

**Location:** Abstract, Conclusions item 1.

**Issue:** The abstract reports “~141× the size of the largest prior … 378,080/2,685 = 140.8 ≈ 141” and “a ~73× increase … 195,829/2,685 = 72.9”. The 378,080 is derived from 378,280 − 200; both the point‑source tier and the headline count are unverifiable per PAPER-DEE-B1. Consequently, the central scale claims are not reproducible from currently documented data.

**Fix:** After resolving PAPER-DEE-B1, recalculate the multipliers from the verified unique‑object count. Until then, insert a caveat that the scale numbers are preliminary pending deduplication recompute, or remove them.

---

## PAPER-DEE-N1 — nit: “37.3 million sources” ambiguity with ACT inclusion

**Location:** Abstract, first sentence.

**Issue:** The abstract says “applying the BigAE autoencoder framework to 37.3 million sources and CMB map patches across seven retained astronomical archives … with ACT DR6 carried only as a quarantined cross‑transfer artifact … excluded from all headline numbers.” The total source count for the seven retained surveys sums to 37,272,042; adding ACT’s 20,000 patches yields 37,292,042, which rounds to 37.3 million. It is unclear whether the stated 37.3 million includes the quarantined ACT patches or not. The text should explicitly reference which table row yields the number and whether ACT is included.

**Fix:** Add a footnote or an inline clarification: “37.3 million = 37,272,042 sources from the seven retained surveys + 20,000 ACT patches (quarantined).” Or adjust the round number to match exactly the seven‑survey sum.

---

## PAPER-DEE-N2 — nit: Injection‑recovery gate classification mixes mask test with autoencoder tests

**Location:** Abstract, line “Six injection‑recovery gates yield 3 PASS (SDSS continuum‑dip, Planck CMB native, NEOWISE) …”, and Table 1 footnotes.

**Issue:** The NEOWISE “gate PASS” is not an injection‑recovery test on the autoencoder but a separate ecliptic‑mask specificity/sensitivity test (rejection of polar‑cap anomalies). Treating it as a parallel injection‑recovery gate for the autoencoder is a category mismatch that may mislead readers about the uniformity of the validation protocol.

**Fix:** Clearly separate the NEOWISE mask validation from the autoencoder injection‑recovery gates. For example, list the autoencoder injection‑recovery results separately and state that NEOWISE passed a spatial‑mask fidelity gate rather than an autoencoder sensitivity gate.
