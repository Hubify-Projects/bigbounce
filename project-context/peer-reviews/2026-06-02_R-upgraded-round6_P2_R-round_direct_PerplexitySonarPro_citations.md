# P2 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round6
**Wall time**: 15.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=34690, completion=1404, total=36094, search_context_size=low, cost={'input_tokens_cost': 0.10407, 'output_tokens_cost': 0.02106, 'request_cost': 0.006, 'total_cost': 0.13113}

---

## PAPER-PER-B1 — Mis-cited Zhu & Cai 2026 “echoes” paper

- **Location:** Assumptions §2.3, line with “Zhu~\&~Cai~\cite{Zhu:2026echoes}”
- **Issue:** Bibkey `Zhu:2026echoes` is asserted (in comments) to correspond to arXiv:2603.13924, PRD 109 123511, describing a bounce model with prolonged post-bounce inflation. No such paper exists as of 2026; arXiv:2603.13924 is unrelated (different authors/topic), and there is no Zhu & Cai 2026 “echoes” bounce paper in INSPIRE/ADS/arXiv matching the description.[1][2]
- **Fix:** Replace `Zhu:2026echoes` with a real published example of bounce+inflation models (with correct arXiv ID, title, and venue), or clearly flag it as a hypothetical / in-prep work and remove fake arXiv/DOI details from comments and bibliography.

---

## PAPER-PER-B2 — Mis-cited Jung 2025 Planck PR4 fNL result

- **Location:** §\ref{sec:currentdata}, “Planck PR4/NPIPE (CMB bispectrum, $\fnl = -0.1 \pm 5.0$~\cite{Jung2025PlanckPR4fNL})”
- **Issue:** There is no Jung et al. 2025 Planck PR4/NPIPE local-\(f_{\rm NL}\) paper with that title or result; Planck PR4 NPIPE local-\(f_{\rm NL}\) constraints post-2019 are by other collaborations and with different central values/uncertainties.[3][4] The combination of author “Jung”, “Planck PR4 fNL”, year 2025, and the quoted numbers appears to be fused/LLM-generated metadata.
- **Fix:** Replace with an actually published Planck PR4/NPIPE local-\(f_{\rm NL}\) reference (correct authors, title, year, and numbers), or, if using an in-prep/private result, label it explicitly as such and remove invented bibliographic details.

---

## PAPER-PER-M1 — Eskilt & Komatsu birefringence citation / numbers

- **Location:** Discussion §\ref{sec:discussion}, paragraph starting “An independent observable—cosmic birefringence…”
- **Issue:** The text attributes a “3.6σ” detection with \(\beta_{\rm obs} = 0.342^\circ \pm 0.094^\circ\) to Eskilt & Komatsu and claims consistency with a bounce prediction β = 0.27°. The actual birefringence results in 2022–2025 (Eskilt et al., Diego-Palazuelos et al.) have different central values, errors, and significance; the specific triplet (authors + numbers + significance) does not match any single real paper.[5][6]
- **Fix:** Cross-check against the actual birefringence measurements; update the cited paper(s), numerical values, and σ-levels to match a real publication, or rephrase as an illustrative numerical example without attaching fictitious citation details.

---

## PAPER-PER-M2 — Heinrich et al. 2023/2024 SPHEREx bispectrum forecast details

- **Location:** Abstract and §§\ref{sec:intro},\ref{sec:spherex}, multiple mentions of “Heinrich et al. 2024~\cite{Heinrich:2023}”
- **Issue:** The paper repeatedly cites a “Heinrich et al. 2024” SPHEREx multi-tracer galaxy bispectrum forecast with σ(\(f_{\rm NL}^{\rm local}\)) ≈ 0.7 based on a specific normalization \(B^{\rm local} = (6 f_{\rm NL}/5)[P_1 P_2 + 2\text{ perms}]\). The real Heinrich et al. SPHEREx forecasts (arXiv:2311.13082 / related) give different σ-values and slightly different setup; the precise combination of year, σ = 0.7 bispectrum-only, and the stated normalization is not present as claimed.
- **Fix:** Verify the exact σ(\(f_{\rm NL}\)) numbers and template normalization in the actual Heinrich et al. paper and adjust the quoted σ, year, and the parenthetical “Fig. 6 / Table 3” description to match the real publication, or clearly state that 0.7 is a recast number derived by the author, not directly quoted.

---

## PAPER-PER-M3 — Barreira 2022 bφ prior / degradation reference

- **Location:** Systematics §\ref{sec:systematics}, PNG bias discussion citing Barreira~\cite{Barreira:2022}
- **Issue:** The text attributes specific quantitative degradation factors (e.g., 20–50% widening of σ(\(f_{\rm NL}\)) when marginalizing bφ per bin) to “Barreira 2022”; the actual Barreira 2022 PNG-bias paper discusses bφ modeling and impact, but not with the exact numerical prior ranges and degradation factors claimed here.
- **Fix:** Re-derive those percentages explicitly as this paper’s own Fisher recast (and say so), or replace with the actual numbers/qualitative statements found in Barreira (2022), avoiding the impression that the quoted 20–50% band is taken directly from that paper.

---

## PAPER-PER-n1 — Cosmoglobe DR1 birefringence numbers and error bars

- **Location:** Discussion §\ref{sec:discussion}, sentence: “Cosmoglobe DR1 II reanalysis… reports the considerably weaker $\beta = 0.35^\circ \pm 0.70^\circ$”
- **Issue:** Cosmoglobe DR1 analyses of birefringence do not report a central value and 1σ error matching 0.35° ± 0.70°; this looks like an invented loose constraint attached to a real-sounding pipeline label (“DR1 II”).[6]
- **Fix:** Replace with the actual Cosmoglobe DR1 birefringence constraint (correct central value, error, and reference) or state only that Cosmoglobe finds a result consistent with zero without fabricating a specific ± value.
