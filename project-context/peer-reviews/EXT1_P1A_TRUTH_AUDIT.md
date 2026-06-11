# EXT1 P1A — External Truth-Audit (Round EXT1)

**Paper**: `arxiv/paper1a_ech_nogo.tex` · v1A.0.56 · compiled PDF `arxiv/paper1a_ech_nogo.pdf` (26 pp.)
**Reports audited**:
- `EXT1_P1A_ChatGPT.md` — ChatGPT Pro Extended — **REJECT** (8 BLOCKERS, 8 MAJORS, 9 MINORS)
- `EXT1_P1A_Grok.md` — Grok Heavy — **MAJOR REVISIONS** (3 BLOCKERS, 3 MAJORS, 5 MINORS)
- `EXT1_P1A_Gemini.md` — Gemini 3.5 Thinking — **MAJOR REVISIONS** (2 BLOCKERS, 1 MAJOR, 2 MINORS)

**Audit date**: 2026-06-10
**Protocol**: feedback_peer_review_truth_audit_protocol (per-finding verdict; reviewer claims verified against repo before credit).

---

## Verdict table

| # | Reviewer | Severity-as-called | Finding (one line) | Verdict | Evidence |
|---|----------|--------------------|--------------------|---------|----------|
| F1 | GPT B1 | BLOCKER | Dim-+1 parity-odd operator drives headline claims (N_tot, fine-tuning, DE-closure) even though paper admits it is a scaling ansatz | **PARTIAL/VERIFIED** | tex L355–368 abstract; L2333–2398 App B candidly labels ansatz; but L398 still uses N_tot≈92 as a structural-tension lever. Paper self-disclosed but headline propagates the ansatz. Real demotion needed at title/abstract/conclusions. |
| F2 | GPT B2 | BLOCKER | R2/R3 use ansatz EFT estimates not derived coefficients (Mercuri/Benedetti–Speziale not literally giving Eq.(14)/(16)) | **PARTIAL/STALE-IN-PROSE** | tex L1268–1287 ALREADY states "Eq.(\ref{eq:gamma_running}) is a chiral-count EFT bound rather than the full perturbative result." R2 similarly self-labelled L1216. ChatGPT's `add a derived/cited/ansatz table` fix is actionable; the underlying complaint is largely closed in prose. |
| F3 | GPT B3 | BLOCKER | Abstract "each fails at the amplitude level" contradicts §IV.D which explicitly says R4 is NOT closed by amplitude mismatch | **VERIFIED** | tex L357 (abstract): "each fails at the amplitude level under stated assumptions." tex L1392–1394 (§IV.D): "R4 is therefore \emph{not} closed by amplitude mismatch (as prior analyses claimed); it is closed by [...] cosmological-constant fine-tuning." Headline ↔ body contradiction is real and unfixed. |
| F4 | GPT B4 | BLOCKER | Reheating thermal-reset (§II.C.1) asserts Γ_washout > H but supplies no rates / chemical-potentials / sphaleron-Yukawa computation | **VERIFIED** | tex L961–975: assertion only ("C/P-violating scattering rates [...] exceed the Hubble rate at T~T_reh"). No species table, no Γ_washout(T) curve, no sphaleron/Yukawa rates, no Boltzmann eqn. Paper itself concedes "we do not assign a quantitative scale to the incoherent fluctuation residual." Real gap. |
| F5 | GPT B5 | BLOCKER | ALP convention mixed: Eq.(17) implies θ has dim +1 (since α/M is dim −1 and FF̃ is dim 4) but App C uses θ dimensionless in V=m²f²(1−cosθ) | **VERIFIED** | tex L1316–1318 (operator −¼(α/M)θFF̃) vs L2429 (V=m_θ²f²(1−cosθ)). Both conventions coexist; canonical resolution is θ_phys = f_a·θ_dimless and the operator becomes (α/M)·(θ_phys/f_a)·FF̃, i.e. a g_φγ coupling absorbing f_a. Paper does sketch this at L2487 (`α/M ≡ C_aγ α_em/(2π f_a)`) but Eq.(17) and L1316–1326 still read dimensionally inconsistent as written. Real fix needed. |
| F6 | GPT B6 | BLOCKER | Reproducibility bundle README labels itself "v0.9.0" "Geometric Dark Energy" — does not match v1A.0.56 | **VERIFIED** | `reproducibility/README.md` L4–5: "Geometric Dark Energy from Spin-Torsion Cosmology... Version: v0.9.0 (2026-03-03)". Paper's Data-and-Code statement at tex L2263–2272 claims "All materials necessary to reproduce the cosmological and galaxy spin results are publicly available." Bundle ↔ manuscript desync is real. ChatGPT did real on-disk checking here. |
| F7 | GPT B7 | BLOCKER | Figs 1, 2, 5, 6 carry burned-in stale numerical labels disclaimed only in captions | **VERIFIED** | tex L542–543 (Fig 1 PTA γ=3.20±0.42 disclaimed); L673–676 (Fig 1 N≈55 disclaimed; ChatGPT mislabels as Fig 2 — Fig 1 actually carries it); L826–830 (Fig 5 ω/H decade-rounded); L1586–1592 (Fig 6 "115 OOM" disclaimed). Caption disclaimers are honest but ChatGPT correctly notes: stale-text-in-figure ≠ a fix. Regeneration overdue. Consensus w/ Grok B2, Gemini Minor-1. |
| F8 | GPT B8 | BLOCKER | "Fundamental action" Eq.(1) contains T_abc T^{abc} shorthand that is then declared not-varied — confusing | **PARTIAL** | tex L626–644: paper explicitly states "The T^{abc}T_{abc} term [...] is a shorthand [...] not varied independently — the connection variation is performed on the ECH+Dirac action alone." Variational status is stated. Gemini Blocker-2 is the same point. ChatGPT's "split into two equations" fix is presentational cleanup, not a logical error. PARTIAL: real presentation problem, not a derivation error. |
| F9 | GPT M1 | MAJOR | "All perturbation orders" needs to be tightened to "all classical metric/scalar perturbation orders around torsion-free branch" | **VERIFIED** | tex L374–391 abstract: paper says "torsion vanishes at all perturbation orders" without explicit quantum / fermion-loop / propagating-torsion / Immirzi-dynamical exclusion in the abstract itself. Exclusions appear in body but the headline wording is too broad. Real fix. |
| F10 | GPT M2 | MAJOR | N_tot–f_NL tension needs full mode-history (contraction → bounce → inflation → reheating → today) | **VERIFIED** | tex L398 abstract sketch + L2189 Sec XIV.D give an e^32 scale-separation argument; no transfer-function / mode-tracking derivation in the paper. Paper's matter-bounce f_NL=−35/8 is class-level (acknowledged L404–408). The structural-tension claim survives as heuristic but is not derived. Real gap; Grok M3 ("add a one-panel SPHEREx k-mapping figure") is the same. |
| F11 | GPT M3 | MAJOR | Heavy reliance on unpublished companions (P1b, P2, P3, P4) for MCMC, NaMaster, ALP, galaxy-chirality, NANOGrav | **VERIFIED** | 42 occurrences of `companion`/`P1b` in tex; L518 imports H_0=67.68±1.06, ΔN_eff≈0 from P1b; L1049–1056 same. Grok B1 is the consensus version. Real self-containment problem unless companions ship simultaneously to arXiv. |
| F12 | GPT M4 | MAJOR | "DESI lends empirical support to quintom scenarios" is too model-specific | **VERIFIED** | tex L2192: "equation-of-state crossing at 3.1–4.2σ lends empirical support to quintom scenarios." The DESI result is consistent with w0wa-quintom-like phenomenology; "empirical support to quintom" specifically is editorial overreach. Easy textual fix. |
| F13 | GPT M5 | MAJOR | "Structural-incompatibility theorem" language overstates a mixed barrier catalog | **OPINION/PARTIAL** | tex L1607–1613 labels barriers `Novel / Known / Structural-philosophical`; the catalog IS self-disclosed as mixed. "Theorem" usage in headline is loose. Reasonable copy-edit; not a derivation issue. |
| F14 | GPT M6 | MAJOR | R1 "largest plausible cosmic fermion densities at recombination" — should be narrowed to late-time | **VERIFIED** | tex §IV.A (Route 1): the NJL closure is for late-time DE, not for early-thermal-era fermion densities. Narrowing wording is correct. Real, easy. |
| F15 | GPT M7 | MAJOR | ALP β≈0.27° demoted to benchmark — correctly. ACT DR6 0.215°±0.074° is REAL — should not be flagged nonexistent | **FALSIFIED-PREEMPTIVELY-RESOLVED** | bbl L97–106: `DiegoPalazuelos2025` cited correctly; tex L415–417 cites both. ChatGPT is pre-empting any nonexistence concern — paper passes. The LiteBIRD-forecast sharpening request is minor. |
| F16 | GPT M8 | MAJOR | Cautious caveat language has not propagated to title/abstract/conclusions | **VERIFIED** | Title (L344–346) keeps "Closure of Four Minimal ECH Dark-Energy Routes"; abstract L357 keeps "each fails at the amplitude level." Same body-vs-headline drift as F3. Real, same fix root-causes F3, F9, F12, F13. |
| F17 | GPT Minor | MINOR | Abstract too long for MNRAS/JCAP/PRD | **OPINION** | Abstract L354–430 is ~77 lines incl. caveats and correction history. Journal-style call. |
| F18 | GPT Minor | MINOR | PACS deprecated | **OPINION/HOUSTON-DECISION** | tex L432 keeps PACS; revtex4-2 still supports it; PRD does not reject submissions for it. |
| F19 | GPT Minor | MINOR | γ overloaded (Barbero–Immirzi vs PTA slope); β overloaded (birefringence vs RG) | **VERIFIED** | tex shows both usages; consistent subscripting (γ_BI, γ_PTA, β_CB) is a real readability fix. |
| F20 | GPT Minor | MINOR | Eq.(15) denominator hard to parse dimensionally | **OPINION** | Eq.(15) is the dimensionless Δθ_one-loop/Δθ_obs ratio (tex L1220–1233); already explicit. Style call. |
| F21 | GPT Minor | MINOR | Several captions essay-length and contain correction history | **VERIFIED** | Fig 1 caption (L668–676), Fig 5 (L817–833), Fig 6 (L1578–1597) all carry burned-in disclaimers. Move to body. |
| F22 | GPT Minor | MINOR | Table II should reflect "14 entries, 13 independent" in count column | **VERIFIED** | tex L1616: B14 subsumes B8 noted in caption; column count not updated. Easy. |
| F23 | GPT Minor | MINOR | Table III "Quintom-B — consistent" with daggers is confusing | **PARTIAL/VERIFIED** | tex L1899–1905: extensive dagger footnotes explain "theoretical accommodation, not posterior preference." Houston-Decision style call. |
| F24 | GPT Minor | MINOR | Sec X Step 5 "total derivative contributes nothing" should be deleted | **FALSIFIED** | tex L1803–1808 already says Step 5 is "logically distinct from the pointwise Bianchi-vanishing of the previous step" and covers the residual Nieh–Yan boundary term at T≠0. Logically consistent; ChatGPT misread the structure. |
| F25 | GPT Minor | MINOR | Acknowledgments — "all scientific claims independently verified" too sweeping | **OPINION** | tex L2288–2290; editorial. |
| F26 | GPT Minor | MINOR | Popławski / Domagała / Gödel accent encoding | **FALSIFIED** | tex L657 `Domaga\l{}a`, L1553 `G\"odel`, L2281 `Pop\l{}awski` all encoded correctly. ChatGPT inferred from extracted text; on-disk source is fine. |
| F27 | Grok B1 | BLOCKER | Self-containment / companion-paper dependence — companions [2], [6] forwarded too heavily | **VERIFIED** | Same as F11. Consensus. |
| F28 | Grok B2 | BLOCKER | Outdated figure annotations (Figs 1, 4, 5, 6) — regenerate with γ=2.567±0.382, updated forecasts | **VERIFIED** | Same as F7. Consensus. |
| F29 | Grok B3 | BLOCKER | R2/R3 coefficients are ansatzes not derivations; need explicit "conservative upper bounds, closures survive O(1) larger" disclaimer | **VERIFIED-AND-NEAR-CLOSED** | Same root as F2. Grok's specific fix (single inline statement) is on-disk feasible; less work than ChatGPT's table demand. |
| F30 | Grok M1 | MAJOR | Barrier catalog: B8 subsumed by B14 should drop count to 13, label each "first-principles / scaling ansatz / heuristic" | **VERIFIED** | tex L1607–1613 already labels; tex L394–395 says 13 independent (14 historical, B8 subsumed). Drop column-count in Table II body. Same as F22. |
| F31 | Grok M2 | MAJOR | Prose density — consolidate scope disclaimers into one Intro paragraph | **OPINION** | Editorial; real but style. |
| F32 | Grok M3 | MAJOR | Structural tension N_tot=92 vs f_NL needs a SPHEREx k-mapping figure | **VERIFIED** | Same as F10. Consensus. |
| F33 | Grok Minor | MINOR | MNRAS style ("section" not "Sec."), Oxford commas, self-contained captions | **OPINION** | Journal-style. |
| F34 | Grok Minor | MINOR | Eq.(11) prefactor (T_reh/M_GUT)^{3/2} flag as dimensional-analysis estimate (boldface disclaimer in eq env) | **OPINION** | Already in text. Style. |
| F35 | Grok Minor | MINOR | Move "we do not assign a quantitative scale to incoherent fluctuation residual" to footnote | **OPINION** | tex L972–975. Editorial. |
| F36 | Grok Minor | MINOR | Typos: "falsification criteria"→"falsifiability criteria"; "naMaster"→"NaMaster"; remove "burned-in" after regen | **VERIFIED** | Standard copy-edit. |
| F37 | Grok Minor | MINOR | References — format "in preparation" entries per journal | **OPINION** | Style. |
| F38 | Gemini B1 | BLOCKER | Off-shell action S_eff has dim −3 not 0; path integral exp(iS) ill-defined off-shell unless α→α M_Pl³/M inserted | **VERIFIED-AND-ACKNOWLEDGED** | Same root as F1. tex L2353–2360 explicitly says exactly this: "if Eq.(\ref{eq:Seff_comp}) is to map to a dimension-+4 local operator without on-shell curvature insertions, the coupling must carry three additional powers of M_Pl (α/M → α M_Pl³/M)." Gemini's proposed fix is in the paper. Real-but-self-disclosed; the headline use of the ansatz is what makes Gemini call it a BLOCKER. |
| F39 | Gemini B2 | BLOCKER | Eq.(1) "fundamental action" with explicit T_abc T^{abc} added to torsionful R causes double-counting / unmotivated constraint | **PARTIAL/STALE-IN-PROSE** | Same as F8. tex L638–644 explicitly states the T² term is a shorthand and not independently varied. Logical structure is OK; presentational fix would silence the complaint. |
| F40 | Gemini M1 | MAJOR | Tension between "canonical-scalar perturbation-transparency" (torsion=0) and "reheating reset" (requires fermion plasma to thermalize axial current) | **PARTIAL** | Real consistency thread. Paper at L976–982 explains the thermal reset is "an independent thermodynamic erasure channel" that "strengthens B14" — i.e. it applies in the fermion-dominated scenario, not contradicting the spinless-matter theorem. A one-sentence clarifier ("scenario-A vs scenario-B") closes Gemini M1 cleanly. |
| F41 | Gemini Minor 1 | MINOR | Figs 1, 5 burned-in placeholders | **VERIFIED** | Same as F7. Consensus. |
| F42 | Gemini Minor 2 | MINOR | Eq.(21) tensor EOM — clarify comoving-k vs ∇²/a² | **OPINION** | tex Sec X.C. Standard notation; explicit clause is a clarity polish. |

