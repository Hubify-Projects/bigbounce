# R26conf P1A — TRUTH AUDIT (v1A.0.53 → edits applied 2026-06-10)

Auditor: in-session Claude (native tex + committed-artifact recompute). Ground truth: `arxiv/paper1a_ech_nogo.tex`, `.bbl`, prior-round closure log (tex header), committed artifacts.

Auto-falsify rules applied: future-date (June 2026 project dating) → FALSIFIED; citation-nonexistence → checked `.bbl` first; correction-note removal → HOUSTON-DECISION.

| Finding | Class | Verdict | Action |
|---|---|---|---|
| INSESSION M1 (App C sign convention) | presentation | STALE | Sentence already at L2408–2411 ("overall sign matches Eskilt–Komatsu convention") — applied pre-audit |
| INSESSION M2 (App C → Eq.17 bidirectional pointer) | presentation | STALE | Forward pointer already at L2406–2408 — applied pre-audit |
| INSESSION m1 (gauge spec understated) | presentation | VERIFIED | CLOSED: Coulomb–temporal gauge sentence ($A_0=0$, $\partial_i A^i=0$, $\epsilon^{ijk}A_j\partial_k$ structure) added in App C |
| INSESSION m2 (radio-galaxy achromaticity cites) | presentation | STALE | CarrollFieldJackiw1990 + HarariSikivie1992 already cited in App C |
| INSESSION m3 (C_aγ basis-conversion cross-ref) | presentation | VERIFIED | CLOSED: App C now points to the Sec. IV.D basis-conversion footnote |
| INSESSION m4–m10 | all-clears | N/A | Reviewer's own arithmetic verifications; no action |
| META-E1 (Cartan eq. factor-2: Eq.(3) 8πG·(1/4) vs §IV.A κ/2) | claim-truth (derivation) | **VERIFIED** | PARTIAL CLOSE: convention-disclosure footnote added at Eq.(3) noting the factor-2 between spin-tensor weight conventions + OOM-immateriality (all downstream closures carry ≥2-OOM slack). Single-convention re-derivation **QUEUED** (operator-level follow-up; pattern-036 forbids same-day fabricated re-derivation) |
| META-E2 (residual ~√n_ψ/T_reh^1/2 dimensionally inconsistent: dim 1 vs J5 dim 3) | claim-truth | **VERIFIED** | CLOSED per reviewer's fallback fix: unsupported residual-scaling clause removed; barrier now rests solely on the rate-vs-Hubble washout argument |
| META-M3 (M symbol collision) | presentation | STALE | TIER-A3/v1A.0.49 footnote already disambiguates M_area-gap vs CS scale (L1280–1302) |
| META-M4 (Fig 2 N≈55 vs N_tot≈92) | claim-truth | STALE | Caption already marks N≈55 as "illustrative … quantitative bookkeeping uses N_tot≈92" (R24conf closure) |
| META-M5 (ALP anisotropic birefringence check) | recompute | QUEUED | Requires Cℓ^αα consistency computation vs Planck anisotropic-rotation limits; not same-day |
| META-M6 (Route-2 imports α/M from photon sector) | recompute (derivation) | QUEUED | Same operator-level follow-up as META-E1; Eq.(15) footnoted conservatism band (10⁻⁵⁸ vs 10⁻⁶⁰) already absorbs the normalization ambiguity |
| META-m7 (ε tensor-vs-symbol in Eq.(6)) | presentation | QUEUED (minor) | Notation-block addition deferred to the same operator-level pass |
| META-m8 ("observed isotropic birefringence at β≈0.27°–0.30°") | claim-truth (wording) | VERIFIED | CLOSED: rephrased — published 0.342°±0.094° (WMAP+Planck) / 0.215°±0.074° (ACT DR6) stated; 0.27°–0.30° labeled as the paper's benchmark within both 1σ bands |
| META-m9 (confidence-cut post-hoc stability) | recompute | OUT-OF-SCOPE here | Paper-IV pipeline property; P1A already carries matched-footprint caveat (R24conf META-M8/E7 closure) |
| META-m10 (Table IV fNL survivability note) | presentation | VERIFIED | CLOSED: footnote added to tab:params fNL row (erased at SPHEREx scales under N_tot≈92 dilution) |
| META-N1 ("~60 orders" unquantified) | presentation | VERIFIED | CLOSED: one-line estimate added ((α/M)θ′ ~10⁻⁶³ eV vs k~6×10⁻⁴ eV → ~10⁵⁹) |
| OpenAI B1 (Fig 10⁻²⁰ vs body 2.5×10⁻²¹; "different units" wrong) | claim-truth (wording) | VERIFIED | CLOSED: caption text now says decade-rounded ceiling of the same dimensionless ratio |
| OpenAI E2/E6 + Perplexity E4 (correction-note / draft-history removal) | presentation | HOUSTON-DECISION | Deliberate transparency artifacts; removal not auto-applied |
| Grok E2 / OpenAI E1/M6/M11 / Perplexity E1/E4 (companion-paper self-containment) | process | FALSIFIED/STALE | Companions exist in-repo and post concurrently; `.bbl` entries verified (Golden2026P1b etc.); multi-round prior adjudication |
| Perplexity E2/E5 + Grok N1 (future-dated arXiv IDs, June 2026 date) | citations | AUTO-FALSIFIED | Project dating rule; arXiv:2509.13654 (ACT DR6) present in `.bbl` |
| Grok E1/E3/E4, M1–M3; OpenAI E3–E5, M1–M10, E7–E10; Perplexity E3/E6, M1–M5 | scope/heuristic-labeling/length | STALE/OPINION | Re-statements of items adjudicated R3–R24conf (paper already labels ansatz/heuristic status explicitly at every flagged site; length/REJECT recommendations are editorial opinion) |
| OpenAI E7 (Eq.(4) undefined N / coefficient mismatch) | claim-truth (derivation) | MERGED → META-E1 queue | Same normalization audit |

**Substantive verified items this round: META-E1 (disclosed, re-derivation queued), META-E2 (wrong dimensional claim, removed).**
Recompile after closures: 25 pp, 0 errors, 0 undefined refs; remaining overfull hboxes are 3 pre-existing sub-7pt equation overhangs outside edited regions.
