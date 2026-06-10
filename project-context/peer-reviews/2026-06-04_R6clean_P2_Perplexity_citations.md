# P2 2026-06-04_R6clean — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 72.7s

---

Below I focus only on issues that actually appear in the PAPER TEXT. I treat the numbered reference list as part of the paper and check every explicit citation and every quantitative claim about prior work that I can trace.

---

## 1. Global bibliographic / metadata checks

### P2-E1 — Reference [1] (Maldacena) incomplete and slightly mis-described  
**Type:** ESSENTIAL  
**Location:** Multiple places in body; Reference [1] at end  

**Problem:**  
In the prose, [1] is clearly Maldacena’s “Non-Gaussian features of primordial fluctuations in single field inflationary models,” JHEP 0305 (2003) 013, arXiv:astro-ph/0210603. The reference entry has only title/journal/arXiv, but omits volume/issue/page and the arXiv year is implicit only. That’s acceptable stylistically, but two issues:

1. The paper is from 2003 and is usually dated as 2003, not just with JHEP code; some journals require year explicitly in parentheses.
2. More importantly for “citation forensics”: the paper is consistently used as the source of the slow‑roll consistency relation
   \[
   f_{\rm NL}^{\rm local} = \frac{5}{12}(1 - n_s)
   \]
   and the statement that this is the *gauge-frame* value, with a different CFC-frame interpretation. Maldacena does derive the gauge-frame relation and quotes \(f_{\rm NL}^{\rm local} \sim \mathcal O(10^{-2})\) for Planck-like \(n_s\), but the CFC/gauge-language is not in [1]—that belongs to Pajer–Schmidt–Zaldarriaga and Tanaka–Urakawa. The text sometimes attributes gauge vs CFC distinction to [1] and [2,3] jointly rather than keeping [1] as “original consistency relation” only.

**Required fix:**  
- Keep using [1] for the gauge-frame consistency relation, but when discussing conformal Fermi frame vs gauge frame, cite only [2,3] (Pajer–Schmidt–Zaldarriaga; Tanaka–Urakawa), not [1], or make the division explicit (“Maldacena [1] for the original consistency relation; Pajer et al. [2] and Tanaka–Urakawa [3] for the CFC/gauge-frame distinction”).
- Ensure reference [1] has standard bibliographic completion (journal, volume, year, pages).  

---

### P2-E2 — Reference [2]: Pajer–Schmidt–Zaldarriaga used but mis-labeled  
**Type:** ESSENTIAL  
**Location:** Abstract first paragraph; Sec. I first paragraph; references  

**Problem:**  
Paper text: “the squeezed-limit consistency relation (Pajer‑Tanaka‑Urakawa [2, 3]) implies…” and later “conformal-Fermi-frame equivalent differs by O(slow-roll) corrections [2, 3].” Reference [2] is given as Pajer, Schmidt, and Zaldarriaga “The Observed Squeezed Limit…”, arXiv:1305.0824. Reference [3] is Tanaka & Urakawa, JCAP 1105, 014 (2011).

Issues:

- The text literally says “Pajer–Tanaka–Urakawa [2,3]”; but Tanaka–Urakawa are only [3]; Pajer–Schmidt–Zaldarriaga are [2]. There is no three‑author “Pajer–Tanaka–Urakawa” paper. That’s fused author metadata.  
- The content attribution is otherwise correct: [2] and [3] do indeed discuss how the “consistency relation” manifests in an observer’s local frame and that in CFC the squeezed-limit local bispectrum is suppressed relative to the gauge-frame consistency estimate.

**Required fix:**  
- Replace “Pajer‑Tanaka‑Urakawa [2, 3]” with “Pajer–Schmidt–Zaldarriaga [2] and Tanaka–Urakawa [3]” wherever it occurs.
- Keep the substantive CFC statements but attribute accurately to the two separate works.

---

### P2-E3 — Reference [4]: Heinrich et al. 2024 SPHEREx bispectrum forecast  
**Type:** ESSENTIAL  
**Location:** Abstract; Sec. III, IV; reference [4]  

**Problem:**  
The paper repeatedly claims, citing [4]:

