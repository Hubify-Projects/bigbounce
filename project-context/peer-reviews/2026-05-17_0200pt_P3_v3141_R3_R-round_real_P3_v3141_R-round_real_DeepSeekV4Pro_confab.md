# P3_v3141 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_0200pt_P3_v3141_R3_R-round_real
**Wall time**: 139.3s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=55788, completion=8176, reasoning=6191, total=63964

---

## Adversarial Peer Review — P3 v3.1.41 (Multi-Survey Anomaly Catalog)

**Reviewer**: DeepSeek-V4-Pro (confabulation‑hunter, reasoning mode)  
**Round**: R3, adversarial focus on numerical provenance and internal consistency  
**Criteria**: PRD/MNRAS‑referee strictness; every load‑bearing scalar must be traceable to a specific JSON/script/dataset on disk.

---

### Finding 1 — BLOCKER: Headline catalog size (378,280) rests on unreconciled dedup arithmetic

**ID**: PAPER‑DEE‑B1  
**Section**: Abstract, §4.3, §7, Table 1 footnotes, §6.4 caveat (a)  
**Issue**:  
The paper states that the 7‑way positional deduplication collapses 388,493 survey‑level detections to 378,280 unique objects, implying 10,213 duplicate detections removed. Simultaneously, §4.3 reports only 637 multi‑survey coincidence clusters (all pairwise). The two numbers are incompatible: 637 coincidences cannot account for 10,213 removed duplicates. The paper itself acknowledges this mismatch as an unresolved deferral (§6.4, item (a)), yet the 378,280 figure is used throughout the abstract, conclusions, and as the primary catalog size. The dedup script’s output (`pathc_dedup_summary_no_act.json`) is not publicly described, and the union‑find cluster manifest that would reconcile the counts is explicitly deferred. A central headline number derived from an internally inconsistent pipeline is not acceptable for a PRD‑class submission.

**Fix**:  
Re‑run the positional dedup with explicit per‑cluster multiplicity reporting and publish the cluster manifest. Until the arithmetic is reconciled, either remove the 378,280 headline and report only the raw survey‑level sum (388,493) with a clear warning, or state the number as provisional with a prominent caveat in the abstract.

---

### Finding 2 — MAJOR: Genuine novelty fraction (17.8%) has no traceable artifact

**ID**: PAPER‑DEE‑M1  
**Section**: Abstract, §4.1 (“Archival cross‑match and genuine novelty fraction”), §7  
**Issue**:  
The abstract and conclusions prominently feature “∼17.8%” as the genuine novelty fraction (178/1,000 DESI top‑1,000 anomalies). The text states this comes from a cross‑match against 20 curated all‑sky catalogues via CDS X‑Match, with the full characterization “detailed in the companion data release”. However, the data availability section (§Acknowledgments) lists only the Path‑C anomaly catalog and per‑survey parquet files; no cross‑match result file, CDS query log, or script that produces the 17.8% figure is mentioned. A reader cannot reproduce the number from the supplied artifacts. For a load‑bearing discovery‑rate claim, this is insufficient.

**Fix**:  
Include the cross‑match output table (e.g., `desi_top1000_xmatch_20catalogs.parquet` or a CSV with match flags) in the HuggingFace deposit and cite its exact filename. Alternatively, if the cross‑match was performed interactively and cannot be exactly reproduced, downgrade the claim to an approximate estimate and remove the precise 17.8% from the abstract.

---

### Finding 3 — MAJOR: OOD anomaly‑rate preservation claim is unsubstantiated

**ID**: PAPER‑DEE‑M2  
**Section**: §2.2 (“In‑sample scoring and held‑out validation”), §6.4 caveat (b)  
**Issue**:  
The paper asserts that “the 0.87% DESI anomaly rate is preserved on this independent OOD sample” (the 100,000‑spectrum SPARCL retrieval). However, the OOD results only report the MSE distribution (median 0.178, IQR, percentiles) and state that the S>5 threshold corresponds to MSE≈0.143. No fraction of the 100k spectra with S>5 (or MSE>0.143) is given. The median OOD MSE (0.178) is above the threshold, but that does not guarantee the anomaly rate is 0.87%; the actual fraction could be substantially different. The paper itself lists this as a deferred recompute item (§6.4 (b)). Claiming preservation without the number is misleading.

