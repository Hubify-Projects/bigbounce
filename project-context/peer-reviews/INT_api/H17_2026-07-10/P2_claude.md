I now have what I need. I verified the core algebra by hand (script execution is gated in this session, but I read every relevant script and re-derived the sums symbolically). Key findings below, with the exact arithmetic I performed.

---

## REFEREE REPORT — P2 (`02_full_draft.tex`)

### (1) VERDICT: **MAJOR REVISIONS**

The headline value $\fnl=-35/16$ is genuinely well-supported (I independently re-derived it two ways). But Appendix A's *error-mechanism* narrative — presented as a "certified, cross-checked three ways" resolution of the Cai–Li factor of two — contains an internal inconsistency, and several provenance/reproducibility claims do not match the committed artifacts they cite. For a paper that explicitly stakes its credibility on auditability ("every quantitative result verified against committed computational artifacts"), these must be fixed before publication.

### (2) ISSUES

**[MAJOR] — Appendix A, Eq. (spurious) `\label{eq:spurious}` (line 1414) and the "inflates it to $-35/8$" claim (lines 1414, 1479, 1494).** The paper states $A_T^{\rm printed}-\sum(\text{vertices})=+\tfrac{99}{128}\sum_i k_i^3$ and repeatedly calls this the "spurious term" that "inflates" Cai's polynomial to $-35/8$. This does not hold arithmetically:
- I evaluated Cai's printed-coefficient polynomial $A_T$ exactly as coded in the certification script `scripts/caili_certification/cai_vertices.py:31` (coeffs $(3,1,-9,5,-66,9)\times\tfrac{3}{256}$). Its squeezed limit is $\fnl(A_T)=-305/64=-4.766$, **not** $-35/8=-4.375$. So the committed $A_T$ reproduces *neither* Cai's stated $-35/8$ *nor* $-35/16$.
- The difference I get is $A_T-\sum\text{vert}=-\tfrac{99}{128}\sum k^3$ (uniform $\fnl$ shift of $-2.578$ at both squeezed and equilateral), i.e. the **opposite sign** to Eq. (spurious).
- More fundamentally, a *single local* $\pm\tfrac{99}{128}\sum k^3$ term shifts $\fnl$ by a config-independent $\mp 2.578$; it **cannot** double $-35/16\to-35/8$ (which needs a shift of exactly $-2.1875$, not $2.578$, and of multiplicative "doubling" character). The paper half-concedes this ("the WRONG sign to reach $-35/8$"; "we do not claim a complete term-by-term derivation," line 1417) yet still presents Eq. (spurious) as a definite certified equation and says the term "inflates it to $-35/8$." Verified against: `cai_vertices.py:31-32` (the script that computes exactly this quantity — please run it and print `A_total - A_T`) and my hand expansion of $A_T$ to $O(k_1^2 k^7)$.

**[MAJOR] — Table VII `tab:vertexwalk` provenance (lines 1442, 1445).** The caption states each per-vertex value is "transcribed verbatim from the committed exact-fraction SymPy certification (`scripts/p2_vertex_check.py`)." The committed `p2_vertex_check.py` computes only the **total** $A=v_1+v_2+v_3+v_4$ and prints the total squeezed/equilateral $\fnl$ (lines 60–70) — it never isolates or prints the four per-vertex contributions. Neither does `cai_vertices.py`. So the four-row table cannot be reproduced from the cited script. (The *values* are correct — I verified all eight by hand: squeezed $-\tfrac{25}{16},-\tfrac{5}{32},0,-\tfrac{15}{32}$ sum to $-35/16$; equilateral $-\tfrac{35}{32},-\tfrac{5}{32},-\tfrac{5}{8},-\tfrac{15}{128}$ sum to $-255/128$, using the six-permutation convention — so this is a provenance/reproducibility defect, not a math error. Fix by adding the per-vertex loop to the script, or by re-attributing to whichever script actually emits them.)

