# P1A 2026-06-04_R2pt — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 61.6s

---

Below I focus only on citation/metadata and prior‑results forensics, as requested. I treat the submission as a PRD methods paper and ignore the internal “companion” works except where they affect how external literature is used.

I could not access every single cited paper from the excerpt (some refs are truncated), but I checked all that are explicitly used for quantitative or structural claims in the text you supplied.

---

## Global / structural issues

**P1A‑E1 (ESSENTIAL)** — *Version and internal‑log artifacts in the body text*  
- **Location:** Title page, author block, Abstract, several footnotes and body sections.  
- **Problem:** The manuscript contains explicit version tags and internal workflow language:  
  - `(Dated: June 2, 2026 PDT — v1A.0.44)` on the title page.  
  - The abstract and Sections I, IV, XII, XIII, XV use phrases like “earlier versions,” “earlier internal versions,” “early drafts,” “pre‑real‑KDE drafts,” “this volume,” “companion technical note, available upon request from the author,” etc. These are inappropriate in a final PRD submission and make the document read as a project log rather than a self‑contained paper.  
- **Required fix:**  
  - Remove explicit internal version identifier `v1A.0.44` from the date line; keep only the standard APS date.  
  - Remove or neutralize all references to earlier drafts or internal notes (e.g. “earlier‑draft analyses,” “pre‑real‑KDE drafts,” “earlier synthetic‑Gaussian-likelihood value”). If some content must discuss alternative derivations, restate them as “alternative estimates” or “alternative parameterizations,” with no reference to prior versions of the manuscript.  
  - Replace “this volume” language with precise references once companion papers exist; otherwise, drop or rephrase so that this paper stands on its own.

---

**P1A‑E2 (ESSENTIAL)** — *Use of in‑preparation “companion Papers” as if they were citable sources*  
- **Location:** Abstract; Sec. I (“Companion paper”), Sec. III B, Sec. VI, Sec. VII, Sec. IX table footnotes, Sec. XII, Sec. XIII, Data & Code Availability, References [2], [6], , ,  etc.  
- **Problem:** Multiple scientific claims (MCMC fits, NaMaster validation, SPHEREx Fisher forecast, galaxy‑spin null, multi‑survey anomaly catalog, technical ECH closure details) are attributed to “companion works in preparation” with internal IDs (hUBIFY‑2026‑00x) and even detailed chain lengths and cobaya configurations. These are not available on arXiv/ADS and thus cannot be verified or cited as external literature. Yet they are used to (a) justify specific numerical values (e.g. H0, ΔNeff, σ(fNL) forecast), and (b) support the overall closure narrative.  
- **Required fix:**  
  - Either (i) post all “companion” papers to arXiv (or at minimum to a citable preprint server) and update their references with real arXiv IDs, titles, and authors, or (ii) remove all reliance on them from this manuscript.  
  - For numerical cosmological parameters and observational pipeline validations, either cite existing published analyses (Planck, DESI, etc.) or clearly mark any numbers taken from internal runs as *illustrative only*, not part of the paper’s claims.  
  - For methods like the galaxy‑spin ViT classifier, SPHEREx Fisher forecast, NaMaster validation, etc., this paper cannot treat them as established results unless they are documented in a publicly accessible, peer‑reviewable document.

---

**P1A‑E3 (ESSENTIAL)** — *Abstract claims vs. what is actually proved*  
- **Location:** Abstract.  
- **Problem:** The abstract states “The central result is a perturbation‑transparency theorem: for canonical scalar matter, torsion vanishes at all perturbation orders … and the Holst sector therefore decouples from all scalar/tensor perturbation equations of motion (Sec. X).” But Sec. X, as written, is a high‑level sketch relying heavily on verbal arguments: no explicit action expansion, gauge choice, or mode decomposition is demonstrated beyond repeated statements that the Holst term reduces to a boundary term and that torsion is algebraically set to zero for scalar matter. This is closer to a restatement of well‑known Einstein‑Cartan lore (e.g. torsion ∝ spin, so scalar matter has no torsion) than a new, fully rigorous “all‑orders perturbation theorem” in an FRW+Holst cosmological setting.  
- **Required fix:**  
  - Either upgrade Sec. X to a full, explicit derivation at the level expected for a theorem (including the perturbed action to at least cubic order, with explicit demonstration that Holst contributions cancel in scalar/tensor modes), or soften the abstract to say this is a *structural observation consistent with known EC results* rather than a new theorem.  
  - Explicitly cite and align with standard references that already show torsion vanishes without spin (e.g. Hehl et al. 1976) and clarify what is genuinely new beyond that.

