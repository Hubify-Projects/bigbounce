I now have everything needed. I verified the load-bearing arithmetic by hand and by reading the committed script sources and JSON outputs (I could not *execute* the scripts — a Bash permission gate blocked it — so per your instructions I verified by source-reading + hand-arithmetic and say so explicitly). The committed `c9k`/`c9g` JSON outputs reconcile with the paper's Table III/tab:gr and tab:bayes values, and the citation-consistency items the changelog claims (Addis/Jolicoeur, Heinrich year) are genuinely consistent in numeric-citation style.

---

# Referee Report — P2: "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook" (v1.7.112)

## (1) VERDICT: **MINOR REVISIONS**

This is a re-test after the H17H presentation/disclosure closure round. I confirm that **all five requested closures were executed and are technically correct**: the abstract is now a single PRD-format paragraph with no displayed equations (L926); the proxy nature of the 1.3σ floor is explicitly disclosed in both the abstract and the new "Scope and conventions" paragraph (ρ=−0.868 transferred from the power-spectrum SDB channel, Cov_B not public, L926/L935/L1283); the Cai–Li "resolution" is reframed as "certify −35/16 four ways; the printed −35/8 is an unreproduced erroneous literature value" (L926/L976/L1509); assumption-(d) closure is softened to conditional-on-dressed-metric with the deformed-algebra signature-change window flagged (L1027/L1466); and the r/r_cos/r_eff/r_t/ρ notation is consolidated into one canonical clause (L935, cross-referenced from L1054).

The manuscript is **technically sound, contains no computational error I can find, fabricates nothing, and is exemplary in its honesty**. The central claim is fully supported. The residual items below are polish and one scope/impact judgment for the editor — none is a correctness defect. I recommend acceptance after minor revision.

## (2) ISSUES

**[MAJOR] M1 — Scientific weight of the observational forecast vs. its honest floor (abstract L926; §IV L1122; §VII L1283).**
The paper's deliverable observational result is a sensitivity *recast* of a single external forecast (Heinrich et al. σ(f_NL)≈0.7), and the abstract claims SPHEREx can test the prediction at "∼1.3–2.75σ." But the paper's own honest bracket for the conservative floor is **0.8–1.3σ** (L1283, tab:systematics final two rows): the in-repo |ρ|≈0.95 GR-projection shape overlap gives 0.8σ, and the adopted 1.3σ endpoint rests on the ρ=−0.868 *proxy* transferred from a different (power-spectrum) channel because the bispectrum Cov_B is not public. A strict reading is that at the conservative end SPHEREx has **essentially no power** to test −35/16, and the honest lower edge (0.8σ) is not carried into the abstract's headline range. This is not a defect of honesty — it is disclosed — but the abstract should either (a) state the floor as "∼0.8–2.75σ (conservative floor proxy-dependent)" or (b) explicitly note that the 1.3σ lower endpoint is the proxy-based value and the channel-native floor could be lower. As written, the abstract headline is marginally more optimistic than the body supports. The editor should also weigh whether a ≤2.75σ single-source recast, whose per-triangle covariance is unavailable, clears PRD's impact bar independent of the (solid, self-contained) amplitude-correction note of Appendix A.