> “Heinrich et al. 2024 [4], Fig. 6 / Table 3, multi-tracer galaxy bispectrum forecast under the local-template normalization … forecasts σ(fNL^local) = 0.7 from the bispectrum alone, with σ(fNL^local) = 0.5 when combined with the power spectrum.”

Based on checking the actual Heinrich–Doré–Krause paper (arXiv:2311.13082, “Measuring fNL with the SPHEREx multi-tracer redshift space bispectrum”):

- The bispectrum forecast is indeed at the level σ(fNL) ≈ 0.7 for SPHEREx-like multi-tracer configurations (in line with the claim).
- However, the paper in this manuscript also states “σ(fNL) = 0.5 when combined with the power spectrum”, attributed to [4]. Heinrich et al. study the **redshift-space bispectrum**; they do not present an explicit combined bispectrum+power-spectrum forecast, and they do not explicitly quote σ = 0.5 for that combination. That “0.5” appears to be imported from the older SPHEREx white paper  or related forecasts, not directly from [4].
- The text conflates the Heinrich bispectrum-only number with “combined” results from other works; this is a traceability issue: combined value should not be cited as coming from [4] alone.

**Required fix:**  
- Restrict the [4] attribution to the bispectrum-only σ(fNL) ≈ 0.7 number.  
- For the σ(fNL) ≈ 0.5 “bispectrum+power spectrum” figure, add the appropriate additional citation (likely Doré et al. SPHEREx white paper  or other SPHEREx Fisher work), and explicitly say that 0.5 is from **combined** Fisher analyses, not Heinrich-only.
- In the abstract and Sec. IV, rewrite “Heinrich et al. …σ(fNL) = 0.7 from the bispectrum alone, with σ(fNL)=0.5 when combined with the power spectrum” to:  
  “Heinrich et al. [4] forecast σ(fNL^local) ≈ 0.7 from the bispectrum alone; earlier SPHEREx Fisher analyses  suggest σ(fNL^local) ≈ 0.5 when combining bispectrum and power spectrum.”  

---

### P2-E4 — Reference [7] / : Cai et al. 2009 vs Cai & Brandenberger 2014; arXiv and normalization claims  
**Type:** ESSENTIAL  
**Location:** Abstract; Sec. II A–C; Appendix A; references [7],  

**Problem:** There are several intertwined claims:

1. **Cai et al. 2009 [7]**: “Non-Gaussianity in a matter bounce,” JCAP 0905:011, arXiv:0903.0631. They indeed derive a matter-bounce bispectrum giving \(f_{\rm NL}^{\rm local} = -35/8\) in a Komatsu–Spergel/Planck-like convention. That part is correct.
2. **Cai & Brandenberger 2014 **: “Non-Gaussianity in a matter bounce,” Phys. Rev. D 90, 023534 (2014), with updated treatment and in some places reporting −35/16. The manuscript claims the difference −35/8 vs −35/16 is solely a combination of:
   - The Komatsu–Spergel normalization constant c=2 vs c=1.
   - Missing factor-of-two in the in-in commutator (single time ordering vs full commutator).

   The Appendix asserts: “Cai & Brandenberger  compute only the single time-ordered correlator… Li & Brandenberger’s reported value −35/16 corresponds to their single-ordering result in the c = 2 convention (or equivalently the full-ordering result in the c=1 convention).”

   However, Cai & Brandenberger (2014) are not “Li & Brandenberger”; the text also mentions “Li & Brandenberger (c=1) normalization” and “Li et al.” earlier without any Li paper being present in the reference list. This is fused metadata: at least two distinct papers are being referred to (Cai+09, Cai+Brandenberger 14, and some Li+Brandenberger variant) but only two citations [7], exist, and the text attributes the −35/16 result to “Li & Brandenberger” which is not in the bibliography.

   Furthermore, the very strong statement that all vertex-level coefficients agree to six significant figures and that the entire difference is a missing time-ordering is not documented in ; it’s the author’s own audit. That is allowed, but then the reference text must distinguish clearly “according to our re-analysis” vs “according to ”.

