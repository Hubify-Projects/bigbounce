# P1U M23-EXT truth-audit (vs byte-unchanged v1U.0.20)

Raws read verbatim before any verdict: `P1U_grok_M23.md` (MAJOR, 3M/3m),
`P1U_chatgpt_M23.md` (REJECT, 12M/1m). ledger_match.py drafts + full §3 manual
truth-audit vs `arxiv/paper1_unified.tex` + `DISPOSITIONS/P1U.md`.

**Verdict: 0 genuinely-new real+editable findings. Every finding is a
source-cited re-flag of a standing DP1U D-id. clean-wave streak 9→10; cap 62 HOLDS.**

## Grok (MAJOR) — 3 MAJOR + 3 MINOR
1. **[MAJOR] title/abstract too long, acronym-heavy, bury scoped claim** → **DP1U-06 +
   DP1U-22** (channel-level "under stated assumptions" is the paper's own framing L1190/L1219;
   length OPINION). Re-flag.
2. **[MAJOR] core results (Fierz lemma, NJL gap eq, perturbed-tetrad) relegated to
   appendices without self-contained main-text steps** → **DP1U-19 + DP1U-05** (regulated
   NJL gap eq CLOSED-BY-COMPUTE v1U.0.14, App `app:njl_gap`; presentation-relegation is
   DP1U-22 length/venue OPINION). Re-flag.
3. **[MAJOR] Barrier-14 washout Γ_wash(T_reh)>H(T_reh) heuristic, no Boltzmann
   integration** → **DP1U-14** (reheating-reset D_inf disclosed "mathematical scaffolding"
   for an order-of-magnitude estimate; washout rate is an OOM SM-channel estimate, disclosed).
   Re-flag.
4. **[MINOR] "basis-complete at M_Pl-power-counting" over-readable as full diffeo no-go** →
   **DP1U-07 + DP1U-20** (completeness argued analytically via F1/F2/NDA; abstract softened
   to "script verifies two identities, not completeness" L1226-adj; full operator-level
   OUT-OF-SCOPE). Re-flag.
5. **[MINOR] 14-barrier justifications scattered; MCMC/NaMaster/ALP inflates to 62pp** →
   **DP1U-13 + DP1U-15 + DP1U-22** (independence caveat disclosed sec:barriers head;
   appendices labeled non-load-bearing illustrative; length OPINION). Re-flag.
6. **[MINOR] ECH-DE vs f_NL mutual-exclusivity needs explicit N_coh window/plot** →
   **DP1U-14 + DP1U-12** (D_inf/N_tot bookkeeping disclosed; coherence-window is the
   disclosed scaffolding argument). Re-flag.

Grok matches M21-MAJOR (same structure). pattern-066.

## ChatGPT (REJECT) — 12 MAJOR + 1 MINOR
1. **[MAJOR] Eqs.(1)–(4) no consistent variational principle; ¼T·T displayed not varied;
   Eq.(3) omits γ-inversion** → **DP1U-03** (first-order Palatini-EC over {e,ω,ψ}; ¼T·T
   "not varied", on-shell shorthand; two-step reading added v1U.0.10). Re-flag.
2. **[MAJOR] Eq.(6) has dim +1, inadmissible; Bianchi can't change dimension; NDA doesn't
   repair; restates CC problem** → **DP1U-08 (+ DP1U-11)** (+1→+4 dressing labeled
   "dispensable illustrative heuristic, not load-bearing"; genuine dim-4 O1–O6 basis
   primary). Re-flag.
3. **[MAJOR] basis completeness not demonstrated; O1=O6, O4 ill-defined; excludes
   derivative/mixed/flavor operators** → **DP1U-07 + DP1U-20** (analytical completeness
   argument; non-minimal/derivative/multi-species explicitly OUT-OF-SCOPE). Re-flag.
4. **[MAJOR] inflationary-dilution inconsistent with algebraic torsion; J5²/M_Pl²∝a^-6
   stiff not w=-1; D_inf∝e^-3N can't apply to vacuum energy** → **DP1U-14** (a^-6
   stiff-fluid-like disclosed verbatim L5292; "no coherent w=-1 vacuum component" L2594;
   D_inf = "mathematical scaffolding" L4172). Re-flag.
