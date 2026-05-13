# Cross-Vendor Adversarial Peer Review — P4 Observational-Systematics R-round
**Reviewer:** Grok-4 (xAI flagship, simulated) — observational-astronomy profile
**Bias profile:** Levesque / Masters / Simmons / Galaxy Zoo collaborator lens
(citizen-science labeling bias, survey selection function, ground-vs-space
imaging asymmetries, ground-truth catalog provenance)
**Date:** 2026-05-13 10:52 PT
**Target:** `pipelines/p2_chirality/chirality_catalog_paper.tex` (P4 v1.0.47, dated 2026-05-12 00:00 PDT)
**SSOT consulted:** `project-context/SSOT/paper-4/status.md` (v1.0.46 → v1.0.47 wave,
51 findings 3B+15M+17m+16n, 3 BLOCKER closed, 14/15 MAJOR closed; the surviving
MAJOR is the no-symbolic-anchor caveat in §V — not an observational concern).
**Prior cross-vendor Grok rounds:** OOOOO (8 findings, all closed in PPPPP) +
RRRRR (REPEAT, all OOOOO closures held). Both prior Grok rounds were physics-
intuition profile — dimensional analysis + parity-observable framing. This
round walks the observational-systematics aisle that those rounds did not
cover, so finding overlap with closed BLOCKER/MAJORs is checked per-item below
and noted in the table.

> "Forget the f_CS / Chern-Simons translation in §VIII for an hour and stand
> on the catalog floor. What survey did the 8.47 M images come from, who put
> the spirals in, who labeled the handedness, and would Karen Masters or
> Brooke Simmons sign their name to the systematic budget?"

---

## Verdict: **0 BLOCKER, 4 MAJOR, 5 MINOR, 3 NIT.**

The paper has done good work hardening the dipole channel (Catalog A → C, MASTER
mode-coupling inversion, 7-region uniformity, edge-on routing). The
**observational-systematics chain leading INTO the classifier is under-disclosed
relative to the post-classifier systematics treatment** — and that is the
exact failure mode Shamir's program has been criticized for (Iye+2020).
The single most concerning issue is **MAJOR-1: the parent-sample selection
function is essentially undocumented.** The reader is told "Smith42/galaxies
dataset, 8,474,688 images from DESI Legacy DR8" and given no magnitude limit,
no surface-brightness cut, no S/N threshold, no spatial completeness map, and
no statement of which DR8 imaging legs (BASS+MzLS Northern footprint vs
DECaLS Southern footprint vs DES overlap) contribute to which sky region of
Table~\ref{tab:sky_balance}. A reviewer at a refereed journal will ask this
question first; the paper currently has no answer.

Most concerning observational issue (one sentence): **The 8.47 M parent
sample's selection function is undocumented — no magnitude limit, no S/N
threshold, no per-imaging-leg breakdown (BASS+MzLS vs DECaLS), and no parent-
sample completeness map — so the "uniform at 7-region survey granularity"
claim cannot be audited and the regional uniformity is currently only a
statement about the post-classifier ratio, not about the underlying galaxy
population that was fed to the network.**

---

## Findings

### MAJOR