---

## Consensus findings (flagged by ≥2 reviewers)

| Consensus # | Theme | Reviewers | Verdict | Action root |
|-------------|-------|-----------|---------|-------------|
| C1 | Burned-in figure annotations stale (Figs 1, 5, 6 at minimum) | GPT B7, Grok B2, Gemini Minor 1 | VERIFIED | Regenerate figures; F7/F28/F41 |
| C2 | Headline-vs-body drift: "each fails at amplitude level" vs §IV.D R4 = naturalness-only; also "all perturbation orders" too broad; also "quintom support" too strong | GPT B3+M1+M4+M8 | VERIFIED | Title/abstract/conclusions rewrite; F3/F9/F12/F16 |
| C3 | Companion-paper dependence: imports MCMC H_0/ΔN_eff, NaMaster, ALP fits, galaxy chirality from unpublished P1b/P2/P3/P4 | GPT M3, Grok B1 | VERIFIED | Either ship companions simultaneously OR demote numbers to "from companion in prep, not used in proof"; F11/F27 |
| C4 | R2/R3 ansatz status not derivation — needs explicit derived/cited/ansatz separator | GPT B2, Grok B3 | PARTIAL/CLOSED-IN-PROSE | Already labeled in body; add a single explicit sentence or a 3-row inline table; F2/F29 |
| C5 | Reheating thermal-reset asserts Γ_washout>H without computation | GPT B4, Gemini M1 (consistency arg) | VERIFIED | Either supply rates (sphaleron, Yukawa, chirality-flip vs H(T)) or downgrade to conjectural caveat; F4/F40 |
| C6 | Eq.(1) T² term presentation: "fundamental action" vs "not-varied shorthand" | GPT B8, Gemini B2 | PARTIAL | Split Eq.(1) into off-shell Palatini–Holst–Dirac action + on-shell effective four-fermion result; F8/F39 |
| C7 | Dimensional status of off-shell parity-odd operator drives headline despite ansatz status | GPT B1, Gemini B1 | PARTIAL/SELF-DISCLOSED | Paper acknowledges in App B; need headline demotion not derivation; F1/F38 |
| C8 | N_tot=92 vs f_NL=−35/8 structural tension needs mode-history calc + SPHEREx k-mapping figure | GPT M2, Grok M3 | VERIFIED | Add transfer-function panel; F10/F32 |
| C9 | "burned-in" verb / "NaMaster" capitalization / accent polish | Grok Minor, Gemini Minor 2 | VERIFIED | Copy-edit pass; F36 |

