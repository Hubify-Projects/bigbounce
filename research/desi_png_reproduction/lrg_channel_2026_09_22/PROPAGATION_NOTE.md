# Propagation note — ledger row 4 LRG channel (lane LS11-row4-lrg, 2026-09-22)

**The paper that owns this material is A3M** — the Track-A multi-channel
flagship, `research/track_a3_multichannel/paper/main.tex`, §VI (the DESI
DR1 comparison and the "As an independent check of the pipeline these
forecasts rest on…" paragraph, currently around line 1435–1490). No other
live paper carries the f_NL forecast/DESI-reproduction material: P2 was
rescoped to P2′ and then folded into A3M's theory section
(`PAPER_LINEAGE_2026-08-05.md`, decision record 2026-09-02 evening).

**This lane edited no `.tex`, no SSOT page and no site data.** What follows
is for A3M's owner lane to use, verify and land under directive-G hygiene.
Every sentence below is printable as-is.

---

## 1. Two statements currently in A3M §VI are now factually wrong

A3M §VI presently reads:

> This reproduction's $\sigma=25$ is $\sim2.8\times$ the published $9.0$
> because wide-angle corrections (\texttt{PowerSpectrumOddWideAngleMatrix})
> are not applied and only $2$ of $5$ imaging-systematics splits were run;
> full manifest cited in the reproducibility statement below.

Both stated causes are false, and the lab's own artifacts already say so:

- **Wide-angle corrections cannot explain any σ inflation.** `LEDGER4_RESULT_v4`
  (2026-09-04) established, using pypower's own runtime guard, that
  order-1 wide-angle terms source **only odd multipoles**, while the official
  window matrix uses ℓ = 0, 2, 4 only — a genuine null. v3's numbers stood
  unchanged as the wide-angle-corrected result.
- **All five imaging-systematics splits were run**, in `LEDGER4_RESULT_v5`
  (2026-09-04). And in any case the splits are null tests: they never enter
  the headline fit's σ.

**Replacement sentences (printable):**

> This reproduction's $\sigma=25$ at $p=1.6$ is larger than the published
> $9.0$ for three reasons, none of them wide-angle: the response lever
> $b_1-p$ is $0.649$ at $p=1.6$ against $1.249$ at $p=1.0$, so the same data
> give a $1.9\times$ weaker constraint; the published number combines LRG and
> QSO while this fit uses QSO alone; and this fit frees only $b_1$ and
> $\fnl$, with $n_{\rm shot}$ fixed at $0$, against DESI's full nuisance
> marginalisation. Applying the identical pipeline to the DR1 LRG sample at
> $p=1.0$ returns $\sigma=5.7$, confirming that the $\sigma=25$ figure is a
> property of the QSO configuration and not of the pipeline.

> Order-1 wide-angle corrections were implemented and verified to be a
> genuine null for this configuration: they source only odd multipoles,
> while the official window matrix uses $\ell=0,2,4$. All five
> imaging-systematics splits have been run.

---

## 2. New material: the LRG channel

Printable as a short addition to the same paragraph, or as its own
paragraph after it.

> Applying the same machinery to the public DESI DR1 LRG sample --- DESI's
> own window matrix, measured $P_\ell$ and EZmock covariance for each of the
> three official redshift bins ($z_{\rm eff}=0.510$, $0.706$, $0.919$), with
> $b_1$ free per bin, $n_{\rm shot}$ fixed at $0$, and
> $k\le0.08\,h\,{\rm Mpc}^{-1}$ --- gives
> $\fnlloc = -3.4\pm5.7$ at $p=1.0$ (the universality response adopted for
> LRGs), or $-1.1\pm6.9$ restricted to $0.6<z<1.1$, the redshift range of
> the published LRG sample. The two tracers agree: the LRG and QSO channels
> differ by $0.16\sigma$ on a common convention. The fitted linear biases
> rise monotonically with redshift ($b_1=1.87$, $2.05$, $2.21$) without
> being imposed.

> These uncertainties are optimistic and are not competitive with the
> published constraint: only $b_1$ and $\fnl$ are free, no cross-bin
> covariance product exists so the three bins are combined as independent,
> and the untreated (no $\theta$-cut, unrotated) data vectors are used. The
> value of the exercise is an internally consistent comparison of the two
> tracers on one convention, not an independent measurement.

> A five-row imaging-systematics table (E(B--V), stellar density, $z$-band
> galactic depth, \texttt{WEIGHT\_SYS} on/off, and Galactic latitude), run
> for each redshift bin at the same window/covariance fidelity, returns no
> detectable sensitivity in any of the fifteen rows; the largest, E(B--V) in
> $0.8<z<1.1$, reaches $1.0\sigma$ after the disclosed $\sqrt2$
> covariance-reuse correction. Notably, \texttt{WEIGHT\_SYS} --- the
> dominant systematic in the QSO channel at $3.1\sigma$ --- is a null in
> every LRG bin, consistent with quasar target selection being far more
> sensitive to imaging depth and stellar contamination than LRG selection.

---

## 3. The discrimination statement is unchanged — do not soften it

> With $\sigma=5.7$, the LRG channel places $\fnlloc=-35/16$ and $-35/8$
> $0.21\sigma$ and $0.17\sigma$ from its central value, separated by
> $0.38\sigma$: DESI DR1 still cannot distinguish them. Opening the LRG
> channel improves the reach by a factor $\sim2.3$ over the QSO-only
> configuration and remains an order of magnitude short of a test.

The existing A3M sentence "the near-coincidence of the recovered central
value with $-35/16$ is a coincidence, not evidence" applies verbatim to the
LRG number too and should be kept.

---

## 4. Reproducibility statement

Add to A3M's reproducibility statement alongside the existing v3/v5 manifest:

> `reproducibility/manifests/experiments/ledger4-desi-dr1-lrg-fnl-channel.json`

and, if a method sentence is wanted:

> The LRG catalogues and randoms (6.2\,GB) were read directly from the DESI
> public server by HTTP range request and reduced in memory; no bulk
> catalogue was written to disk.

---

## 5. What the A3M lane must check before landing any of this

1. Re-read `LEDGER4_LRG_RESULT_2026-09-22.md` §1 (the optimistic-σ caveat)
   and keep it in whatever text lands — the number must never be presented
   as beating DESI.
2. The count `1{,}631{,}716` LRGs in A3M §VI is correct and is now
   independently confirmed by this lane (1,631,715 on a strict edge cut).
   The QSO count and the rest of the Chaussidon quotation are untouched.
3. Directive-G hygiene: `\paperVersion` patch bump, `\date`/`\paperTimestamp`,
   4-pass recompile with 0 undefined refs, `/latex-audit`, byte-identical PDF
   re-mirror to every served path, and the Convex `paperVersions:bump` — the
   last of which is currently **queued, not written**, because Convex is
   disabled for the campaign (see `CONVEX_BACKFILL_QUEUE_2026-09-21.md`).
4. Directive R2: this note is science, not a review round. It does not
   consume A3M's convergence-round budget.