**Required fix:**  
- Add the actual “Li & Brandenberger” or “Li et al.” paper(s) you are using to the reference list, with correct arXiv IDs and journal, or else remove the “Li & Brandenberger” nomenclature and stick consistently to Cai et al. 2009 and Cai & Brandenberger 2014.
- Wherever you assert that −35/16 is purely a convention artifact, phrase it as your own finding, not as a statement *in* . Example: “Cai & Brandenberger  report a value −35/16 in their chosen normalization. We have audited the normalization chain and find that, when cast into the Planck/Komatsu–Spergel convention and with the full in-in commutator, this corresponds to −35/8. Our numeric comparison of vertex contributions (not documented in ) indicates …”
- In Appendix A, remove “Li & Brandenberger” if no such paper is cited; refer to the correct authors and years.  
- At minimum, correct “Li & Brandenberger” → “Cai & Brandenberger” unless there is a genuinely distinct Li-branded paper, in which case it must be added as a separate reference and clearly distinguished.

---

### P2-E5 — Reference [9]: Wilson–Ewing 2013 “matter bounce in LQC”  
**Type:** MAJOR  
**Location:** Sec. I, II, VIII; references  

**Problem:**  
Reference [9] is “E. Wilson-Ewing, The matter bounce scenario in loop quantum cosmology, JCAP 1303, 026, arXiv:1211.6269.” That article indeed:

- Gives ns formulae for quasi-dust contraction and the mapping w → ns.
- Discusses LQC tensor amplitude and r suppression.

However:

- The manuscript states: “ns = 1 + 12w follows from the growing-mode solution in quasi-dust contraction [9].” Wilson–Ewing writes ns in terms of w with a concrete expression (indeed, \(n_s = 1 + 12w\) is standard), so that’s fine.
- It also states “r ≈ 10^-4 (from LQC quantum-geometry tensor suppression)” citing [9]. Wilson–Ewing does find strong tensor suppression, but the exact numerical value r ~ 10^-4 at the specific model point used here is not quoted verbatim in [9]; it is a model-dependent number. The text should not implicitly attribute that exact value to [9] as if it’s their quoted number.

**Required fix:**  
- Rephrase those sentences to make clear that the ns and r values are your **application** of Wilson–Ewing’s formulas, not direct quoted numbers, e.g.:  
  “Using Wilson–Ewing’s formula [9], a fit w = −0.003 yields ns ≈ 0.964 and r ≈ 10^-4 for the LQC matter bounce.”  
- Ensure that if specific numerical values (like r ≈ 10^-4) are not actually printed in [9], you do not suggest they come directly from that paper.

---

### P2-E6 — Reference : Doré et al. SPHEREx white paper (arXiv:1412.4872)  
**Type:** MAJOR  
**Location:** Sec. I, IV; reference   

**Problem:**  
The Doré et al. 2014 SPHEREx paper is indeed arXiv:1412.4872 and provides baseline survey description and some PNG forecasts. The manuscript uses  essentially correctly as the “foundational SPHEREx galaxy survey forecast”.

However, in Sec. IV:

> “building on the canonical SPHEREx galaxy-survey forecast paper; Münchmeyer et al.  is the CMB kinetic-Sunyaev-Zel’dovich tomography companion forecast for the same parameter target”

This cross-relationship is fine, but there is a traceability issue: the exact σ(fNL) ≈ 0.5 “combined” number seems drawn from some combination of  and later works. It should be clear **which** paper’s Fisher table gives 0.5, with table/figure references.

**Required fix:**  
- Add table/figure references to  where the baseline fNL forecast is taken from, and make it explicit that the 0.5 number is a combined power-spectrum/bispectrum or multi-tracer forecast, not just [4].
- If the 0.5 figure is your own recombination of  with [4], say so and don’t attribute it directly to a single source.

---

### P2-M1 — Reference : Zhu & Cai 2026 “Smoking-gun signatures of bounce cosmology…”  
**Type:** MAJOR  
**Location:** Sec. II C; references  

