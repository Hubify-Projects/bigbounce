# PRE-REGISTRATION — in-domain `d(θ)` and the dilution bound `D`
### lane `bb-LS10-indomain-d180`, 2026-09-22

Committed **before any statistic in this directory was computed.** It fixes the
sample, the statistic, the positive control, the threshold that counts as
in-domain, and the decision rule, in advance.

Lifts (or does not lift) the hold that lane `bb-LS6-row16-tta` placed on
`../row16_tta_2026_09_21/PROPAGATION_NOTE.md` item **Q-1**, which itself holds
item **P-5** of `../row16_pa_parity_transfer/PROPAGATION_NOTE.md`
(`D ≤ 0.7166 ± 0.0047`, `A₉₅^phys ≥ 1.37 %`).

---

## 0. The thing being tested

Row 16(ii-b) measured `d(θ) ≡ P(L(0) ≠ L(θ))` — the rate at which the released
pipeline contradicts its own label between two lossless rotations of the same
image — on **Legacy Survey viewer cutouts** (`jpeg-cutout?…&size=150&layer=ls-dr9`,
a 39.3″ field upsampled 150 → 224). Lane LS6's pre-registered control P2c then
failed: on those cutouts the released checkpoint reproduces the released
catalogue's class for only **43.9 %** of galaxies. The images are not the
catalogue's images.

The catalogue's inference ran on `Smith42/galaxies`
(`pipelines/p2_chirality/run_eq_fast.py:37`, keyed by `dr8_id`); the `image_url`
column that rows 13/16 fetched was appended afterwards for display
(`run_eq_fast.py:265-270`). This lane re-runs the rotation pass on the
`Smith42/galaxies` images themselves, at the pinned revision
`bdd1b063a9a22874a79a4363aa9fb6a2b356a4c2`.

**Recorded before pre-registering** (facts about the source, not statistics):
the `v1.0` config (`data/train-*`, the files `run_eq_fast.py` reads) stores
**512 × 512 px RGB JPEG** cutouts, 442 row groups of 100 rows per shard, 192
train shards, 8,474,566 rows, ≈ 113 kB/galaxy. `main.tex:171` describes the
parent as "$224\times224$~px $grz$ cutouts at $0.262''$/pixel"; 224 is the
**network input** after `Resize((224,224))`, not the cutout size. That
discrepancy is reported separately and is not part of any statistic here.

## 1. Model and preprocessing — unchanged, reused verbatim

* Checkpoint `bamfai/galaxy-chirality-v2` / `chirality_model_v2_best.pt`,
  revision `237d021c451d75cf86a875e86d4de498b74e2f12` — loaded through
  `../row16_pa_parity_transfer/run_pa_transfer_inference.py::load_model`,
  imported, not re-implemented.
* Preprocessing `TFM` imported from the same module: `Resize((224,224))` →
  `ToTensor` → `Normalize(ImageNet)`. This is byte-for-byte the released
  preprocessing (`run_eq_fast.py:88-92`). **No crop.**
* Rotations `θ ∈ {0°, 90°, 180°, 270°}` are PIL transposes — lossless pixel
  permutations of a square image, no interpolation anywhere. Mirror `M` is
  `FLIP_LEFT_RIGHT`.
* Two forward-pass families per galaxy, 8 passes total:
  `A_θ = TFM(Rot_θ(I))`, `B_θ = TFM(Rot_θ(M I))`.
* Production equivariant triple, since `M·Rot_θ = Rot_{−θ}·M`
  (identical to `s5b_nocrop_dilution.py::eq_triple`, which is re-imported, not
  re-derived):
  `eq_cw(X_θ) = (p_cw(A_θ) + p_ccw(B_{−θ}))/2`, and cyclically.
  `L(θ) ≡ argmax` over `(cw, ccw, ns)`.

## 2. Sample — fixed in advance

Disk, not GPU, is the binding constraint (≈ 10 GB free on the Data volume, other
lanes running). The pull is therefore **streamed**: `HfFileSystem` + `pyarrow`
HTTP range reads of individual row groups. **No image byte is written to disk**;
row groups are decoded, inferred, and discarded. On-disk products of this lane
are the probability array and JSON/markdown (≤ 60 MB).

* **Row groups**: shards `s ∈ {0, 10, 20, …, 190}` (20 shards, evenly spaced over
  the 192), and from each, **20 row-group indices** drawn without replacement,
  uniformly from `[0, 442)`, `numpy.random.default_rng(20260922)`.
  **400 row groups = 40,000 galaxies**, ≈ 4.5 GB streamed.
* This is a uniform random sample of the parent: the dataset is fully shuffled
  with respect to sky position — a single 100-row group already spans
  `dec ∈ [−66°, +85°]` and `ra ∈ [0°, 360°]` (verified locally against the
  released catalogue on shards 0 / 96 / 191).
* **Abort rules, fixed now**: stop pulling if free disk drops below 5 GB, or at
  90 min wall-clock on the streaming stage. Whatever `N` is reached is reported
  as exactly that `N`, with the row-group count that produced it, and is **never**
  described as a measurement on the 8,474,531-row parent.
* These are **not** the same galaxies as row 16(ii-b)'s N = 19,800 (those are
  keyed by `ra/dec` and are scattered across all 192 shards; fetching them
  individually would stream ≈ 220 GB). The comparison is between two population
  rates on two samples of the same parent, and is stated that way.

## 3. Selections — fixed in advance