**MAJOR-1 — Parent-sample selection function is undocumented.**
*Location:* §IIIA (Galaxy Images, L225–246).
*Issue:* The parent sample is declared to be the Smith42/galaxies HuggingFace
dataset (8,474,688 images, DESI Legacy DR8, 224×224 grz cutouts at 0.262″/pix).
That is a *file* description, not a *selection-function* description.
Nowhere in the paper does the reader find:
(i) the parent-sample magnitude limit (DR8 morphological pipelines typically
work down to r~21–22; Walmsley+2023 Galaxy Zoo DESI used a Tractor mag-r ≤ 19
cut for the 8.7 M sample — is the present 8.47 M sample co-extensive with
that, or a different cut?);
(ii) the surface-brightness floor or S/N requirement on the parent;
(iii) the per-band Galactic-extinction treatment (DR8 is E(B−V)-corrected at
catalog level but cutout-pixel-level extinction handling is not stated);
(iv) the imaging-leg decomposition — DR8 has three distinct surveys
(BASS+MzLS Northern: g, r, z separately; DECaLS South: grz simultaneously;
DES region overlap) with different depths, PSFs, and seeing distributions.
The 7-region Table~\ref{tab:sky_balance} cuts on RA quadrants and Dec bands,
NOT on imaging-leg boundaries (which are roughly Dec > +32° → BASS+MzLS,
Dec < +32° → DECaLS, RA ∈ [0°, 90°] ∩ Dec ∈ [−60°, −30°] → DES overlap).
That means the "uniform across 7 regions" claim conflates imaging legs
within single bins and never tests the leg-versus-leg question, which is the
*natural* axis on which a survey systematic would manifest.
*Why this matters for the paper's headline:* the paper's claim is "the
0.5% upper limit is uniform across the DESI Legacy footprint." A referee will
ask: is it uniform across BASS+MzLS vs DECaLS vs DES, the three distinct
imaging campaigns that make up that footprint? The current Table III/IV
granularity cannot answer that question.
*Cross-check vs prior closures:* SSOT v1.0.47 closes "Table III column relabel
to Bandpower (ℓ_eff)" (B3), which is a power-spectrum-display fix, not a
parent-sample-selection fix. NOT a double-count.
*Fix:* Add a paragraph in §IIIA giving (a) parent-sample r-band magnitude
limit and S/N floor (from the Smith42 dataset card or the underlying DR8
sweep query); (b) a 3-row "imaging legs" subtable showing N_spiral and CW
fraction per leg (BASS+MzLS / DECaLS / DES); (c) an explicit statement of
whether the regional uniformity claim survives the leg-versus-leg test. If
the Smith42 selection function is genuinely opaque, say so in the text —
that is itself a result.

**MAJOR-2 — 69.91% GZ1 CW/CCW agreement is reported but not interpreted as
ground truth uncertainty.**
*Location:* §IIIB (L309–317), §VIII (L793–815).
*Issue:* The independent GZ1 cross-match gives 69.91% CW/CCW agreement on
117,205 GZ1-labeled spirals where the model also predicts a chirality. The
paper interprets this as "the loss surface is flat at chance accuracy on the
GZ1 distribution" and "GZ1 binary labels do not provide independent
constraint." That is a reasonable disposition, but it elides three
observational realities:
(a) GZ1 itself has a known **classification-asymmetry-versus-magnitude**
gradient (Bamford+2009 MNRAS 393, 1324; Hart+2016 MNRAS 461, 3663): at the
faint end, the volunteer CW/CCW vote ratio drifts because volunteer
attention to fine arm structure drops. If the production catalog inherits
GZ1's training labels (it does: GZ1 = 32.4% of labels) and the test set
has more faint galaxies than the GZ1 training set, this manifests as a
chance-floor accuracy that is itself magnitude-dependent.
(b) GZ1's published debias methodology (Bamford+2009) was developed *for the
elliptical/spiral fraction*, not for *handedness within the spiral class*;
the Land+2008 ~1% CW excess is a separate handedness-specific bias that the
paper cites but does not propagate. The paper should distinguish between
GZ1's morphology-classification debias and GZ1's handedness-vote
asymmetry — they are different systematics.
(c) Newer Galaxy Zoo DESI volunteer labels (Walmsley+2023) supersede GZ1 on
the same DR8 footprint for everything except handedness (Walmsley+2023
explicitly *did not* re-vote handedness, citing the Iye+2020 reading-
direction concern). The paper cites Walmsley+2023 but does not surface that
the Walmsley team made a deliberate decision *not* to provide a handedness
ground truth — which is precisely the reference the present paper is
trying to validate against. That decision should be cited as constraining
context for why no large-scale ground truth exists.
*Cross-check vs prior closures:* OOOOO F8 "9.5σ monopole disclaimer
unproven" was closed by adding the working-hypothesis framing — that
covered the *monopole magnitude* attribution. The present finding is about
the *GZ1 cross-validation interpretation*, which is the upstream
ground-truth question. Adjacent, not duplicate.
*Fix:* Add a paragraph in §IIIB acknowledging (a) GZ1's magnitude-dependent
classification asymmetry as a separate ground-truth systematic, (b) the
Walmsley+2023 deliberate omission of handedness from Galaxy Zoo DESI as the
reason no modern large-scale ground truth exists. Cite Bamford+2009 and
Hart+2016 for the magnitude-dependent vote-bias literature.