---

## Action plan (VERIFIED + PARTIAL items, hardest-first)

**TIER 1 — substantive (drive 95→99 readiness):**

1. **[C7+F1+F38] Dimensional ansatz: demote headline use.** Edit title, abstract sentence 1, §IV scope paragraph, §XIV conclusions, App B intro. Replace "Channel-Level **Closure** of Four Minimal ECH Dark-Energy Routes" with "Channel-Level **Constraints** on Four Minimal ECH Dark-Energy Routes" OR keep "Closure" only after the perturbation-transparency theorem. Files: `arxiv/paper1a_ech_nogo.tex` L344–346 (title), L355–368 (abstract), L1083–1100 (§IV scope), L2189–2200 (§XIV.D). [Tier 0 root for C2, C7.]

2. **[C5+F4+F40] Reheating thermal-reset rates.** Add to §II.C.1 (`arxiv/paper1a_ech_nogo.tex` L951–982): a paragraph with Γ_washout vs H(T) for (a) electroweak sphalerons, (b) Yukawa chirality flips for SM fermions, (c) ν oscillation chirality randomization. Cite Kuzmin–Rubakov–Shaposhnikov + Cline-style equilibrium tables. If full Boltzmann calc is out of scope, downgrade the sentence "providing an independent thermodynamic closure" to "providing a plausible thermodynamic erasure channel; a quantitative Γ_washout(T) vs H(T) computation is left to a follow-up." Add Gemini-M1 scenario-disambiguation sentence at L976: "(spin-density inflaton → B14 by perturbation-transparency; fermion-dominated reheating → thermal reset)."