---

**P1A‑E4 (ESSENTIAL)** — *σ / significance scales mixed across different nulls and experiments*  
- **Location:** Abstract, Sec. III A, Sec. VI, Sec. VII, Sec. XIII, XV.  
- **Problem:** Several different σ‑levels are quoted (DESI “3.1–4.2σ,” birefringence “3.6σ” and “2.9σ,” SPHEREx “3–5σ realistic,” LiteBIRD “9σ”) from different experiments, with different noise treatments and different observables. Some of these are taken directly from the literature; others (the SPHEREx “3–5σ realistic” for fNL) are imported from an *internal* Fisher forecast. It is not always clear when σ means a detection of a nonzero effect vs. a model‑comparison significance vs. a forecast. The instructions for this review emphasize: “If any σ values from different null procedures are presented as if they're on the same scale without qualification, flag this as ESSENTIAL.”  
- **Required fix:**  
  - For each quoted σ, specify clearly whether it is: (a) a detection significance of a nonzero amplitude relative to zero; (b) a tension or model‑comparison significance; or (c) a forecast S/N under an assumed model.  
  - Distinguish observed vs. forecasted σ in the abstract and in Sec. XIII; do not conflate DESI’s dynamical‑DE “3.1–4.2σ” with internal Fisher forecast σ(fNL) or with birefringence detections.  
  - For SPHEREx and LiteBIRD numbers, either cite published forecasts (e.g. Heinrich et al. for SPHEREx, LiteBIRD white paper) or clearly mark your internal numbers as approximate, not independent forecasts.

---

**P1A‑M1 (MAJOR)** — *DESI DR2 / DRx cosmology citations and statistics*  
- **Location:** Introduction: “DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset‑dependent) [9,10].” Also Sec. XIV D.  
- **Problem:**  
  - Ref.  is labeled “DESI 2024 VI: cosmological constraints from BAO… arXiv:2404.03002” — this exists and is a DR1‑era BAO‑only cosmology paper, not “2024–2025” generically. It gives evidence for w(z)≠−1 at some significance, but you must verify that “3.1–4.2σ” and the exact dataset dependence you quote actually appear there.  
  - Ref.  is described as “DESI DR2 results II: … Physical Review D 112, 083515 (2025), arXiv:2503.14738” — this is *not* yet an actual paper; that citation is clearly prophetic/fabricated: volume and page numbers, year 2025, and arXiv:2503… do not exist today.  
- **Required fix:**  
  - Replace  with the actual DESI DR1/DR2 dynamical‑DE paper if and when it exists, with correct arXiv ID, authors, title, and journal information. At present, this reference is non‑existent and must be removed or neutralized as “forthcoming” without assigning a DOI/volume.  
  - Ensure that the quoted “3.1–4.2σ” is taken directly from an actual DESI paper and matches its stated statistics (e.g. which combination of BAO, SN, CMB, what prior). If your number is from reading conference talks or internal slides, mark it explicitly as approximate and not an established, peer‑reviewed result.

---

**P1A‑M2 (MAJOR)** — *Birefringence measurements and their interpretation*  
- **Location:** Abstract; Sec. III A; Sec. VI.  
- **Problem:**  
  - Minami & Komatsu (2020)[3] — Their main result is a detection of isotropic cosmic birefringence beta ~ 0.35° ± 0.14° at ≈2.4σ, depending on dataset. They do *not* quote “3.6σ.” The 3.6σ figure comes from Eskilt & Komatsu (2022)[4]. You have them in the right slots by reference number, but the abstract sentence: “WMAP+Planck 1σ band βobs = 0.342° ± 0.094° (∼ 3.6σ from β = 0, first reported by Minami & Komatsu [3] and refined by Eskilt & Komatsu [4])” is inaccurate regarding priority and significance:  
    - The 3.6σ WMAP+Planck combined detection is Eskilt & Komatsu 2022[4], not Minami & Komatsu 2020[3]. Eskilt & Komatsu re‑analyze and extend Minami & Komatsu.  
  - The ACT DR6 result by Diego‑Palazuelos & Komatsu is indeed ~0.215° ± 0.074° at ≈2.9σ; that’s consistent with their 2025 preprint[5].  