Taken from the released catalogue
`../../p2_chirality/apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet`,
joined on `dr8_id = object_id`:

| tag | selection | matches row-16(ii-b) row |
|---|---|---|
| `all_drawn` | every galaxy in the drawn row groups | — |
| `catalogue_spiral` | `class_eq ∈ {CW, CCW}` | "all spirals (N = 19,800)" |
| `primary_hc` | `primary_hc == True` | "`primary_hc`, the catalogue's own cut (N = 7,982)" |
| `primary_hc_safe` | `primary_hc ∧ ¬raw_flip_qc_unsafe` | the Q-2 strict row |

Row 16(ii-b)'s N = 20k sample was drawn spiral-only (10,000 CW + 10,000 CCW,
sky-uniform NSIDE = 64, seed 44), so `catalogue_spiral` is the like-for-like row.

## 4. Statistic — identical to the held one, no redefinition

For `θ ∈ {90°, 180°, 270°}`, on each selection:

* `d(θ) = P( L(0) ≠ L(θ) | L(0) ≠ NS ∧ L(θ) ≠ NS )` — the s5b conditioning,
  unchanged.
* `D ≤ 1 − max_θ d(θ)` (the headline bound) and `D ≤ 1 − d(180°)` (the
  assumption-free row: position angle is defined mod 180°, so a 180° rotation
  depicts the same galaxy at the same position angle).
* `A₉₅^phys = A₉₅^obs / D`, with `A₉₅^obs = 0.98 %` on the strict subset as in
  P-5.
* Uncertainties: 1,000 galaxy-level bootstrap resamples, `rng(20260922)`,
  reported as the SE of the bound, exactly as `s5b_nocrop_dilution.py` does.

## 5. Positive controls — computed and checked BEFORE any `d(θ)` is quoted

**C1 (catalogue-scale, local, free).** The committed in-domain full-catalogue
re-run `../../p2_chirality/outputs/canonical_provenance/e2e_fullrun/e2e_shards/`
(192 shards, 8,474,531 galaxies, same checkpoint, same preprocessing, A100,
2026-07-11) vs the released catalogue's `class_eq`, joined on `dr8_id`. Reported
as an argmax-class agreement over all 192 shards. (`NS` and `NOT_SPIRAL` are the
same class under two names; the comparison is made on the class, not the string.)

**C2 (this lane's own forward passes).** Agreement of **this lane's** `L(0°)`
with the released catalogue's `class_eq` on the drawn galaxies, plus
`max |eq_cw(0°) − score_cw_eq|` and its median.

**C3 (TTA identity).** The exact algebraic control from `s5b`: at `θ = 0°` and
`θ = 180°` the flip TTA makes the parity operation exact, so the identity
residual `|eq_cw(Y_θ) − eq_ccw(X_θ)|` must be **0.0** to float32 and the class
swap fraction excluding ties must be **1.0**. Asserted, not reported.

### The in-domain threshold — fixed now

> **C2 ≥ 99.0 %** counts as in-domain.

Justification fixed in advance: the failing out-of-domain figure is 43.9 %
(42.4 %, 44.7 % on two further draws), and the committed in-domain e2e re-run
is the reference for what "same images" looks like. 99.0 % is far above the
failure mode and leaves room for JPEG-decoder and float differences between an
A100 `float32` run and an MPS one.

## 6. Decision rule — fixed now

1. **C2 < 90 %.** Then the released catalogue is not reproducible from the
   released checkpoint and preprocessing on *its own documented image source*.
   That is a **larger finding than the bound**. It is reported as such; **no
   `d(θ)` or `D` is quoted as a result**, the hold on P-5 **STANDS**, and the
   lane stops and escalates.
2. **90 % ≤ C2 < 99 %.** Ambiguous: neither domain is established. Numbers are
   reported as diagnostics only, the hold **STANDS**, and the shortfall is
   characterised.
3. **C2 ≥ 99 %.** In-domain confirmed. `d(θ)` and `D` on these images are the
   in-domain measurement, and then:
   * **LIFTED** — if the in-domain `primary_hc` bound agrees with the held
     `D ≤ 0.7166 ± 0.0047` within `2 × ` the combined bootstrap SE. P-5 prints
     as drafted.
   * **LIFTED-WITH-DIFFERENT-NUMBERS** — otherwise. The in-domain numbers
     replace the held ones verbatim in P-5, P-5a, P-5b; the out-of-domain values
     are withdrawn, never averaged with the new ones, never quoted as a range.
   * In either case the same `θ = 180°` row is reported alongside the
     `max_θ` row, and Q-2's `d(180°)` is superseded by the in-domain value.

A value that comes out **above** `D ≤ 1` is impossible by construction
(`d ≥ 0`); a `d(θ)` that comes out ≈ 0 is a real possible outcome and would mean
the in-domain classifier is nearly rotation-stable and the dilution bound is
vacuous — that outcome is printed as plainly as any other. Nulls stay nulls.

## 7. What this lane does NOT do

* Does not edit any paper `.tex` (`bb-L4e-p4p-hold-correction` owns P4′).
* Does not re-run, re-tune, or re-train anything. The checkpoint and the
  preprocessing are used exactly as released.
* Does not touch items P-1…P-4 of the row-16(ii-b) note or Q-3/Q-4 of the row-16
  note — those are image-independent or separately scoped.
* Does not write to Convex (disabled campaign-wide); intended mutations are
  queued in `project-context/CONVEX_BACKFILL_QUEUE_2026-09-21.md`.
