# P1U ChatGPT EXT review — G15 2026-07-09

- Paper: P1U v1U.0.8 (59pp), g_P1U.pdf
- Reviewer: ChatGPT Pro (Extended Thinking)
- URL: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a5049a9-4db8-83e8-9d3e-75600c667a90
- Verdict: **REJECT** (F14 baseline: REJECT)

## Raw response

Referee report

I reviewed the full 59-page manuscript, including the theoretical derivations, the route-by-route “closure,” the perturbation argument, and the numerical appendices. 

g_P1U

Overall assessment

The manuscript contains one sound result of limited scope: for classical minimal Einstein–Cartan–Holst gravity coupled only to canonical scalar matter, the scalar has no spin current, the Cartan equation gives vanishing torsion, and the Holst density vanishes on the resulting Levi-Civita connection by the algebraic Bianchi identity. The “all perturbative orders” extension then follows immediately because these are exact identities rather than order-by-order cancellations.

The broader claims do not follow. In particular:

the starting ECH variational formulation is internally inconsistent;

the paper assigns a vector–axial contact interaction to minimal fermion coupling even though the cited literature says it requires non-minimal coupling;

Routes 2 and 3 are closed using effective operators or observable mappings that are not derived;

the purported dimension-four operator-basis proof contains dimensional and normalization errors and does not establish completeness;

the inflationary-dilution construction does not derive a constant w=−1 stress tensor;

Route 4 is an external ALP model subjected to a naturalness criticism, not an ECH no-go;

several headline “barriers,” forecasts, and structural tensions are asserted rather than calculated.

These defects affect the title, abstract, principal equations, figures, and conclusions. They cannot be repaired by local corrections.

Major concerns
1. MAJOR — Equation (1) is not a consistent first-order ECH action, and Eq. (3) is not the Holst-modified Cartan solution

Equation (1), Sec. II A 1, is presented as the “fundamental action” in which the tetrad and Lorentz connection are varied independently. It nevertheless includes +
4
1
	​

T
abc
	​

T
abc
, while the accompanying discussion says this term is an on-shell shorthand that is “not varied independently.”

That is not a well-defined variational prescription. The manuscript must choose one of two formulations:

the genuine first-order Einstein–Cartan–Holst plus Dirac action, varied with respect to e, ω, and ψ; or

the second-order effective action obtained after solving for and eliminating ω.

An on-shell contact term cannot be inserted into the first-order action while simultaneously being declared absent from its variation. As written, Eq. (1) invites double counting and does not lead unambiguously to Eqs. (3)–(4). 

g_P1U

More seriously, Eq. (3),

T
abc
	​

=κS
abc
	​

,

is asserted to be the exact connection equation for the full ECH+Dirac system. That is the Einstein–Cartan form, not the finite-γ Holst solution. Even for minimal fermion coupling, the Holst operator mixes torsion irreducible components. Freidel, Minic, and Takeuchi obtain a contorsion containing both the ϵ
IJKL
	​

A
L
 term and an η
I[J
	​

A
K]
	​

/γ term. Thus a totally antisymmetric spin current does not imply the simple totally antisymmetric torsion relation used in Eq. (3). 
VTechWorks

The paper later uses the correct γ
2
/(γ
2
+1) axial–axial effective coefficient in Eq. (4), but that coefficient does not follow from the stated Eq. (3). The action and connection equation must be replaced and the elimination of torsion rederived consistently.

2. MAJOR — The vector–axial “Holst partner” in Eq. (16) is absent for the manuscript’s stated minimal coupling

Section IV B claims that finite γ
BI
	​

 generates

L
int
VA
	​

∝
γ
BI
2
	​

+1
γ
BI
	​

	​

8πGJ
μ
	​

J
5
μ
	​

(16)

from the same minimal torsion-elimination step as the axial–axial interaction.

This is contrary to the cited foundational calculation. In the notation of Freidel, Minic, and Takeuchi, the effective interaction is

A
2
+
γ
2α
	​

A⋅V−α
2
V
2
,

where α is the non-minimal fermion coupling. The vector–axial interaction disappears at α=0; for minimal coupling only the axial–axial term remains. The authors explicitly state that minimal coupling produces no parity-violating A⋅V interaction. 
VTechWorks
+1

Consequently:

Eq. (16) is not part of minimal ECH as defined in the paper.

Section IV B does not close an omitted minimal-ECH operator; it introduces a non-minimal operator while claiming the opposite.