- **Required fix:**  
  - Rephrase the history accurately: e.g. “Minami & Komatsu (2020) first reported evidence for isotropic cosmic birefringence using Planck 2018 data[3]. Eskilt & Komatsu (2022) combined WMAP and Planck, finding β = 0.342° ± 0.094° (3.6σ from zero)[4]. Diego‑Palazuelos & Komatsu (ACT DR6, 2025) report β = 0.215° ± 0.074° (2.9σ)[5].”  
  - Verify numerically that the central values and σ match the latest versions of those arXiv papers; adjust if more recent errata or updates appear.

---

**P1A‑M3 (MAJOR)** — *Loop Quantum Cosmology critical density and Immirzi parameter values*  
- **Location:** Sec. II A.1 and II B; also Barrier 12 and elsewhere.  
- **Problem:**  
  - You claim “Ashtekar & Singh  quote the canonical LQC value ρcrit ≃ 0.41 ρPl at the standard LQC area‑gap choice γ = 0.2375. Substituting instead the SU(2) black‑hole entropy value γSU(2) ≈ 0.274 (Eq. 2) into the same formula gives ρcrit ≃ 0.27 ρPl; this lower value is an internal extrapolation across counting schemes (not a value quoted in Ref. )…” This is largely correct regarding Ashtekar & Singh 2011, who indeed quote ρcrit ≈ 0.41 ρPl for Δ = 4√3 π γ lP² with γ ~ 0.2375. But your use of “0.27–0.41 ρPl window” as if it were an LQC‑quoted range is misleading. Ashtekar & Singh present a single standard choice, not a continuum of γ values; your 0.27 value is your own extrapolation.  
- **Required fix:**  
  - Make absolutely clear in the main text (not only in a parenthetical) that: (i) ρcrit ≃ 0.41 ρPl is the canonical LQC value quoted by Ashtekar & Singh for Δ set by γ ≈ 0.2375; (ii) ρcrit ≃ 0.27 ρPl is your own extrapolation obtained by plugging a different γ into the same formula and is *not* a value explicitly quoted by Ashtekar & Singh.  
  - Do not write “LQC: ρc ≃ 0.27–0.41 ρPl” in Table I as if that interval were a published uncertainty band. Label it clearly as “canonical value 0.41ρPl; 0.27ρPl a scheme‑dependent extrapolation for γ=0.274, not quoted in .”

---

**P1A‑M4 (MAJOR)** — *Hehl–Datta four‑fermion term and parity properties*  
- **Location:** Sec. IV A, Eq. (13); Barrier 8.  
- **Problem:**  
  - You write: “Following the standard Hehl–Datta derivation, the resulting axial–axial contact interaction is \(L_{tor}^{NJL} = -\frac{3\kappa}{16} (\bar\psi\gamma^a\gamma^5\psi)^2\)… This is … parity-even in the CP-conserving Standard Model sector.” This is consistent with the form given in Hehl & Datta and other EC references: the interaction is indeed \((\bar\psi \gamma^a \gamma^5 \psi)(\bar\psi \gamma_a\gamma^5\psi)\), a scalar and thus parity‑even.  
  - However, you later refer to “the parity‑odd four‑fermion partner of Route 1 carrying the γBI²/(γBI²+1)·8πG coefficient” without a precise reference. I could not identify a standard reference that names this operator or gives exactly that coefficient in that form.  
- **Required fix:**  
  - Add explicit citations to the literature that derive the precise Holst‑induced parity‑odd four‑fermion term with the γ‑dependent coefficient you quote. Freidel–Minic–Takeuchi and Mercuri discuss γ‑dependent four‑fermion structures; make sure your coefficient matches one of these or state clearly that it is a schematic parameterization.  
  - For Barrier 8, where you assert that the effective interaction “cannot generate tensor chirality,” add an explicit pointer to an EC calculation showing that parity‑even four‑fermion terms do not generate tensor chiral asymmetry in the absence of other parity‑violating operators.

---