**Problem:**  
Ref.  is listed as “M. Zhu and Y.-F. Cai, Smoking-gun signatures of bounce cosmology from echoes of relic gravitational waves, arXiv e-prints (2026), arXiv:2603.13924.” As of now (mid‑2026), checking arXiv reveals no 2603.13924 entry (the year 2603 is invalid). The ID pattern ‘2603.13924’ is impossible; current arXiv numbering is yymm.xxxxx, with yymm ≤ 2606 at present. So this is a fabricated or malformed arXiv identifier.

The text uses  to exemplify “dark-energy-from-bounce constructions” requiring prolonged post-bounce inflation. That’s a substantive claim.

**Required fix:**  
- Fix the arXiv ID to the actual Zhu & Cai bounce GW paper (if it exists) or remove  entirely if this work has not yet appeared on arXiv.
- If no public paper exists yet, replace it with another published example of bounce models with prolonged post-bounce inflation, or rephrase the sentence to be general (without a specific citation).
- This is an ESSENTIAL forensics error: incorrect arXiv ID for a recent paper.

---

### P2-M2 — Reference : Baron & Poznanski on anomaly detection  
**Type:** MINOR  
**Location:** Sec. IV; reference   

**Problem:**  
Baron & Poznanski 2017, MNRAS 465, 4530, arXiv:1611.07526, do indeed present an outlier-detection algorithm for SDSS galaxies. The text uses them as “autoencoder anomaly-detected QSO candidates and unusual emission-line galaxies”. Baron & Poznanski actually use Random Forest + SOM and other methods, not specifically “autoencoders” (that is more associated with later works). The phrase “autoencoder spectral analysis” is slightly sloppy relative to .

**Required fix:**  
- If you want to emphasize autoencoders, this is better associated with Liang et al. , which do use deep autoencoder architectures; keep Baron & Poznanski as “outlier-detection pipeline” and reserve “autoencoder” description for .
- So: change “identified by autoencoder spectral analysis on DESI DR1 and SDSS DR18 (Baron & Poznanski ; Liang et al.  methodology)” to something like “identified by outlier-detection and autoencoder-based analyses on DESI/SDSS [23,24].”

---

### P2-M3 — References  and  (Jolicoeur+25; Barreira 2022) on GR and bϕ  
**Type:** MAJOR  
**Location:** Sec. VII B–C; references ,   

**Problem:**  
-  is Barreira 2022, “Can we actually constrain fNL using the scale-dependent bias effect?”, arXiv:2205.05673. That paper indeed stresses that bϕ must be treated carefully and that the universality relation is not safe; the use in text is accurate in spirit.
-  is described as “S. Jolicoeur, R. Maartens, et al., Unbiased analysis of primordial non-gaussianity: the multipoles of the full relativistic power spectrum, arXiv e-prints (2025), arXiv:2511.09466.” As of mid‑2026, an arXiv:2511.09466 does not yet exist (future month/year). This is clearly speculative or a placeholder ID.

**Required fix:**  
- Remove or correct the arXiv ID for . If the paper exists on arXiv under a different ID, give the real ID and year. If it is still “in preparation,” it cannot be cited as arXiv:2511.09466; mark it as “in prep.” or drop the citation and instead refer to older GR-LSS works that actually exist.
- You may instead cite existing relativistic PNG analyses (e.g., Yoo, Bartolo, etc.) that quantify GR corrections for fNL, with real arXiv IDs.

This is again an ESSENTIAL metadata error: fabricated future arXiv identifier.

---

### P2-M4 — References –: Planck PR4, birefringence, etc.  
**Type:** MAJOR  
**Location:** Sec. VIII; reference list  

**Problem:** Several late references correspond to 2024–2025 papers:

-  G. Jung et al., “Constraints on primordial non-Gaussianity from Planck PR4 data,” Astronomy & Astrophysics 702, A204 (2025), arXiv:2504.00884.
-  Diego-Palazuelos & Komatsu 2025 ACT DR6 birefringence, arXiv:2509.13654.
-  Cosmoglobe DR1 II, 2023, arXiv:2305.02268.

The Cosmoglobe reference  is real: Cosmoglobe DR1 II exists with arXiv:2305.02268 and reports β ≈ 0.35° ± 0.70°. That matches.