The statements that R1, R4, and the VA term are “three projections” of one minimal torsion-elimination operator are incorrect.

The mixed-VA part of Appendix C cannot support minimal-ECH completeness.

This is a direct error in the route classification, not a matter of scope.

3. MAJOR — Route 2, Eqs. (17)–(18), is neither derived nor dimensionally valid, and the cited one-loop coefficients are misreported

The manuscript introduces

Γ
one−loop
	​

∼−
16π
2
1
	​

M
Pl
	​

β(γ)
	​

∫
−g
	​

∂
μ
	​

ϑ
NY
	​

J
5
μ
	​

(17)

but explicitly acknowledges that this operator was not obtained in the cited one-loop work. It then nevertheless assigns it a roughly sixty-order birefringence suppression and treats the route as closed.

There are three independent problems.

First, the cited Shapiro–Teixeira coefficients are not quoted correctly. The manuscript gives, among other expressions,

Ω
44
	​

=
16(1+γ
2
)
2
81γ
4
	​

,Ω
24
	​

=
40(1+γ
2
)
2
81γ
2
	​

.

The source instead gives

Ω
24
	​

=−
(1+γ
2
)
2
81γ
2
	​

,Ω
44
	​

=−
20(1+γ
2
)
2
378+783γ
2
	​

,

while the 81/16 expression belongs to Ω
34
	​

, not Ω
44
	​

. 
arXiv
+1

Second, the object renormalized in that paper is not Eq. (17). Their effective charge is

λ
4
	​

=γκ
2
(W⋅J),

built from external vector and axial currents. It is not a pseudoscalar derivative coupling ∂
μ
	​

ϑ
NY
	​

J
5
μ
	​

/M
Pl
	​

. 
arXiv

Third, Eq. (18) loses the scalar-field normalization. The manuscript assigns [ϑ
NY
	​

]=1, hence

[∂
μ
	​

ϑ
NY
	​

]=2.

It then substitutes ∂
μ
	​

ϑ
NY
	​

∼H
0
	​

, which has dimension one. A slowly evolving dimension-one scalar would instead have 
ϑ
˙
∼H
0
	​

ϑ. Moreover, an accumulated rotation from a derivative coupling depends on the endpoint excursion Δϑ/M
Pl
	​

, not on an uncancelled H
0
	​

/M
Pl
	​

. Over a Hubble propagation time, the factor of H
0
	​

 can cancel against the integration interval. The manuscript’s own Appendix D, Eq. (D4), correctly obtains an endpoint formula proportional to Δϕ, contradicting the logic of Eq. (18). 

g_P1U

The claimed 10
−60
 ratio is therefore not an upper bound derived from an effective action. Route 2 remains uncalculated.

4. MAJOR — Route 3 establishes, at most, a small one-loop change in γ; it does not establish a small dark-energy contribution

Equation (19) is openly an ad hoc “chiral-count EFT” beta function rather than a result from the cited literature. It should not be presented as a theoretically grounded upper bound.

Equation (20) does reproduce the Benedetti–Speziale one-loop beta function, and the quoted integration to ∣Δγ/γ∣∼1.4×10
−6
 for a GUT-scale endpoint is numerically plausible. But the source calculation is performed in Euclidean signature, where the effective four-fermion denominator and the distinguished points γ
2
=1 differ from the standard real Lorentzian-Holst structure. The source explicitly flags the Euclidean-signature qualification. 
Pure MPG
+1

More importantly, no equation in Sec. IV E derives

ρ
DE
	​

δρ
DE
	​

	​

orδβ

from Δγ. The additional factor

(Δγ/γ)(H
0
	​

/M
Pl
	​

)

is simply asserted. A small RG shift in a dimensionless coupling does not imply a universal H
0
	​

/M
Pl
	​

 suppression of every observable constructed from it. That conclusion requires:

the explicit renormalized operator generated by the running;

its Wilson coefficient;

evaluation on the relevant cosmological background;

the resulting stress tensor or photon propagation equation.

None is supplied. Thus the running calculation, even if accepted, does not close Route 3.

5. MAJOR — The claimed dimension-four completion contains exact normalization and dimensional inconsistencies

The operator-basis closure in Sec. II A 2 and Appendix B 1 is advertised as an exact algebraic result. It is not internally consistent.

First, the footnote following Eq. (3) correctly obtains

