# R54 P1A — Truth Audit (convergence-confirmation round)

**Paper:** P1A — `arxiv/paper1a_ech_nogo.tex` (v1A.0.79)
**PDF:** `/tmp/R54_P1A/paper1a_ech_nogo.pdf` md5=439212bf, 29pp
**Round purpose:** Convergence test after R52+R53+EXT21/22/23 (P1A EXT23 ChatGPT=ACCEPT).
**Method:** Verdict-first vs source; patterns 061/062/063/064 + June-2026 calibration.

## Vendor legs
| Vendor | Status | Verdict | Net |
|--------|--------|---------|-----|
| Anthropic (Claude) | FAILED — no file produced | — | leg missing |
| Perplexity | FAILED — 401 quota (expected, quota-dead) | — | leg missing |
| Grok (grok-4.3, rasterized) | returned | MAJOR REVISIONS | harsh-outlier (pattern-064) |
| Gemini (2.5-pro) | returned | MAJOR REVISIONS | calibrated-handled |
| OpenAI (gpt-5, reasoning=high) | returned | REJECT | rigorous; 1 genuine item |

## Verdict table

### OpenAI (gpt-5) — the rigorous leg
gpt-5 independently RE-DERIVED the paper's arithmetic and CONFIRMED it:
Eq.7 (α/M)MPl≈3e-3 OK; Eq.9 ρcrit/ρPl OK; Eq.11 prefactor 0.032 OK; Eq.17
ρθ≈1.6e-10 eV⁴≈6ρΛ OK; EB diff 1.06σ OK; LiteBIRD 0.73σ OK; γPTA 1.13σ OK.
Pass-2: "NO FURTHER ARITHMETIC DISCREPANCIES."

| ID | Verdict | Basis |
|----|---------|-------|
| **E-M1** ρΛ benchmark mismatch (NJL leg uses (10⁻³ eV)⁴, rest uses (2.3 meV)⁴) | **VERIFIED — CLOSED** | Real internal inconsistency. Consistent benchmark → 1.4e-70 ρΛ (~70 orders). Fixed at L1664-65, synced ~69→~70 at L1680/2030/2702. pattern-036-safe (number from in-body canonical ρΛ). |
| E1 companion non-public | OPINION/calibrated | HOUSTON-DECISION companion-placeholder; L986-994 states none enter closure proof |
| E2 Zenodo/DOI not archival | calibrated | HD-4/HD-11; DOI at submission, L3001-02 |
| E3 Route-2 not controlled deriv | STALE | already "amplitude-budget bound, not derived... exploratory, not load-bearing" L1746/1789 |
| E4 dim-1 op load-bearing | STALE | extensively ansatz-caveated; N_tot demoted 92±2 OOM L3134 |
| E5 Table IV MCMC posteriors | calibrated | rows †-marked "not peer-reviewable" L3043 |
| E6/E7 fig/abstract companion #s | OPINION | figures already "in preparation"-labeled |
| E8 "13 independent" no DAG proof | OPINION/STALE | catalog explicitly historical; B8⊂B14 explained; raised+ruled prior rounds |
| E9 "§VI8" broken xref | FALSIFIED | rasterization of "§VI"+footnote-8 marker; companion §VI ref deliberate |
| E10 Eq.1 T² as fundamental | STALE | footnote L1020-34 explicitly "on-shell Hehl-Datta shorthand, not varied"; closed R29/R27conf |
| M2 Route-2 scheme ref | STALE | already labeled upper-bound ansatz, γ5-scheme caveat present |
| M3 Fig5 fine-tuning undef | OPINION | bar-chart definition request; numbers illustrative |
| M4 thermal washout qualitative | STALE | conditional Γ>H already explicit L1395/1422-27 |
| M6 Route-3 RG ad hoc | STALE | "upper-bound EFT ansatz, not verbatim"; Benedetti-Speziale cited L1820-25 |
| M7 Fig5-top RG running | OPINION | figure-method detail |
| M8 Barrier-3 "precisely at bounce density" | OPINION/minor | one-line barrier summary; rigorous version in Sec X |
| M9 >100 OOM spin | OPINION/STALE | longstanding qualitative claim |
| M10 ~50 e-fold rotation | OPINION | labeled, separate from N_tot L1194-98 |
| M11 ϑNY dimension | STALE | mass-dim+1 stated, parity footnote present |
| M12 App-B equivalence | STALE | "agree at OOM... phenomenological assignment" L1597-1608/3098 |
| m7 1.06σ lacks "not comparable" | FALSIFIED | 1.06σ is a two-angle CONSISTENCY check (directly comparable), not different-null significances |
| m8 ζ-cubic Holst=0 | STALE | pointwise Bianchi-zero at T=0 ⇒ zero in any action; L2528-31 |
| typography (Domagała, R̃, km/s/Mpc) | NIT | ł renders correct; style |