5. **[MAJOR] Route 2 ϑ_NY not a d.o.f.; [∂ϑ]=2 but ∂ϑ~H0 dim-1 substitution; 10^-60
   unsupported** → **DP1U-09** (∂ϑ dim +2 correct, ∂ϑ~H substitution + alternative-ordering
   bound disclosed; Route 2 "exploratory framing, not load-bearing"). Re-flag.
6. **[MAJOR] Route 3 Benedetti-Speziale Euclidean/Majorana/scheme-dependent, no stress
   tensor derived; (Δγ/γ)(H0/M_Pl) an ansatz** → **DP1U-10** (H0/M_Pl amplitude-budget
   mapping flagged conditional/ansatz; scheme-spread disclosed). Re-flag.
7. **[MAJOR] NJL exclusion not rigorous; Fierz doesn't fix Hartree channel; pseudoscalar
   condensate Lorentz-invariant** → **DP1U-05 + DP1U-19** (CLOSED-BY-COMPUTE v1U.0.14:
   regulated gap eq, repulsive scalar channel + sub-critical coupling; strong-coupling-
   beyond-mean-field OUT-OF-SCOPE, disclosed). Re-flag.
8. **[MAJOR] Route 4 not a minimal-ECH channel; ALP/potential/coupling not derived; not an
   amplitude exclusion** → **DP1U-11** (abstract states R4 "NOT closed by amplitude mismatch
   but by explanatory-deficit / CC fine-tuning" L1195-1198; ALP imported, disclosed). Re-flag.
9. **[MAJOR] Sec.X transparency = standard classical result, not a constraint on R1–R4;
   Table III converts scope-exclusions to constraints** → **DP1U-12 + DP1U-13** (labeled
   "standard on-shell equivalence", narrow solid-positive-core scope; B8-subsumption
   disclosed). Re-flag.
10. **[MAJOR] −35/16 nor erasure established; companion still titled −35/8; N_coh~O(few)
    asserted without transfer matrix** → **DP1U-17 + DP1U-14** (−35/16 quadruple-certified
    in the P2 companion; erasure = disclosed scaffolding, matter-bounce-erasure caveat).
    Re-flag.
11. **[MAJOR] no unified cosmological model; combines LQC/EC-Holst/matter-contraction/BH-
    origin/inflation/ALP without common action or junction conditions** → **DP1U-14** (bounce-
    junction matching explicitly "outside the scope" L4200; no-coherent-single-action
    disclosed). Re-flag.
12. **[MAJOR] Appendices F–H / Figs 3–11 don't validate; stock-CAMB, ALP posterior
    re-expresses its own datum, NaMaster synthetic; Fig 4 assumed cross-correlation; Fig 5
    fine-tuning scores unsupported** → **DP1U-15 + DP1U-24** (each appendix labeled
    stock-CAMB proxy / synthetic-sky / import, "not an ECH test"; Fig ρ curves labeled
    ASSUMED cross-correlation in-caption). Re-flag.
13. **[MINOR] repetitive; R3 derived-vs-Tier-III, 13-vs-14 catalog, N_tot 92-vs-94,
    companion-dependent-vs-non-load-bearing inconsistencies** → **DP1U-22 + DP1U-13 +
    DP1U-08** (length/style OPINION; catalog independence + N_tot spread disclosed
    bookkeeping). Re-flag.

ChatGPT §(3) closing concedes the classical Holst-decoupling core is supported — disputes
the four-route/basis-complete closure, which is the paper's own honestly-scoped channel-level
claim. Structural harsh-referee floor (directive-H, DP1U-21 disclosure-backfire).

## DAS cross-check (per M22-P3 DP3-21 pattern)
Grep of both M23 P1U raws for data-availability / DAS / released / self-contradiction /
reproducibility: NO Data-Availability internal self-contradiction of the M22-P3 class was
flagged. ChatGPT #12's appendix-provenance critique is the standing DP1U-15 "appendices
don't test ECH" (disclosed in-caption), NOT a DAS-vs-body self-contradiction. Cleared.

## Integrity
No ACCEPT faked; every finding dispositioned to a source-cited D-id; no math fabricated;
no hedging removed; no bump (0 genuinely-new); directive_g.sh NOT run (no edit).
Verdicts recorded as-is (Grok major-revisions, ChatGPT reject) via post_verdict.sh.