3. **[C8+F10+F32] Mode-history figure for N_tot vs f_NL.** Add one panel `figures/figureN_mode_history.png` showing k_comoving constant across contraction → bounce → inflation → today, with the SPHEREx-mode k_phys/k_bounce_phys = e^{N_tot − N_exit} ≈ e^{32} stack. Reference at abstract L398 and at §XIII.

4. **[F5] ALP convention single-source.** Pick ONE convention in §IV.D and App C:
   - Operator: −¼ g_φγ φ FF̃ with g_φγ = α/M, φ canonical (dim +1).
   - Potential: V = m_φ² f_a² (1 − cos(φ/f_a)).
   - Identify Δθ ≡ Δφ/f_a explicitly at first use.
   Edit `arxiv/paper1a_ech_nogo.tex` L1316–1326 (Eq.(17)), L2418–2430 (App C Eq.(C1)–(C4)), L2487–2493 (basis bridge). Re-derive Eq.(17) → Eq.(eq:beta_bound) in the chosen convention.

5. **[F6] Reproducibility bundle alignment.** Either bump `reproducibility/README.md` to a `v1A.0.56`-labelled bundle with `IMPLEMENTATION_MAP.md` updated to current paper claims and Table IV row-by-row pointers; or narrow §"Data and Code Availability" to "minimal-ECH structural calculations are in the repository; MCMC chains and NaMaster pipeline are documented in companion P1b." Hardest path: full DOI freeze (Zenodo) of a v1A.0.56 bundle.