S
abc
	​

S
abc
=−
8
3
	​

J
μ
5
	​

J
5
μ
	​


from

S
abc
	​

=
4
1
	​

ϵ
abcd
	​

J
5
d
	​

.

Later, Sec. II A 2 and Appendix B 1 instead state

S
abc
	​

S
abc
=6(J
5
	​

⋅J
5
	​

),

dropping both the 1/16 normalization and the Lorentzian sign. These expressions differ by a factor of −16. 

g_P1U

 

g_P1U

Second, O
4
[4]
	​

 is defined in Eq. (8) as schematically

O
4
[4]
	​

=M
Pl
2
	​

T
2
.

After T=κS,

O
4
[4]
	​

=M
Pl
2
	​

κ
2
S
2
∼κS
2

up to the convention-dependent 8π factor. Table VII instead reports O
4
	​

→κ
2
(J
5
	​

⋅J
5
	​

), omitting the explicit M
Pl
2
	​

 that was introduced to make the operator dimension four. The displayed result consequently has the wrong mass dimension. 

g_P1U

Third, Eq. (C1) is the usual 5×5 Fierz map for the diagonal Clifford classes. It does not, by itself, prove the manuscript’s subsequent claim that the mixed V⊗A operator “rotates only within the {V,A} block.” A mixed-class rearrangement requires a separately indexed generalized Fierz identity, including the ordering of the four spinors and any flavor labels. No such derivation is shown.

These errors directly affect the “symbolically verified” basis lemma that the abstract treats as completing the no-go.

6. MAJOR — The six schematic operators in Eqs. (7)–(8) do not establish operator-basis completeness, and the NDA monotonicity argument fails at the bounce scale

The manuscript claims to enumerate every relevant local dimension-four parity-odd density, but the list is not presented as a genuine independent operator basis:

O
1
	​

 and O
6
	​

 appear to be the same single-curvature Holst contraction written once in tetrad notation and once in spacetime-index notation.

O
4
	​

, written as ϵ
IJKL
	​

T
IJ
T
KL
, uses a torsion object T
IJ
 that is not defined; standard torsion is a vector-valued two-form T
I
.

O
5
	​

=ϵTeJ
5
	​

 remains schematic rather than a fully contracted Lorentz invariant.

No systematic reduction modulo integration by parts, equations of motion, Bianchi identities, and flavor/chiral redundancies is supplied.

Appendix C itself admits that derivative four-fermion terms, curvature–torsion mixed invariants, additional flavor structures, and other classes are not enumerated, while Sec. IV claims that the dimension-≤6 minimal basis is exhausted. 

g_P1U

 

g_P1U

The relevant one-loop literature emphasizes that quantization generates an infinite tower of Riemann/contorsion operators and that even the fixed-dimension expressions contain a substantially broader set of invariants than the six schematic entries here. 
Pure MPG

The claimed monotonic suppression with operator dimension is also inapplicable at the scale where the manuscript uses it. For an operator

M
Pl
d−4
	​

O
d
	​

	​

,

higher dimensions are suppressed only when the characteristic field gradients and curvatures satisfy E≪M
Pl
	​

. At the proposed bounce, the manuscript sets R∼M
Pl
2
	​

 and E∼M
Pl
	​

. Then operators of every dimension can contribute at order M
Pl
4
	​

; the EFT expansion is not monotonically ordered.

Finally, the fact that Eq. (6) has dimension one does not itself constitute a “dimensional impossibility.” It means Eq. (6), with the stated coefficient, is not a dimension-four local Lagrangian density. NDA may estimate a coefficient after a valid operator has been specified, but it does not prove that the operator’s vacuum matrix element is M
Pl
	​

, nor that its stress tensor is M
Pl
4
	​

g
μν
	​

. The manuscript is converting a malformed ansatz into a no-go theorem.

At most, Appendix B restates the usual cosmological-constant naturalness problem under a single-scale assumption. It does not prove an ECH amplitude closure.

7. MAJOR — Route 1 is not closed as an NJL condensate by evaluating the operator on the late-time particle number density

The numerical estimate in Sec. IV A,

ρ
NJL
	​

∼
M
Pl
2
	​

n
ψ
2
	​

	​

,

is a reasonable upper bound on the contribution of an ordinary dilute late-time fermion population. I do not object to the conclusion that this contribution is negligible at cosmic or interstellar number densities.

