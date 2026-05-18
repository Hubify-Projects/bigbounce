# P3_v3146_R8 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1145pt
**Wall time**: 85.4s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=58530, completion=5390, reasoning=3639, total=63920

---

# Adversarial Peer Review — R8 (Focus: Headline-number provenance and load-bearing arithmetic)

## PAPER-DEE-B1 — BLOCKER  
**Location:** Abstract (“$\mathbf{378{,}280}$ unique anomalies”…), §6.4(a), §6.4(c) deferral (a)  
**Issue:** The headline unique‑object count of 378 280 is called the “canonical catalog size” yet the paper’s own deduplication arithmetic exposes a **$9{,}576$-object shortfall** from the all‑pairwise upper bound ($388{,}493 - 637 = 387{,}856$). The deferral item (a) explicitly states the headline is frozen from a previous version pending a union‑find recompute, and that recompute has not been executed. **No artifact on disk currently yields the value 378 280** — it is an unverified carry‑over. Every downstream statistic that uses this number (rates, comparisons, fractions) is therefore untethered.  
**Fix:** Either run the union‑find cluster manifest recompute and update the headline to the actual output, or remove the exact number and state “pending verification” throughout the abstract and conclusions. Do not publish a frozen‑from‑memory integer as a precise result.

---

## PAPER-DEE-B2 — BLOCKER  
**Location:** Abstract (5‑fold section), §6.4(c) item (g)  
**Issue:** The text describes a 5‑fold cross‑validation where each fold scores only its disjoint held‑out split of $9{,}400$ spectra, giving a per‑fold top‑1% set of $94$ objects. It then reports a union of $546$ objects and $399$ objects appearing in all five folds. With $5\times94 = 470$ maximum possible unique objects, $546$ union and $399$ in‑all‑five are **mathematically impossible**. The paper itself flags this as a “BLOCKER” internal inconsistency but does not correct it. The claimed stability $\bar{J}=0.862$ and the $73\%$ in‑all‑five statement directly depend on those numbers and are therefore unsound until reconciled.  
**Fix:** Resolve the inconsistency against the companion artifact at `pipelines/p3_anomaly_engine/r42_results/kfold_stability/`. Either (i) the fold scoring was done on the full $47{,}000$ pool and the text must be revised to say so, or (ii) the union/overlap statistics must be recomputed on the true disjoint‑held‑out splits. In either case, the corrected numbers must replace the current ones before the paper can be published.

---

## PAPER-DEE-M1 — MAJOR  
**Location:** Abstract (§*“Extended archival cross‑matching … yields a genuine novelty fraction of ${\sim}17.8\%$”*), §4.1 (“Archival cross‑match and genuine novelty fraction”)  
**Issue:** The headline $17.8\%$ novelty fraction ($178/1{,}000$) for the DESI top‑1,000 anomalies, obtained by cross‑matching against 20 curated all‑sky catalogs via CDS X‑Match, has **no traceable companion artifact** cited in the paper. The text says the “deeper NED+VizieR sweep” is in a companion data release but provides no file name, no query log, and no reproducible script. A number that appears repeatedly in the abstract and conclusions must be backed by a concrete digital object; currently it is an unsourced claim.  
**Fix:** Add an explicit reference to the cross‑match result file (e.g., `crossmatch_20cat_top1000.parquet` or a JSON with the 178/1000 count) and ensure it is included in the data‑availability statement. If the cross‑match was a one‑off CDS query, deposit the query and the output table as a Zenodo artifact and cite it.

---

## PAPER-DEE-M2 — MAJOR  
**Location:** Abstract (Fisher CI $[3.62,12.95]$), §5 (fnl section)  
**Issue:** The 95% confidence interval on $\sigfnl$ is obtained by plugging the exact $\alpha$-CI bounds $[-1.084,+1.464]$ into the linear relation $\sigfnl(\alpha) = 8.98 - 3.66\alpha$.  
- The slope $3.66$ is inferred from the sensitivity table in Appendix A, which itself is derived from a “linear scaling of the fiducial 7‑bin Fisher result at $\alpha=0.15$” and covers only $\alpha\in[0.05,0.50]$. **No script is cited that explicitly outputs the linear coefficient or recomputes the Fisher matrix at the far‑off bound $\alpha=1.46$**; the extrapolation goes well beyond the tabulated range.  
- The headline CI therefore depends on a hand‑derived linear approximation that is not directly verified by the Fisher code. The reader cannot reproduce the endpoints $3.62$ and $12.95$ from the provided artifacts alone.  
**Fix:** Either (a) run the full Fisher pipeline at $\alpha=-1.084$ and $\alpha=+1.464$ and report those values with a pointer to the output JSON, or (b) state clearly that the CI is based on a linear extrapolation and include a script that computes the slope and the endpoints from the sensitivity table, depositing it as a reproducibility artifact.

---

## PAPER-DEE-M3 — MAJOR  
**Location:** Abstract (“$\mathbf{378{,}080}$ point‑source object detections … the catalog‑grade tier is the $\sim\!265{,}000$ unique objects …”), §6.4(h), Table 1 footnotes  
**Issue:** The $265{,}000$ “catalog‑grade” point‑source subset is a derived figure meant to guide downstream users, but its composition is **not backed by a single table or script that sums the per‑survey counts at their chosen thresholds**: DESI uses $S>5$ (195 829), SDSS native uses $S\ge0.106$ (77 905) or $S>5$ (12), eROSITA uses $S>0.259$ (298), Gaia top‑1% (500), NEOWISE masked (419). The paper splits surveys into “gate‑PASS” and “diagnostic” categories without giving a unified per‑threshold count that adds to $\sim\!265{,}000$. A reader cannot verify the number from the numbers in the paper or from the cited artifacts.  
**Fix:** Produce a summary table (e.g., an appendix) that lists, row‑by‑row, which survey contributes how many objects to the catalog‑grade tier under the stated criteria, and point to the exact parquet files that yield those counts. The abstract should cite that table so that the provenance is explicit.

---

## PAPER-DEE-M4 — MINOR  
**Location:** Abstract (“LAMOST native contributes $\sim\!113{,}000$ additional unique objects … after $7$‑way $5''$ dedup overlap, the LAMOST‑attributable headline contribution is $\sim 113{,}000$ objects”), §3.4 footnotes  
**Issue:** The $113{,}000$ figure is described as approximate and the precise attribution is deferred to the released cluster manifest `pathc_multi_survey_matches.parquet`. While acceptable for an approximate statement, the paper’s abstract and conclusions use this number repeatedly without a cross‑reference to the manifest that would allow exact verification. It would be a minor nit if all other numbers were solid, but in a paper with multiple provenance problems it adds to the overall opacity.  
**Fix:** In the abstract and the conclusions, add a brief parenthetical such as “(exact count: 113 342 from native re‑score, reduced by $X$ after $5''$ dedup; see `pathc_multi_survey_matches.parquet`)” so the reader knows where to find the hard number.
