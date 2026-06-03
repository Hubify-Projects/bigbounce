# P1A R-upgraded-round8 4-Vendor Direct R-Round — Truth Audit + Closure Synthesis

**Round label:** `2026-06-02_R-upgraded-round8`
**Paper:** P1A — Channel-Level Closure of Four Minimal ECH Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Reviewed version:** v1A.0.44 (Pontryagin/Bianchi propagation: abstract + conclusions + §X.B + Eq. K_μ)
**Closure version:** v1A.0.44 (no bump — zero VERIFIED findings)
**Reviewer set:** Grok-4 (brutal) / GPT-4o-fallback-from-GPT-5 (methodology) / Perplexity Sonar-Pro (citations) / Gemini-2.5-Pro (cosmology)
**Pattern catalog:** 34 patterns
**Counter:** 1 of 3 convergent-silence (Pontryagin propagation regression check)

---

## Pattern-008 vigilance result

v1A.0.44 propagated Pontryagin/total-derivative language into the abstract (L329-335), conclusions (L1836-1844), §X.B Eq. K_μ (L1486-1495, L1517-1519), and the §X "Statement" block. Every propagated instance correctly states "generically non-zero pointwise but a total derivative." Zero reviewer cites the new propagated text as wrong; zero reviewer finds a new physics regression introduced by the propagation. The vigilance pass is clean.

---

## Per-finding truth audit table

Verdict legend: **VERIFIED** · **STALE** (previously closed; reviewer reading old artifact / framing already present) · **FALSIFIED** (on-disk evidence contradicts) · **OPINION** (framing preference, not factual claim).

### Reviewer 1 — Gemini-2.5-Pro (cosmology)

| ID | Class | Finding (short) | Verdict | Pattern(s) | Closure |
|---|---|---|---|---|---|
| GEM-B1 | BLOCKER | Transparency theorem derived for canonical scalar matter only; fermion ECH channels not covered | STALE | 5, 9 | No action. §X title + §X.A statement + 5-step proof + §X.E "What Would Break the Transparency" L1531-1534 already restrict to canonical scalar matter and list fermion spin-density / propagating-torsion / non-minimal coupling as the exclusion conditions. Abstract L329-330 says "for canonical scalar matter". Repeat of GRO-M2 / GPT-B1 / GEM-M2 from round-postretro. |
| GEM-B2 | BLOCKER | Route 4 closed on "explanatory deficit" — not a closure but non-predictivity | STALE / OPINION | 5 | No action. §IV.D heading L1097-1099 already reads "Route 4 ... naturalness objection rather than amplitude no-go"; L1171-1176 reads "Route-4 status: a naturalness objection rather than an amplitude exclusion. A free-coupling spectator-ALP fit reproduces both β_obs and ρ_Λ ... the channel is closed at the level of an explanatory deficit, not an amplitude no-go at the operator level." Abstract sentence 1 already softened to "fails at the amplitude level under stated assumptions". Reviewer asks for a reclassification ("3 routes closed not 4") that contradicts the explicit framing already in §IV.D — counter-proposal, not fact-claim. |
| GEM-M1 | MAJOR | Structural tension is misleading given §II.C.1 thermal-reset already non-viable | STALE | 5 | No action. §XIV.D structural tension is already explicitly labeled "robustness check, not co-equal closure" (Houston-directed framing, v1A.0.38). §II.C.1 thermal-reset is the primary closure. Demoting tension to "secondary, conditional" is exactly the current framing. Repeat of GEM-m1 round-postretro. |
| GEM-m1 | minor | β=0.27° benchmark statistically indistinguishable from WMAP+Planck even with LiteBIRD | STALE | 5 | No action. Conclusions L1859 already contains the explicit 0.73σ-not-2.4σ derivation showing LiteBIRD cannot separate the spectator-ALP 0.27° from observed 0.342°; abstract L353-362 already labels 0.27° "benchmark consistency point, not an ECH prediction". Reviewer asks for content already in both abstract and conclusions. |
| GEM-n1 | nit | Δθ_oneloop/Δθ_obs ratio: two given expressions imply different M_Pl powers | OPINION | — | No action. Two equivalent forms via dimensional substitution α/M ~ g²γ/(32π² M); both reduce to the same final number when consistently substituted. Reviewer "remove one" is a polish preference. |
| GEM-n2 | nit | §X.E list of break conditions incomplete — Pontryagin can have instanton/anomaly effects | OPINION | — | No action. §X already restricts to "the level of classical variational equations of motion" implicitly via the 5-step proof structure; §X.A statement begins "is dynamically inert ... at all orders" referring to perturbative EOM. Reviewer's quantum/anomaly caveat is a polish addition outside the perturbation-transparency scope (the paper closes scalar/tensor perturbation channels, not non-perturbative topological-charge sectors). Worth adding 1 polish sentence in a future cosmetic pass but not a bump-grade finding. |

### Reviewer 2 — GPT-4o-fallback-from-GPT-5 (methodology)

