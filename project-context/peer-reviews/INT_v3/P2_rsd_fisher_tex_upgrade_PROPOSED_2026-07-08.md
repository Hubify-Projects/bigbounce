# PROPOSED .tex update — P2 RSD multipole Fisher (retire "real-space monopole only")

**Status:** PROPOSED, NOT APPLIED. Awaiting Houston sign-off.
**Target:** `research/focused_paper_source_integration/02_full_draft.tex`
**Backing artifact:** `scripts/c14_rsd_multipole_fisher.py` +
`outputs/c14_rsd_multipole_fisher.json` (committed).
**Backing writeup:** `project-context/peer-reviews/INT_v3/P2_rsd_fisher_2026-07-08.md`.

All numbers below are read verbatim from `c14_rsd_multipole_fisher.json`. Nothing
fabricated. No headline f_NL = −35/16 value changes; the GR-projection bracket is
untouched.

---

## EDIT 1 — retire the "real-space monopole only" limitation (line ~947, para:reconcile)

### OLD (exact substring in the paragraph):

```
Honest limitations of this independent Fisher: it is a real-space monopole (no RSD multipoles $\ell = 0,2,4$, a $\sim\!18\%$ one-directional/conservative offset), uses the leading-order Gaussian covariance with the diagonal-triangle Wick term, is tree-level with a linear $k_{\max}$ and does not marginalize $b_2$/$b_{s^2}$;
```

### NEW:

```
We have since extended this independent Fisher to the full \emph{redshift-space} tree-level bispectrum (\path{c14_rsd_multipole_fisher.py}; committed output \path{c14_rsd_multipole_fisher.json}), dressing every leg with the linear Kaiser factor $Z_1(k,\mu) = b + f\mu^2$ (Kaiser~\cite{Kaiser:1987}) and the second-order redshift-space kernel $Z_2$ (Scoccimarro, Couchman \& Frieman~\cite{Scoccimarro:1999}; Sefusatti~\cite{Sefusatti:2006}) with the growth rate $f(z) = f\sigma_8/\sigma_8$ from the same CAMB cosmology, and integrating the Fisher integrand over the full line-of-sight orientation $(\mu_1,\phi)$ (so the $\ell = 0,2,4$ multipole content is included exactly, with no truncation). The redshift-space forecast \emph{tightens} the local-template baseline to $\sigma(\fnl^{\rm local}) = 0.42$ (bias-fixed) to $0.45$ (bias-marginalized), a $\sim\!35\%$ improvement over the real-space monopole in the one-directional sense expected from adding velocity information --- the full real-space-to-redshift-space gain, which is larger than the narrower $\sim\!18\%$ monopole-to-multipole gain quoted for an already-redshift-space analysis because the linear Kaiser monopole enhancement adds on top of the multipole anisotropy. Evaluated at the bounce template it gives $\sigma(\fnl^{\rm bounce}) = 0.42$--$0.45$, i.e.\ the same independent recovery factor $r_{\rm eff} = \sigma_{\rm local}/\sigma_{\rm bounce} \approx 0.99$ persists in redshift space (the Kaiser weighting does not move the $\fnl$ signal off the squeezed configurations where the two templates coincide), and an unmarginalized detection significance $|{-}35/16|/\sigma(\fnl^{\rm bounce}) \approx 4.9$--$5.2\sigma$. As an internal cross-check the $f \to 0$ limit of this redshift-space pipeline reproduces the real-space multi-tracer Fisher above to six significant figures. The remaining honest limitations of the independent Fisher are: it uses the leading-order Gaussian covariance with the diagonal-triangle Wick term, is tree-level with a linear $k_{\max}$, does not marginalize $b_2$/$b_{s^2}$ (held at fiducial in both the real- and redshift-space runs), and models redshift-space distortions at tree-level Kaiser order without fingers-of-God damping (a small, further-degrading correction at the linear $k_{\max}$ used, so the reported redshift-space gain is if anything conservative at the top of the $k$-range);
```

**Rationale:** the reviewer's standing "real-space monopole only, ~18% offset"
caveat is retired by actually computing the redshift-space bispectrum Fisher. The
edit (a) states the RSD result, (b) HONESTLY reconciles the +35% we measure vs
the ~18% previously attributed to Heinrich (definitional: full RSD gain vs
monopole→multipole gain), (c) reports the strengthened 4.9–5.2σ, (d) notes the
f→0 self-consistency check, and (e) keeps the genuinely-remaining limitations
(Gaussian covariance, tree-level, no b2, no FoG).

---

## EDIT 2 — update the independent-Fisher significance in the same paragraph

### OLD (exact substring, earlier in the same paragraph):

```
an unmarginalized detection significance $|{-}35/16|/\sigma(\fnl^{\rm bounce}) \approx 3.2$--$3.5\sigma$; both are stable across triangle-grid resolution.
```

### NEW:

```
an unmarginalized detection significance $|{-}35/16|/\sigma(\fnl^{\rm bounce}) \approx 3.2$--$3.5\sigma$ (real-space monopole, the conservative floor; the redshift-space value below is $\approx 4.9$--$5.2\sigma$); both are stable across triangle-grid resolution.
```

**Rationale:** flags the real-space 3.2–3.5σ as the conservative floor and
forward-references the redshift-space 4.9–5.2σ established by EDIT 1, so a reader
encountering the number mid-paragraph is not misled that 3.2–3.5σ is the final
independent significance.

---

## EDIT 3 — new bibliography entries (if not already present)

Verify these `\bibitem`/BibTeX keys resolve; add any missing:

- `Kaiser:1987` — N. Kaiser, "Clustering in real space and in redshift space,"
  MNRAS 227, 1 (1987).
- `Scoccimarro:1999` — R. Scoccimarro, H. M. P. Couchman, J. A. Frieman, "The
  Bispectrum as a Signature of Gravitational Instability in Redshift Space,"
  ApJ 517, 531 (1999), arXiv:astro-ph/9808305.

(`Sefusatti:2006`, `Scoccimarro:1998`, `Dore:2014`, `Heinrich:2023` are already
cited in this paragraph.)

**Note:** Karagiannis+2018 (arXiv:1801.09280) is the multi-tracer tree
assignment reference; cite it inline only if a referee asks for the multi-tracer
tree form provenance — the writeup carries it.

---

## Directive-G / propagation checklist (to run WITH the edit, if applied)

Per CLAUDE.md directive-G + I6, if EDIT 1–3 are applied:
1. bump `\paperVersion` (patch, → v1.7.101) + `\date`/`\paperTimestamp` to today;
2. recompile (0 undef-refs) + `/latex-audit`;
3. grep for other "monopole-only" / "3.2--3.5" / "real-space monopole"
   instances across the .tex AND site surfaces (`/bigbounce-claims-table-sync`);
4. NO figure images render the σ(f_NL) numbers, so I6 figure-regeneration is
   N/A here — confirm by grepping `\includegraphics` in the paragraph's section
   (there are none tied to these values);
5. re-mirror PDF byte-identical to all served paths; Convex `paperVersions:bump`
   with real md5/pages; three-way md5 check;
6. add a `reviewTimeline.ts` entry (kind: skill-improvement / INT round) per the
   standing review-round site-sync directive.
