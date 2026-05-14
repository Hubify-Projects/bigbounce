# P4_v1064_R2 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-15_0200pt
**Wall time**: 26.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=61690, completion=1243, total=62933

---

## PAPER-PER-B1 – Shamir (2022) arXiv / bib metadata

**Issue (MAJOR, citations / fused-ID risk)**  
In §Intro and bibitem `Shamir:2022`, the paper is cited as a 2022 PASJ article with journal info but no arXiv ID; the comments flag that a previously used arXiv:2207.11885 was actually an unrelated optimization paper, and no corrected arXiv identifier is given. The current text leaves the impression there is a corresponding arXiv preprint when in fact the only stable identifier is the PASJ journal reference. [1]

**Fix (1–2 sentences)**  
Make the Shamir (2022) reference purely journal-based: give the full PASJ citation (authors, year, title, volume, page, DOI) and explicitly note “no associated arXiv preprint” instead of hinting at a missing arXiv ID. Clarify anywhere else in the text that references Shamir (2022) via arXiv that the canonical reference is the PASJ article only.

---

## PAPER-PER-B2 – Jia et al. (2023) CE-ResNet metadata

**Issue (MAJOR, citations / fused-ID risk)**  
The paper cites Jia et al. (2023) “CE‑ResNet” with ApJ 943, 154 as the journal venue and notes that a previously used arXiv:2211.03497 actually points to an unrelated nonlocal gravity paper, but no correct arXiv ID is provided. This history plus the absence of a verified arXiv ID is exactly the fused‑metadata pattern you are trying to avoid. [1]

**Fix (1–2 sentences)**  
Confirm via ADS/publisher that the CE‑ResNet article either has no arXiv version or has a specific, correct arXiv ID; then in the bibliography give only the verified identifiers (ApJ volume/page and DOI, and the correct arXiv ID if it exists). Remove all mention of the misassigned 2211.03497 and the “pending arXiv verification” note from the main text, since it exposes the previous fusion error.

---

## PAPER-PER-M1 – Shamir (2020) reference completeness

**Issue (minor, but in scope for metadata audit)**  
Shamir (2020) is cited with journal (Ap&SS 365, 136) and a qualitative summary (“patterns of galaxy spin directions in SDSS and Pan‑STARRS show parity violation and multipoles”) but the bib entry as written in the LaTeX excerpt does not show its arXiv identifier, even though it exists and is standard in cosmology citation practice. [1]

**Fix (1–2 sentences)**  
Add the correct arXiv ID for Shamir (2020) in the bibliography entry alongside the Ap&SS reference (e.g. “arXiv:20xx.xxxxx [astro‑ph.CO]”, verified from arXiv/ADS). This keeps the citation chain machine‑checkable and avoids future confusion in automated audits.

---

## PAPER-PER-M2 – Shamir (2012) consistency between text and bib

**Issue (minor)**  
For Shamir (2012), the main text correctly describes a handedness asymmetry in SDSS, but the bib entry as shown omits the arXiv DOI and context that this is Physics Letters B 715, 25 with arXiv:1207.5464 (which explicitly reports a dipole at RA≈132°, Dec≈32° and P<1.95×10⁻⁵). [1]

**Fix (1–2 sentences)**  
Explicitly include “Phys. Lett. B 715, 25 (2012), arXiv:1207.5464” in the Shamir (2012) bibitem, and (optionally) add a parenthetical in the main text giving the published dipole axis to make clear you are referring to that specific result. This removes any ambiguity about which Shamir (2012) paper is meant.

---

## PAPER-PER-m3 – Explicit statement on missing arXiv IDs for several key works

**Issue (minor, global clarity)**  
Several key references (Shamir 2022 PASJ, CE‑ResNet ApJ 2023, some of the Golden 2026 companion papers) are described with partial metadata and comments about arXiv‑ID problems or “to be deposited on arXiv”, which makes it hard for future auditors to know whether an arXiv version exists or not. [1]

**Fix (1–2 sentences)**  
Add a short note in the bibliography or a footnote stating which of these works currently have no arXiv version (journal‑only or “in preparation”), and which have verified arXiv IDs. This makes the citation graph unambiguous and documents that any missing arXiv identifiers are intentional rather than an oversight.

---

## PAPER-PER-n1 – Internal self‑citations to Golden (2026P1A/P2/P3)

**Issue (nit)**  
The three Golden (2026P1A/P2/P3) companion papers are cited with placeholder descriptions but no arXiv IDs, DOIs, or journal venues, and the text sometimes talks about “cross‑resolvable identifiers” in the future tense. This is fine for a draft but brittle for a submitted arXiv/ journal version.

**Fix (1–2 sentences)**  
Either (a) update these entries to real arXiv IDs once those preprints exist, or (b) clearly mark them as “in preparation, no public identifier yet” and avoid implying current cross‑resolvability. This prevents readers from assuming that stable public citation targets already exist.
