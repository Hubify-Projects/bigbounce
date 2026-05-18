# P3_v3152_R14 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1500pt
**Wall time**: 277.5s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=62060, completion=8895, reasoning=8019, total=70955

---

## Adversarial Peer Review — Numerical Provenance Audit (v3.1.52)

**Blocker:** PAPER‑DEE‑B1  
**§4.3, Abstract, Conclusions (headline unique count)**  
The canonical unique‑anomaly count **378 280** (and its point‑source partition **378 080**) is presented as the primary result of the deduplication, but the paper itself states that the current dedup artifact `pathc_dedup_summary_no_act.json` only identifies 637 pairwise cross‑survey coincidences — yielding **387 856** unique objects — and that “the published headline … remains frozen at the previously‑reported value pending a full intra‑survey duplicate recompute”. The abstract and conclusions use 378 280 without qualifying that it is **not** the output of the delivered dedup script. No on‑disk file that produces 378 280 is cited.  
**Fix:** Re‑run the full union‑find dedup (including intra‑survey duplicates) against the per‑survey native‑retrained parquets so that the number becomes reproducible from a labelled artifact, or replace the headline with the actual dedup output (387 856) and clearly note that intra‑survey duplicates remain unresolved.

**Major:** PAPER‑DEE‑M1  
**Abstract, §4.3, Table I (cross‑transfer baseline total)**  
The abstract says: “The initial cross‑transfer baseline identified 319 443 anomaly detections (across the seven retained surveys; ACT~DR6 excluded).” The per‑survey cross‑transfer counts in Table I sum to **319 243** when ACT is excluded (195 829 + 77 905 + 44 075 + 298 + 200 + 500 + 436). The table row itself lists 319 443 and is labelled “ACT‑incl. archival”, so the abstract’s parenthetical “ACT~DR6 excluded” is arithmetically incompatible with the number quoted.  
**Fix:** Correct the abstract to either state the total for the seven retained surveys as **319 243** or clarify that 319 443 includes ACT and represents the pre‑quarantine baseline.

**Major:** PAPER‑DEE‑M2  
**§4.1, Abstract, §7 (genuine novelty fraction 17.8 %)**  
The headline novelty claim “178/1 000 (17.8 %) absent from all 20 curated all‑sky catalogs” is not backed by a referenced companion artifact or script output. The description mentions CDS X‑Match but gives no file path (e.g., a list of the 178 objects with cross‑match flags) that would allow reproducibility. This is a load‑bearing discovery‑rate number in the abstract and conclusions.  
**Fix:** Deposit the cross‑match result artifact (e.g., `desi_top1000_xmatch_20catalogs.json`) alongside the catalog release and cite its path in the paper.

**Minor:** PAPER‑DEE‑m1  
**Abstract (§5, “5 384 QSO‑candidate sample”)**  
The sample of 5 384 objects used for the empirical α measurement is mentioned but a direct reference to the on‑disk list (e.g., `qso_candidate_sample.fits`) is omitted. The companion artifact for α is cited, but whether it contains the full membership list is not stated, making it difficult to verify that the count matches.  
**Fix:** Add a sentence confirming that the `alpha_empirical_results.json` artifact includes the exact list of 5 384 target IDs or point to a separate membership file.

No other blocker‑grade provenance failures were identified in the abstract or conclusions; the Fisher‑positivity envelopes, the DESI anomaly count, the per‑survey native re‑score totals, and the NANOGrav MCMC results all point to on‑disk artefacts or are algebraically consistent with the cited inputs.