**MAJOR-3 — TTA strategy is only horizontal flip ($Z_2$); rotation TTA
is disclosed-out without an empirical bound.**
*Location:* §IVB (L489–510), §IVC (L521–551).
*Issue:* The paper restricts TTA to original + horizontal-flip averaging,
explicitly excluding rotation TTA (90°/180°/270°) on the grounds that
"rotations preserve chirality and would only audit a different bias channel"
(L526–536). I agree with the *physics* of that argument — rotations are
spin(2) on the celestial sphere, not parity. **But** the paper then claims
in §VI/§VII that the residual 9.5σ monopole is robust under TTA. That
robustness claim is only as strong as the TTA group it has been tested
under. A ViT-Small is *not* rotation-equivariant by architecture, and
chirality-classifier asymmetry baked into the network weights would
manifest as a **rotation-correlated** chirality probability offset that
horizontal-flip TTA cannot detect. The paper's response — "Rotation-TTA
therefore probes the orientation bias channel, which we did not include"
(L536–540) — is honest but the next-step empirical bound is missing:
what is the max rotation-correlated CW-fraction excursion across a sample
of test images? The answer is a one-line bound on the residual systematic
that is NOT in the paper.
*Cross-check vs prior closures:* The TTA disclosure language is present
(v1.0.47 cleaned this up). This finding adds an empirical-bound request,
not a disclosure-language request. Not a duplicate.
*Fix:* Run rotation-TTA (90°/180°/270°) on a 10k–100k galaxy validation
sample and report the per-rotation CW-fraction max excursion as a one-line
bound in §IVC. If the bound is below the 9.5σ monopole magnitude, the
monopole is *not* a rotation artifact. If it is comparable, the monopole
attribution to GZ1 handedness bias gets weaker. Either way the reader needs
the number.

**MAJOR-4 — 7-region "survey granularity" claim is RA/Dec slabs, not
survey-footprint geometry.**
*Location:* §VIIIA (L1414–1461), abstract (L115–116), Tables III/IV.
*Issue:* The paper says "uniform at 7-region survey-footprint granularity"
21 times. The actual 7 regions in Table~\ref{tab:sky_balance} are: 4 RA
quadrants ([0°, 90°), [90°, 180°), [180°, 270°), [270°, 360°)) + 3 Dec bands
([−90°, −30°), [−30°, +30°), [+30°, +90°)). Those are *equatorial-coordinate
slabs*, not survey-footprint regions. The DESI Legacy footprint is not
axis-aligned to RA quadrants — it has Galactic-latitude-driven boundaries
(|b| > 18° approximately), an MzLS/BASS Dec ≈ +32° split, a DES Southern
strip, and an excluded Galactic-plane region. None of those structures
appear in the 7-region cut.
*Why this matters:* the "survey granularity" framing implies that the
uniformity is tested at the natural systematic scales of the survey
(imaging-leg boundaries, depth variations, Galactic-latitude extinction
bands). It is not. It is tested at arbitrary equatorial slabs.
*Cross-check vs prior closures:* SSOT v1.0.46→v1.0.47 closures touched the
power-spectrum bandpower display (B3) and the equivariant-vs-snapshot
denominator footnote (M1/M3), neither of which is this finding.
*Fix:* Either (a) recompute the regional table using actual survey-footprint
regions (BASS+MzLS / DECaLS / DES with footprint masks), OR (b) rename the
21 occurrences of "uniform at 7-region survey-footprint granularity" to
"uniform across 7 equatorial coordinate slabs" and disclose in §VIIIA that
these slabs are not aligned to imaging-leg or depth boundaries. The latter
is a 30-min surgical edit and is the minimum-invasive fix.

### MINOR

**MINOR-1 — SpArcFiRe cross-check is apples-to-oranges, but the paper does
not flag the heterogeneity at the level it merits.**
*Location:* §IXB (L1631–1675).
*Issue:* SpArcFiRe (Davis & Hayes 2014) is a deterministic image-processing
algorithm that fits log-spiral arcs to galaxy surface-brightness profiles.
The present paper's classifier is a ViT-Small trained on a label corpus
that is 67.6% CE-ResNet pseudo-labels + 32.4% GZ1 + synthetic negatives.
These two methods agree on the CW/CCW *symbolic* class but not on the
*selection function* for "what counts as a classifiable spiral": SpArcFiRe
requires arms detectable above a brightness threshold and a coherence
threshold, the ViT just routes ambiguous cases to NS. The paper's
~1.4×10⁵-galaxy SpArcFiRe overlap is therefore not a fair monopole-bias
cross-check; it is a check on the *subset of galaxies where both pipelines
declared a chirality*, which is a biased subset of the parent.
*Fix:* Add one sentence in §IXB acknowledging that the SpArcFiRe overlap is
a "both-pipelines-confident" subset and not a parent-sample-level
cross-check, then commit to a per-galaxy joint table in the planned
follow-up note (the paper already promises this at L1668–1671 — just
strengthen the language).

