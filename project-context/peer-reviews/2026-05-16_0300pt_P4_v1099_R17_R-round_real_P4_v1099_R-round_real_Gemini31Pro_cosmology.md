# P4_v1099 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0300pt_P4_v1099_R17_R-round_real
**Wall time**: 38.3s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=83503, completion=4746, reasoning=3815, total=88249

---

## PAPER-GEM-B1: Contradictory Parity-Violation vs Isotropy-Breaking Language (BLOCKER)
**Location:** Abstract (L124) and Section VI.G Conclusions (L1861)
**Issue:** The v1.0.99 sweep correctly established that the $\ell=1$ dipole is parity-EVEN (an isotropy-breaking axial-vector) and the monopole is parity-ODD. However, the text still explicitly claims "The parity-violation observable is the dipole, not the monopole" (Abstract) and "The parity-violation hypothesis is therefore tested by the dipole bound, not the monopole offset" (Conclusions). This is a direct physics contradiction within the text.
**Fix:** Change to "The isotropy-breaking observable is the dipole, not the monopole" and "The isotropy-breaking hypothesis is therefore tested by the dipole bound...".

## PAPER-GEM-M1: Stale `paper4-v1.0.98` Release Tags (MAJOR)
**Location:** Footnote 2 (L274) and Section VII Data Availability (L1983)
**Issue:** The prompt explicitly requires checking for propagation-tail stale tags. Two URLs/references still point to the `paper4-v1.0.98` release tag instead of the current `paper4-v1.0.99`.
**Fix:** Update `\url{https://github.com/Hubify-Projects/bigbounce/releases/tag/paper4-v1.0.98}` and the text `immutable release tag \texttt{paper4-v1.0.98}` to `v1.0.99`.

## PAPER-GEM-M2: Stale $f_{\rm sky} = 0.494$ Values (MAJOR)
**Location:** Table I (L361-363) and Section VIII NaMaster Config (L1951)
**Issue:** The global $f_{\rm sky}$ drift from 0.494 to 0.49005 was not fully propagated. Table I lists $f_{\rm sky} = 0.494$ for rows (iii), (iv), and (v). Section VIII lists `canonical-$N$ mask ($f_{\rm sky}=0.494$, ...`.
**Fix:** Update all instances of `0.494` in Table I and Section VIII to `0.49005`.

## PAPER-GEM-m1: Unresolved $f_{\rm sky} = 0.491$ Values (minor)
**Location:** Section IV.C (L862, L881), Table III caption (L901), Table VII (L1804)
**Issue:** While the prompt flagged 0.4938/0.494, there are several lingering instances of $f_{\rm sky} = 0.491$ associated with the canonical mask/production binning. If the canonical mask $f_{\rm sky}$ is strictly 0.49005, these 0.491 values are also stale artifacts.
**Fix:** Update `0.491` to `0.49005` where referring to the canonical mask, or explicitly define why the 0.491 mask differs from the 0.49005 mask.

## PAPER-GEM-m2: Redundant Phrasing in Abstract (minor)
**Location:** Abstract (L161)
**Issue:** The text reads "...and an empirical injection-recovery empirical 50\%-recovery-$3\sigma$ threshold...". The words "empirical" and "recovery" are redundantly stacked.
**Fix:** Simplify to "...and an empirical 50\%-recovery-$3\sigma$ threshold...".

## PAPER-GEM-N1: Punctuation/Capitalization Boundary (nit)
**Location:** Section VI.H (L1656)
**Issue:** The sentence boundary after the parenthetical is awkward: "...insensitive to that bias); if the tidal field...". 
**Fix:** Change the semicolon to a period and capitalize: "...insensitive to that bias). If the tidal field...".
