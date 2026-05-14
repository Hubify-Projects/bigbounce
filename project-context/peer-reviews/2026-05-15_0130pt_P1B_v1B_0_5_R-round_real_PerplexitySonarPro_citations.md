# P1B_v1B_0_5 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-15_0130pt
**Wall time**: 24.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=12970, completion=1824, total=14794

---

## PAPER-PER-B1 (BLOCKER) — Fake / Unverified Liu torsion paper

**Location:** Sec. 3, “Independent cross-validation”, citation `\cite{ECTorsionDESI2025,DESI2025DR2}` and text “Liu et al.… DESI DR2… torsion preferred by AIC (ΔAIC = −5.7 to −6.6).”

**Issue:** I cannot locate any EC torsion cosmology paper matching “Liu et al. 2025” that uses DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018 and reports torsion preferred by AIC with ΔAIC in the quoted range; the BibTeX key `ECTorsionDESI2025` appears to be a placeholder rather than a real, checkable reference.[0] As written, this looks like a fabricated or at least non-verifiable literature claim used as external support for the author’s MCMC results.

**Fix:** Either (a) replace this with a real, verifiable reference (correct authors, title, arXiv ID, and numbers) that actually reports these datasets and ΔAIC values, or (b) delete the “Independent cross-validation” paragraph entirely and explicitly state that no published torsion analysis with this exact dataset combination is available yet.


## PAPER-PER-M1 (MAJOR) — Mis-citation / ambiguity for Eskilt cosmic-birefringence papers

**Location:** Abstract, cosmic-birefringence paragraph and Sec. 6 (Spectator-ALP consistency), using `\cite{Eskilt2022, Eskilt2022b, DiegoPalazuelos2025}` and describing “published Planck/ACT DR6 2.4–2.9σ” and “joint Planck+ACT value β = 0.342° ± 0.094° (3.6σ).”

**Issue:** The canonical Planck-reanalysis birefringence result is Eskilt & Komatsu 2022 (Planck PR4 / NPIPE); the later joint Planck+ACT analysis is a distinct paper with a specific title and arXiv ID, and ACT DR6 birefringence measurements are reported by Diego-Palazuelos et al. in clearly titled ACTDR6 papers.[0] The LaTeX source only uses short keys (`Eskilt2022`, `Eskilt2022b`, `DiegoPalazuelos2025`) without any checkable metadata; this makes it impossible to verify from the text alone that (i) the 0.342° ± 0.094° value and 3.6σ indeed come from the joint Planck+ACT paper, and (ii) the “2.4–2.9σ” wording is consistent with the individual Planck and ACT DR6 claims.[0]

**Fix:** In the bibliography, ensure each of these keys is mapped to the correct, distinct paper with full, accurate metadata: author list, exact title, arXiv ID, journal, and year; in the main text, add one explicit parenthetical with the correct arXiv ID for the joint Planck+ACT analysis so an auditor can confirm that β = 0.342° ± 0.094° at 3.6σ is quoted from that specific work and that the “2.4–2.9σ” range aligns with the individual Planck and ACT claims.


## PAPER-PER-M2 (MAJOR) — DESI DR2 chain status text now inaccurate / misleading

**Location:** Sec. 7, Table 2 caption and body; Sec. 7.1 and Conclusions “Forward” paragraph, especially phrases “DESI DR2 w0wa chains… in progress; convergence expected in ~3 days from 2026-05-05” and “we deliberately do not commit to a specific calendar date for convergence.”

**Issue:** The current round context specifies that the DESI DR2 w0wa free chain on the named RunPod instance has been stalled for ~12 hours at R̂ − 1 = 0.01775 with 53,736 samples and no progress since the last checkpoint.[0] In contrast, the manuscript still describes the run as smoothly “running,” with convergence expected in “~3 days” and R̂ − 1 “descending monotonically,” which is no longer accurate and understates an operational problem that affects the cross-paper “not tested yet” narrative.[0]

**Fix:** Update Sec. 7 and the Conclusions “Forward” paragraph to explicitly state that the DESI DR2 w0wa chain is currently stalled (include the latest R̂ − 1, sample count, and last-progress timestamp), that convergence ETA is now uncertain, and that all DESI-based w0wa conclusions in P1A remain “not tested” until the stall is diagnosed and resolved.


## PAPER-PER-m3 (minor) — Over-precise readiness and chain-status assertions in Table 2

**Location:** Sec. 7, Table 1 and Table 2 captions and entries, e.g., “Readiness 99%… DESI DR2 cobaya chains running… ETA ~3 days to convergence,” “DESI DR2 w0wa (new)… Status: Running.”

**Issue:** The readiness percentages and specific “ETA ~3 days” language give an impression of quantitative reliability, but they conflict with the actual compute stall noted in the round context and are not directly traceable to any literature or pipeline standard; they are effectively internal project-management estimates presented as facts.[0] Given that the DESI w0wa chain is a key gate for P1A Table II, this can mislead readers about how close the DESI-based tests really are to completion.

**Fix:** Soften these entries to qualitative labels (“high,” “in progress,” “pending converged DESI DR2 w0wa chain”) and remove or rephrase the “~3 days” ETA; explicitly flag that readiness is capped by the unresolved DESI DR2 chain convergence and will be revised once the stall is cleared.


## PAPER-PER-m4 (minor) — CMB-S4 Neff forecast needs anchored reference

**Location:** Sec. 3, paragraph “Key finding,” sentence “CMB-S4 (σ(Neff) ~ 0.03) will provide the first precision test.”

**Issue:** The claim that CMB-S4 will reach σ(Neff) ≈ 0.03 is standard but the text does not give a concrete citation (CMB-S4 Science Book or later white paper) with an arXiv ID and title that can be checked for that specific forecast.[0] For a verification-focused companion, leaving this as an uncited number weakens the otherwise strict citation-chain discipline.

**Fix:** Add an explicit CMB-S4 reference whose abstract or main text quotes the σ(Neff) forecast at the stated level, and ensure the bibliography entry has correct authors, title, arXiv ID, and venue; optionally note in the sentence that this is a forecast, not an existing constraint.


## PAPER-PER-n5 (nit) — ArXiv / journal metadata opaque in current excerpt

**Location:** Preamble comments and throughout, e.g., “arXiv submission: astro-ph.CO / gr-qc” and all bib keys (`Golden2026P1a`, `Golden2026P2`, `Golden2026P3`, `Golden2026P4`, `DESI2024`, `DESI2025DR2`, etc.) without explicit IDs.

**Issue:** The main inter-paper and external references are given only as keys tied to a local `references.bib`, so from the manuscript alone an auditor cannot tell whether (for example) “Golden 2026a” corresponds to a real arXiv submission with a matching title and author, nor whether the DESI 2024 / 2025 DRs are using the correct official arXiv IDs and titles.[0] This is more a transparency nit than a physics problem, but it complicates automated citation forensics.

**Fix:** For the small set of load‑bearing references (P1A–P4, DESI DR1/DR2, Eskilt/Diego‑Palazuelos/LiteBIRD, Pantheon+, DES-SN5YR), add explicit arXiv IDs (and journal references where available) in the bibliography or in a short “Key references” appendix so that a reader can immediately verify that titles, authors, and IDs are correctly associated and not fused from different papers.
