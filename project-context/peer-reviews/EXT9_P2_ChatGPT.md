# EXT9 P2 — ChatGPT (in-thread delta round 9; recalibrated prompt)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e646-8510-83e8-8999-77b849c6519d
**PDF**: paper2_fnl_forecast_v1.7.61.pdf · harvested 2026-06-13 13:27 PT
---
Referee report on Paper 2 v1.7.61

Updated recommendation: MINOR REVISIONS.

The paper has moved toward publishability since v1.7.60. I no longer see a load-bearing scientific problem requiring major revision. The remaining issues are narrow: one incorrect arXiv identifier and one bookkeeping/label consistency problem in the b
ϕ
	​

 treatment.

1. Closure verification against my prior report
Prior blocker/major	Status	Verification
Prior blockers	None	My v1.7.60 report had no new blockers.
FM1. Fondi reference had the wrong arXiv identifier	NOT ADDRESSED	Ref. [35] still cites Fondi et al. as arXiv:2503.14057, while the cited DESI QSO assembly-bias result is f
NL
loc
	​

=−3.3±9.2. The current PDF’s Ref. [35] still gives arXiv:2503.14057. 

paper2_fnl_forecast_v1.7.61

 That arXiv ID is actually Bitcoin Burn Addresses: Unveiling the Permanent Losses and Their Underlying Causes, not a DESI PNG paper. 
arXiv
 The correct Fondi et al. paper is arXiv:2602.12357, Assembly bias and local Primordial non-Gaussianity from DESI DR1 Quasars, and it reports f
NL
	​

=−3.3±9.2. 
arXiv

FM2. b
ϕ
	​

 combination rule inconsistent between Table IV and §V	PARTIAL	Table IV is much improved: Row 1 is split, the naive 6.25σ value is marked as not used, and the all-combined b
ϕ
	​

+GR floor is explicitly shown as σ
eff
	​

=1.41→2.6σ. 

paper2_fnl_forecast_v1.7.61

 However, the b
ϕ
	​

-only rows still say “add. quadrature” while their quoted 4.1σ and 3.5–3.7σ values are computed by replacing/widening the baseline denominator to 0.9 or 1.0, not by quadrature with the original 0.7. The caption partially fixes this by saying the b
ϕ
	​

 marginalization “replaces the baseline,” but the table column still says quadrature. 

paper2_fnl_forecast_v1.7.61

 §V also still uses 4.375×0.84/
0.7
2
+0.9
2
	​

≃3.2σ as an intermediate MegaMapper stress test, which is a different bookkeeping convention from Table IV. 

paper2_fnl_forecast_v1.7.61

Other carry-forward items from earlier rounds

The recast framing is closed: the paper now states that r is applied as a shape-weighted degradation to Heinrich et al.’s external σ(f
NL
	​

)≃0.7, not recomputed as an independent SPHEREx cross-Fisher forecast. 

paper2_fnl_forecast_v1.7.61

The null-space issue is now closed at publication standard: the text describes the ±0.13 scatter as basis/measure dependent and not a calibrated basis-independent uncertainty, with the basis-independent claim restricted to shape-cosine stability. 

paper2_fnl_forecast_v1.7.61

The 2.6–5σ headline is now adequately scoped as a sensitivity recast with a quadrature budget whose conservatism would require a full joint Fisher to confirm. 

paper2_fnl_forecast_v1.7.61

2. Fresh pass — new findings only
BLOCKERS

None.

MAJORS

None new.

MINORS / required pre-publication fixes

Ref. [35], p.27: Replace arXiv:2503.14057 with arXiv:2602.12357 and update the year/title metadata to the Fondi et al. DESI DR1 QSO assembly-bias paper. This is a simple but mandatory bibliographic fix.

Table IV, p.19: Change the b
ϕ
	​

-only rows’ combination rule from “add. quadrature” to “Fisher widening / baseline replacement.” Keep the all-combined rows as quadrature of the widened b
ϕ
	​

 denominator with σ
GR
	​

.

§V, p.11: Either label the 3.2σ MegaMapper line as a separate “double-counting stress test not used in Table IV,” or rewrite it to match Table IV’s convention: b
ϕ
	​

=30% only gives ∼4.1σ; b
ϕ
	​

=30%+σ
GR
	​

=1 gives ∼2.7σ.

§VIII.A, p.18: Change “from the LRG combined sample” to “from the combined LRG+QSO sample under the stated PNG-bias assumptions.” Chaussidon et al. report the −3.6
−9.1
+9.0
	​

 constraint from the combined DESI 2024 LRG and QSO samples, not an LRG-only result. 

paper2_fnl_forecast_v1.7.61

 
arXiv

Optional current-data polish: Add the 2026 DESI tracer cross-correlation result f
NL
loc
	​

=2.1
−8.3
+8.8
	​

, or state that §VIII.A summarizes only the auto-clustering-style constraints. This does not change the conclusion. 
arXiv

3. Recommendation

MINOR REVISIONS.

The manuscript is scientifically publishable after these targeted corrections; the remaining issues do not require new calculations or substantial scientific rework.