That calculation is not, however, a no-go for an NJL condensate. A vacuum or medium condensate involves

⟨(
ψ
ˉ
	​

γ
μ
γ
5
ψ)(
ψ
ˉ
	​

γ
μ
	​

γ
5
ψ)⟩,

not merely the square of the classical mean current. The statements

⟨J
5
μ
	​

⟩=0and⟨J
5
μ
	​

J
μ
5
	​

⟩=0

are not equivalent. Indeed, the manuscript acknowledges that the variance need not vanish and then dismisses it without calculating its stress tensor.

A condensate analysis would require, at minimum:

a regulator and physical cutoff;

the gap equation and critical coupling;

the vacuum subtraction and renormalized effective potential;

the resulting equation of state;

a demonstration that the relevant stationary solution is absent or unstable.

None is given. The route may well fail, but the paper has only excluded the dilute-particle mean-field realization, not the NJL route as advertised.

8. MAJOR — Equations (12)–(13) do not derive a cosmological constant, and the N
tot
	​

≃92 construction is circular parameter fitting

The manuscript defines

Λ
eff
	​

=ΞM
Pl
2
	​

,Ξ=[(α/M)M
Pl
	​

]D
inf
	​

,
(12)

and

D
inf
	​

=e
−3N
tot
	​

(
M
GUT
	​

T
reh
	​

	​

)
3/2
.
(13)

No effective stress tensor is derived from the ECH action that yields

T
μν
	​

=−ρg
μν
	​

with
ρ
˙
	​

=0.

A torsion or axial-current amplitude proportional to a
−3
 continues to redshift. A local four-fermion energy density proportional to its square redshifts as a
−6
. Neither becomes a constant merely because inflation has made it small.

The half-integer thermal factor is explicitly described by the manuscript as a “dimensional-analysis aesthetic” rather than the result of a partition function or matching calculation. 

g_P1U

The paper later states that the physical reheating reset drives the coherent axial source to zero and that D
inf
	​

 is only “mathematical scaffolding” for a hypothetical channel. 

g_P1U

 That produces an internal dilemma:

if reheating erases the source, the mechanism yields zero, not a residual cosmological constant;

if the source survives, its stress tensor and evolution must be calculated;

choosing N
tot
	​

 so that Eq. (12) numerically equals ρ
Λ
	​

 is a fit, not an explanation.

Therefore N
tot
	​

≃92, the purported 10
5
 residual fine-tuning score, Figure 2, Figure 5, and the later bounce-f
NL
	​

 tension cannot be treated as consequences of ECH dynamics.

9. MAJOR — Route 4 is an external ALP model subjected to a naturalness criticism, not a closed ECH route

The manuscript repeatedly concedes that minimal ECH does not derive the Maxwell–Chern–Simons operator, the ALP potential, the ALP mass, or the photon coupling. Thus R4 is not a route contained in minimal ECH. It is a GR+ALP model appended to ECH.

The internal treatment of its coupling is also inconsistent. Equation (9) leaves an unestimated finite contribution δ
NY
	​

 and says α/M should be treated phenomenologically. Section IV F then argues that a “rigid” one-loop value of α/M produces a hard overshoot. A coefficient cannot simultaneously be an uncomputed, data-fitted parameter and a rigid ECH prediction.

Equation (21) further assumes

Δϕ
rec→0
	​

∼
m
θ
	​

2ρ
θ
	​

	​

	​

.

That identifies the endpoint displacement with the full oscillation amplitude. It is not generally valid for a frozen field: for m≪H
0
	​

, the field amplitude can be large while the endpoint displacement between recombination and today is small. The displacement must be obtained from the equation of motion and initial conditions.

The Appendix G fit does solve the field equation, but its fixed-coupling posterior has a median m≃36H
0
	​

, not m≃H
0
	​

. This is a different parameter regime and does not numerically validate the main-text endpoint estimate. 

g_P1U

Most importantly, the manuscript admits that floating α/M allows both β
obs
	​

 and ρ
Λ
	​

 to be matched. The remaining statement—that m
θ
	​

∼H
0
	​

 is unexplained—is a naturalness objection common to ultralight dark-energy models. It is not an amplitude exclusion and cannot justify language such as “the route does not survive.”

The defensible conclusion is narrower: minimal ECH does not predict the required ALP-photon sector and therefore provides no ECH-specific explanation of the observations.

