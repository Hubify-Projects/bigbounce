# Referee report — P1A v1A.0.116

Paper: *Algebraic Torsion in Minimal Einstein–Cartan–Holst Gravity: Four-Fermion Contact Bounds and Classical Scalar-Sector Transparency*  
Commit declared by author: `91ad88e36121da128175415f55be44d5e458f9f1`

I reviewed all six rendered pages and the active portions of the exact TeX source. I independently checked the action/contact coefficient, density conversion, Fierz matrix, NJL threshold and ratios, classical transparency proof, citations, scope statements, reproducibility links, and visual presentation.

## Overall assessment

Two parts are basically correct:

1. For the cited minimal-fermion convention, integrating out torsion gives
   \[
   \mathcal L_{4\psi}
   =-\frac{3\kappa}{16}\frac{\gamma^2}{1+\gamma^2}J_5^I J_{5I}.
   \]
   This agrees with the minimal-coupling limit of Freidel–Minic–Takeuchi, whose effective interaction is \(-\frac32\pi G\,\gamma^2/(1+\gamma^2)A^2\), since \(\kappa=8\pi G\). The same source confirms that minimal coupling produces only the axial–axial term, while vector–axial parity violation requires nonminimal coupling. [Freidel, Minic, and Takeuchi](https://arxiv.org/abs/hep-th/0507253)

2. The canonical-scalar transparency argument is correct for an invertible tetrad, real nonsingular constant Immirzi parameter, classical minimal matter, and ordinary boundary conditions: the scalar has no spin current, the algebraic connection equation gives \(T=0\), and
   \[
   \epsilon^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma}=0
   \]
   follows pointwise from the torsion-free algebraic Bianchi identity.

However, the advertised NJL magnitude result is not correct under the paper’s own Planck-mass and cutoff conventions. The normalization error is large enough to turn the reported maximum from subcritical to supercritical in the magnitude-only test. The manuscript also does not disclose the scan parameters necessary to reproduce the reported maximum, and “single species” does not describe the parameters that generate \(0.156\).

## Independent recomputations

### Contact coefficient and finite-density estimate

The contact coefficient in Eqs. (3)–(5) is correct within the cited convention. The natural-unit conversion is also correct:

\[
1\ {\rm cm}^{-3}=(1.973\times10^{-5}\ {\rm eV})^3
=7.68\times10^{-15}\ {\rm eV}^3,
\]

so \(100\ {\rm cm}^{-3}=7.68\times10^{-13}\ {\rm eV}^3\). Using the paper’s unreduced Planck mass \(M_P=1.22\times10^{28}\) eV,

\[
\frac{n^2}{M_P^2}=3.96\times10^{-81}\ {\rm eV}^4,
\qquad
\frac{n^2/M_P^2}{(2.3\ {\rm meV})^4}
=1.42\times10^{-70}.
\]

Restoring the actual Einstein–Cartan coefficient,
\[
\frac{3\kappa}{16}=\frac{3\pi}{2M_P^2},
\]
changes this to \(6.67\times10^{-70}\rho_\Lambda\), still approximately 69–70 orders below \(\rho_\Lambda\). Thus the qualitative late-density conclusion survives.

### Fierz rearrangement

The displayed matrix satisfies \(F^2=1\). Its axial column gives

\[
AA\rightarrow \frac14 SS+\frac12 VV-\frac12AA-\frac14PP.
\]

Consequently, with the manuscript’s contact sign,

\[
G_{\rm scalar}
=-\frac{3\kappa}{16}\frac14
=-\frac{3\kappa}{64}.
\]

That algebra is correct as a declared exchange-channel/Fierz convention. The manuscript appropriately acknowledges that this does not eliminate mean-field Fierz ambiguity.

### NJL gap equation

For the normalization explicitly stated in Appendix B,
\[
\mathcal L_{\rm int}=G_s(\bar\psi\psi)^2,
\]
one finds
\[
M=-2G_s\langle\bar\psi\psi\rangle,
\qquad
\langle\bar\psi\psi\rangle
=-4N_fN_cM
\int^\Lambda\frac{d^4p_E}{(2\pi)^4}\frac1{p_E^2+M^2}.
\]

Since
\[
\int^\Lambda\frac{d^4p_E}{(2\pi)^4}\frac1{p_E^2+M^2}
=
\frac1{16\pi^2}
\left[
\Lambda^2-M^2\ln\left(1+\frac{\Lambda^2}{M^2}\right)
\right],
\]
the gap equation is
\[
M=
\frac{G_sN_fN_cM}{2\pi^2}
\left[
\Lambda^2-M^2\ln\left(1+\frac{\Lambda^2}{M^2}\right)
\right],
\]
and therefore
\[
G_{\rm crit}=\frac{2\pi^2}{N_fN_c\Lambda^2}.
\]