**[MINOR] — Stale, contradictory committed artifact `scripts/fig_4vertex_sum.py`.** This released script still encodes the *superseded* $-35/8$ with an entirely different per-vertex breakdown (V1 $+21/8$, V2 $-45/8$, V3 $-27/8$, V4 $+16/8$, field-redef $0$; docstring lines ~50–70) and asserts it is "validated against Li & Brandenberger (2014)." It contradicts Table VII and the paper's central claim. It is not `\includegraphics`'d into the PDF (checked: only fig1/fig2/fig3/fig5/bphi/fig4 appear), so it doesn't corrupt a figure — but a referee auditing `scripts/` per the Data/Code Availability statement will find code that computes the value the paper says is wrong. Remove or clearly mark as deprecated.

**[MINOR] — Convention-dependence of the certified value is under-disclosed.** `p2_vertex_check.py` runs *two* interpretations of the triple sums ("6-perms" and "distinct-monomial"). Only the six-permutation branch yields $-35/16 / -255/128$; the distinct-monomial branch gives a different equilateral value (I get $-65/32$ vs $-255/128$). The whole result hinges on reading Cai's $\Sigma$ notation as ordered permutations. The `tab:vertices` caption does declare "six ordered pairs / six all-distinct triples," which is defensible, but the paper should state explicitly that the alternative reading is inconsistent and why the ordered convention is the correct transcription of arXiv:0903.0631, since the committed script leaves both in.

**[MINOR — UNVERIFIABLE IN THIS REVIEW] — Independent-Fisher $\sigma$ values (Sec. IV, line 1027) and $\sigma_{\rm RSD}=0.449$.** The claimed $\sigma(\fnl^{\rm local})=0.63$–$0.69$ (real space) and $0.42$–$0.45$ (redshift space, i.e. the $0.415/0.449$ committed numbers) could not be verified against `c13_independent_bounce_fisher.py` / `c14_rsd_multipole_fisher.py` because script execution is gated in this session (and a sub-agent hit the same gate). I confirmed only that the numbers are **internally arithmetic-consistent**: $2.1875/0.45=4.86$, $/0.42=5.21$ ($\to$ "$4.9$–$5.2\sigma$" ✓); $0.63/0.7=0.90$, $0.69/0.7=0.986$ ($\to$ validation ratio "$0.89$–$0.98$" ✓); real-space $2.1875/0.69$–$0.63=3.17$–$3.47\sigma$ ✓. A referee (and the authors) should re-run c13/c14 and confirm they emit these exact values.

**[MINOR] — Verified-correct arithmetic (no action, recorded for completeness).** I checked and confirm: SPHEREx quadrature floor $2.1875\times0.84/\sqrt{0.7^2+1.0^2}=1.505\sigma$ ✓; noise-weighted $/0.7=2.63\sigma$ ✓; optimistic $r{=}0.876\Rightarrow2.74\sigma$ ✓; Li Eq. (5.1) at $c_s{=}1$: $-165/16+65/8=-35/16$ ✓; Bayes-factor self-consistency $30/(\sqrt{2\pi}\cdot0.7)=17.07$ ✓.

### (3) Central claim
The central *scientific* claim — that the matter bounce predicts a kinematically fixed $\fnl=-35/16$ testable at modest ($\sim$1.3–2.75σ SPHEREx) significance and distinguishable in sign/magnitude from inflation — **is supported**: the $-35/16$ value survives two independent derivations (vertex re-summation, which I reproduced by hand, and Li's independent $c_s$ formula), and the forecast is honestly framed as a recast with disclosed systematics; however, the paper's stronger secondary claim to have *certified the precise mechanism of Cai's arithmetic error* (the $+99/128\sum k^3$ "spurious term") does not hold as written and should be corrected or withdrawn.

---

**Best Next Steps**
1. Run `cai_vertices.py` and print `A_total - A_T`; reconcile the sign of Eq. (spurious) and rewrite the "inflates to $-35/8$" narrative to match what the committed $A_T$ actually yields ($-305/64$).
2. Add an explicit per-vertex loop to `p2_vertex_check.py` so Table VII is reproducible from the cited script, or fix the attribution.
3. Delete/deprecate `fig_4vertex_sum.py` (stale $-35/8$).
4. Re-run `c13`/`c14` and paste the raw $\sigma$ outputs into the artifact JSONs so $0.42/0.45/0.63/0.69$ are third-party-verifiable.

Say `continue` and I will take the next best scoped step.
