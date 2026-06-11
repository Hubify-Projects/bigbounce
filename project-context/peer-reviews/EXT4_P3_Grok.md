# EXT4 P3 — Grok Heavy (in-thread delta round 4)
**Chat**: https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=de56f195-4cae-4dc6-bc3e-f9dbf4de9b54
**PDF**: paper3_anomaly_catalog_v3.1.95.pdf (799d13fc) · harvested 2026-06-11 15:57 PT · loc de56f195
---
Thought for 31s

Referee Report: MNRAS-style (target: MNRAS or PRD/JCAP)
Manuscript: v3.1.95 (28 pp., updated from v3.1.91)

1. CLOSURE VERIFICATION (previous BLOCKERS/MAJORS only)
BLOCKER 1 (eROSITA score-axis irreproducibility + “novel” over-claim, §III E + Table I + Table IV + top-5 table): CLOSED. Explicit “membership-only tier” / “n = 298 membership list only” + “per-object SBigAE score axis non-reproducible” everywhere; the SBigAE column is now fully stripped from the top-5 table (Table IV); 203 sources correctly labeled “203 SIMBAD-unmatched membership-list sources” at all occurrences. No regression.
BLOCKER 2 (headline number mixing tiers + like-for-like/scale claims, abstract + §I + §III A + §VII): CLOSED. Abstract and introduction now lead with the recommended catalog-grade tier (269 317 / 269 117 point-source) and 6-way dedup provenance. The DESI 73× claim is retained only as the disclosed full-spectra-stream statement and is immediately qualified by the newly computed science-class-restricted recount (only 2,468 / 190,015 clusters = 1.3% at 1″ on primary-science-class spectra; ≈0.9× the Liang et al. benchmark; ∼98.7% on non-primary / sky-fiber / filler spectra). The recount is now in the abstract, a new dedicated Table II (“DESI science-class recount at a glance”), §III A, discussion, and conclusions. No regression.
All previous MAJORS (novelty framing, Fisher language, NANOGrav over-statement, foreground claim, 20-vs-18 catalogs, z-provenance, LAMOST denominator, TARGETTYPE/SPECTYPE clarity, χ² spatial test, fNL envelope, SMBHB Bayes factor): CLOSED. Genuine novelty 17.8 % leads; Fisher mapping now numerically auditable inline with explicit F0 = 1/8.98² = 0.01239; NANOGrav environmental caveat strengthened (“decisive only against the idealized circular-orbit reference … not a cosmological detection”); foreground claim fully scoped; 18 catalogs consistent; Redrock SPECTYPE vs TARGETTYPE clarified; χ² reframed as “raw, selection-uncorrected count distribution”; fNL envelope clarified (“the envelope — not the convex central value — is the appropriate summary”); SMBHB Bayes factor tightened. Citations and data-release notes updated. No regressions.
2. FRESH PASS (new findings only)

BLOCKERS (none)
No new blockers. All reproducibility, tiering, and over-claim issues are resolved.

MAJORS (none)
No new majors. The manuscript is internally consistent, rigorously caveated, and methodologically sound.

MINORS (polish – 1 item)

Abstract (first paragraph, final sentence) + Table I footnote ♠ (LAMOST)
The recount is now fully integrated and correctly placed, but the stale “an earlier draft quoted 264,938/264,738 from headline-minus-LAMOST subtraction arithmetic …” sentence survives in both the abstract and Table I footnote ♠. This is now factually incorrect (the recount supersedes it) and should be excised.
Fix: Delete the stale arithmetic sentence in both locations and replace with a clean cross-reference to the committed 6-way dedup JSON and the new Table II recount.

No other issues. Math (Fisher envelope, NANOGrav posterior, injection-recovery curves, dedup arithmetic, new recount numbers) is clean and auditable. All extraction artifacts resolved in rendered PDF. The paper is now publication-ready.

3. RECOMMENDATION

ACCEPT

The paper has moved decisively to publication-ready status since v3.1.91. All substantive concerns from the previous round have been addressed cleanly and completely; the single remaining minor is trivial polish that can be fixed in proof. This is a landmark multi-survey anomaly catalog suitable for immediate acceptance in MNRAS/PRD/JCAP. I recommend acceptance after the one minor change and will not require re-review.

Signed: External Referee (June 2026)
