# Propagation note — LRG E(B−V) on the θ-cut products (lane LS14-row4-ebv, 2026-09-22)

**The paper that owns this material is A3M** — the Track-A multi-channel
flagship, `research/track_a3_multichannel/paper/main.tex`, §VI (the DESI
DR1 comparison paragraph, the same passage lane LS11 wrote its propagation
note for). No other live paper carries the f_NL forecast / DESI-reproduction
material: P2 was rescoped to P2′ and folded into A3M's theory section
(`PAPER_LINEAGE_2026-08-05.md`, decision record 2026-09-02 evening).

**This lane edited no `.tex`, no SSOT page and no site data.** It also does
not supersede LS11's propagation note — that note's §1–§4 stand unchanged.
What follows is *additive*: two amendments and one new sentence for A3M's
owner lane to use, verify and land under directive-G hygiene. Every
sentence is printable as-is.

---

## 1. Amendment — the E(B−V) caveat sentence is now stronger than LS11 could make it

LS11's note offers this sentence for A3M §VI (printable, currently
unlanded):

> … returns no detectable sensitivity in any of the fifteen rows; the
> largest, E(B--V) in $0.8<z<1.1$, reaches $1.0\sigma$ after the disclosed
> $\sqrt2$ covariance-reuse correction.

**Replace its second clause with (printable):**

> … returns no detectable sensitivity in any of the fifteen rows. The
> largest, E(B--V) in $0.8<z<1.1$, reaches $1.0\sigma$ after the disclosed
> $\sqrt2$ covariance-reuse correction, and has been re-tested on DESI's
> $\theta$-cut ($\theta_{\rm cut}=0.05^\circ$) products: it remains a null
> there, at $0.94\sigma$, with the verdict unchanged under a deliberately
> wrong-geometry transfer. The row is reported as a null because the
> pre-registered rule says so, not because it is far from the threshold ---
> every treatment tried places it between $0.93\sigma$ and $1.00\sigma$,
> a margin an order of magnitude below the $\sim\pm0.2$ precision these
> split $\Delta/\sigma$ values carry while no split-specific covariance
> exists.

## 2. Amendment — the "untreated data vectors" disclosure

LS11's note offers:

> … and the untreated (no $\theta$-cut, unrotated) data vectors are used.

**Extend it to (printable):**

> … and the untreated (no $\theta$-cut, unrotated) data vectors are used.
> Moving the $0.8<z<1.1$ bin to DESI's $\theta$-cut products --- measured
> $P_\ell$, window and covariance all replaced together, so the comparison
> is free of any approximation --- shifts $\fnlloc$ by $+1.9$ at $p=1.0$
> ($+3.8$ at $p=1.6$), i.e.\ $0.18\sigma$, with $b_1$ falling from
> $2.2133$ to $2.1883$. The untreated convention is retained throughout so
> that the LRG and QSO channels stay directly comparable; the
> $\theta$-cut shift is quoted as a convention systematic of that size.

## 3. New, optional sentence — if A3M wants the cross-tracer point made

> The one LRG imaging systematic that approaches its threshold, E(B--V) at
> $0.8<z<1.1$, cannot be arbitrated by the quasar channel: had the QSO
> sample carried the same $\Delta\fnl$, its larger split uncertainty would
> have registered it at $0.85\sigma$ --- on the same null side of the same
> threshold.

## 4. Reproducibility statement

Add alongside the existing v3/v5 and LRG-channel manifests:

> `reproducibility/manifests/experiments/ledger4-lrg-ebv-thetacut.json`

## 5. What the A3M lane must check before landing any of this

1. Land LS11's note first, or land both together — §1 and §2 here are
   edits *to sentences LS11 proposed*, not to text currently in the paper.
2. Do **not** move the LRG headline. It is unchanged:
   $-3.4\pm5.7$ at $p=1.0$, $-1.1\pm6.9$ on $0.6<z<1.1$. The E(B−V) row
   did not flag, so no systematic was added to it.
3. Do **not** present the $\theta$-cut numbers as the channel's result. The
   channel is on the untreated convention by design; the $\theta$-cut
   figures are a measured convention systematic on one z-bin only, and the
   QSO side has not been re-run the same way.
4. Directive-G hygiene on whatever lands: `\paperVersion` patch bump,
   `\date`/`\paperTimestamp`, 4-pass recompile with 0 undefined refs,
   `/latex-audit`, byte-identical PDF re-mirror to every served path, and
   the Convex `paperVersions:bump` — the last **queued, not written**,
   because Convex is disabled for the campaign
   (`CONVEX_BACKFILL_QUEUE_2026-09-21.md`).
5. Directive R2: this note is science, not a review round; it does not
   consume A3M's convergence-round budget.
