# Independent scientific-value assessment of the BigBounce portfolio

**Date:** 2026-09-02
**Requested by:** Houston Golden (owner), in confidence
**Stance:** strategic, not a referee report. Challenge, not reassurance.
**Method:** every current manuscript read in full (or skimmed where noted);
literature checked against the arXiv API (every id below was resolved live on
2026-09-02; nothing is cited from memory alone). "Fact" and "Judgment" are
separated throughout. Where I could not verify something, I say so.

---

## 0. The one-paragraph answer

There are **two** genuine papers in this repository today (P2 and P4), **one**
potential paper that does not yet exist (the DESI anomaly flagship), **one**
optional short software note (P1B), and **five** documents that should stop
consuming review cycles (P1A, P1C, the MCMC companion, current P3, P5). Only
one of the nine — P2 — is on the stated vision ("show bounce cosmology beats
ΛCDM+inflation, bounce-model agnostic"). The three-program framing is an
honest description of what exists, but it is a retrofit: two of the three
programs have, by their own manuscripts' admission, no bounce content and no
path to any. The portfolio strayed in early 2026 when a specific model
(minimal Einstein–Cartan–Holst as a *dark-energy* source) was pursued to
exhaustion and its negative residue was split into four documents, and when
two survey-ML products (chirality, anomalies) were kept alive after the bounce
motivation for them was removed. The way back is not more manuscripts; it is
one calculation (cubic transmission of f_NL through an explicit nonsingular
bounce) plus two or three cheap, model-agnostic observational tests listed in
§4.

---

## 1. Per-work assessment

Format for each: **Fact** (what the manuscript says/contains) → **Novelty vs
literature** → **Publishability / honest venue** → **Verdict**.

### 1.1 P2 — "The Exact Matter-Contraction Non-Gaussian Amplitude" (`research/focused_paper_source_integration/02_full_draft.tex`, v1.7.130, ~11 pp PRD)

**One-sentence description a field expert would use:** "They claim the
squeezed-limit local f_NL of the canonical matter bounce is −35/16, not the
−35/8 printed by Cai, Xue, Brandenberger & Zhang (2009), via a vertex-by-vertex
re-summation of the same cubic action."

**Fact.**
- Headline: f_NL^local = −35/16 for ε=3/2 contraction, ordered-basis
  coefficients (3,1,−9,5,−33,9), symbolic (sympy) cross-checks; benchmarks
  −35/16 / −255/128 / −9/8 (squeezed / equilateral / folded).
- The paper states that *both* printed polynomials (Cai et al. Eq. 37 and
  Li–Quintin–Wang–Cai 2016 Eq. 4.19 at c_s=1) reduce to −35/8, and that the
  vertex re-summation yields −35/16 "independently of either printed
  polynomial" (changelog v1.7.102).
- The SPHEREx section is labelled "illustrative … not an observational
  headline"; the nuisance ladder runs 3.5σ → 0.4σ depending on whether b_φ is
  free. Nonlinear (third-order) transmission through the bounce is stated as
  open; only linear transmission (Wilson-Ewing 2012) and a dressed-metric
  cubic gate are established.
- 209 commits on this file; ~160 lines of changelog comment precede the text.
- The stale `arxiv/main.tex` (v2.3.18, May 2026) and
  `project-context/bounce_portfolio_strategy.md` still carry −35/8 as the
  flagship number. The repo is internally inconsistent on its own headline.

**Novelty vs literature (verified):**
- Cai, Xue, Brandenberger, Zhang, arXiv:0903.0631 (JCAP 2009) — the origin of
  the matter-bounce bispectrum; the −35/8 value is from its body (abstract
  does not state it; I did not re-derive it).
- Li, Quintin, Wang, Cai, arXiv:1612.02036 — generalized-c_s matter bounce
  bispectrum; extended no-go.
- Quintin, Sherkatghanad, Cai, Brandenberger, arXiv:1508.04141 — f_NL is
  enhanced through the bounce if curvature perturbations grow; single-field
  matter bounce no-go (r vs f_NL tension).
- Dehghani, Geshnizjani, Quintin, arXiv:2503.01992 (2025) — cuscuton bounce
  bispectrum computed *through* the bounce; finds negligible NG on observable
  scales in their (isocurvature-seeded) setup. This is the current state of
  the art for "does the contraction-phase bispectrum survive the bounce" and
  P2 does not engage it.
- Choudhury et al., arXiv:2409.18983 — uses f_NL=−35/8 as the matter-bounce
  input for PBH abundance.

**Status of the headline:** *new if correct.* A factor-of-two correction to a
17-year-old, widely-cited coefficient is a legitimate short theory paper. I
could not verify the algebra here and I note the asymmetry of evidence: two
published derivations (overlapping authors) versus one unpublished
re-summation plus a self-run symbolic check. The v1.7.106 changelog's own
phrase "evidence DECISIVELY FAVORS −35/16" is the wrong register — it is a
claim that needs an *independent human* derivation (a different gauge or the
δN / in-in with different field variables), not more LLM review rounds.

**Publishability / venue (judgment):** PRD or JCAP short paper, ~5–6 pages:
the derivation, the ordered-basis result, the discrepancy diagnosis (App. A),
one table of shape benchmarks, and a two-paragraph consistency-relation check
against Planck. A strong referee will (a) demand the independent check above,
(b) delete the SPHEREx sigma ladder as not load-bearing, and (c) ask why the
result matters given arXiv:1508.04141 and arXiv:2503.01992 — i.e., whether
−35/16 survives any actual bounce. (c) is the real scientific gap and is
exactly the next experiment (§4.1).

**Verdict: KEEP — RESCOPE to a ≤6-page theory Letter/short paper; get one
independent human derivation before submission; fix the −35/8 residue
everywhere in the repo and site.** This is the only manuscript on the vision.

### 1.2 P1A (current) — "Algebraic Cartan Elimination in Minimal ECH Gravity" (`arxiv/paper1a_ech_nogo.tex`, v1A.0.127, 8 pp, targeted at CQG as a Note)

**One-sentence description:** "A convention-audited restatement that in
minimal ECH the connection is algebraic, spin sources give the standard
−(3κ/16)γ²/(1+γ²) J₅² contact term, and spinless scalar matter sees exactly
GR."

**Fact.** The abstract's own closing sentences: "The identities used here are
standard. The contribution is their convention-audited consolidation… no ECH
dark-energy or birefringence prediction is made." 3,300+ of 5,142 lines are
`\begin{comment}` blocks holding the old four-route dark-energy version.

**Novelty vs literature (verified):** the contact term and its γ-dependence
are in Freidel–Minic–Takeuchi, arXiv:hep-th/0507253; Perez–Rovelli,
arXiv:gr-qc/0505081; Mercuri, arXiv:gr-qc/0601013; the torsion-vanishes-
without-spin statement is Hehl et al. 1976 (RMP 48, 393). Alexandrov,
arXiv:0802.1221 argues the Immirzi dependence can be reabsorbed with general
non-minimal coupling — a point that limits how "physical" the γ²/(1+γ²) factor
is and which the Note does not confront.

**Status:** re-derivation/consolidation. Not new.

**Publishability:** a CQG referee would ask "what does the reader learn that
is not in FMT 2005 §III?" and the honest answer is a dimensional benchmark
(κn²/ρ_Λ ~ 10⁻⁶⁹) that nobody disputed. This is an appendix, not a Note.

**Verdict: RETIRE as standalone (content preserved).** It already has a
Zenodo DOI; that is the right terminal state. If any ECH text is kept alive,
this becomes Appendix A of the merged ECH note (§1.4).

### 1.3 Stale `arxiv/main.tex` — "Structural Closure of ECH Dark Energy…" (v2.3.18, May 2026, 34 pp)

**Fact.** Pre-split draft still on disk with f_NL=−35/8, an LQC bounce density,
a withdrawn NANOGrav Bayes factor marked SUPERSEDED inline, a galaxy-spin
null, an MCMC proxy, and a "Theoretical Research Program" section.
**Verdict: RETIRE — move under `arxiv/_retired/` with a README pointing to the
split papers.** Its continued presence at the canonical path is the reason the
task brief (and any future agent) will misidentify it as P1A.

### 1.4 P1C — "A Structural No-Go Survey of Minimal Spin-Torsion Routes to Dark Energy and Bounce Phenomenology" (`arxiv/paper1c_nogo_survey/main.tex`, v1C.0.16, 25 pp)

**One-sentence description:** "A catalogue of fourteen reasons minimal ECH
cannot be the dark energy, of which two are theorems and the rest are
dimensional-analysis or naturalness statements."

**Fact.**
- Only B14 (the scalar-transparency statement — the same content as P1A) is
  graded Tier-I by the paper itself. Route-2/3 closures are "Tier-III
  ansatz-level" estimates (58–67 orders of magnitude).
- Five of fourteen barriers are self-described as not ECH-specific.
- The 2009 Cai matter-bounce literature is not cited; the paper is not about
  bounce non-Gaussianity despite "Bounce Phenomenology" in the title.
- External review R10→R13: Grok REJECT four consecutive rounds ("defects are
  structural and cannot be repaired by minor revision"); Gemini oscillated
  minor → major → accept → major. Recurring complaints across ≥2 rounds:
  not self-contained (leans on unpublished P1A), abstract outruns body, the
  "fourteen" count is inflated, too long for its Tier-I content, unfrozen
  computational DOI, M_Pl symbol overloading, R4 channel rests on the
  companion.

**Novelty vs literature (verified):** Torsion-as-Λ was proposed by Poplawski,
"Cosmological constant from quarks and torsion", arXiv:1005.0893; his
torsion-bounce papers are arXiv:1007.0587, 1105.6127, 1111.4595, and
Cubero–Poplawski arXiv:1906.11824 (all verified). P1C cites Poplawski 2010
exactly once, in passing (line 2391); the no-go is never framed as "this
closes the arXiv:1005.0893 proposal," which is the only framing under which
a referee would see a target worth closing. A crisp
no-go against a specific published proposal is a legitimate short paper. A
25-page barrier catalogue against a hypothesis few people held is not. The
scale-invariant EC line (Shaposhnikov et al., arXiv:2007.16158; Långvik et
al., arXiv:2007.12595) and the Nieh–Yan bounce line (Bombacigno et al.,
arXiv:2111.03338) are the live ECH-cosmology literature; a referee from that
community would note that P1C's "minimal" assumptions exclude exactly the
models people now study.

**Status:** null result of marginal interest; mostly re-derivation.

**Publishability:** as-is, not at CQG/PRD (four straight rejects from the
harsher calibrated referee is the signal, not noise). As a ≤10-page note
"Minimal ECH cannot source Λ: two theorems and their scope" with P1A folded
in as the appendix, it would be an acceptable gr-qc posting and a plausible
CQG Note. Even then, its scientific value is low and its opportunity cost —
thirteen review boards — has been very high.

**Verdict: MERGE P1A INTO P1C, cap at ≤10 pages, one arXiv gr-qc posting, then
stop.** No further INT/EXT rounds. This entire ECH-dark-energy branch is the
clearest case of the portfolio straying: it is model-specific (violates the
agnostic rule), about dark energy rather than the bounce, and produced only
negative content.

### 1.5 P1B — `namaster-proof` software paper (`arxiv/paper1b_namaster_proof.tex`, v2B.0.16, ~8 pp, JORS-style)

**One-sentence description:** "A small Python layer that evaluates a rotated
EE/EB/BB spectrum through the full NaMaster bandpower-window operator and
writes hash-bound result receipts."

**Fact.** 41 tests; window-operator equivalence to 1.4×10⁻¹⁸; no cosmology
content; not affiliated with NaMaster. Zenodo software DOI exists.

**Novelty:** methods/software. NaMaster (Alonso, Sanchez, Slosar, MNRAS 484,
doi:10.1093/mnras/stz093) already exposes `get_bandpower_windows`; the
contribution is a guard-rail plus provenance receipts. Real but thin.

**Publishability:** JOSS/JORS would likely accept a short software paper if
the package has tests, docs, and a stated user beyond the author. It is not a
science paper and should not be counted as one.

**Verdict: KEEP as optional software note, lowest priority.** Submit to JOSS
(shorter, faster) or leave at Zenodo. Zero further review rounds.

### 1.6 MCMC companion — "Reproducible Cosmological Proxy and Pipeline Checks" (`arxiv/paper1b_mcmc_companion.tex`, v1B.0.112, ~20–24 pp PRD)

**One-sentence description:** "Three unrelated exercises — a stock-CAMB
ΛCDM+ΔN_eff run, a synthetic NaMaster rotation-recovery test, and a spectator-
ALP fit to a published birefringence number — each prefaced by a statement
that it is not evidence for anything."

**Fact.** Abstract: "None implements a torsion-modified Boltzmann solver, none
measures torsion, and none is evidence for ECH gravity or for a bounce
cosmology." ΔN_eff = −0.020±0.169 (Planck 2018 itself: N_eff = 2.99±0.17).
~1,300 of 3,381 lines are changelog comments. 117 commits.

**Novelty:** none. The ΔN_eff result reproduces Planck 2018; the NaMaster test
is the P1B validation campaign re-reported; the ALP "accommodation" of
β≈0.34° (Eskilt & Komatsu, arXiv:2205.13962) is explicitly not a prediction.

**Publishability:** no PRD referee accepts a paper whose abstract says it is
evidence for nothing. Its value is as a reproducibility record.

**Verdict: RETIRE (content preserved at Zenodo).** Do not submit anywhere.

### 1.7 Current P3 — "Public-ID Recovery for a Historical DESI DR1 Anomaly List" (`pipelines/p3_anomaly_engine/paper3_apjs.tex`, v3.2.0-r17, 17 pp ApJS)

**One-sentence description:** "A k-d-tree rejoin of 190,015 historical
anomaly clusters to DESI DR1 public TARGETIDs, yielding 181 warning-free
associations, with the caveat that the sub-0.1″ core is self-recovery of the
seed objects."

**Fact.** No bounce content. The paper's own abstract states the core tier
"verifies the recovery end-to-end rather than providing independent
association evidence" and the outputs are "not validated detections."

**Novelty:** a data-provenance repair. The interesting number (181 of a
195,829-row list are rejoinable) is a statement about the lab's earlier
bookkeeping, not about DESI.

**Publishability:** not a standalone ApJS paper (the repo already reached this
conclusion on 2026-08-03; I agree). At most an RNAAS-length note or a Zenodo
data release cited by the flagship.

**Verdict: RETIRE as a paper; keep as a data release (already decided).**

### 1.8 Old P3 — multi-survey autoencoder catalogue (`pipelines/p3_anomaly_engine/paper3_draft.tex`, deprecated)

**Fact.** 268,519 "validated" anomalies across six archives; LAMOST and
eROSITA injection-recovery FAIL (5.8%, 1.2%); NANOGrav fit claiming SMBHB
disfavoured at +4.63σ and matter-bounce γ=3 within +1.14σ; a 9.5% σ(f_NL)
improvement the claim inventory later found to be "not a result." The claim
inventory (2026-08-03) documents that the parent catalogue cannot be restored
and that headline numbers conflict across generations.

**Judgment.** Correctly retired. Two pieces of content are worth preserving
as *ideas* (not as results): (i) the PTA free-spectrum test of the
matter-bounce γ=3 prediction, which is on-vision and model-agnostic (§4.3) —
but the +4.63σ-against-SMBHB number should be treated as unreproduced until
redone, because NANOGrav's own analyses find SMBHB consistent; (ii) anomaly-
selected tracers for f_NL — dead unless a selection-function analysis is
done. **RETIRE (content preserved).**

### 1.9 Planned anomaly flagship — DESI DR1 clean-rerun autoencoder scan (architecture doc 2026-08-05; not drafted)

**One-sentence description (intended):** "A survey-scale, provenance-sealed
reconstruction-outlier scan of 27.5 million DESI DR1 spectra, with a
characterised 3,810-object S≥8 candidate slice and a rebuilt taxonomy."

**Fact.** AUG-011 completed: 28,425,963 rows → 27,547,223 unique TARGETIDs;
52,188 at S>5; 3,810 at S≥8 (decision 2026-08-26). Cross-match, taxonomy,
per-class injection-recovery, and notable-object validation are all still
PLACEHOLDER. The architecture doc rules f_NL out of the paper. The model is
the archived 496→512→256→128 deterministic autoencoder trained in 2025.

**Novelty vs literature (verified):** Liang, Melchior, Hahn et al.,
arXiv:2307.07664 (outliers in DESI BGS); Nicolaou, Nathan, Lahav,
arXiv:2506.17376 (VAE on DESI spectra); Astronomaly at scale, Etsebeth et
al., arXiv:2309.08660 (4M galaxies); Lochner & Bassett, arXiv:2010.11202. The
lab's differentiators are scale (full DR1 rather than BGS) and sealed
provenance. Scale alone is not a scientific result; the paper becomes real
only if the taxonomy or the notable-object gate produces something a
DESI collaboration paper has not — e.g., independently validated z>6 QSO
candidates, or a new spectral class.

**Publishability:** ApJS catalogue paper with substantial remaining work
(cross-match, taxonomy, per-class validation, at least a few independently
validated objects). Plausible in 2–3 months of focused work. Off-vision: it
is an astro-ph.IM/GA product with no bounce content, and the manuscript
architecture already says so.

**Verdict: KEEP AS A SEPARATE SURVEY-ML PRODUCT, contingent on the taxonomy
finding something.** Do not call it a bounce-program paper. Hard stop rule: if
after cross-match and taxonomy no candidate survives independent validation,
release the catalogue at Zenodo/HF with a short data note and do not write
the ApJS paper.

### 1.10 P4 — DESI chirality catalogue and dipole null (`pipelines/p2_chirality/chirality_catalog_paper.tex`, v1.0.274, ~25 pp, ApJS-formatted; 347 commits)

**One-sentence description:** "An 8.47-million-galaxy ViT handedness catalogue
from DESI Legacy DR8 imaging whose 890k high-confidence spirals show no
observed-label dipole (z=+0.64, p=0.24; A₉₅ ≈ 0.98%)."

**Fact.** The paper states the ℓ=1 morphology observable is parity-even and
yields no primordial-parity bound. A composition-faithful retrain of the
classifier "collapses to chance on chirality"; a residual handedness monopole
(f_CW ≈ 0.5012) has "unresolved upstream label asymmetry." Longo 2011, Land et
al. 2008 (Galaxy Zoo), Iye et al. 2020, and Hayes et al. are not all cited
(Land and Longo absent).

**Novelty vs literature (verified):** Land, Slosar, Lintott et al.,
arXiv:0803.3247 (Galaxy Zoo; apparent excess traced to human bias); Longo,
arXiv:1104.2815 (claimed dipole); Shamir, arXiv:2208.13866 (DESI Legacy,
claimed asymmetry) and arXiv:2204.01192; Iye, Yagi, Fukumoto,
arXiv:2011.00662 (SDSS dipole null with 3D random-walk simulations; Shamir's
signal not reproduced); Tadaki, Iye et al., arXiv:2006.13544 (80k HSC
spirals via deep learning, null); Iye & Yagi arXiv:2605.05570 (2026, HSC
Wide). P4 is the largest catalogue in this line and its null agrees with
Iye/Tadaki against Shamir.

**Status:** a replication null on a larger sample plus a catalogue release.
Genuine, moderately useful to the Shamir-vs-Iye debate. Not a cosmology
result.

**Publishability:** yes, with cuts — AJ or MNRAS (ApJS is acceptable for the
catalogue). A strong referee will focus on the label-asymmetry issue (the
monopole and the retrain collapse are the paper's soft underbelly; mirror-flip
symmetrisation at training time is the standard fix and the paper should
either show it or explain why not) and will want the paper to be ~12–15
pages, not 25 with 18 tables.

**Verdict: KEEP — RESCOPE to a ≤15-page catalogue + null paper; stop review
loops; submit.** Make no bounce claim; there is none to make.

### 1.11 P5 — chirality vs DESIVAST environment (`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`, v0.1.147, 46 pp, 28 tables)

**One-sentence description:** "Classifier-labelled CW fraction does not differ
between DESIVAST void and non-void galaxies (Δf_CW = +0.0015 ± 0.0033, p=0.66),
in an exploratory, post-hoc analysis for which no model predicts a signal."

**Fact.** The abstract says: hierarchy "changed after review and after
inspecting the data"; "exploratory, post-hoc, and not preregistered"; the
introduction says the authors "identify no bounce or inflation model that
predicts a specific signal for this … estimand." 46 pages for one null with
a 2.4-pp CI width. Two large `\iffalse` dead-text blocks remain in source.

**Novelty:** none in the literature sense — the physically motivated
spin–environment literature (Motloch/Yu/Pen, arXiv:1904.01029, spin–tidal
alignment as a chirality probe) uses 3D spin vectors, which P5 does not have.
A handedness-vs-void null with no predicted effect is not a finding.

**Publishability:** AJ would not, in my judgment, take this as a standalone
paper; a strong referee's first question ("what would a detection have
meant?") has no answer in the manuscript.

**Verdict: MERGE INTO P4 as a one-page subsection (or an RNAAS note); RETIRE
the standalone.** This is the clearest example of a paper that exists because
a catalogue existed, not because a question did.

### 1.12 Retired concepts with surviving content

- **Quintom / Lee–Wick bounce f_NL (strategy doc Track B):** never executed.
  Good on-vision idea (§4.2).
- **PBH regulation by negative f_NL (Choudhury et al. arXiv:2409.18983):**
  never executed with the lab's own number (§4.4).
- **NANOGrav γ=3 test (Papanikolaou arXiv:2504.11641):** executed once inside
  old P3 with unreproduced numbers; worth redoing cleanly (§4.3).
- **"Structural tension: ECH dark energy vs bounce f_NL" section of the
  monolith:** dropped from every split paper. It was the only sentence in the
  ECH line that connected to the vision; it is also moot once ECH-DE is
  retired.
- **Galaxy-spin chirality as an ECH parity probe** (March 2026 fragment
  `paper2_chirality_section.tex`): theoretically undercut by the lab's own
  P1A transparency result (scalar sector of minimal ECH is GR) and by P4's
  admission that image handedness is parity-even. Retire the idea; the live
  parity-odd LSS observable is the 4PCF (§4.5).

---

## 2. The owner's questions

### 2.1 How many real papers are there?

| Work | Real paper? | Publishable now / with work / not | Honest venue |
|---|---|---|---|
| P2 | **Yes** (if −35/16 survives an independent check) | Now, after rescoping to ≤6 pp + one human check | PRD / JCAP short |
| P4 | **Yes** | With work (cut to ≤15 pp; address label asymmetry) | AJ / MNRAS / ApJS |
| Anomaly flagship | **Potentially** | With substantial work; contingent on finding something | ApJS |
| P1B | Software note | Now, if wanted | JOSS |
| P1A + P1C merged | Marginal note | With merge + cut to ≤10 pp | arXiv gr-qc; maybe CQG Note |
| MCMC companion | No | Not | Zenodo only |
| Current P3 | No (data release) | — | Zenodo/HF + RNAAS at most |
| P5 | No | — | Fold into P4 |
| Old P3, stale main.tex | No | — | Retired |

**Count: 2 real papers now, 1 contingent, 2 optional notes.** Not six, not
three.

### 2.2 Is the "three research programs" organisation right?

**Fact.** The reset document (2026-08-03) defines programs by research
question: bounce theory (P2 lead), survey discovery (anomaly flagship lead),
galaxy chirality (P4 lead). The chirality and anomaly manuscripts each state
that they test no bounce prediction.

**Judgment: no — it is honest but it is not a research program structure, it
is a filing structure for what happened to get built.** Two of the three
"programs" are DESI machine-learning data products with no cosmological
question attached; calling them programs of a bounce-cosmology lab makes the
lab look unfocused to exactly the readers (bounce theorists, DESI
collaboration members) whose opinion matters. A better structure:

1. **Bounce phenomenology (the lab's actual identity).** One lead paper (P2,
   tightened) and a queue of concrete positive-discovery experiments (§4).
   Everything here must be bounce-model agnostic and must produce a number
   that ΛCDM+inflation predicts differently.
2. **DESI survey-ML data products (program-agnostic, astro-ph.IM/GA).** P4 and,
   if it earns it, the anomaly catalogue. Present them as what they are:
   large, well-provenanced catalogues with one clean null or one clean
   candidate list each. No bounce framing, no "program" language.
3. **Closed side-branch: minimal ECH.** One merged arXiv note, then nothing.
   Listed on the site under "completed/negative" so the lab is seen to close
   lines rather than accumulate them.

This is "a single flagship plus notes," which is how a small independent lab
is actually read. The site should lead with P2 and the open experiments, not
with a six-card or three-card grid of equal weight.

### 2.3 Where has the portfolio strayed from the vision?

Vision: *show bounce cosmology beats ΛCDM+inflation; bounce-model agnostic.*

1. **The ECH dark-energy line (P1A, P1C, MCMC companion, stale main.tex, and
   the monolith) is a model-specific dark-energy project, not a bounce
   project.** It violates the agnostic rule by construction, and its output
   is entirely negative. Four documents and roughly 300 commits were spent
   discovering that minimal ECH does nothing to scalar perturbations — which
   is a consequence of the algebraic Cartan equation that Hehl wrote down in
   1976. The lab's own CLAUDE.md directive ("never … document the barriers
   as a paper") was, in effect, overridden by the review loop.
2. **Chirality started as an ECH parity observable and outlived its
   motivation.** Once P1A proved the scalar sector is GR and P4 conceded the
   observable is parity-even, no bounce model predicts a galaxy-handedness
   dipole; the catalogue is still useful, but it is not a bounce test and
   P5 compounded the drift.
3. **The anomaly engine started as an f_NL tracer-selection tool (on-vision)
   and became a provenance exercise.** The one on-vision use — a defensible
   σ(f_NL) gain from anomaly-selected tracers — was found to be "not a
   result." What remains is a survey-ML product.
4. **P2 itself drifted toward forecast padding.** The contraction-phase
   coefficient is the science; ~40% of the manuscript is a SPHEREx mapping
   the abstract calls "not a headline."
5. **The review machinery became the product.** Facts: 347 commits on P4's
   .tex, 209 on P2's, 138 on P1A's; changelog comment blocks of 160–1,300
   lines; abstracts that are majority disclaimer (MCMC companion, P5). A human
   referee reads a paper that spends most of its abstract on what it is not
   as a paper with nothing to say. Thirteen boards on P1C against a referee
   that rejected four times in a row is the loop optimising the wrong
   objective.

### 2.4 Uncertainties in this assessment

- I did not re-derive −35/16. If it is wrong, P2 collapses to a confirmation
  of Cai et al. and the lab has zero papers on the vision — which raises,
  not lowers, the priority of the independent check.
- I did not audit P4's classifier or the monopole systematics; my "keep" is
  conditional on the label-asymmetry story being resolvable.
- I have not seen the anomaly flagship's cross-match/taxonomy outputs (they
  do not exist yet); "contingent" is the strongest word I can use.
- Venue judgments are mine; a different senior referee could plausibly put
  the merged ECH note at CQG rather than arXiv-only.

---

## 3. Recommended ideal paper set (12-month horizon)

1. **P2′ — "The matter-contraction bispectrum amplitude is −35/16" (PRD/JCAP,
   ≤6 pp).** After one independent human derivation. Submit first.
2. **B1 — "Does the contraction-phase bispectrum survive the bounce?"** The
   cubic-transmission calculation through one explicit nonsingular bounce
   (§4.1). This is the paper that turns P2′ into a *prediction* and is the
   single most valuable thing the lab can write. PRD.
3. **B2 — "Model-agnostic PTA and PBH consistency of a matter-contraction
   phase"** (§4.3–4.4). JCAP/PRD short. Cheap, on-vision, positive-discovery
   shaped.
4. **P4′ — DESI Legacy handedness catalogue + dipole null (≤15 pp, AJ/MNRAS)**
   with P5's environment null as one subsection.
5. **Anomaly catalogue (ApJS)** — only if the taxonomy/validation gate
   produces validated objects; otherwise a Zenodo/HF data note.
6. **ECH note (arXiv gr-qc; optional CQG Note)** — P1A+P1C merged, ≤10 pp,
   no further review rounds.
7. **`namaster-proof` (JOSS)** — optional.

Everything else: Zenodo DOIs stand; no journal submission.

---

## 4. Next experiments that move toward the vision (positive-discovery, tractable)

Per the repo's research directive these are research directions, not
write-ups. Ordered by leverage per month.

### 4.1 Cubic transmission through an explicit nonsingular bounce (highest leverage; 4–8 weeks)

**Why:** P2's own open item; arXiv:1508.04141 says f_NL is enhanced through
the bounce if curvature grows, arXiv:2503.01992 computed a bounce bispectrum
end-to-end and found negligible NG in their setup. Whether −35/16 is *the*
bounce prediction, or a pre-bounce coefficient that gets rescaled by an O(1–
10) transfer factor, is currently unknown — and it is the difference between
"bounce beats inflation at SPHEREx" and "no prediction."
**What:** pick two bounce completions with known stable linear transmission
(LQC/dressed-metric, already in P2 at linear order; and the cuscuton bounce
of Kim & Geshnizjani arXiv:2010.06645 / Dehghani et al. arXiv:2503.01992),
derive the third-order action through the bounce, compute the in-in
bispectrum transfer T₃(k₁,k₂,k₃) numerically, and report f_NL^after =
T₃ × (−35/16) with shape. Model-agnostic framing: "for any bounce whose
transfer is ≤X, the prediction is −35/16 to Y%."
**Positive-discovery shape:** a concrete, testable number (or a bounded
band) plus the shape distortion — a signature ΛCDM+inflation does not give.

### 4.2 Is −35/16 mechanism-independent? Quintom / Lee–Wick / k-essence contraction (2–4 weeks, analytic)

**Why:** strategy doc Track B, never executed; arXiv:1612.02036 already
gives the general-c_s result — the lab can cross-check its −35/16 against
Li et al.'s general-c_s formula at c_s≠1 (P2 says it did at c_s=1 only) and
then compute the Lee–Wick quintom bounce (Cai, Qiu, Piao, Li, Zhang
arXiv:0704.1090) contraction-phase f_NL. If the squeezed amplitude is
universal for ε=3/2 contraction regardless of field content, that is a
genuinely model-agnostic bounce prediction and directly serves the vision.
**Positive-discovery shape:** a universality statement with a proof, or a
discriminating exception.

### 4.3 PTA free-spectrum test of the matter-contraction induced-GW slope (2–3 weeks, data on disk)

**Why:** Papanikolaou arXiv:2504.11641 predicts γ=3 (f² IR scaling) for the
matter bounce; NANOGrav 15-yr gives γ≈3.2±0.6; EPTA DR2 and (soon) IPTA DR3
are public. The old P3 did this once with unreproduced numbers.
**What:** fit the released NANOGrav 15-yr + EPTA DR2 free-spectrum posteriors
with (i) SMBHB γ=13/3 with astrophysical-prior width, (ii) matter-contraction
γ=3 with amplitude free, (iii) a broken power law; report Bayes factors with
proper priors. Keep it honest: NANOGrav's own analysis finds SMBHB
consistent, so the deliverable is "PTA data cannot yet distinguish; here is
the IPTA DR3 sensitivity needed," unless the data actually prefer γ=3.
**Positive-discovery shape:** either a preference or a concrete forecast for
when the discrimination becomes decisive.

### 4.4 PBH-abundance consistency with the lab's own f_NL (1–2 weeks, analytic + numerics)

**Why:** Choudhury et al. arXiv:2409.18983 used −35/8; the lab claims the
right number is −35/16. Redo their compaction-function PBH abundance with
−35/16 and the P2 shape. If the "PBH overproduction is cured by matter-bounce
NG" statement survives at half the amplitude, that is a second, independent
channel where the bounce number does work inflation must fine-tune for.
**Positive-discovery shape:** a predicted f_PBH window tied to the same
number SPHEREx measures — a cross-channel consistency test.

### 4.5 Replace image-handedness with a parity-odd observable, or drop parity (decision, 1 week)

**Why:** minimal ECH gives GR in the scalar sector (P1A) and image handedness
is parity-even (P4). If the lab wants a parity test of *any* bounce, the
existing observable is the LSS parity-odd 4PCF (Philcox arXiv:2206.04227;
Hou–Slepian–Cahn arXiv:2206.03625; Krolewski–May–Smith arXiv:2407.03397 find
no evidence in BOSS; Slepian–Krolewski–Greco arXiv:2508.09133 on DESI Y1
LRGs). **Theory task first:** does any bounce model produce a parity-odd
scalar trispectrum at tree level? If no model does (my expectation for
single-field bounces), close the parity line entirely and say so on the site.
If one does, that is a sharp, new prediction to test against the DESI LRG
4PCF.

### 4.6 Anomaly catalogue: run the discovery gate before writing anything (4–6 weeks)

Cross-match the 3,810 S≥8 slice against SIMBAD/NED/DESI VACs, rebuild the
taxonomy, and put ≥5 candidates through independent redshift/photometry
validation. The decision rule is in §1.9. This is not on the bounce vision;
it is a separate product line and should be labelled as one.

---

## 5. Immediate housekeeping (non-research, one session)

- Move `arxiv/main.tex` and `arxiv/paper1_unified.tex` under `arxiv/_retired/`
  with a README; grep-and-fix every remaining `-35/8` outside a "superseded"
  context (strategy doc, site copy, figures).
- Freeze P1C, MCMC companion, P5, current P3 at their Zenodo versions; remove
  them from the active review queue and the readiness dashboard.
- Rewrite the site's lead to: one flagship (P2′), one open-experiments list
  (§4), one data-products section (P4, anomaly), one "closed lines" section
  (ECH note). Retire the per-paper readiness grid from the front page.
- Commission the independent −35/16 check (a human theorist; not another
  LLM board).