**[MINOR] m1 — "Resolves the factor of two" framing slightly exceeds what is delivered (title/abstract L926; Conclusion L1480).**
Appendix A is scrupulously careful ("We do not claim a complete term-by-term reconstruction of Cai's published −35/8," L1509): the printed polynomial reduces to −305/64, *not* to Cai's stated −35/8, so the origin of Cai's published number is **not** reconstructed. What is established, four ways, is that the correct value is −35/16. "Resolved in favour of −35/16" is defensible (Li et al.'s independent general-c_s method plus the vertex re-sum both give −35/16), but the Conclusion's unqualified "resolves the historical Cai–Li factor-of-two" is marginally stronger than "establishes −35/16 as the correct amplitude; the origin of the printed −35/8 is not reconstructed." Recommend aligning the Conclusion/title phrasing with the appendix's own careful statement.

**[MINOR] m2 — Verbosity and repetition (throughout).**
The abstract closure is done, but the body still repeats each core caveat many times: the Cai–Li disclosure appears in ≥7 locations (abstract, intro L941, §II L976, assumptions L1027, appendix, caveats L1463, conclusion L1480); the r-vs-r_eff reconciliation appears three times (L935, L1054, L1118) with an explicit "referenced throughout" pointer. For a PRD paper this is fatiguing and works against the reader. The notation consolidation helped; a further pass consolidating the repeated Cai–Li and r/r_eff disclosures to one canonical statement each (with cross-refs elsewhere) would materially improve readability. Presentation only.

**[MINOR] m3 — Abstract length (L926).**
The single-paragraph abstract is ~250 words — at the upper practical limit for PRD. Trimming the parenthetical proxy-floor mechanics (keeping the disclosure, shortening the "Cov_B not public" clause) would bring it to a more standard length without losing load-bearing content.

**[MINOR] m4 — Stale comparison targets in helper certification scripts (scripts/caili_certification/cai_shape.py, cai_conv.py).**
These helper scripts hard-code the *pre-correction* −35/8 and −255/64 as `target_loc`/`target_eq`. This is intentional and correct — they exist to demonstrate the printed polynomial does *not* reduce to the correct value — but a code reviewer (or the JSON `c9i` reader, whose `target_full` shows −35/8 for "squeezed") can misread these as stale. Recommend a one-line comment in each helper making clear these are the *printed/reference* Cai targets, not the adopted amplitude. (The self-contained certification `scripts/p2_vertex_check.py` correctly targets −35/16 and is a faithful transcription of Table tab:vertices.)

**[MINOR] m5 — Bibkey/first-author cosmetic mismatches (verified non-defects).**
`Jolicoeur:2025` has first author Addis (bib L164–167), and the prose correctly names "Addis et al." (L1137, L1311); `Heinrich:2023` bibkey ≠ its 2024 year, and the prose "Heinrich et al. 2024" matches the year. Both are invisible in PRD's numeric citation style — **no change strictly required** — but renaming the bibkeys to first-author-year would remove a standing source of reviewer confusion.

## (3) Is the central claim supported?

**Yes.** The central claim — that the correct minimally-parameterized matter-bounce squeezed-limit local amplitude is f_NL = −35/16 (not the printed −35/8) — is **well-supported and independently verifiable**. I confirmed every load-bearing fraction by hand:

- Per-vertex squeezed sum −25/16 − 5/32 + 0 − 15/32 = **−35/16** ✓; equilateral −35/32 − 5/32 − 5/8 − 15/128 = **−255/128** ✓ (tab:vertexwalk).
- ε-order-grouped −5/2 + 5/16 + 0 = **−35/16** ✓ (Eq. order_grouped).
- Li Eq. 5.1 at c_s=1: −165/16 + 65/8 = **−35/16** ✓.
- Printed-polynomial squeezed reduction −35/16 − (10/3)(99/128) = **−305/64** ✓ (≠ Cai's −35/8, consistent with the paper's honest "not reproduced" statement).

The four independent certifications (vertex re-sum, Cai's own ε-order intermediates, three-configuration benchmark matching, and Li et al.'s independent general-c_s formula) are mutually consistent, and the `p2_vertex_check.py` source is a faithful, exact-fraction transcription of the four vertex expressions in Table tab:vertices. **I could not execute the scripts** (a Bash permission gate blocked execution in this session), so this verification rests on reading the committed script/JSON sources plus hand-arithmetic; the committed JSON outputs I could read (`c9k`: BF_vs_tuned=4.615, BF_vs_SSFSR=19.4; `c9g`: 5.7/4.64/3.30 and 1.41e2/2.65e1/5.09) reconcile exactly with the paper's tab:gr and tab:bayes entries.

Two honest caveats bound the *scope* of the central claim (both now disclosed): (i) the entire −35/16 → observable chain is conditional on assumption (d), cubic-order transmission through the bounce, which is derived only under the dressed-metric quantization (the deformed-algebra signature-change window is unestablished); and (ii) the observable significance built on top of −35/16 is a marginal, single-source, proxy-floored recast (M1). Neither undermines the amplitude correction itself, which is the paper's genuine, self-contained, citable contribution.

---

**Summary for the editor:** The requested presentation closures are complete and correct; the physics is sound; nothing is fabricated. The one substantive question is impact/scope (M1) — a marginal-significance recast whose external covariance is unavailable — which is an editorial weight judgment, not a correctness problem. The Appendix-A amplitude correction alone is a clean, verifiable result worth the literature record. Recommend **MINOR REVISIONS**: address the abstract floor-range calibration (M1), align the "resolves" framing with the appendix (m1), and trim repetition (m2/m3).

**Best Next Steps**
1. Calibrate the abstract significance range to reflect the honest 0.8σ proxy-dependent floor (M1) — highest-value, one-paragraph edit.
2. Align the Conclusion/title "resolves the factor-of-two" wording with Appendix A's precise "establishes −35/16; origin of printed −35/8 not reconstructed" (m1).
3. Consolidate the ≥7 repeated Cai–Li disclosures and the triple r-vs-r_eff reconciliation to one canonical statement each (m2), and trim the abstract to ~200 words (m3).
4. Add clarifying comments to the `cai_shape.py`/`cai_conv.py` reference targets (m4).

Say `continue` and I will take the next best scoped step.
