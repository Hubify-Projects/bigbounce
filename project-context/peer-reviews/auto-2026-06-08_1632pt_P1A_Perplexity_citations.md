# P1A auto-2026-06-08_1632pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 NO_NEW
**Wall time**: 27.3s

---

I can’t complete the requested referee-style citation-forensics audit to PRD standards from the material provided alone. The prompt includes the full text of the manuscript, but I do **not** have live web-search access in this environment, so I cannot verify arXiv IDs, titles, venues, DOI matches, or NASA ADS records against external databases as you explicitly require.

What I *can* do is flag internal-paper issues that are visible directly in the text:

- **Major:** The bibliography contains multiple **“in preparation”** citations as load-bearing support for central numerical claims and pipeline validation: [2], [6], , , and several places in the body. These are not independently checkable and are unacceptable as primary support for key results in a PRD submission.
- **Major:** The paper repeatedly relies on **companion internal analyses** for central numbers such as \(H_0 = 67.68 \pm 1.06\), \(\Delta N_{\rm eff}\approx 0\), the SPHEREx forecast, ALP fitting, and galaxy-spin results, while stating they are “in preparation” or “available upon request.” Those claims are not reproducible from the manuscript itself.
- **Major:** The manuscript uses a large number of **self-referential, unpublished companion-paper placeholders** as if they were established references, which is not appropriate for a physics paper whose conclusions depend on them.
- **Major:** The manuscript contains explicit **version-history / internal bookkeeping language** in the body, including phrases like “earlier versions,” “Paper I(b),” “Paper II,” “Paper III,” “Paper IV,” “supersedes the earlier synthetic-Gaussian-likelihood value,” and references to “frozen accepted samples” and “running on a dedicated MPI pod.” These are not proper scientific prose for the rendered paper and should be removed or moved to internal notes.
- **Major:** Several numerical claims are presented without a traceable derivation in the displayed text, especially the quoted significance levels and order-of-magnitude comparisons. Examples include the \(3.1\text{–}4.2\sigma\) DESI claim, the \(3\text{–}5\sigma\) SPHEREx significance, the \(\sim 58\text{–}60\) orders suppression in Route 2, and the \(\sim 22\) / \(\sim 36\) orders overshoot in Route 4. These need line-by-line recomputation and source traceability.
- **Major:** The manuscript appears to mix **distinct hypotheses and null procedures** side by side, including WMAP+Planck birefringence, ACT DR6 follow-up, LiteBIRD forecast, and current-central-value comparisons. The paper itself does not consistently label these as not directly comparable at every juxtaposition.
- **Major:** The claimed “channel-level closure” is repeatedly softened in the text by admissions that the operator basis is incomplete. That is scientifically important: the paper does **not** establish a complete no-go theorem for ECH, only a limited channel-level argument under stated assumptions.
- **Minor:** There are multiple instances of awkward duplication and internal phrasing issues, such as “channel-level closure,” “channel-level amplitude closure,” “closure summary,” and repeated restatements of the same caveat. This weakens readability.
- **Minor:** Some equations and units appear to be presented as phenomenological ansätze rather than derived results, and the manuscript often says so; that is honest, but the paper should clearly separate derivation from assumption in the main text.
- **Minor:** The paper is very long for the stated contribution. For a narrow “closed-form no-go for ECH at tree level,” the current 21-page length appears overextended; a tighter maximum would be about **12–15 pages** for the main text, with appendices only for genuinely necessary derivations.

Because I cannot verify the external bibliography, arXiv records, DOI metadata, or ADS entries, I cannot responsibly issue the exact itemized forensics report you requested.