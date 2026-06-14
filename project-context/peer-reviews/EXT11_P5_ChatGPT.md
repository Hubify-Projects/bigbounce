# EXT11 Harvest — P5 — ChatGPT

- Provider: ChatGPT
- Model/Effort: Pro Extended
- Chat URL: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc684-5918-83e8-b53e-28fde5fca69a
- PDF md5: 5af39737 (p5_desi_chirality_v0.1.76-2026-06-13_5af39737.pdf)
- Harvested: 2026-06-13 17:19 PDT

---

## Headline Verdict: MINOR REVISIONS

No major scientific rework required. The core scientific closures are strong: DESIVAST is now clearly declared as the primary path; the T-Web run is explicitly secondary; the ASTRA result is correctly framed as diagnostic; the dual-parent ledger is reconciled; and the conditional-permutation / monopole-reference framing is statistically sound. The paper is very close to acceptance.

## EXT10 Items Still Open

### Residual V-Web labels after the T-Web rename (downgraded to minor)

The text-level rename is substantially closed. However, several visible rendered figure labels and variables still say V-Web:

- **Fig. 2, p. 6:** plot title still says "V-Web volume fractions, in-footprint mask," while the caption says "T-Web volume fractions."
- **Fig. 3, p. 9:** plot title still says "canonical V-Web."
- **Fig. 9, p. 26:** figure title and left panel still say "V-Web vs Tempel" / "V-Web canonical," while the caption has been corrected to T-Web.
- **§VIII A / p. 17:** the phrase "+8–18 pp V-Web-vs-T-Web void-fraction discrepancy" remains after the rename. Should become "P5 T-Web vs external Ref. 11 T-Web" or similar.
- **§IX B / p. 25:** the variables n_{V-Web} remain in the Tempel comparison; replace with n_{T-Web} or n_{P5 T-Web}.

**Proposed fix:** Regenerate Figs. 2, 3, and 9 from the updated plotting scripts; replace remaining non-historical V-Web tokens with T-Web; use "P5 T-Web" and "Ref. 11 T-Web" where two T-Web implementations are compared.

### Mostly closed: reproducibility / frozen tree

Appendix C substantially closes the referee-level reproducibility concern. Production item: insert actual Zenodo/archival DOI in the final accepted version.

### Still open as presentation preference: row-level T-Web table ordering

Not a publication blocker. Object-level-first would be cleaner but current treatment is statistically adequate.

### Still open: Fig. 8 visual overlap (p. 22)

Top colorbar / lower-panel title overlap remains visibly present. Layout polish: regenerate with more vertical spacing.

### Still open: referee-like "Verdict." prose

The Tempel subsection has a paragraph beginning "Verdict." Change to "Summary" or absorb into the paragraph. Editorial only.

## EXT10 Items Now Closed

- DESIVAST primary analysis properly foregrounded.
- DESIVAST footprint / exact-membership concern closed scientifically (exact rerun changes membership by only 100 galaxies).
- ASTRA-DESI cross-validation framing now correct.
- Conditional-permutation correction closed.
- Primary/secondary hierarchy closed.
- Fixed-redshift-space caveat closed.

## New Items Introduced by Closures

### N1. Remove adversarial referee-facing language in unit-convention footnote (MINOR, fix required)

The new footnote on the Mpc-to-h⁻¹Mpc convention contains: "Any reviewer claim…" and "INCONSISTENT… FALSIFIED…" — inappropriate for a journal manuscript.

**Proposed replacement:**
> "Numerically, a distance D in Mpc is expressed in h⁻¹Mpc as hD. The pipeline therefore implements chi *= cosmo.h; this convention matches the DESIVAST coordinate convention used in §VIII."

### N2. "T-Web vs T-Web" ambiguity in §IX C (MINOR, wording fix)

After the rename, §IX C compares the paper's T-Web run to Ref. 11's T-Web run. Disambiguate throughout that subsection as "P5 T-Web" versus "Ref. 11 T-Web" or "external DR1 T-Web."

### N3. Figure files not fully regenerated after text rename (MINOR, figure regeneration required)

Captions say T-Web while the embedded figure art still says V-Web. Fixing the plot titles will close this cleanly.

## Final Referee Position

MINOR REVISIONS. After the stale V-Web figure labels, the adversarial footnote wording, the Fig. 8 overlap, and the final DOI placeholder are corrected, would move to ACCEPT. No remaining item changes the DESIVAST primary null, the T-Web secondary null, the ASTRA diagnostic result, or the sample-ledger/conditional-permutation statistical interpretation.