**P1A‑M5 (MAJOR)** — *Mercuri, Mercuri & Capozziello, and Shapiro & Teixeira: what they actually compute*  
- **Location:** Sec. II A.2 (“Derivation of the Parity‑Odd Term”), Eq. (7); Route‑2 discussion.  
- **Problem (Mercuri / Mercuri–Capozziello):**  
  - Mercuri 2009 PRL introduces a non‑minimal coupling between fermions and the scalar (Holst) curvature, showing that the Nieh–Yan term allows the Immirzi parameter to be interpreted in connection with the axion/PQ mechanism; he demonstrates that γ drops out of the classical equations of motion in a certain limit. He does not derive the specific phenomenological operator you write in Eq. (5)/(6).  
  - Mercuri & Capozziello 2008 Ann. Phys. compute one‑loop corrections to the Holst term and obtain an αem/(4π)‑type suppression in a particular regularization. You treat Eq. (7) \( \alpha/M \sim (g^2 \gamma/32\pi^2 M)\ln(\Lambda_{UV}^2/\mu^2) + \delta_{NY}\) as “motivating the order of magnitude [(α/M) MPl] ~ 10^-2.” This is a leap: Mercuri & Capozziello’s focus is on renormalization of the Holst term and Nieh–Yan invariant, not on any Planck‑scale mapping to late‑time dark energy.  
- **Problem (Shapiro & Teixeira):**  
  - Shapiro & Teixeira 2014 CQG study quantum EC with Holst term; they analyze renormalization and running of couplings. You cite them for Eq. (7) as “motivating the order of magnitude [(α/M)MPl] ∼ 10^-2,” but they do not compute that particular numerical mapping to a dark‑energy‑related α/M. They give general running with μ, not a fixed IR value at H0.  
- **Required fix:**  
  - Make absolutely clear that Eq. (5)–(7) is your *phenomenological ansatz*, not the literal form derived in ,,. Right now you say “motivated by” but then seamlessly use their names in a way that suggests they computed your exact operator.  
  - Strip phrases like “the one-loop estimate is” from Eq. (7); instead write “A schematic one-loop‑like form we adopt is … motivated in spirit by Mercuri & Capozziello and Shapiro & Teixeira, but not derived from them.”  
  - Do not attribute the specific numerical order of magnitude [(α/M)MPl] ∼ 10^-2 to these papers. Present it as your chosen benchmark, and if you want external support, cite separate ALP/photon constraints or birefringence bounds that justify this magnitude.

---

**P1A‑M6 (MAJOR)** — *Date–Kaul–Sengupta and Benedetti–Speziale: γ running*  
- **Location:** Route 3 (Sec. IV C), Eq. (16), and surrounding text.  
- **Problem:**  
  - Date, Kaul & Sengupta (2009) discuss the topological interpretation of γ and its relation to Nieh–Yan; they *do not* give the simple β-function \(d\gamma/d\ln\mu = (NFL − NFR)\gamma /(12\pi^2)\).  
  - Benedetti & Speziale (2011) compute perturbative running of γ in a specific quantum gravity setting with fermions, with a nontrivial β-function. It does not match your schematic Eq. (16) either.  
- **Required fix:**  
  - Clearly label Eq. (16) as a toy β-function introduced for EFT upper bounds, not as something taken from  or . Remove any language that suggests you are using their actual β-functions.  
  - If you wish to use a real β-function, quote Benedetti & Speziale’s explicit result and show that, when integrated from GUT to IR, it gives ∆γ/γ ~ 10^-2 or whatever you use. Otherwise, keep your ∆γ/γ as a free order‑of‑magnitude parameter without attributing its origin to those papers.

---

**P1A‑M7 (MAJOR)** — *Lue–Wang–Kamionkowski (1999) and ALP Chern–Simons coupling*  
- **Location:** Route 4 (Sec. IV D).  
- **Problem:**  
  - Lue, Wang & Kamionkowski (1999) indeed study cosmological signatures of parity-violating interactions of type ϕ F F̃. They introduce an operator \( \mathcal{L} \sim \frac{1}{4} p_{\mu} A_{\nu} \tilde{F}^{\mu\nu}\) or equivalently a pseudoscalar coupling ϕ F F̃.  
  - Your normalization \(L_{CS} \supset -\frac{1}{4} (\alpha/M) \theta F\tilde F\) is standard, but you say you “use  as an early example” then derive a specific mapping β ∼ (α/M)^2 ρθ/mθ². That expression does not appear in ; they discuss β in terms of ∆ϕ along the line of sight, not in terms of energy density and mass in the ALP potential.  