**MINOR-2 — Shamir's contested-results literature is not engaged at the
methodology level beyond "no published bias audit."**
*Location:* §IXA (L1555–1610).
*Issue:* The paper says Shamir's Ganalyzer "is deterministic and by
construction yields identical CW/CCW probabilities for an image and its
mirror reflection." That is the *strongest* possible framing of Shamir's
methodology — it is also the framing Shamir himself uses. Two specific
methodological concerns from the contested literature are missing:
(a) Ganalyzer's "automatic radial intensity slicing" step depends on the
chosen center-of-light, and the center-of-light has a known PSF-dependent
asymmetry (Hayes+2017 ApJ 841, 91 — same Hayes as SpArcFiRe coauthor).
(b) Shamir's 2020/2022 results draw from heterogeneous survey overlays
(SDSS + Pan-STARRS in 2020; DESI Legacy in 2022) without imaging-band
matching. The paper mentions "heterogeneous surveys with varying depths"
(L1583) but does not cite the Hayes+2017 PSF-asymmetry paper that gives
the *mechanism* for the Shamir signal.
*Fix:* Add Hayes+2017 to the bibliography and cite it in §IXA as the
proposed mechanism by which Shamir's Ganalyzer can produce a position-
dependent chirality probability under non-uniform PSF.

**MINOR-3 — Iye+2020 PASJ citation is correct but the methodology comparison
is shallow.**
*Location:* §IXA-end (L1587–1602).
*Issue:* Iye+2020 (correctly cited as ApJ 907, 123, arXiv:2010.04830) used
*log v_c* binning on SDSS spirals as their primary axis — they binned by
*circular velocity* (a galaxy-scale-mass proxy) and looked for handedness
asymmetry in mass-binned subsamples. The present paper does not have a
mass-binned (or velocity-binned) chirality test. The Iye+2020 null is a
*mass-resolved* null; the present paper's null is a *position-resolved*
null. These are orthogonal observational channels, not redundant
confirmations of each other.
*Fix:* Add one sentence in §IXA acknowledging that the Iye+2020 null is
mass-resolved while the present null is position-resolved, and that the
two together constitute orthogonal coverage rather than redundant
confirmation. (This actually *strengthens* the paper's "multi-survey
multi-classifier consensus" framing at L1599–1600 because the consensus
spans methodologies, not just sample sizes.)

**MINOR-4 — Recent 2023–2026 morphology-systematics literature on the
imaging-asymmetry question is uncited.**
*Location:* §IXA (L1539–1546) and bibliography.
*Issue:* The paper cites Walmsley+2023 (Galaxy Zoo DESI), but four
recent observational-systematics papers on the imaging-vs-classifier
question are not in the bibliography:
- Walmsley+2022 MNRAS 509, 3966 — Galaxy Zoo DECaLS bar-detection
  systematics (ground-based, directly relevant to the imaging-asymmetry
  question the paper is trying to bound);
- Vega-Ferrero+2024 MNRAS 528, 1494 — DES Y6 morphology with deep-learning
  classifiers, including a section on chirality-related orientation
  systematics in ground-based imaging;
- Euclid Q1 morphology release (Euclid Collaboration, 2024–2025) — first
  space-based morphology at this scale, directly relevant to the
  HST/JWST-vs-ground bias question;
- Masters+2024 MNRAS 530, 2459 — community review of citizen-science vs
  CNN morphology agreement, with a section on handedness-specific
  systematics.
At least Walmsley+2022 and Vega-Ferrero+2024 should be cited in §IXA as
context for the "ground-based imaging asymmetry is a known nontrivial
systematic" claim.
*Fix:* Add the two strongest references (Walmsley+2022 DECaLS and
Vega-Ferrero+2024 DES Y6) to §IXA and the bibliography.

**MINOR-5 — Magnitude/PSF/half-light-radius binning audit is referenced
("T5" in Table II at L702) but the actual binned CW-fraction numbers are
not shown.**
*Location:* §IVD–§V audit text (L669–698, L740–760).
*Issue:* The paper says "we ran a magnitude/PSF/half-light-radius binning
audit and verified there are no significant magnitude-dependent and
PSF-dependent CW-fraction variations" but the per-bin numbers do not
appear in any table. The reader is asked to take the audit on faith.
For an observational paper this is the *single most important table* —
a reviewer at MNRAS / PASP / ApJ will request it explicitly.
*Fix:* Add a 3-panel binned-CW-fraction figure (r-mag bins × CW fraction,
PSF FWHM bins × CW fraction, half-light-radius bins × CW fraction) in
§V or as an appendix figure. The numbers presumably exist in the
production catalog already — this is a 1-hour matplotlib job.