**Fix**:  
Compute and report the exact fraction of the 100k OOD spectra that exceed the S>5 threshold (or the equivalent MSE cut). If the fraction deviates from 0.87%, adjust the text accordingly. Until then, remove the unsupported claim.

---

### Finding 4 — MAJOR: SDSS DR18 table row presents cross‑transfer count as primary, despite native retrain superseding it

**ID**: PAPER‑DEE‑M3  
**Section**: Table 1, §3.3, §6.4  
**Issue**:  
Table 1 lists SDSS DR18 with N_anom = 77,905 and a rate of 3.38%, but this is the cross‑transfer baseline. The Path‑C native retrain (val_loss 0.0311, gate PASS) yields only 12 sources at S>5, and a top‑1% slice of 19,253. The table footnote explains that the native counts supersede the cross‑transfer values, yet the main table row still displays the inflated cross‑transfer number. A reader skimming the table will quote 77,905 as the SDSS anomaly count. The abstract does not repeat this number, but the table is the primary data summary and should reflect the canonical Path‑C results.

**Fix**:  
Replace the SDSS row with the Path‑C native count (e.g., 19,253 for the top‑1% slice, or 12 for the S>5 cut, with clear labelling). Move the cross‑transfer 77,905 to a separate “before/after” diagnostic table or a footnote only.

---

### Finding 5 — minor: Many bibliography entries lack DOIs, hindering automated verification

**ID**: PAPER‑DEE‑N1  
**Section**: References  
**Issue**:  
Several key references (e.g., DESI DR1, LAMOST DR10, NEOWISE, SPHEREx proposal, Phinney 2001) are given only as URLs or arXiv IDs without DOIs. A Shamir‑DOI‑class regression sweep (as requested) cannot be performed on these entries. While not a scientific error, it reduces the paper’s compliance with journal data‑citation standards and makes reference validation labour‑intensive.

**Fix**:  
Add DOIs for all references that have them (e.g., DESI DR1 has a DOI: 10.5281/zenodo.XXXXXXX; LAMOST DR10: 10.1088/1674-4527/...). For arXiv preprints, include the arXiv ID in a standard `\doi` or `\eprint` field.

---

### Finding 6 — minor: HuggingFace catalog version not pinned; public access pending

**ID**: PAPER‑DEE‑N2  
**Section**: Acknowledgments (Data availability)  
**Issue**:  
The catalog is deposited at `https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog` but is marked “private pending arXiv acceptance”. No commit hash, dataset version, or DOI is provided. A reviewer cannot inspect the data to verify the counts. Even after acceptance, without a version tag, future changes could silently alter the numbers.

**Fix**:  
Mint a Zenodo DOI for the exact dataset version used in the paper and include it in the data availability statement. If the repository must remain private during review, provide a temporary anonymous access link or a checksum manifest.

---

### Truth‑Audit Summary

| Finding ID       | Class   | Load‑bearing scalar affected            | Traceable artifact? | Status                               |
|------------------|---------|-----------------------------------------|----------------------|--------------------------------------|
| PAPER‑DEE‑B1     | BLOCKER | 378,280 unique anomalies                | No (dedup arithmetic unreconciled) | Must fix before publication          |
| PAPER‑DEE‑M1     | MAJOR   | 17.8% genuine novelty fraction          | No (cross‑match file missing)     | Provide artifact or downgrade claim  |
| PAPER‑DEE‑M2     | MAJOR   | 0.87% anomaly rate preserved on OOD     | No (OOD fraction not reported)    | Compute and report actual fraction   |
| PAPER‑DEE‑M3     | MAJOR   | SDSS anomaly count (77,905 in Table 1)  | Misleading (native count is 12/19k) | Replace with Path‑C native count     |
| PAPER‑DEE‑N1     | minor   | Reference DOIs                          | Partially missing                  | Add DOIs where available             |
| PAPER‑DEE‑N2     | minor   | Catalog version                         | Not pinned                         | Mint DOI or commit hash              |