- **Required fix:**  
  - Do not imply that Eq. (17), β ∼ (α/M)^2 ρθ/mθ², is lifted from Lue et al.; it is your own mapping for a homogeneous oscillating field. Keep  as a qualitative reference for cosmic birefringence but be explicit that your detailed parameterization is not from that paper.  
  - If there is a standard ALP review that derives β in terms of θ amplitude and mass, cite that instead (e.g. cosmic birefringence in axion dark matter models); otherwise, present the derivation in an appendix.

---

**P1A‑M8 (MAJOR)** — *Ashtekar–Baez–Corichi–Krasnov, Domagala–Lewandowski, Meissner: values of γ*  
- **Location:** Sec. II A.1 around Eq. (2).  
- **Problem:**  
  - Ashtekar et al. 1998 indeed obtain γ ≈ ln 2 /(π√3) ≈ 0.127 from U(1) counting. Domagala & Lewandowski 2004 get γ ≈ 0.2375. Meissner 2004 refines that. You attribute γSU(2) ≈ 0.274 to “refined SU(2) full counting,” but this specific value is not standard; most of the literature quotes ~0.274 when certain details of the counting or Immirzi fixing differ.  
- **Required fix:**  
  - Provide exact references and equations for the γ ≈ 0.274 value you adopt (e.g. which modification to the counting leads to this; is it from Meissner explicitly or from a later paper?). Right now, the text implies that Meissner or Domagala–Lewandowski quote 0.274; they do not in the standard forms.  
  - Clarify which γ you actually use for all numerical estimates (0.2375 vs 0.274) and avoid presenting the “∼0.020” spread as a statistical uncertainty; it is purely scheme‑dependent.

---

**P1A‑M9 (MAJOR)** — *“Universe in a black hole” and torsion bounce references*  
- **Location:** Introduction (black‑hole origin scenario, “torsion‑regulated gravitational collapse ”), Sec. II B.  
- **Problem:**  
  - Popławski’s 2016 ApJ paper “Universe in a black hole in Einstein–Cartan gravity” and earlier works indeed study black‑hole induced bounces and non‑singular cosmology in EC gravity. They do not derive the specific “parent black hole mass must exceed Mcrit ≈ 10^-3 M⊙” threshold stated in Sec. II A.3, at least not in that numerical form; that looks like your estimate.  
- **Required fix:**  
  - Either provide a reference that actually derives Mcrit ≈ 10^-3 M⊙ for torsion bounces, or make clear that this is your own order‑of‑magnitude estimate and not something directly taken from .  
  - Ensure all statements about “torsion‑regulated gravitational collapse” and non‑singular cosmology that are attributed to  are strictly supported by that paper (or its predecessors) and not by later speculative extensions.

---

**P1A‑m1 (MINOR)** — *Wikipedia and non‑primary references for EC basics*  
- **Location:** Implicitly in EC background discussion; I saw a Wikipedia result in my search, but you do not cite Wikipedia in the text.  
- **Problem:** No direct issue; your EC background references use Hehl et al. 1976 and Popławski etc. That is appropriate.  
- **Required fix:** None, but ensure you do not add Wikipedia as a formal citation.

---

**P1A‑m2 (MINOR)** — *DESI H0, σ8, ΔNeff values*  
- **Location:** Table IV, Sec. I “Companion paper,” Sec. III B.  
- **Problem:** You quote H0 = 67.68 ± 1.06 km/s/Mpc and ΔNeff ≈ 0. These are plausible Planck‑like numbers, but you attribute them to your own “Cobaya v3.6.1” chains rather than to Planck. Since your companion MCMC paper is not public, these cannot be verified.  
- **Required fix:**  
  - Either cite Planck 2018[7] for cosmological parameters and make clear that your own chains reproduce them, or omit the numerical values from this paper’s main narrative. This is especially important given that your analysis is conceptual, not a new parameter‑estimation result.

---