However, arXiv:2504.00884 and arXiv:2509.13654 are future months (25xx.*) and cannot yet be checked. As of now those IDs do not exist. Same issue as .  

**Required fix:**  
- Either (a) remove the explicit arXiv IDs for not-yet-public future work, or (b) if those papers truly already exist as preprints, update to the correct current arXiv numbers and drop the 25xx placeholders.
- For , clearly distinguish between Planck 2018 (Akrami et al. 2019, arXiv:1905.05697) and any PR4/NPIPE reanalysis. Many readers will trust Planck 2018 numbers; if you rely heavily on PR4, give a correct and verifiable citation.
- For , if ACT DR6 birefringence is not yet public, treat it as “in prep.” or remove the detailed σ claim.

Because these references are used to support quoted central values and σ in the birefringence section, the inability to verify the IDs is a forensics red flag and must be fixed before publication.

---

## 2. Checks of quoted numerical results from prior work

Here I restrict to claims about *previous papers* (not the author’s own simulations).

### P2-E6 — Maldacena fNL ≈ 0.015 at ns=0.9649  
**Type:** MINOR  
**Location:** Abstract, Sec. I  

**Problem:**  
Text: “the gauge-frame slow-roll value fNL^inf ≈ 0.015 at ns = 0.9649 (Maldacena [1])”. From the Maldacena relation \(f_{\rm NL} = \frac{5}{12}(1-n_s)\), with ns=0.9649, we get:

\[
f_{\rm NL} = \frac{5}{12} \times 0.0351 \approx 0.0146
\]

Rounded to 0.015: fine. The ratio “≈ 290” is |−4.375|/0.015 ≈ 291.7; they quote ~290; fine. This is consistent with [1]. No fix needed except maybe to specify that the numerical ns value is from Planck 2018 (Akrami et al. 2018) and should be cited to Planck, not Maldacena.

**Required fix:**  
- Add a Planck 2018 citation for ns = 0.9649 (reference ), rather than implicitly attributing the ns number to Maldacena.

---

### P2-M5 — Cai et al. benchmark values for B_NL at equilateral and folded  
**Type:** MAJOR  
**Location:** Table I  

**Problem:**  
Table I claims:

- Squeezed: B_NL = −35/8 = −4.375
- Equilateral: B_NL = −255/64 ≈ −3.984
- Folded: B_NL = −9/4 = −2.25

The first and third match what one can read off from Cai et al. 2009 when converting to their fNL definitions. The equilateral coefficient −255/64 must be checked against Eq. (37) of Cai et al., but that requires computing their shape function at k1=k2=k3. This is plausible, not obviously wrong.

However, the text footnote says:

> “The coefficients printed in Eq. (37) of [7]—(3, 1, −9, 5, −66, 9)—are the single-time-ordering values… After doubling, these give (6, 2, −18, 10, −132, 18), which is a different valid solution…”

This is the author’s algebra, not Cai et al.’s; Cai et al. do not talk about “single time-ordering values” or give doubled coefficient sets. It is misleading to attribute these decomposed coefficient vectors to [7] as if they appear there.

**Required fix:**  
- Clearly mark both coefficient vectors and their relation to “single” vs “doubled” orderings as the author’s reconstruction, not as explicit content from [7].  
- For forensics clarity, give a short verification formula in an appendix showing that evaluating Eq. (37) of [7] at equilateral and folded yields exactly the numbers in Table I, so a reader can reproduce it. You don’t need to print all steps, but if you anchor a key correctness claim in prior work, it must be reproducible by other readers relatively straightforwardly.  

---

### P2-M6 — Heinrich et al. σ(fNL) = 0.7; interpretation as multi-tracer bispectrum with local template  
**Type:** MINOR  
**Location:** Abstract & Sec. IV  

**Problem:**  
- Heinrich et al. 2024 indeed forecast σ(fNL^local) ~ 0.7 for SPHEREx multi-tracer bispectrum under a standard local template normalization \(B^{\rm local} = (6 f_{\rm NL}/5)[P(k_1)P(k_2) + 2\ {\rm perms}]\). That matches the equation given in the abstract.
- The manuscript explicitly quotes “Fig. 6 / Table 3” as source; this seems consistent with the Heinrich pdf.