6. **[C3+F11+F27] Companion-paper self-containment.** Either coordinate-package P1b/P2/P3/P4 onto arXiv same-day as P1A, or in `arxiv/paper1a_ech_nogo.tex` L518, L596–610, L1049–1056: move imported MCMC H_0/ΔN_eff numerics to a footnote with the disclaimer "drawn from companion in preparation, not used in the structural closure proof."

7. **[C2+F3+F16] Body-vs-headline drift sweep.** Single substitution pass replacing "each fails at the amplitude level" (L357) with "R1–R3 are amplitude-suppressed under stated ansätze; R4 is closed by a naturalness/CC-tuning objection." Propagate to conclusions L2180–2200.

**TIER 2 — presentation:**

8. **[C1+F7+F21+F28+F41] Regenerate Figs 1, 5, 6.** Use current γ_PTA = 2.567±0.382, N_tot = 92, "10⁵ residual" (not "115 OOM improvement"), tight ω/H bound 2.5×10⁻²¹. Remove burned-in disclaimers from captions after regen.

9. **[C6+F8+F39] Split Eq.(1).** `arxiv/paper1a_ech_nogo.tex` L626–644: present (a) off-shell Palatini–Holst–Dirac action with R̂(ω) and independent ω, then (b) the on-shell effective four-fermion action after Cartan elimination. Move shorthand statement to L638 paragraph break.

