## (1) VERDICT: MINOR REVISIONS

## (2) Numbered issues

1. **MINOR — NEW verified catalog-description error.**  
   **Location:** Page 4, §4.3, “Sky and positional coverage.”  
   **Claim:** “five of six coarse equal-area declination bins are occupied.”  
   **Evidence:** Recomputing the stated six equal-area bins in \(\sin(\delta)\) gives counts \([0,0,47,38,23,73]\): **four**, not five, occupied bins. The frozen `SELECTION_AUDIT.json` independently records `occupied_equal_area_dec_bins: 4`.  
   **Required fix:** Change “five” to “four.” If a different bin convention was intended, define its edges and regenerate the corresponding audit value. This does not affect selection or the catalog’s central claim.

2. **MINOR — NEW verified reproducibility-validation gap.**  
   **Location:** Page 11, Appendix C, Table 6, “Strict cohort count”; associated independent validator.  
   **Claim:** The strict 181-object cohort is independently reproduced from checkpoint parts.  
   **Evidence:** The validator constructs `final_expected` from the 2,448 primary matches and confirms only that `len(final_expected) == len(final) == 181`. It never asserts equality of released and expected identifiers. Thus a different 181-row catalog satisfying the per-row gates could pass. My independent comparison finds that the actual release is correct: its `(cluster_id, TARGETID, fits_row)` set exactly equals the strict checkpoint-derived set.  
   **Required fix:** Add an explicit set-equality assertion between `final_expected` and the released catalog, preferably over `(cluster_id, targetid, fits_row)`, then regenerate the audit report and manifest in a successor immutable release.

3. **MINOR — NEW verified audit-reporting defect.**  
   **Location:** Page 6, §6.2; page 11, Appendix C, Table 6, “Remote parity”; `SELECTION_AUDIT.json`.  
   **Claim:** Eight sampled 1-MiB ranges passed local-versus-remote parity testing.  
   **Evidence:** The released validator does not issue range requests or compare those byte ranges. It writes `remote_range_parity.status = "PASS"`, the eight offsets, and the claimed method unconditionally. The frozen closure audit documents a separate manual comparison, and the full local FITS hash independently equals the [official DESI checksum](https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/redux_iron_zcatalog_v1.sha256sum), so this does not invalidate FITS provenance. It does make the machine-generated PASS non-reproducible from the bundled validator.  
   **Required fix:** Either implement and fail on the eight range comparisons, or relabel this entry as externally supplied audit evidence and preserve the observed local/remote sample digests.

4. **MINOR — non-load-bearing publication and attribution corrections.**  
   **Location:** Pages 7–8, Acknowledgments and References [1], [4].  
   **Evidence:** The acknowledgments omit the prescribed DESI acknowledgment. Reference [1] dates the DR1 paper to 2025, whereas DESI identifies it as DESI Collaboration et al. (2026). Reference [4] gives “547, 2,” but the publication locator is volume 547, issue 2, article `stag010`. See the [DESI acknowledgment requirements](https://data.desi.lbl.gov/doc/acknowledgments/) and the [Nicolaou et al. publication record](https://academic.oup.com/mnras/article/547/2/stag010/8416432).  
   **Required fix:** Insert the prescribed DESI acknowledgment and correct both references.

The explicitly stated limitations—no novelty claim, no anomaly confirmation, no population or occurrence-rate inference, no cosmological inference, and no exact recovery of historical neural scores—are appropriate scope boundaries, not defects. I found no additional load-bearing editorial issue.

## (3) Central-claim support

**SUPPORTED.** The reviewed PDF has the specified SHA-256 and matches the frozen commit. Independent recomputation establishes:

- 28,425,963 scanned rows and 20,299,155 historical science-bit rows.
- 2,468 one-arcsecond matches, of which 2,448 are global primaries.
- Removal of 2,267 nonzero-`ZWARN` primaries leaves exactly **181** candidates; \(2267/2448=92.6062\%\).
- The released 181-row set exactly equals the checkpoint-derived strict set.
- All 181 `TARGETID`, FITS-row and candidate keys are unique; every selection gate passes.
- All 18 carried DESI fields match the pinned FITS source rows exactly.
- The reported class, targeting, redshift, separation, sky-hemisphere and score summaries reproduce, except for the four-versus-five declination-bin error above.
- Historical inputs reproduce the stated 378,480 clusters, 190,015 DESI-containing clusters and 195,829 anomaly rows; all released historical-lineage fields match their pinned inputs.
- Every manifest-listed payload hash and size passes; the full 22.37-GB FITS SHA-256 is `2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b`, matching DESI’s official checksum.

The frozen closure evidence records tag `p3-v3.2.0-r1` at commit `983209ae606be311d9bda9f0258716d56386ee69` and 11/11 byte-parity checks. I could not freshly download that exact tag in this review environment, so remote-tag parity is supported documentarily rather than by a new remote fetch; all local release and manifest claims were independently verified.

## (4) Fresh verified MAJOR blocker

**No. I found no fresh verified MAJOR blocker.**