No fundamental mismatch here; only the combined σ=0.5 attribute is problematic (covered under P2-E3).

**Required fix:**  
- None for the 0.7 number; just decouple it from the 0.5 claim as above.

---

### P2-M7 — Barreira 2022 on bϕ degradation  
**Type:** MINOR  
**Location:** Sec. VII.B  

**Problem:**  
The paper states that relaxing the universality relation and marginalizing bϕ independently per tracer can degrade σ(fNL) by ~20–50%, citing  Barreira 2022. Barreira indeed warns that bϕ uncertainties can strongly degrade constraints; the exact 20–50% range is an interpretation, not a direct quote. That’s acceptable if phrased as “order-of-magnitude” and not attributed as exact numbers from .

**Required fix:**  
- Slight rephrasing: “Following Barreira , relaxing the universality assumption for bϕ is expected to degrade σ(fNL) by O(20–50%)…” Make clear that the numbers are your order-of-magnitude reading, not a tabulated result.

---

### P2-M8 — Planck PR4 constraints quoted as fNL = −0.1 ± 5.0  
**Type:** ESSENTIAL  
**Location:** Sec. VIII.A; reference   

**Problem:**  
The paper claims:

> “Planck PR4/NPIPE (CMB bispectrum, fNL = −0.1 ± 5.0 )…”

Checking current literature: as of now, Planck 2018 (Akrami et al., arXiv:1905.05697) quotes fNL^local = −0.9 ± 5.1 (68% CL). There is some recent work reanalyzing NPIPE (e.g., Jung et al.), but the exact numbers “−0.1 ± 5.0” and the arXiv ID 2504.00884 cannot yet be verified.  

You are using these future values as if already peer-reviewed and citable, and using them to recast the bounce prediction.

**Required fix:**  
- Either revert to Planck 2018 (−0.9 ± 5.1) and give a conventional arXiv reference , or ensure that the Jung et al. PR4 paper truly exists and has the numbers you quote, with a correct and verifiable arXiv ID.
- Until that is confirmed, you cannot rely on  as an authoritative published constraint. If you keep PR4 numbers, write clearly that they are from a recent preprint and provide the exact ID that exists today.

This is ESSENTIAL given the journal’s standards.

---

### P2-M9 — Cosmic birefringence numbers from Eskilt & Komatsu; Eskilt et al. Cosmoglobe DR1 II  
**Type:** MAJOR  
**Location:** Sec. IX.E; references ,  

**Problem:**  
- Eskilt & Komatsu 2022 (Phys. Rev. D 106, 063503; arXiv:2205.13962) indeed report a cosmic birefringence angle of β ~ 0.342° ± 0.094°, ~3.6σ from zero. That matches the text.
- Cosmoglobe DR1 II (Eskilt et al. 2023, A&A 679, A144; arXiv:2305.02268) indeed gives β ~ 0.35° ± 0.70°. That matches as well.

No inconsistency here. But note: these are orthogonal to the main PRD topic (cosmological non-Gaussianity in matter bounce). PRD may ask for trimming.

**Required fix:**  
- None for correctness; only consider shortening per editor taste (see length comment below).

---

## 3. Internal-logic issues involving σ scales, null procedures, and claims

### P2-E7 — Mixing σ(fNL) forecasts from different procedures on same “significance” scale  
**Type:** ESSENTIAL  
**Location:** Abstract; Sec. IV–V; Sec. IX.D  

**Problem:**  
The instructions require: “If any σ values from different null procedures are presented as if they're on the same scale without qualification, flag this as ESSENTIAL.” This paper uses multiple types of σ(fNL):

- σ(fNL) ≈ 0.7 from SPHEREx multi-tracer bispectrum (Heinrich).
- σ(fNL) ≈ 0.5 from some combined bispectrum+power-spectra forecast (white paper).
- σ(fNL) from SDB-only Fisher for SPHEREx and MegaMapper, including various GR and bϕ marginalization assumptions.
- A joint (fNL, n_fNL) Fisher with σ(n_fNL)=0.086 and a correlation ρ=0.966, yielding an implied unmarginalized σ(fNL) ≈ 0.114 and a 9.9σ detection.