### Grok (harsh-outlier, pattern-064 — each reason audited)
| ID | Verdict | Basis |
|----|---------|-------|
| E1 abstract overstates / remove "channel-level closure" | OPINION/STALE | abstract L719-730 ALREADY "channel-level assessment, not operator-level theorem... conditional on ansatz" |
| E2 fNL in abstract | STALE | abstract L767-796 extensively qualifies "not predictions of ECH itself... not a distinctive ECH prediction" |
| E3 companion not self-contained | OPINION/calibrated | = OpenAI-E1 |
| E4 2.6-5σ comparability | STALE | "not directly comparable" already at abstract L784, figs |
| E5 transparency restriction | STALE | abstract L739 "for canonical scalar matter... excluding [sectors]" |
| M1 length ≤18pp | OPINION | editorial |
| M2 Fig5 10^120 conv-inconsistent | FALSIFIED | source L2168 says **10^122** + "unreduced M_Pl convention throughout"; Grok read stale value, both claims false |
| M3 "no explicit numbers in Sec IV" | FALSIFIED | Sec IV gives 4e-69/4e-81, 10⁻⁶⁰, 10⁻⁶³, 6ρΛ, 22-36 OOM explicitly |
| M4 ρ=0,0.3,0.5 unjustified | STALE | Fig7/8 captions label ρ assumed/illustrative |
| m1 PACS "04." truncated | FALSIFIED | source L802 = `04.50.Kd` complete; rasterization misread |
| m3 Eq(2) no scheme | STALE | already γ_{SU(2)} subscript + scheme spread text |

### Gemini (calibrated-handled)
| ID | Verdict | Basis |
|----|---------|-------|
| E1 "June 19 2026" future date | FALSIFIED | calibration: today=2026-06-26; date is current, not future |
| E2 companion not self-contained | OPINION/calibrated | = OpenAI-E1 |
| M1 (Treh/MGUT)^3/2 aesthetic | STALE | already labeled aesthetic; N_tot demoted 92±2 OOM; tension survives OOM L2674-90 |
| M2 length | OPINION | editorial |
| M3 emphasize conditional more | STALE | abstract L726-30 already "all R4... conditional on this ansatz" (Gemini concedes "which is good") |
| m1 add caveat to §XV | FALSIFIED/STALE | §XV pt2 discusses 0.27 vs 0.342 only; no 3.6/2.9 juxtaposition there |
| m2 quote 2.6σ headline | OPINION | range deliberately disclosed w/ footnote |
| m3 Fig3 param justify | calibrated | EXT7-disclosed spin-torsion benchmark; labeled illustrative |
| N1/N2 phrasing | NIT | cosmetic |

## Closure
**NEW VERIFIED closed: 1** (E-M1, MINOR, internal-consistency).
- `arxiv/paper1a_ech_nogo.tex` L1664-65: `4×10⁻⁶⁹ ρΛ for ρΛ~(10⁻³ eV)⁴` → `1.4×10⁻⁷⁰ ρΛ for the canonical ρΛ≈(2.3 meV)⁴≈2.8×10⁻¹¹ eV⁴ used throughout this paper`
- L1680, L2030, L2702: `~69 orders` → `~70 orders` (claims-sync)

Recompile ×3 exit 0; **0 undef refs; 0 overfull hboxes**.

## Convergence statement
All cross-vendor BLOCKER/MAJOR items FALSIFIED / STALE / OPINION / calibrated
except the single ρΛ-benchmark MINOR (now closed). gpt-5's independent
arithmetic audit confirms every quantitative claim in the paper. Grok =
harsh-outlier (PACS + Fig5 rasterization misreads, "no numbers" false).
Gemini = calibrated (future-date FALSIFIED; rest already-disclosed). Anthropic +
Perplexity legs failed (no file / quota).

**P1A CONVERGED — 1 NEW VERIFIED MINOR closed (ρΛ-benchmark consistency); 0 residual real items.**
