# INT API Review — P3APJS unknown-version — openai (gpt-5.5)
paper: P3APJS  version: unknown-version  model: gpt-5.5
provenance: commit=3f5582c2  pdf=pipelines/p3_anomaly_engine/paper3_apjs.pdf  sha256=3dc9d45862ccaad2ae7c61db991e5a5b7025390876c492905e127bdde3308db8
modality: native-PDF (Files API input_file)
UTC: 2026-07-14T11:48:40.005222Z  |  latency: 70.2s  |  attempt: 1
usage: {"input_tokens": 11233, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 4452, "output_tokens_details": {"reasoning_tokens": 2588}, "total_tokens": 15685}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) **VERDICT: MINOR REVISIONS**

(2) **Numbered issues**

1. **[MINOR] Page 7, Data Availability: “immutable correction tag” wording is too strong.**  
   **Claim:** The release bundle is published under the “immutable correction tag” `p3-v3.2.0-r1`, resolving to commit `983209ae606be311d9bda9f0258716d56386ee69`.  
   **Evidence:** The manuscript also gives the exact commit hash, which is the genuinely load-bearing provenance identifier. A Hugging Face/Git tag is not intrinsically immutable in the same sense as a content-addressed hash unless repository-side tag protection and archival guarantees are documented. This is not a catalog defect because the commit hash is supplied.  
   **Required fix:** Rephrase to “pinned tag and commit” or “release tag currently resolving to commit …”; make the commit hash the authoritative immutable identifier. If the tag is protected by repository policy, state that explicitly.

2. **[MINOR] Page 7, Data Availability: the copy-paste build command should not split the SHA-256 argument.**  
   **Claim:** The command supplies the FITS SHA-256 split across two physical lines and states that “the shell joins the two physical hash lines because the first ends in a backslash.”  
   **Evidence:** The exposed hash is internally consistent and has 64 hex characters:  
   `2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b`.  
   However, a backslash-newline continuation can be fragile when copied from PDF if whitespace is introduced after the backslash or before the continuation line. Since this hash is load-bearing for provenance validation, the executable example should minimize copy-paste ambiguity.  
   **Required fix:** Put the full 64-character hash on one physical line in the command, or assign it first, e.g. `FITS_SHA256=...`, then pass `--fits-sha256 "$FITS_SHA256"`.

3. **[MINOR] Sections 3.1, 6.1, Appendix B: specify the exact FITS HDU/extension used.**  
   **Claim:** The validator rereads the public FITS row values from `zall-pix-iron.fits`, and Appendix B says `fits row` is the zero-based row in the public DR1 `ZCATALOG` extension.  
   **Evidence:** The manuscript is reproducible in substance, but the exact HDU name/number is only implicit or appears late. Since the release relies on exact zero-based FITS row numbers, the HDU must be unambiguous.  
   **Required fix:** In Section 2.2 or 3.1, state explicitly that all row numbers refer to the `ZCATALOG` binary-table extension of `zall-pix-iron.fits`, preferably with the HDU name and/or index used by the scripts.

4. **[MINOR] Sections 2.1, 3.1, 3.3, 4.3, Appendix B: clarify score-to-spectrum association for multi-member historical clusters.**  
   **Claim:** When a cluster contains more than one DESI anomaly member, the canonical historical member is chosen by highest score, while the public DESI row is recovered by nearest match to the cluster coordinate. The catalog carries the historical score as ranking metadata.  
   **Evidence:** This is explicitly scoped and not a hidden defect. The paper repeatedly states that the score is not recalibrated and that a 1″ positional association is not proof of physical identity. Still, the released `match_separation_arcsec` is target-to-cluster separation, not necessarily target-to-canonical-original-member separation. For clusters with multiple DESI historical members, a user could wrongly interpret `original_score` as belonging uniquely to the recovered public spectrum.  
   **Required fix:** Add one sentence in Section 3.3 or 4.3 stating that the positional cut is to the cluster coordinate, not necessarily to the canonical original anomaly-member coordinate. Ideally report how many of the final 181 have `n_detections > 1`, and either add or document a target-to-`original_ra/dec` separation column if already present/computable.

