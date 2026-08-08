# INT Claude-subscription Review — P1U v1U.0.11 — claude-opus-4-8
paper: P1U  version: v1U.0.11  tex: arxiv/paper1_unified.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-11T02:31:03Z
context-note: Wave-1 stability re-test at current version; no changes since last review

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I now have a complete, verified assessment. The body math is internally consistent and correct (footnote L1809-1811, O4/O5 reduction L1957, and Check D L4884 all now agree on $-\tfrac38(J^5\!\cdot\!J^5)$ with Lorentzian $\varepsilon\varepsilon=-3!\delta$). But the v1U.0.11 "Check D" fix was propagated only through the .tex body, not the cited artifact or the abstract.

---

## Referee Report — *Channel-Level Constraints on Four Enumerated Minimal ECH Dark-Energy Routes* (v1U.0.11)

**(1) VERDICT: MINOR REVISIONS**

The central content is unchanged from the prior converged state and remains sound: the perturbation-transparency result rests on the algebraic Bianchi identity (correct), the single-scale NDA dimensional no-go is honestly scoped as a channel-level (not operator-level) statement, and the load-bearing numbers I could recompute are internally consistent (e-fold mapping $92-60=32$; $H_0=67.68\pm1.06$ consistent across all ~7 occurrences; $\fnl=-35/16=-2.1875$; birefringence $0.342/0.094=3.6\sigma$, $0.215/0.074=2.9\sigma$; MCMC $176{,}240+132{,}949=309{,}189$; $N_{\rm tot}\!\approx\!92$ vs $94$ 2% offset disclosed). The just-fixed torsion-square contraction is now mathematically correct in the body ($6/16=3/8$, and Lorentzian $\varepsilon_{abcd}\varepsilon^{abce}=-3!\delta$ is the right identity). The one real defect is that this same fix was **not** propagated to the artifact the paper cites as verifying it, nor to the abstract — a reproducibility/self-consistency problem, not a science error.

**(2) ISSUES**

1. **[MAJOR] The cited verification script contradicts the corrected Check D equation it is claimed to verify.** `paper1_unified.tex:4860-4885` states both identities are "verified symbolically in the released script `dim4_parityodd_enumeration.py`," and Check D (`:4883-4884`) gives $\varepsilon_{abcd}\varepsilon^{abce}=-3!\,\delta^e_d$ "(verified symbolically)" $\Rightarrow S_{abc}S^{abc}=-\tfrac38(J^5\!\cdot\!J^5)$. But the actual script `arxiv/scripts/dim4_parityodd_enumeration.py:163` asserts `expected = 6*sp.eye(d)` and prints (`:165-168`) `eps_{abcd} eps^{abce} = 3! delta^e_d` and `equals 6*I (=> S_abc S^abc = 6 (J5.J5))` — the exact pre-v1U.0.11 value (positive $3!$, no $1/16$, wrong by a factor $-16$ relative to the corrected Eq.). Worse, the docstring (`:151-153`, `:26-28`) explicitly states the Lorentzian sign is "immaterial to the collapse coefficient," so the script does **not** verify the signed $-3!\delta$ identity the body attributes to it; it verifies only the unsigned Euclidean magnitude $=6$. A referee re-running the cited artifact obtains output that directly contradicts Eq. at `:4884`/`:1810`/`:1957`. Fix: update `check_D()` to compute/assert the Lorentzian signed contraction and carry the $(1/4)^2$ normalization so its printed conclusion matches $-\tfrac38(J^5\!\cdot\!J^5)$, or soften the "verified symbolically" wording to "magnitude verified symbolically; Lorentzian sign fixed analytically in the footnote below Eq.(torsion)." This is the paper's own directive-G/I6 artifact-sync requirement applied to the last edit.

2. **[MINOR] Abstract states the same identity with the opposite (pre-fix) sign.** `paper1_unified.tex:1243` lists "the two load-bearing tensor identities verified symbolically — the $\varepsilon R=0$ Bianchi contraction and the $\varepsilon\varepsilon=3!\,\delta$ collapse," i.e. positive $3!\delta$, contradicting the body's emphasized Lorentzian $-3!\delta$ (footnote `:1811`, `:1957`, `:4883`). Make the abstract consistent (either state $-3!\delta$ or explicitly frame it as a magnitude).

3. **[MINOR] Reproducibility tree not resolvable from this submission checkout.** The abstract (`:1442-1447`) claims the frozen MCMC chains are "archived with this submission … can be inspected and re-derived *now*," but the cited `parameter_summary_CORRECTED.json` files backing the $309{,}189=176{,}240+132{,}949$ reconciliation (changelog `:177-185`) are not present in the `reproducibility/` tree in this checkout (only `README.md`). The arithmetic is correct and these numbers are explicitly non-load-bearing, but the "archived with this submission" claim should either be satisfied in the tarball or reworded to point at the actual (external/HF) archive location.

**(3)** Yes — the central claim (channel-level closure of the four enumerated minimal-ECH dark-energy routes, honestly scoped as assumption-conditional and *not* an operator-level theorem, plus the perturbation-transparency result) is supported by correct body derivations; the only required change is synchronizing the cited Check D artifact and the abstract with the already-correct v1U.0.11 body fix.

---

Note on the CONTEXT NOTE ("no changes since last review"): the body *is* stable and correct, but this re-test surfaced that the v1U.0.11 Check D correction was applied to the `.tex` only — the cited script (`dim4_parityodd_enumeration.py:163`) and the abstract (`:1243`) still carry the pre-fix identity. That's a genuinely-new internal inconsistency introduced by the last version's incomplete propagation, so under directive K this resets P1U's clean-wave count rather than confirming a clean wave. It's editable with no science change.