The manuscript’s equation is larger by a factor two and its \(G_{\rm crit}\) is smaller by a factor two.

## Findings

### P1A-E01 — ESSENTIAL

**Type:** Real technical defect.

The manuscript uses mutually incompatible Planck conventions. It defines \(\kappa=8\pi G\) in Sec. II but later writes \(\kappa=1/M_{\rm Pl}^2\), while explicitly taking \(M_{\rm Pl}=1.22\times10^{19}\) GeV, the unreduced mass. See [Sec. II, lines 1624–1649](</Users/houstongolden/Desktop/CODE_YOU/bigbounce/project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1-EXACTPDF-91ad88e3-NONANTHROPIC/P1A/frozen/arxiv/paper1a_ech_nogo.tex:1624>) and [Sec. III, lines 2466–2481](</Users/houstongolden/Desktop/CODE_YOU/bigbounce/project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1-EXACTPDF-91ad88e3-NONANTHROPIC/P1A/frozen/arxiv/paper1a_ech_nogo.tex:2466>).

The correct identities are
\[
M_P=G^{-1/2},\qquad
\bar M_P=(8\pi G)^{-1/2},\qquad
\kappa=\bar M_P^{-2}=\frac{8\pi}{M_P^2}.
\]

Using the manuscript’s own critical-coupling formula, restoring \(8\pi\) changes
\[
0.156\rightarrow 3.92,\qquad
0.31\rightarrow 7.84.
\]

Using instead the correctly normalized gap equation derived above changes the combined result to
\[
R_s=
\frac{3N_fN_c}{16\pi}\frac{\Lambda^2}{M_P^2}.
\]
For the parameters underlying the reported maximum, this gives
\[
R_s\simeq1.96,\qquad R_A\simeq3.92.
\]

Thus the abstract and body statements that the magnitude “remains subcritical” are false under the stated maximal-Einstein–Cartan scan. The negative scalar sign still prevents the particular standard scalar condensate, but the claimed independent magnitude closure does not survive.

### P1A-M01 — MAJOR

**Type:** Real technical defect.

The Appendix-B gap equation and threshold have a factor-of-two error for the explicitly declared interaction \(G_s(\bar\psi\psi)^2\). See [lines 4579–4597](</Users/houstongolden/Desktop/CODE_YOU/bigbounce/project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1-EXACTPDF-91ad88e3-NONANTHROPIC/P1A/frozen/arxiv/paper1a_ech_nogo.tex:4579>).

The correct threshold is
\[
G_{\rm crit}=\frac{2\pi^2}{N_fN_c\Lambda^2},
\]
not \(\pi^2/(N_fN_c\Lambda^2)\), unless the four-fermion interaction is redefined with an additional factor of two. No such alternative normalization is stated.

This error partly counteracts P1A-E01 numerically, but does not rescue the magnitude claim: the corrected worst-case scalar ratio remains approximately \(1.96\).

### P1A-M02 — MAJOR

**Type:** Real technical/reproducibility defect.

The active paper never states the \(N_f,N_c,\gamma\) values used in the “declared cutoff/flavor scan,” despite reporting maxima to three significant digits. See the [abstract, lines 1086–1090](</Users/houstongolden/Desktop/CODE_YOU/bigbounce/project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1-EXACTPDF-91ad88e3-NONANTHROPIC/P1A/frozen/arxiv/paper1a_ech_nogo.tex:1086>) and [Appendix B, lines 4598–4604](</Users/houstongolden/Desktop/CODE_YOU/bigbounce/project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1-EXACTPDF-91ad88e3-NONANTHROPIC/P1A/frozen/arxiv/paper1a_ech_nogo.tex:4598>).