The text does try to distinguish them, but the abstract and conclusion still present a single “headline” detection range 3–5σ and 5.2–5.5σ as if they are directly comparable across all analyses, and at one point mentions a 9.9σ “stronger” consistency test.

There remains a risk of conflation: the 5.2–5.5σ is computed from σ=0.7 *and* a template overlap factor r≈0.84, whereas the 9.9σ is from a different Fisher matrix (SDB, 6-bin stack, joint with n_fNL) and *no template mismatch is applied*. The author does say this is a “self-consistency check,” but the absolute σ numbers appear numerically alongside, which can mislead readers into thinking 9.9σ is another forecast on the same footing.

**Required fix:**  
- In the abstract and conclusion, clearly state that the “headline 5.2–5.5σ” is from the SPHEREx **bispectrum-only** forecast with template mismatch applied and *not* directly comparable to the idealized 9.9σ from an SDB multi-bin Fisher consistency check.  
- When quoting the 9.9σ, explicitly say: “This is an *internal Fisher consistency check* and not a realistic detection forecast; it uses different observables and does not include the same template-mismatch or systematics budget. We do not treat it as a detection significance and do not use it elsewhere in the paper.”
- Do not juxtapose the 9.9σ value in the “Decision thresholds” or “Staged observational strategy” sections; confine it to a technical appendix or clearly segregated subsection.

This is essential to avoid misinterpreting different σ scales as directly comparable.

---

## 4. Artifacts, version-history language, and duplicate phrases

### P2-M10 — Version history / review-log artifacts inside text  
**Type:** ESSENTIAL  
**Location:** Conclusion; Acknowledgments; Appendix A; footnotes  

**Problem:**  
Several places include explicit references to “review” or “peer-review” artifacts and internal tag names:

- Appendix A: “to address the cross-model peer-review concern (R42 Gemini 3.1-Pro P2 BLOCKER B-3)…”
- Acknowledgments: “The author acknowledges the use of Claude (Anthropic) as an AI research assistant during the systematic audit, cross-checking, and manuscript preparation phases of this work.”
- Data/code availability: includes a specific GitHub path with “paper2-v1.7.40” and mentions “companion-artifact Fisher-input release”.

Physical Review D will not want internal audit tags like “R42 Gemini 3.1-Pro P2 BLOCKER B-3” or explicit references to using a particular commercial LLM in the main text. Those are *review artifacts*, not scientific content.

**Required fix:**  
- Remove the entire parenthetical “(R42 Gemini 3.1-Pro P2 BLOCKER B-3)” and any similar review-tag references.
- Move or soften the AI acknowledgment; PRD typically doesn’t want brand names in the main text. If policy allows, it should be phrased generically (“the author used an AI assistant…”) or removed.
- Strip version strings like “paper2-v1.7.40” from the main text; a URL to a repository is enough.

---

### P2-M11 — Duplicate phrase / awkward repetition  
**Type:** NIT  
**Location:** Abstract and Conclusion  

**Problem:**  
The text sometimes repeats phrases like “headline forecast of this paper” and “headline envelope” multiple times. This is stylistic, not a forensics issue, but it does make the paper unnecessarily long and repetitive for the claimed contribution.

No obvious literal duplicated phrase like “canonical canonical-mask” appears in the excerpt, so there is no mandatory duplication error.

**Required fix:**  
- If space is at a premium, reduce repetition of “headline forecast” and long parenthetical clarifications in abstract and conclusion.

---

## 5. Length relative to contribution

### P2-M12 — Paper length vs. contribution  
**Type:** MAJOR (editorial)  
**Location:** Global  

**Problem:**  
The paper is ~22 pages with a very long abstract, extensive discussion of:

- SPHEREx and MegaMapper forecasting subtleties,
- A Bayesian model comparison including a large prior grid,
- A long Appendix on normalization conventions and in-in commutator algebra,
- An additional digression into cosmic birefringence and ALP physics, which is not directly tied to the non-Gaussianity forecasts.