10. MAJOR — The perturbation-transparency result is correct within its narrow domain, but its novelty and relevance are substantially overstated

I agree with the mathematical core of Sec. X:

canonical scalar matter has no Lorentz spin current;

minimal algebraic torsion therefore vanishes;

the connection becomes Levi-Civita;

e
I
∧e
J
∧R
IJ
	​

 vanishes by the first Bianchi identity.

The all-orders statement then follows because the identity holds for the full perturbed metric, not because of a new nontrivial all-orders perturbative calculation. Equations (27)–(32) are essentially repeated expansions of an already exact zero. 

g_P1U

The manuscript has not established that this elementary consequence is new, nor compared it adequately with the existing literature on the classical equivalence of the torsion-free Holst sector to GR. Calling it a central “theorem” that generalizes prior work is not justified without a serious novelty analysis.

The result also excludes precisely the sectors relevant to most of the rest of the paper:

fermionic spin sources;

quantum loops;

a dynamical Immirzi field;

propagating torsion;

non-minimal matter;

a photon Chern–Simons coupling.

It therefore cannot reinforce the R2, R3, or R4 arguments. At most it establishes that a canonical scalar-only cosmology cannot probe the constant Immirzi parameter through classical scalar or tensor perturbations.

11. MAJOR — The “13 mechanism-class barriers” are mostly assertions or general observations, not derived constraints

Section IX presents the number of named barriers as cumulative evidence, but many entries have no calculation behind them.

Examples include:

Barrier 1, Eq. (22): invokes a Poincaré-gauge-theory mass scaling even though propagating torsion is outside minimal ECH, and labels the relation an ansatz.

Barrier 2, Eq. (23): states a biconditional between mass protection and absence of a geometric fingerprint without proving either direction.

Barrier 3: claims to treat the “most general” torsion-scalar action but writes no such action and performs no variation.

Barriers 5, 6, 10, and 13: are generic naturalness arguments or verbal dichotomies, not ECH calculations.

Barrier 7: treats γ as universally immutable despite the scheme dependence discussed in Sec. II and the running analyzed in Route 3.

Barrier 9: is explicitly conditional on an ideal nondissipative system and is inapplicable when particle production or reheating occurs.

Barrier 12, Eq. (24): is openly an assumed quadratic ceiling and is not propagated into an observable spectrum.

Counting these as separate “mechanism-class constraints” does not increase their logical force. Several share the same unproved ansatz, several apply outside minimal ECH, and several are reformulations of the same naturalness concern. The abstract and conclusion should not claim that thirteen distinct barriers collectively close the theory.

12. MAJOR — The claimed definitive erasure of f
NL
	​

=−35/16 in Sec. XIV D is not demonstrated

The paper argues that because an observed mode would be deep inside the inflationary horizon at the bounce for N
tot
	​

−N
exit
	​

≃32, the matter-bounce state is “definitively erased” and replaced by a vacuum-inflationary fluctuation.

Being subhorizon does not by itself reset a mode to the Bunch–Davies state. Under unitary linear evolution, a pre-existing excited or correlated state remains encoded in Bogoliubov coefficients unless a physical damping, decoherence, interaction, or attractor calculation demonstrates otherwise. A quantitative statement requires the transfer matrix through:

contraction;

the nonsingular bounce;

the onset of inflation;

inflation and reheating.

The manuscript explicitly states that it has not calculated this transfer function. The introduced coherence scale N
coh
	​

∼O(few) is not derived. Therefore “definitive erasure,” “purely vacuum-inflationary,” and the claimed structural incompatibility are unsupported. 

g_P1U

In addition, the value f
NL
	​

=−35/16 is not derived in this manuscript. It is attributed to an unpublished coordinated paper, while Ref. [2] is still titled as a forecast for f
NL
	​

=−35/8. 

g_P1U

 A corrected result that is prominent in the abstract, figures, and conclusions must either be derived here or cited to an accessible, internally consistent source.

13. MAJOR — The observational appendices do not test ECH, and Figures 4, 5, and 7 are not supported by defined statistical calculations

The manuscript is commendably explicit that:

Appendix E uses stock CAMB with a generic ΔN
eff
	​

 parameter, not an ECH Boltzmann hierarchy;

Appendix F validates a pseudo-C
ℓ
	​

 pipeline on synthetic skies, not the ECH model or a real-sky birefringence likelihood;

Appendix G fits an appended ALP model to a Gaussian summary of the same published β measurement.

