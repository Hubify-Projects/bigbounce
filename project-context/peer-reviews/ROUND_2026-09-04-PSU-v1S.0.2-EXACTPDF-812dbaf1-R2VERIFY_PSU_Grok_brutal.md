# PSU ROUND_2026-09-04-PSU-v1S.0.2-EXACTPDF-812dbaf1-R2VERIFY — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `arxiv/paper_su_criterion/main.pdf` sha256=812dbaf1af7e8eafa5769730fed55c81cfa8b429fbeab022d1125be1527aca31 pages=4
**Review packet(s)**: `6d4b976e59cb7f187f428cfca2fb0b6bd9df8c6ec08ed1656a4fc9ecb2e07887, 30e69b8b918ba26bfbc42ce471aee0e8dc1e5b3f2a0665da98b6cf4bfeddb5db`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 self-critique (1691 chars)
**Wall time**: 142.2s

---

**Referee Report**

**Paper:** "The separate universe computes a different variable: an exact criterion for \(\delta N = \zeta\) in non-attractor phases" (Houston Golden)

**Venue target:** PRD Letter (high bar: must contain a self-contained, novel, high-impact result with rigorous derivations and no reliance on external unpublished companions).

**Findings (adversarial audit)**

**PSU-E1 (ESSENTIAL)**  
Section: Abstract (p. 1) + Sec. III (p. 2)  
Problem: Abstract states the identification "\(\delta N_c = \zeta\) at linear order iff \(I \to 0\)" and claims an "exact, invertible change of variable" with the specific form \(\delta N_c = \zeta_{L,f}[1-I/3] + O(k_L^2/a^2 H^2)\). The body derives this only after dropping the gradient term and assuming a flat super-Hubble initial slice plus constant \(\epsilon, c_s=1\). No standalone derivation of the ADM constraints or the integration that produces Eq. (2) is supplied.  
Required fix: Provide the full derivation of Eq. (2) from the exact identity Eq. (1) without citing companion notes; otherwise the central claim is not verifiable from the submitted manuscript.

**PSU-E2 (ESSENTIAL)**  
Section: Abstract + Sec. I (p. 1) + Reproducibility Statement (p. 3)  
Problem: Abstract and introduction repeatedly invoke "a second companion note" and "the committed script" (SHA-256 hashes, github commits dated 2026) for the second-order map, the in-in monopole adjudication, and the four validations. The letter is not standalone.  
Required fix: All load-bearing algebra and numerical checks must appear inside the four-page limit or the submission must be withdrawn.

**PSU-E3 (ESSENTIAL)**  
Section: Abstract (p. 1)  
Problem: Abstract asserts "reproduces the in-in monopole exactly, \(-5\)", for every constant \(\epsilon\). The body (Eq. 3) obtains this only for the initial-position label and only after imposing the specific ADM solution for constant \(\epsilon, c_s=1\). The final-position label yields a different monopole (Eq. 4). The abstract statement is therefore stronger than the calibrated body result.  
Required fix: Rewrite the abstract to match the final, label-dependent statement in Sec. III.

**PSU-M1 (MAJOR)**  
Section: Sec. II (p. 2) + Fig. 1  
Problem: Fig. 1 and Eq. (5) present a linear rescaling \(\lambda(w) = (1-w)/2\) and a label-independent monopole \(f_{\rm map}^{\rm mono} = -\frac{5}{8}(1+w)\). These are elementary algebraic functions of \(w\); the figure adds no new information beyond the algebra already written in the caption.  
Required fix: Remove the figure or replace it with a non-trivial numerical test that cannot be read off the equations.

**PSU-M2 (MAJOR)**  
Section: Sec. IV (p. 3) + Table I  
Problem: The four "validations" are analytic limits already known in the cited literature (dust, USR, attractor, ekpyrosis). No new observable prediction or quantitative discrepancy resolution with data is provided.  
Required fix: Demonstrate that the new criterion changes a published observable at a level detectable by current or near-future surveys, or reclassify the manuscript as a comment rather than a Letter.

**PSU-N1 (MINOR)**  
Section: Reproducibility Statement + AI Usage Disclosure (p. 3)  
Problem: These sections contain commit hashes, github URLs, and an explicit AI disclosure paragraph. Neither belongs in a PRD Letter.  
Required fix: Delete both sections.

**PSU-N2 (MINOR)**  
Section: Header (p. 1)  
Problem: The string "v1S.0.2" appears in the running head.  
Required fix: Remove all version-control tags from the submitted PDF.

**Summary recommendation**  
REJECT

The manuscript is a narrow clarification that \(\delta N_c\) and \(\zeta\) differ by a controlled factor \(I\) whose vanishing restores agreement. The central algebraic identity is not derived from first principles inside the letter, the result is not standalone, the abstract overstates the domain of validity, and the "validations" are re-derivations of known limits. These deficiencies place the work well below the threshold for a PRD Letter.

---

## PASS 2 — self-critique findings (what initial review missed)

**PSU-E4 (ESSENTIAL)**  
Section: Eq. (3) + text after Eq. (3) + Table I (dust row)  
Problem: The claim that \(f_{\delta N}^{\rm init} \equiv f^{\rm in-in}/\lambda + f_{\rm map}^{\rm init} = -5\) (isotropic, every constant \(\epsilon\)) is false. Substituting the explicit expressions for \(\epsilon=3/2\) (\(\lambda=1/2\), \(f^{\rm in-in}_{\rm mono}=-15/8\)) yields \(-3.75-0.625=-4.375\), not \(-5\). The same mismatch appears for general \(\epsilon\) when the algebraic forms in (3) are inserted.  
Required fix: Either correct the algebra or retract the “exactly \(-5\) for every constant \(\epsilon\)” statement.

**PSU-M3 (MAJOR)**  
Section: Eq. (2) + surrounding text  
Problem: The displayed formula for \(\delta N_c\) is stated to be “exact on super-Hubble scales for any single-field history,” yet the derivation explicitly drops the \(\nabla^2\) term and assumes constant \(\epsilon\), \(c_s=1\), and a flat initial slice. No error estimate or domain-of-validity qualifier accompanies the displayed equation.  
Required fix: Add the precise conditions under which the displayed expression holds, or qualify it as an approximation.

**PSU-N3 (MINOR)**  
Section: Abstract (final sentence)  
Problem: “There is no discrepancy in the physics, only in which variable \(\delta N_c\) is compared to” is an interpretive claim, not a result demonstrated inside the letter; the body never performs a side-by-side observable-level comparison that would substantiate the phrasing.  
Required fix: Remove or rephrase to a statement supported by the derivations shown.

NO ADDITIONAL FINDINGS on classes B, C, E–J; the new issues above are the only ones that survive a line-by-line re-audit.