5. **[MINOR] Section 6.3 and Appendix C: reconcile “11 remote files” versus “10/10 files” in the manifest audit more explicitly.**  
   **Claim:** Data Availability says all 11 remote files were downloaded and verified, while Appendix C says “Payload manifest PASS: 10/10 files,” and Section 6.3 says the manifest excludes itself.  
   **Evidence:** These statements are consistent if the 11 remote files are 10 payload files plus the self-excluded manifest. The manuscript does say the manifest excludes itself, so this is not an error. But the two numbers appear in different places and may look like a discrepancy.  
   **Required fix:** Add a parenthetical such as “10 payload files plus the manifest itself, for 11 remote files total.”

6. **[MINOR] References and journal style need cleanup before publication.**  
   **Claim:** The references use compact bracketed style and include future/incomplete bibliographic entries, e.g. DESI DR1 listed as Astron. J. 2025 with arXiv only, and Nicolaou et al. listed as MNRAS 547, 2 (2026).  
   **Evidence:** This does not affect the catalog result, but ApJS production will require standard bibliographic formatting and verified final publication metadata where available.  
   **Required fix:** Update references to the current ApJS/AAS style and verify all volume/page/article identifiers.

**Arithmetic and internal consistency checks recomputed from the PDF**

- Waterfall:  
  `2,468 − 20 = 2,448` global-primary matches.  
  `2,448 − 2,267 = 181` released candidates.  
  Total exclusions after the 1″ parent cohort: `2,468 − 181 = 2,287`, matching the conclusion.
- Released fraction:  
  `181 / 2,468 = 0.0733387 = 7.33%`, as stated.
- ZWARN reduction among global-primary matches:  
  `2,267 / 2,448 = 0.92606 = 92.6%`, as stated.
- Separation tiers:  
  `170 + 11 = 181`, internally consistent.  
  Tail fraction is `11 / 181 = 6.08%`; high-consistency fraction is `170 / 181 = 93.92%`.
- SPECTYPE counts:  
  `157 GALAXY + 23 QSO + 1 STAR = 181`, internally consistent.
- Program counts:  
  `162 dark + 19 bright = 181`, internally consistent.
- Target-bit labels:  
  `157 + 18 + 7 + 1 + 1 = 184`, not a defect because overlap is explicitly stated.
- Redshift-bin counts:  
  `2 negative + 36 + 36 + 76 + 8 + 13 + 10 = 181`, internally consistent.  
  Positive-redshift subset: `181 − 2 = 179`, as stated.
- North/south sky counts:  
  `134 + 47 = 181`, internally consistent.
- FITS SHA-256 string exposed in the manuscript is a 64-character hexadecimal value and is consistently repeated between Section 2.2 and the build command, modulo line wrapping.

(3) **Whether the central catalog/reproducibility claim is supported**

Yes. Within the four corners of the frozen PDF, the central claim is supported: the manuscript presents a sharply scoped DESI DR1 candidate-catalog recovery yielding **181 unique public DESI TARGETIDs** from **2,448 global-primary positional matches** after the declared **ZWARN=0** gate, with a reproducible positional join, explicit science-bit parent definition, deterministic duplicate handling, source-row rejoin validation, checksum/provenance accounting, and a release bundle pinned by tag plus commit hash.

The paper does **not** overclaim astrophysical novelty, anomaly confirmation, occurrence rates, purity, or recovery of the historical neural-network scores. Those are correctly treated as limitations rather than defects.

(4) **Whether any fresh verified MAJOR blocker exists**

No. I find **no fresh verified MAJOR blocker** in the frozen P3 v3.2.0-apjs manuscript as a focused DESI DR1 candidate-catalog and reproducibility paper. The required changes are documentation/provenance-clarity and publication-polish issues, not failures of the central catalog construction claim.