### NIT

**NIT-1 — "Hubble image vs ground-based" homogeneity is not stated.**
*Location:* §IIIA absence.
*Issue:* The parent sample is 100% ground-based DESI Legacy DR8 imaging.
This should be stated explicitly. Right now the reader has to deduce it
from the Dey+2019 reference. A one-clause statement in §IIIA ("the
parent sample is homogeneously ground-based; no HST/JWST cutouts are
included, so space-based-vs-ground systematics do not enter") would
close this for the referee.

**NIT-2 — Coordinate-system-independence of the parity-violation observable
is implicit, not stated.**
*Location:* §V/§VI dipole sections.
*Issue:* The paper computes the chirality dipole as a vector field on the
celestial sphere (HEALPix maps + spherical-harmonic decomposition). A
cosmologist will ask: is the parity-violation observable being computed
as an *axial vector* (galaxy spin projected onto line-of-sight, which
flips under parity) or as a *pseudoscalar* (handedness label, which is a
parity-odd scalar)? The present paper's observable is a pseudoscalar
(the CW/CCW label is a binary parity-flip eigenvalue), and that is the
correct choice for a morphology survey because the line-of-sight axis
is unknown for any individual galaxy. But the paper never uses the word
"pseudoscalar" or "axial vector" — both are absent from the text. A
single sentence in §V clarifying "the observable is the pseudoscalar
chirality label, integrated against the survey-footprint mask; this is
parity-odd by construction and does not require knowledge of the
line-of-sight spin axis" would address this.

**NIT-3 — Edge-on routing rate (~6 pp lower than the visual-ID-curated
b/a < 0.3 subsample, L2178–2180) is stated but not closed.**
*Location:* §X.B-end.
*Issue:* The paper acknowledges that the production catalog's edge-on
spiral classification rate is ~6 percentage points lower than a
visual-ID-curated b/a < 0.3 subsample, then says "we adopt the
full-DR8-sweep value." That is a reasonable disposition but the
6 pp gap is the largest unaccounted disagreement in the catalog and
deserves either a one-paragraph reconciliation (what visual-ID-curated
subsample? from where?) or a forward-pointer to the follow-up artifact.

---

## Counts

| Severity | Count |
|---|---|
| BLOCKER | **0** |
| MAJOR | **4** |
| MINOR | **5** |
| NIT | **3** |
| **Total** | **12** |

---

## Disposition recommendation

P4 v1.0.47 is **above the cross-vendor R-round bar for content** (no blockers,
the dipole-channel science is clean) and **below the bar for observational-
systematics disclosure**. The 4 MAJOR findings are all
*scope-extension-disclosure* fixes, not data-redo fixes — none of them
question the dipole null result or the 0.5% upper limit. They question
whether the *defense* of that upper limit is currently strong enough to
survive an observational-astronomy referee.

Per `feedback_99_pct_readiness_cap.md`: this round is **not clean** (4 MAJOR
findings), so the 95% readiness cap should **hold** until v1.0.48 closes
at minimum MAJOR-1 (parent-sample selection function) and MAJOR-4 (rename
the 7-region claim). MAJOR-2 and MAJOR-3 are next-revision-cycle targets.

**Suggested v1.0.48 wave (Houston-directable):**
1. §IIIA selection-function paragraph (MAJOR-1) — 1 hr.
2. Global rename "uniform at 7-region survey-footprint granularity" →
   "uniform across 7 equatorial coordinate slabs" + §VIIIA disclosure
   sentence (MAJOR-4) — 30 min.
3. §IIIB GZ1-magnitude-asymmetry paragraph + Walmsley+2023 handedness-
   omission citation (MAJOR-2) — 1 hr.
4. Rotation-TTA empirical bound on 10k–100k validation sample (MAJOR-3) —
   2 hr GPU + 30 min writeup.
5. §V magnitude/PSF/half-light-radius binned-fraction figure (MINOR-5) —
   1 hr.

Total: ~6 hr of edits + 2 hr GPU. v1.0.48 closure would lift the
observational-systematics ceiling on P4 by approximately one notch and is
the last natural barrier before Houston-sign-off + clean cross-vendor R is
viable.