10. **[F2+C4] R2/R3 ansatz vs derivation table.** Add 3-row inline at L1216 or L1268: derived | cited literature | this-paper ansatz | closure conclusion.

11. **[F9] Perturbation-transparency scope.** Restate abstract sentence at L374–391 as "for canonical scalar matter, **at all classical metric/scalar perturbation orders around the torsion-free branch** [...] (excludes propagating-torsion, dynamical-Immirzi-field, fermion-loop, and non-minimal-matter sectors)."

12. **[F12] Quintom language.** L2192: "lends empirical support to quintom" → "motivates dynamical-dark-energy parameterizations including w0wa and quintom-class scenarios."

13. **[F14] R1 density qualifier.** L1134–1153: "largest plausible cosmic fermion densities at recombination or post-recombination" → "for late-time / post-recombination Standard-Model number densities; thermal-era fermion densities are addressed separately in §II.C.1."

14. **[F22+F30] Table II column update.** L1616: change "14 mechanism-class constraints" to "14 catalogue entries, 13 logically independent (B8 subsumed by B14)."

15. **[F19] Notation subscripts.** γ_BI vs γ_PTA, β_CB vs β_RG. Global substitution pass.

**TIER 3 — copy edit (F25, F26-falsified-keep, F33, F34, F35, F36, F37, F42, F17, F18, F20, F23, F24-falsified-keep)** — single editorial pass.

---

## Gap analysis — what the internal R-rounds (R23–R28conf) missed entirely

Internal-reviewer upgrades to load into the catalog:

- **GAP-1 [F3/F16 — body-vs-headline drift]**: Six internal rounds did not catch that the abstract still says "each fails at the amplitude level" while §IV.D explicitly says R4 is "not closed by amplitude mismatch." Internal reviewers were reading §IV and the abstract in isolation; no cross-surface consistency sweep. **Pattern**: `headline-vs-body-claim-drift-after-R4-naturalness-reframe`. Promote to `paper-pre-review-check` automated grep.