These analyses therefore do not provide empirical support for the four-route closure. Their inclusion over roughly one third of the paper creates the appearance of observational validation without testing the claimed theory.

Several associated figures are particularly problematic:

Figure 4 and the duplicated tracks in Figure 7 combine f
NL
	​

 and birefringence “detection significances” using arbitrarily assumed correlations ρ=0.3,0.5. These observables come from different experiments, likelihoods, physical sectors, and null hypotheses. No joint model likelihood or covariance is constructed, so the combined significance curves are not statistically defined.

The milestone-by-milestone growth in those curves is not tied to documented survey data releases or Fisher matrices.

Figure 5, upper panel, shows RG running of α/M, but no beta function for that quantity is derived.

Figure 5, lower panel, assigns 10
60
 and 10
40
 tuning scores to quintessence and f(R) models while admitting that they are illustrative, not calculated. Such numbers should not appear as quantitative comparisons.

The NaMaster validation deliberately uses an unweighted estimator that exhibits a 12% multiplicative bias even though the manuscript reports that inverse-variance weighting removes approximately 80% of it. This may be useful pipeline debugging, but it is unrelated to the ECH conclusions. 

g_P1U

 

g_P1U

The numerical material should be separated from the theoretical paper unless a direct ECH likelihood and internally defined predictions are provided.

Minor concerns
14. MINOR — Planck-mass and gravitational-coupling conventions are inconsistent

The main text declares

M
Pl
	​

=G
−1/2

to be the unreduced Planck mass and uses κ=8πG. Appendix E instead uses the reduced Planck mass and writes variants such as κ
2
=8πG, while the cited one-loop literature uses κ
2
=16πG. These changes are sometimes dismissed as irrelevant at order-of-magnitude level, but they affect exact contact-term coefficients and the claimed algebraic lemmas.

The paper should use one notation throughout and retain all 8π factors consistently.

15. MINOR — The Holst term should not be called “topological” without qualification

The Holst density is not itself a topological invariant for a general torsionful connection. It is related to the Nieh–Yan density plus a torsion-squared term. It vanishes in the torsion-free sector by the Bianchi identity, but that is distinct from being a topological density such as Pontryagin. The manuscript occasionally makes this distinction correctly and elsewhere reverts to “the Holst term is topological in vacuum.” Terminology should be made consistent.

16. MINOR — Figure 3 is not an ECH-versus-ΛCDM comparison

The figure uses different H
0
	​

 values for the two curves, and its caption admits that the plotted 2–3% deviation is dominated by that input difference rather than spin-torsion dynamics. A plot whose apparent signal is known not to be the modeled signal should be removed or regenerated with matched cosmological parameters. 

g_P1U

17. MINOR — The manuscript is excessively repetitive and contains inappropriate referee-directed prose

The abstract spans approximately two pages and repeatedly anticipates objections. Similar scope disclaimers recur in the Introduction, Sec. IV, Sec. IX, Sec. XIV, the conclusions, and multiple appendices. Statements such as a reviewer asking for a stronger result being “asking for a strictly stronger result than the one claimed” are argumentative rather than scientific.

The paper should state its assumptions once, present the derivation, and allow the equations to establish the claim.

18. MINOR — The companion-paper references are not adequate for claims used prominently here

Several companion papers are described as “posted concurrently” without stable identifiers, while their numerical results are quoted in figures and conclusions. Ref. [2] is internally inconsistent with the f
NL
	​

 value used in this manuscript. Claims not needed here should be removed; claims that are needed must be made self-contained or tied to public archival references.

19. MINOR — The reproducibility record is not yet immutable

The repository documentation is extensive, but the manuscript says that DOI assignment and a version-pinned archival release are pending. A mutable branch URL and references to local paths are not substitutes for a permanent release corresponding exactly to the submitted version. The final archival record should include a tagged commit, checksums, environment lock files, and immutable chain/data artifacts.

Conclusion

The scalar-sector Bianchi-identity observation is correct but much narrower than the paper’s advertised result. The claimed closure of the four dark-energy routes depends on an incorrect minimal-coupling operator, unconstructed effective interactions, a dimensionally invalid birefringence estimate, an unsupported mapping from Immirzi running to dark energy, an incomplete operator basis, and a phenomenological dilution formula that does not yield a cosmological-constant stress tensor. The principal conclusions would require a new and substantially different analysis.

Recommendation: REJECT