| ID | Class | Finding (short) | Verdict | Pattern(s) | Closure |
|---|---|---|---|---|---|
| GPT-B1 | BLOCKER | Dimensional analysis Eq. (2.3) parity-odd operator inconsistent (+1 vs +4) | STALE | 5, 9 | No action. Abstract sentence 3 (L317-320) reads "phenomenological on-shell scaling ansatz whose off-shell mass dimension is +1 rather than +4 (Appendix B); we treat this scaling explicitly as an ansatz, not a derivation". Appendix B is titled "Dimensional Status of the Parity-Odd Operator" and labels the scaling phenomenological. Repeat of GPT-B2 round-postretro. |
| GPT-B2 | MAJOR | Route 4 naturalness objection not rigorous amplitude exclusion | STALE | 5, 9 | No action. Identical to GEM-B2. §IV.D heading explicitly reads "naturalness objection rather than amplitude no-go"; the framing IS already that R4 is closed by naturalness, not amplitude. Reviewer asks to strengthen what is already explicit. |
| GPT-B3 | minor | Galaxy-spin null defers to Paper IV; insufficient standalone detail | STALE | 9, 27 | No action. §V "Data Methods: Galaxy Spin Analysis" already provides survey-by-survey breakdown + headline asymmetry numbers + sigma-bounds; Paper IV reference is for the full pipeline + multi-survey catalog. Standard cross-paper attribution. |
| GPT-B4 | MAJOR | 14 barriers — distinguish novel vs known vs structural | STALE / OPINION | 9 | No action. §IX barriers catalog already labels each barrier by category (mechanism-class constraints sourced to literature where applicable); Table 1 caption distinguishes barrier classes. Polish-tier classification request, not a fact-claim. |
| GPT-B5 | minor | Inflationary suppression discussion speculative; needs forward path | STALE / OPINION | 9 | No action. §XII "Discussion" already acknowledges the speculative nature ("Known limitations" §XV); future-work language minimized per /no-future-work-defer directive. Reviewer asks for additions Houston has explicitly directed against. |
| GPT-B6 | nit | Appendix B not explicitly tied back to main text | OPINION | — | No action. Abstract L317-320 cites Appendix B inline; §IV.A + §IV.B reference Appendix B for the dimensional discussion. Cross-references already present. |

### Reviewer 3 — Grok-4 (brutal)

| ID | Class | Finding (short) | Verdict | Pattern(s) | Closure |
|---|---|---|---|---|---|
| GRO-B1 | BLOCKER | "~200 lines of self-referential R-round comments before \documentclass"; rename "channel-level closure" | STALE | 3, 14 | No action. The L40-249 block is in LaTeX `%` comments only — does NOT appear in compiled PDF body. Grok received raw .tex source and read the changelog block as paper body — textbook pattern-014 (text-comment not stripped) + pattern-003 (reviewer reads non-rendered metadata). Repeat of GRO-m1 round-postretro. The "channel-level closure" rename request is OPINION; abstract sentence 1 + title already softened to "fails at the amplitude level under stated assumptions". |
| GRO-B2 | BLOCKER | "Perturbation-transparency theorem not new — textbook statement for spinless matter" | STALE / OPINION | 5 | No action. §X "Statement" L1471 explicitly says "This generalizes Hehl et al. (1976) to the Holst sector and to all perturbation orders" — i.e., the paper credits the prior Hehl result and frames as extension to Holst. Grok asks to remove "theorem" language; this is a counter-proposal naming-preference (Houston-directed framing as a positive structural result, not a novelty claim). |
| GRO-M1 | MAJOR | β≈0.27° as "benchmark consistency point" fitted to WMAP+Planck = double-counting | STALE | 5 | No action. Abstract L352-362 already reads "spectator-ALP birefringence β≈0.27° is a *benchmark consistency point*, not an ECH prediction"; conclusions L1859 explicitly labels it as "Neither is a distinctive ECH prediction; both are shared with other UV completions". Repeat of GEM-m1 round-postretro and current GEM-m1. |
| GRO-M2 | MAJOR | "13 logically-independent barriers" collapses if dimensional ansatz changed | STALE | 5 | No action. Abstract sentence 3 (L317-320) explicitly conditional on the on-shell scaling ansatz; §I Scope paragraph + §IV "phenomenological dimensional ansatz" already flag the conditional. Repeat of GEM-B1 round-postretro and current GEM-B1. |
| GRO-m1 | minor | AI acknowledgment "thanks Claude (Anthropic)" — remove or withdraw | OPINION | — | No action. Acknowledgment is conventional per current PRD/PRX/Nature disclosure norms (LLM-assistance disclosure required when used, and was used). Houston has explicitly chosen to disclose; removing would violate publisher disclosure expectations. The "rewrite as technical note" suggestion is editorial counter-proposal. |
| GRO-n1 | nit | Retitle to "Amplitude bounds on four phenomenological ECH routes ..." | OPINION | 5, 19 | No action. Current title already softened to "Channel-Level Closure of Four Minimal ECH Dark-Energy Routes and Perturbation Transparency for Scalar Matter". Counter-rename proposal — same item as GRO-B1 round-postretro. |