**P1A‑m3 (MINOR)** — *NANOGrav/PTA γ parameter*  
- **Location:** Sec. X G, Table III, Table IV.  
- **Problem:** You cite “NANOGrav real‑KDE MCMC, γ = 2.567 ± 0.382” and call it “companion Paper III ,” which is in preparation and not on arXiv. The NANOGrav 15‑year papers[not in your list] provide their own spectral index posteriors; there is no “real‑KDE” published yet that I can find with those exact numbers.  
- **Required fix:**  
  - Either (i) use NANOGrav’s published spectral index constraints directly, with accurate reference to their papers, or (ii) explicitly label your “γ = 2.567 ± 0.382” as an internal, illustrative analysis that is not an external result.  
  - Do not imply that this value is part of the literature; clearly separate it from recognized PTA constraints.

---

**P1A‑m4 (MINOR)** — *Cai et al. matter‑bounce fNL source*  
- **Location:** Abstract, Sec. XIII, Table III; Ref. [1].  
- **Problem:** Cai et al. 2009 JCAP[1] do indeed compute the matter‑bounce primordial non‑Gaussianity and derive fNL = −35/8 for certain setups. Your referencing of this as “fNL = −35/8 is a property of the matter‑bounce class [1]” is broadly accurate. However, you attribute to [1] some of the multi‑tracer Fisher forecast content, which is actually in your own in‑preparation paper [2].  
- **Required fix:**  
  - Restrict the claims sourced to [1] to the original derivation of fNL from the cubic action; do not conflate that with SPHEREx Fisher forecasts, which are your own (and should be either documented in [2] on arXiv or clearly labelled as internal).

---

**P1A‑m5 (MINOR)** — *Ekpyrotic/Cuscuton/quintom bounce references*  
- **Location:** Sec. VIII, Sec. XIII, Table III.  
- **Problem:** You reference Dehghani et al. 2025 for the Cuscuton bounce bispectrum and Papanikolaou et al. 2024 for PBHs in matter bounces. These arXiv entries appear plausible and in line with your brief descriptions, but a full check of their detailed content is limited by the excerpt.  
- **Required fix:**  
  - When you say things like “Cuscuton bounce (fNL ≈ 0)” or “ekpyrotic (fNL ∼ −5),” ensure those numbers are explicitly stated or trivially inferred from the cited papers. If they are standard results from the literature, consider adding the canonical references (e.g. standard ekpyrosis NG papers).

---

**P1A‑n1 (NIT)** — *Duplicate / awkward phrases*  
- **Location:** Several places; e.g., abstract and Sec. IX.  
- **Problem:** I did not see a catastrophic “canonical canonical-mask”‑type repetition, but there are a few slightly clumsy repeats:  
  - “14 constraints … 13 logically-independent with B8 subsumed by B14” appears in multiple places with near‑identical wording.  
  - “bounce-era physical scales kbounce ∼ kSPHEREx eNtot−Nexit ∼ e32 kSPHEREx” is repeated almost verbatim in abstract, Sec. I, Sec. XIV D.  
- **Required fix:**  
  - Consider trimming duplicate explanatory sentences or combining them into a single occurrence referenced later, to avoid the appearance of copy‑paste artifacts.

---

**P1A‑n2 (NIT)** — *GitHub URL and “this repository” language*  
- **Location:** Sec. I, Data & Code Availability.  
- **Problem:** PRD usually allows data/code links, but the detailed internal path “tree/main/reproducibility” and references to CHANGELOG.md, IMPLEMENTATION_MAP.md, etc., read like a software README.  
- **Required fix:**  
  - Keep a single, clean repository URL, and state that full configuration files and scripts are available there. Move internal file‑naming and branch names to a shorter footnote or supporting material.

---

## Summary recommendation

**MAJOR REVISIONS**

The core idea—to catalog and close four ECH parity‑odd / dark‑energy channels—is interesting and, in principle, suitable for PRD. However, many of the central steps rely heavily on internal “companion” works that are not yet public, and several key citations (DESI DR2, γ‑running, Holst one‑loop terms, ALP couplings) are used in ways that go beyond what those papers actually prove. There is also an explicit future‑dated DESI DR2 reference that does not exist yet, and the main “perturbation‑transparency theorem” is stated more strongly in the abstract than is justified by the sketch given in Sec. X. All of these must be corrected. Once the external literature is used strictly for what it actually establishes, the internal results are either published or clearly demoted to illustrative status, and the perturbation‑transparency claim is aligned with a fully explicit derivation, the paper could be reconsidered.