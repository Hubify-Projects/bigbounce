# paper3 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R25_P3_v3_1_56
**Wall time**: 164.6s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=64180, completion=4836, reasoning=4113, total=69016

---

# Adversarial Peer Review — Provenance Audit

## Finding 1: PAPER-DEE-PROV-1 (MAJOR)
**Section:** Abstract, Sec.~4.1, Sec.~7  
**Issue:** The headline “genuine novelty fraction of ∼17.8 % (178/1,000)” for the DESI top‑1,000 anomalies is derived from a live CDS X‑Match query against 20 curated all‑sky catalogues. No on‑disk JSON/CSV/Parquet file or script output is cited anywhere in the paper or the data‑availability statement; the user cannot verify that exactly 822 objects were identified and 178 remain novel without re‑running the service call, which is not archival.  
**Fix:** Deposit a companion CSV (`top1000_desi_crossmatch_results.csv`) mapping each of the 1,000 TARGETIDs to match/non‑match flags across the 20 catalogues, together with the derived 178 count. Cite the file explicitly in Sec.~4.1 and the data‑availability paragraph.

---

## Finding 2: PAPER-DEE-PROV-2 (minor)
**Section:** Sec.~4.1, Sec.~7 (SIMBAD‑unmatched fractions)  
**Issue:** The per‑survey and aggregate “SIMBAD‑unmatched fraction” numbers (58.8 % overall, per‑survey rates from 27 % to 99 %) are not accompanied by an artefact file that carries the pre‑computed match status. The catalog release provides object coordinates but no SIMBAD‑cross‑match column; therefore the quoted fractions cannot be reproduced without a fresh SIMBAD cone search, which is not part of the deposited pipeline.  
**Fix:** Either append a `simbad_match` boolean column to the per‑survey anomaly parquets (or a separate summary JSON), or provide a script that exhaustively replicates the cone search described in the paper, together with a cached result file. Update Sec.~4.1 to point to that artefact.

---

## Finding 3: PAPER-DEE-PROV-3 (nit)
**Section:** Abstract, Sec.~3.1, Table I  
**Issue:** The abstract states “0.87 %” anomaly rate for DESI DR1, but the denominator (22 504 897 spectra) is not shipped with the anomaly catalog; a reader cannot directly confirm the rate from the released data alone. While the total survey size is public knowledge, the provenance chain is incomplete when the number is presented as a derived property of the deposited catalog.  
**Fix:** In the data‑availability paragraph, include a short provenance note such as “The DESI‑DR1 total source count (22 504 897) was obtained from the official DESI DR1 documentation; dividing the 195 829‑row anomaly catalogue by this number yields the 0.87 % rate.” Alternatively, provide a companion summary JSON that records both the numerator and denominator explicitly.

---

### Assessment
No blocker‑grade provenance gaps were found — the core catalog object count, multi‑survey deduplication arithmetic, α and f_NL measurements, and NANOGrav MCMC result are all traceable to named on‑disk artefacts. The three findings above address the few headline numbers that currently lack an explicit, citable file or reproducible snapshot.