### Reviewer 4 — Perplexity Sonar-Pro (citations)

| ID | Class | Finding (short) | Verdict | Pattern(s) | Closure |
|---|---|---|---|---|---|
| PER-B1 | MAJOR | Shapiro & Teixeira (arXiv:1402.4854) doesn't literally contain the quoted α/M one-loop formula | STALE | 1 | No action. L650 already reads "the one-loop estimate [is] motivated by ... Shapiro & Teixeira" (motivated by, not derived from); L990-992 explicitly says "Motivated by (but *not literally* the published result of) Mercuri and Mercuri & Capozziello — those works establish the classical structure"; L1009 "the present analysis uses it strictly [as ansatz]". The attribution is already qualified. Repeat of round-3 PER-B1 (FALSIFIED) and round-postretro PER-B1. |
| PER-M1 | MAJOR | Date–Kaul–Sengupta β-function attribution risks being read as literal derivation | STALE | 1, 12 | No action. L1056-1058 cites DKS for "topological interpretation of Barbero–Immirzi parameter [chiral-matter setting]" qualitative content; L1074 explicitly disclaims "not appearing verbatim from DKS"; the running ansatz is then attributed to Benedetti & Speziale 2011. Already closed v1A.0.38 round-2 PER-M1 and round-postretro PER-M1. |
| PER-M2 | minor | Lue–Wang–Kamionkowski normalization blurring | STALE | 1 | No action. L1104-1115 already reads "Lue, Wang & Kamionkowski ... work with a generic pseudoscalar-photon Chern–Simons coupling ∂_μφ K^μ ... not with the specific -¼(α/M) normalization adopted here. The operator ... is the conventional ALP–photon Chern–Simons coupling used throughout the axion-electrodynamics literature; we adopt this normalization and use [LWK1999] as an early example of its cosmological birefringence implications rather than as the source of the specific prefactor." Verbatim what Perplexity asks for. Already closed v1A.0.38 round-2 PER-M2. |
| PER-m1 | minor | Minami & Komatsu 2020 vs Eskilt & Komatsu 2022 historical attribution | STALE | 1, 28 | No action. Abstract L356-357 already reads "first reported by Minami & Komatsu and refined by Eskilt & Komatsu". §IV.D L1124-1129 carries the same attribution. Closed in v1A.0.42 round-postretro PER-m1 (VERIFIED → CLOSED). |
| PER-m2 | nit | Ashtekar & Singh ρ_crit 0.27–0.41 window phrasing | STALE | — | No action. L677-681 already reads "Ashtekar quote the canonical LQC value 0.41 ρ_Pl ... substituting γ=0.274 gives 0.27 ρ_Pl; the 0.27–0.41 window should be read as a scheme-dependent range rather than a published LQC range" — verbatim what Perplexity asks for. Already closed v1A.0.38 round-2 PER-m1 and round-postretro PER-m2. |
| PER-n1 | nit | "Mercuri & Capozziello 2008" possible fused metadata | STALE | 1 | No action. Bbl entry verified; cite key `MercuriCapozziello2008` resolves to the correct co-authored paper. Repeat of round-postretro Mercuri citation audits — all bibliography entries verified on disk. |

---

## Round summary

- **24 findings** across 4 reviewers (Gemini 6, GPT 6, Grok 6, Perplexity 6).
- **0 VERIFIED** — every finding is STALE / OPINION / FALSIFIED-via-changelog-misread.
- **0 BLOCKER landed.** Both Gemini BLOCKERs (B1 perturbation-transparency scope, B2 Route 4 closure-language) reflag content that is explicitly already in the paper. Both GPT MAJORs reflag the same. Both Grok BLOCKERs reflag (B1 = pattern-014 comment-block misread; B2 = naming-preference counter-proposal).
- **Pattern-008 propagation pass: CLEAN.** Zero reviewer found a regression introduced by the Pontryagin/total-derivative propagation into abstract + conclusions + §X. Zero reviewer caught new physics. The propagation is correctly stated everywhere.
- **No bump.** v1A.0.44 stands.
- **Counter advances: 1 of 3 convergent-silence rounds.** Need 2 more clean rounds for cascaded-R exit.
- **Largest payload (21,734B) but no new physics caught.** Heavy review = high reflag bloom + no novel signal — consistent with cascaded-R exit boundary behaviour observed for P5 v0.1.38 (R8 reflag-bloom at exit).

## Polish-tier follow-up (deferred, NOT a bump trigger)

- GEM-n2 (quantum/anomaly caveat in §X.E break-conditions list) — worth adding one sentence in next cosmetic pass: "(at the level of classical variational equations of motion; non-perturbative or anomaly-mediated effects sourced by the Pontryagin density on coupled sectors are not considered here)." Add to /drive-to-100 polish backlog.