From the displayed formula,
\[
0.156=
\frac{3N_fN_c}{64\pi^2}\frac{\Lambda^2}{M_P^2},
\]
the reported maximum implies
\[
N_fN_c\frac{\Lambda^2}{M_P^2}=32.85.
\]
With the linked script’s \(\gamma=0.274\) and \(\Lambda=M_P/\sqrt\gamma\), this is \(N_fN_c=9\), i.e. its QCD-like \(N_f=3,N_c=3\) case—not “single species.” The [linked mutable script](https://raw.githubusercontent.com/Hubify-Projects/bigbounce/main/arxiv/scripts/njl_gap_equation_route1.py) confirms that it scans \(N_fN_c=1,3,9\).

The paper must either define “single species” in a nonstandard way, report the actual scan table, or remove that description. As written, the headline number cannot be reproduced from the manuscript.

### P1A-M03 — MAJOR

**Type:** Venue/referee opinion, not a technical defect.

Even after correcting the NJL calculation, the manuscript contains limited original physics suitable for PRD:

- The minimal Holst–Dirac contact coefficient is a cited standard result.
- The late-density estimate is straightforward dimensional scaling.
- The scalar transparency result follows immediately from zero scalar spin current plus the torsion-free Bianchi identity.
- The manuscript itself correctly says that its novelty is not a new curvature identity.
- The potentially new quantitative component—the NJL magnitude scan—is presently incorrect and internally underspecified.

The scope is appropriate to gravitation, but the level of novelty and technical development does not, in my judgment, justify publication as a PRD research article. A concise pedagogical note could be defensible after correction, but that is a venue judgment.

### P1A-M04 — MAJOR

**Type:** Real overclaim, but removable without affecting the density bound.

Section III A argues that \(\langle J_5\rangle=0\) implies absence of a coherent \(w=-1\) component, while acknowledging that \(\langle J_5J_5\rangle\neq0\). See [lines 2487–2497](</Users/houstongolden/Desktop/CODE_YOU/bigbounce/project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1-EXACTPDF-91ad88e3-NONANTHROPIC/P1A/frozen/arxiv/paper1a_ech_nogo.tex:2487>).

A vanishing one-point current does not determine the stress tensor or equation of state of a Lorentz-scalar composite expectation value. Establishing \(w\neq-1\) requires an explicit state-dependent stress-tensor calculation. The finite-density amplitude suppression is sufficient for the paper’s narrow conclusion; the claimed independent equation-of-state “leg” should be removed or derived.

### P1A-m05 — MINOR

**Type:** Real presentation/self-containment defect.

The paper says it “performs” algebraic torsion elimination, but the active text only writes a symbolic \(S_D\) and asserts the result. It never states the Dirac-action normalization, signature, \(\epsilon^{0123}\), \(\gamma^5\), contorsion solution, or substitution step. See [lines 1622–1650](</Users/houstongolden/Desktop/CODE_YOU/bigbounce/project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1-EXACTPDF-91ad88e3-NONANTHROPIC/P1A/frozen/arxiv/paper1a_ech_nogo.tex:1622>).

The result agrees with the cited literature, so this is not a sign/coefficient objection. Nevertheless, conventions are central to the later Fierz-sign claim, and a short explicit derivation is warranted.

### P1A-m06 — MINOR

**Type:** Real technical overstatement.

The equality
\[
v_R(k,\eta)=v_L(k,\eta)
\]
on page 4 does not follow from parity-identical equations. Equal equations imply equal dispersion relations and transfer functions; different or chiral initial conditions can still give \(v_R\neq v_L\). See [lines 3721–3727](</Users/houstongolden/Desktop/CODE_YOU/bigbounce/project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1-EXACTPDF-91ad88e3-NONANTHROPIC/P1A/frozen/arxiv/paper1a_ech_nogo.tex:3721>).

The correct statement is that minimal ECH generates no helicity-dependent propagation or chirality from parity-symmetric initial data.

### P1A-m07 — MINOR

**Type:** Missing hypotheses on an otherwise correct result.

The transparency theorem should state:

- invertible tetrad;
- real constant \(\gamma\), excluding singular complex self-dual values;
- invertibility of the Holst connection operator;
- ordinary boundary conditions or no nontrivial global boundary contribution.

The manuscript discusses quantum, nonminimal, propagating-torsion, and global limitations well, but these elementary local hypotheses should appear in the formal statement at [lines 3646–3669](</Users/houstongolden/Desktop/CODE_YOU/bigbounce/project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1-EXACTPDF-91ad88e3-NONANTHROPIC/P1A/frozen/arxiv/paper1a_ech_nogo.tex:3646>).

### P1A-m08 — MINOR

**Type:** Real reproducibility defect.

The artifact macro links to mutable `main`, not commit `91ad88e…`, and renders both scripts merely as “repository artifact.” See [macro line 51](</Users/houstongolden/Desktop/CODE_YOU/bigbounce/project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1-EXACTPDF-91ad88e3-NONANTHROPIC/P1A/frozen/arxiv/paper1a_ech_nogo.tex:51>) and [Data and Code Availability, lines 3840–3848](</Users/houstongolden/Desktop/CODE_YOU/bigbounce/project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1-EXACTPDF-91ad88e3-NONANTHROPIC/P1A/frozen/arxiv/paper1a_ech_nogo.tex:3840>).

The exact frozen review bundle contains only the TeX and PDF, not the scripts or result JSON. The links should be commit-pinned, show filenames, and archive the parameter/result table.

### P1A-m09 — MINOR

**Type:** Real wording defect; qualitative conclusion unaffected.

\(100\ {\rm cm}^{-3}\) is not an upper bound on astrophysical baryon/electron densities; molecular clouds and compact objects exceed it substantially. See [lines 2471–2478](</Users/houstongolden/Desktop/CODE_YOU/bigbounce/project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1-EXACTPDF-91ad88e3-NONANTHROPIC/P1A/frozen/arxiv/paper1a_ech_nogo.tex:2471>).

It is a deliberately elevated benchmark relative to the homogeneous cosmic mean, which is all the dark-energy comparison needs. “Conservative homogeneous-density benchmark” would be accurate.

### P1A-n10 — NIT

**Type:** Presentation ambiguity.

Step 5 of the scalar proof says a total derivative contributes no equations of motion and then discusses nonzero torsion. At nonzero torsion the Holst density also contains \(T^I\wedge T_I\), which is not a boundary term. The subsequent text understands this correctly, but Step 5 is unnecessary and potentially misleading. See [lines 3700–3705](</Users/houstongolden/Desktop/CODE_YOU/bigbounce/project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1-EXACTPDF-91ad88e3-NONANTHROPIC/P1A/frozen/arxiv/paper1a_ech_nogo.tex:3700>).

### P1A-n11 — NIT

**Type:** Bibliographic/presentation issue.

Reference [6] says the companion is “posted concurrently on arXiv” but supplies no arXiv identifier. Because the manuscript explicitly declares the companion non-load-bearing, this is not a technical problem, but it should be completed or described as an accompanying submission.

### P1A-n12 — NIT

**Type:** Venue/presentation opinion.

The six pages are visually clean: no clipping, overlap, malformed equations, missing figures, or broken tables were observed. Fonts are embedded, and the page-4 wide equation is contained correctly. There are no figures or tables to audit. Minor presentation issues are:

- a full hyperlinked table of contents is unusual and space-inefficient for a six-page PRD article;
- both code links render with the identical label “repository artifact”;
- reference [6] splits awkwardly across the page-6 columns.

None is a publication blocker.

## Scope and citation adjudication

I did **not** treat the following as defects:

- missing R2/R3 cosmological matching;
- absence of an ECH dark-energy or birefringence prediction;
- lack of gravitational-EFT operator completeness;
- absence of beyond-mean-field closure;
- quantum-loop, anomaly, dynamical-Immirzi, propagating-torsion, or nonminimal-matter analyses.

These are prominently disclosed limitations and are genuinely outside the declared paper. Promoting them to blockers would misread the current six-page manuscript.

The running-calculation discussion is accurate. Shapiro and Teixeira explicitly report that the coupled running system is difficult to solve satisfactorily and find no fixed points for the full finite-\(\gamma\) system. [Shapiro and Teixeira](https://arxiv.org/abs/1402.4854) Benedetti and Speziale derive scheme-dependent Immirzi running, including a fermion-sourced beta function in Euclidean signature and its perturbative limitations. [Benedetti and Speziale](https://arxiv.org/abs/1111.0884)

No stale long-form dark-energy claim from the commented historical source was promoted into a finding against the active PDF.

## Summary recommendation

REJECT

The classical transparency result and late-density suppression are correct within their narrow domains, but the central advertised NJL magnitude result contains incompatible Planck-mass conventions and an incorrect gap-equation normalization. Correcting both turns the reported worst-case scalar magnitude ratio from \(0.156\) to approximately \(1.96\), contradicting the abstract. The scan is also not reproducible from the active manuscript and its maximum is inconsistent with the description “single species.” Finally, after those corrections, the remaining correct results are largely direct applications of established identities and standard cited calculations, which in my judgment do not provide sufficient novelty for PRD.

Genuinely new blockers only:

- **P1A-E01:** missing \(8\pi\) from the unreduced Planck-mass convention overturns the subcriticality claim.
- **P1A-M01:** the stated NJL gap equation and \(G_{\rm crit}\) are wrong by a factor of two for the declared interaction normalization.
- **P1A-M02:** the headline scan maximum depends on undisclosed \(N_f,N_c,\gamma\) inputs and is inconsistent with “single species.”
- **P1A-M03:** after correction, the surviving contribution does not, in this referee’s judgment, meet PRD’s originality threshold.