- **GAP-2 [F5 — ALP convention dimensional inconsistency]**: App C's `V = m_θ² f² (1−cosθ)` with θ dimensionless coexists with §IV.D's `(α/M)θ FF̃` where dimensional accounting requires θ dim +1. Internal rounds added App C (MCS derivation) without re-auditing §IV.D's operator. **Pattern**: `new-appendix-not-cross-checked-against-main-body-conventions`. Add to `latex-audit`.

- **GAP-3 [F6 — repro bundle vs manuscript desync]**: `reproducibility/README.md` still labels itself v0.9.0 "Geometric Dark Energy" paper while manuscript is at v1A.0.56. Internal rounds focused on prose; no external review actually clicked the GitHub link. **Pattern**: `reproducibility-bundle-version-not-synced-on-paper-bump`. Add as gate inside `bigbounce-version-bump` skill.

- **GAP-4 [F4 — reheating washout missing calculation]**: All 6 internal rounds accepted "C/P-violating rates exceed H" as a closure-quality statement. No internal reviewer asked for Γ vs H curves. **Pattern**: `qualitative-rate-claim-not-Boltzmann-backed`. Add to internal-review checklist.

- **GAP-5 [F11 — self-containment via companion imports]**: Internal rounds tolerated 42 occurrences of `companion`/`P1b` because the SSOT treats the bundle as one programme. External reviewers do not. **Pattern**: `programme-bundling-blind-spot-for-standalone-submission`. Add to external-review checklist (different from internal).

- **GAP-6 [F10/F32 — structural tension as heuristic vs derived]**: The e^32 scale separation argument went through 6 rounds without anyone asking for the mode-transfer-function calc. **Pattern**: `dimensional-analysis-mistaken-for-derivation`.

These 6 gaps map to 6 new findings-archive entries for `r-round-pattern-mine` and 4 new patterns for `project-context/review-patterns/`.

---

## Assessment of ChatGPT's REJECT verdict

ChatGPT's REJECT rests on B1–B8 (8 BLOCKERS). After audit:
- **VERIFIED, real fixes**: B3 (F3), B4 (F4), B5 (F5), B6 (F6), B7 (F7) — 5 of 8.
- **PARTIAL / self-disclosed but headline propagates**: B1 (F1), B2 (F2), B8 (F8) — 3 of 8.
- **None FALSIFIED at the BLOCKER level.**

Even after demoting the PARTIALs, the 5 VERIFIED BLOCKERs (headline-vs-body drift on R4, missing reheating rates, mixed ALP convention, mismatched reproducibility bundle, stale figure annotations) are individually each a fair MNRAS/JCAP/PRD `Major Revisions` ask. **Bundled, they justify a `Major Revisions` ask, NOT a `REJECT`** — none of these is a fatal logical error or a result-overturning critique. ChatGPT's "REJECT" is harsher than the verified findings support; the harshness is driven by:

1. ChatGPT's framing that "caveats coexist with stronger headline claims" → it treats the gap as a structural rejection ground rather than a revision ask. Grok and Gemini, looking at the same gap, called Major Revisions.
2. ChatGPT's editorial preference for retitling the paper to a "phenomenological audit." That is a HOUSTON-DECISION on framing, not a referee blocker.
3. ChatGPT's reproducibility-bundle finding (F6) is the most damaging single finding; it is the only finding that could plausibly carry a REJECT on its own at top journals. But the fix (bump bundle to v1A.0.56) is mechanical.

Grok and Gemini both correctly identified the same substantive issues at MAJOR REVISIONS severity.

---

## Post-audit recommendation

**MAJOR REVISIONS** (consensus across Grok + Gemini; ChatGPT's REJECT is over-called by ~1 severity step given that all VERIFIED BLOCKERs are addressable without overturning a result). Three external reviewers, three independent reads, ~12 substantive consensus items, zero falsified results. Drive readiness backward from 99% to ~93–94% per `readiness-cap-99`; address the 7 Tier-1 actions above; then re-run cross-vendor R-round and target 99% post-fix. After Tier-1 + Tier-2 close, paper is genuinely publishable at MNRAS/JCAP/PRD as a constrained no-go + perturbation-transparency theorem package.