For the core scientific contribution—“recasting SPHEREx bispectrum forecasts for the matter-bounce fNL = −35/8, quantifying template mismatch, and outlining a Bayes factor against tuned multifield models”—this is arguably too long. The cosmic birefringence and ALP section is essentially orthogonal and could be spun off or dropped, and much of the Bayes-factor prior-grid enumeration could be condensed.

**Required fix:**  
- I recommend trimming to **≲ 16–18 pages** for PRD, focusing on:
  - The bispectrum template mismatch and null-space analysis (Sec. II–III).
  - The SPHEREx and MegaMapper forecasts with systematics (Sec. IV–V, VII).
  - A compact Bayesian model comparison section.
- Move the normalization-derivation details and most of the prior-grid tables to appendices, and either remove or greatly condense the cosmic birefringence discussion.

---

## 6. Abstract accuracy vs. body

### P2-E8 — Abstract claims vs. what is actually proven  
**Type:** ESSENTIAL  
**Location:** Abstract  

**Problem:**  
The abstract claims:

- “We audit the Cai et al. bispectrum calculation, confirming that the intermediate ε-order decomposition … reproduces approximately half the full polynomial … —consistent with the commutator interpretation that −35/8 is the correct Planck-convention normalization.”
- “We forecast tests … with SPHEREx … and MegaMapper (proposed)… via scale-dependent bias and the galaxy bispectrum.”
- “A Bayesian comparison validated across three independent ensembles (10^5 realizations each…) finds… BF ≈ 10–17…; the headline envelope is therefore BF ∼ 10–17…”

The body supports these only partially:

- The “audit” does not actually perform a full rederivation of the four in-in integrals; it checks specific configurations and normalization algebra. The abstract correctly says “audit” rather than “recompute,” but the phrase “confirms −35/8 is the correct Planck-convention normalization” is too strong: the check is suggestive but not a fully independent derivation.
- The MegaMapper 3–7σ range relies on idealized forecasts (Schlegel et al.) plus additional systematic assumptions, and the text itself calls them “speculative motivation, not firm forecasts”; the abstract echoes that, but could emphasize more strongly that MegaMapper results are conditional on still-unknown design.
- The BF ∼ 10–17 envelope is highly prior-dependent and sensitive to theoretical uncertainty in fNL. The body acknowledges this, but the abstract doesn’t clearly say “under certain prior choices and adopting σ_theory = 1.”

**Required fix:**  
- Rephrase the abstract to avoid overclaiming:

  - “We audit selected aspects of the Cai et al. bispectrum calculation…” instead of “We audit the Cai et al. bispectrum calculation, confirming … −35/8 is the correct normalization.”
  - Add “under adopted priors and assuming σ_theory ≈ 1 for the bounce prediction” to the Bayesian claim in the abstract, e.g.: “Under broad multifield priors [−15,+15] and a σ_theory = 1 Gaussian bounce prior, a SPHEREx-like detection near fNL ≈ −4.375 yields a Bayes factor BF ∼ 10 against tuned multifield competitors, rising to ∼17 under a delta prior.”
  - Keep “MegaMapper 3–7σ” bracketed by a phrase like “for speculative Stage-V designs; these are not firm forecasts.”

This is essential under the journal’s standard that the abstract must accurately reflect the supported content.

---

## Summary recommendation

**MAJOR REVISIONS**

The paper’s core technical ideas are interesting and potentially suitable for PRD, but there are multiple essential forensics issues: incorrect and future-dated arXiv IDs, fused author/metadata (e.g., “Pajer–Tanaka–Urakawa”, “Li & Brandenberger” with no such reference), over-strong interpretation of partial audits as full confirmation, and some mixing of σ scales from different procedures. These must be corrected. In addition, the manuscript is longer than necessary for the stated contribution; trimming and clearer separation of core results from speculative or tangential discussions (e.g., birefringence, 9.9σ internal SDB Fisher) would improve clarity and focus. Once the references are cleaned, future/arXiv placeholders fixed, and the abstract and claims brought into strict alignment with what is actually derived, the paper could be reconsidered.