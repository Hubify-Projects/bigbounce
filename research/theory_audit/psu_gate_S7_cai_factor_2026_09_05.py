#!/usr/bin/env python3
"""paper-su gate S7: locate the factor 2 between Cai+2009 (0903.0631) Eq.(37) and Eqs.(38)-(41).
Sources read verbatim: matterbounceng2.tex (0903.0631v2), general_matter_bounce_cosmology.tex (1612.02036).
Every printed intermediate is reproduced under explicit hypotheses; nothing asserted without the equation."""
import json, itertools, sympy as sp
k1, k2, k3, eps, cs = sp.symbols('k1 k2 k3 epsilon c_s', positive=True)
K = (k1, k2, k3); R = sp.Rational
S3 = sum(k**3 for k in K); Pi2 = (k1*k2*k3)**2
def Sij(a, b):  # sum_{i!=j} k_i^a k_j^b over the 6 ordered pairs
    return sum(K[i]**a*K[j]**b for i, j in itertools.permutations(range(3), 2))
def Tperm(a, b, c):  # sum_{i!=j!=k} over the 6 ordered permutations
    return sum(K[i]**a*K[j]**b*K[k]**c for i, j, k in itertools.permutations(range(3), 3))
def Tdist(a, b, c):  # sum over DISTINCT monomials (3 for (5,2,2); 6 for (4,3,2))
    return sum(set(sp.Mul(*[K[p]**e for p, e in zip(perm, (a, b, c))]) for perm in itertools.permutations(range(3), 3)))
Z = lambda e: sp.simplify(sp.expand(e))
out = {}
# ---- Cai rows, FIRST printed forms with the triple sums under the SIX-PERMUTATION reading; compare to their SECOND forms
red1 = -eps/2*S3 - eps**2/(32*Pi2)*(Sij(7,2)+Sij(6,3)-2*Sij(5,4)-2*Tperm(5,2,2)-Tperm(4,3,2))
red2 = (-eps/2+eps**2/8)*S3 + eps**2/32*Sij(1,2) - eps**2/(32*Pi2)*(Sij(7,2)+Sij(6,3)-2*Sij(5,4))
zdz1 = eps**2/(24*Pi2)*(2*Sij(7,2)-2*Sij(5,4)-Tperm(5,2,2))
zdz2 = -eps**2/12*S3 + eps**2/(12*Pi2)*(Sij(7,2)-Sij(5,4))
chi1 = eps**3/(96*Pi2)*(sum(k**9 for k in K)-3*Sij(7,2)-Sij(6,3)+3*Sij(5,4)-Tperm(5,2,2)+Tperm(4,3,2))
chi2 = -eps**3/48*S3 + eps**3/96*Sij(1,2) + eps**3/(96*Pi2)*(sum(k**9 for k in K)-3*Sij(7,2)-Sij(6,3)+3*Sij(5,4))
zz2 = (-eps**2/12+eps**3/24)*S3                       # Cai Eq.(28) [zeta zetadot^2]
conv = {"A_red (Eq.27) first==second under 6-perm": Z(red1-red2)==0,
        "A_zdz (Eq.30) first==second under 6-perm": Z(zdz1-zdz2)==0,
        "A_chi (Eq.32) first==second under 6-perm": Z(chi1-chi2)==0,
        "A_red first==second under DISTINCT reading": Z(red1.subs({}) - red2)==0 and False}
# distinct-reading check done explicitly:
red1d = -eps/2*S3 - eps**2/(32*Pi2)*(Sij(7,2)+Sij(6,3)-2*Sij(5,4)-2*Tdist(5,2,2)-Tdist(4,3,2))
conv["A_red first==second under DISTINCT reading"] = Z(red1d-red2)==0
out["cai_row_convention"] = conv
# ---- Eqs.(34)-(36) orders, and their sum vs the rows
A_e1 = -eps/2*S3
A_e2 = -eps**2/24*S3 + eps**2/32*Sij(1,2) + eps**2/(96*Pi2)*(5*Sij(7,2)-3*Sij(6,3)-2*Sij(5,4))
A_e3 = eps**3/48*S3 + eps**3/96*Sij(1,2) + eps**3/(96*Pi2)*(sum(k**9 for k in K)-3*Sij(7,2)-Sij(6,3)+3*Sij(5,4))
rows_sum = red2 + zz2 + zdz2 + chi2
out["rows_sum_equals_Eqs34_36"] = Z(rows_sum-(A_e1+A_e2+A_e3))==0
AT_rows = Z(rows_sum.subs(eps, R(3,2)))
# ---- Eq.(37) under both readings of sum_{i!=j!=k}
def eq37(T):
    return R(3,256)/Pi2*(3*sum(k**9 for k in K)+Sij(7,2)-9*Sij(6,3)+5*Sij(5,4)-66*T(5,2,2)+9*T(4,3,2))
E37_dist, E37_perm = eq37(Tdist), eq37(Tperm)
out["Eq37_distinct_minus_rows"] = str(Z(E37_dist-AT_rows)); out["Eq37_sixperm_minus_rows"] = str(sp.factor(Z(E37_perm-AT_rows)))
# ---- Li 2016 Eq.(4.19) at general c_s and its c_s=1 limit; Li rows at c_s=1 vs Cai rows at eps=3/2
Li419 = (-R(105,32)+R(39,16)/cs**2+9*cs**2/128)*S3 + R(3,256)*(3*cs**2+6)*Sij(1,2) + R(3,256)/Pi2*(
    3*cs**2*sum(k**9 for k in K)+(10-9*cs**2)*Sij(7,2)-(3*cs**2+6)*Sij(6,3)+(9*cs**2-4)*Sij(5,4))
out["Li419_cs1_minus_rows"] = str(Z(Li419.subs(cs,1)-AT_rows))
Li_zz2 = -cs**2/8*((eps-3+3*cs**2)/cs**4-eps**2/2)*S3
Li_zdz = -eps/8*S3 + eps/(8*Pi2)*(Sij(7,2)-Sij(4,5))
Li_chi = -cs**2*eps**2/32*S3 + cs**2*eps**2/64*Sij(1,2) + cs**2*eps**2/(64*Pi2)*(sum(k**9 for k in K)-Sij(6,3)+3*Sij(5,4)-3*Sij(7,2))
Li_red = (3*eps/16-R(3,4)/cs**2)*S3 + 3*eps/64*Sij(1,2) - 3*eps/(64*Pi2)*(Sij(7,2)+Sij(6,3)-2*Sij(5,4))   # Li Eq.(4.9)
out["Li_rows_cs1_eps32_minus_Cai_rows"] = {n: str(Z((a.subs(cs,1)-b).subs(eps,R(3,2)))) for n,a,b in
    [("redefinition",Li_red,red2),("zeta zetadot^2",Li_zz2,zz2),("zetadot dzeta dchi",Li_zdz,zdz2),("zeta(ddchi)^2",Li_chi,chi2)]}
out["Li_rows_general_eps_minus_Cai_rows_has_factor_(2eps-3)"] = {n: bool(sp.factor(Z(a.subs(cs,1)-b)).has(2*eps-3) or Z(a.subs(cs,1)-b)==0) for n,a,b in
    [("redefinition",Li_red,red2),("zeta zetadot^2",Li_zz2,zz2),("zetadot dzeta dchi",Li_zdz,zdz2),("zeta(ddchi)^2",Li_chi,chi2)]}
# ---- Amplitude parameter f = (10/3) A / sum k^3  (Cai Eq.21 == Li Eq.4.20); evaluate the printed configurations
def fNL(A, pref=R(10,3), norm=S3):
    return sp.simplify(pref*A/norm)
def configs(A, pref=R(10,3), isoc_norm=None):
    f = fNL(A, pref)
    iso = sp.limit(f.subs({k2:1,k3:1}), k1, 0) if isoc_norm is None else sp.limit((pref*A/isoc_norm).subs({k2:1,k3:1}), k1, 0)
    eq = f.subs({k1:1,k2:1,k3:1}); fo = f.subs({k1:2,k2:1,k3:1})
    sq = sp.limit(sp.simplify(A.subs({k1:sp.Symbol('k',positive=True),k2:sp.Symbol('k',positive=True)})/sp.Symbol('k',positive=True)**3), k3, 0)
    return {"isoceles_local": str(iso), "equilateral": str(eq), "folded": str(fo), "A_T_squeezed_over_k3": str(sq)}
printed = {"isoceles_local": "-35/8", "equilateral": "-255/64", "folded": "-9/4", "A_T_squeezed_over_k3": "-21/8"}   # Cai Eqs.(38)-(41)
hyp = {
 "H0_Eq37_distinct_reading_(=rows,=Li4.19)": configs(E37_dist),
 "HA_Eq37_sixperm_reading_(Cai_own_convention)": configs(E37_perm),
 "HB_uniform_x2_on_A_T": configs(2*E37_dist),
 "HC_isoceles_norm_sumk3->k3_only": configs(E37_dist, isoc_norm=k2**3),
 "HD_f=(20/3)A/sumk3_(Wick_2_dropped)": configs(E37_dist, pref=R(20,3)),
}
for h, d in hyp.items():
    d["reproduces_printed"] = {c: sp.nsimplify(d[c]) == sp.nsimplify(printed[c]) for c in printed}
    d["ratio_printed_over_this"] = {c: str(sp.nsimplify(sp.nsimplify(printed[c])/sp.nsimplify(d[c]))) for c in printed}
out["printed_Cai_Eqs38_41"] = printed; out["hypotheses"] = hyp
# ---- Li Eqs. (5.1)-(5.3) at c_s = 1 and squeezed F leading coefficient (Li Eq. 4.22)
out["Li_cs1"] = {"5.1 local": str(-R(165,16)+R(65,8)), "5.2 equil": str(-R(335,32)+R(65,8)+R(45,128)),
                 "5.3 folded": str(-R(37,4)+R(65,8)), "4.22 squeezed F coeff": str(R(3,8)*(-R(33,2)+13))}
out["Li419_configs_cs1"] = configs(Li419.subs(cs,1))
# ---- Cai Fig. 5 (fnl.eps, k2=k3=1, f_NL vs k1): rendered and read by eye (+-0.05); compare to 2 x H0 and to HA
f0 = fNL(E37_dist).subs({k2:1,k3:1}); fA = fNL(E37_perm).subs({k2:1,k3:1})
fig_read = {"0.0": -4.38, "0.5": -4.2, "1.0": -3.98, "1.5": -3.9, "2.0": -2.25}
out["figure_fnl_eps"] = {x: {"read": v, "2xH0": float(2*f0.subs(k1,float(x)) if float(x)>0 else 2*sp.limit(f0,k1,0)),
                             "HA": float(fA.subs(k1,float(x)) if float(x)>0 else sp.limit(fA,k1,0))} for x, v in fig_read.items()}
out["definitions"] = {
 "Cai Eq.(14) P_zeta": "P_zeta(k,eta) = k^3/(12 pi^2) |zeta_k|^2  [verbatim; Li Eq.3.17 uses (2pi)^3 delta (2pi^2/k^3) P_zeta]",
 "Cai Eq.(19) 3pt": "<zeta zeta zeta> = (2pi)^7 delta(sum k) P_zeta^2/prod k_i^3 * A   [identical to Li Eq.(4.6)]",
 "Cai Eq.(20) local ansatz": "zeta = zeta_g + (3/5) f_NL zeta_g^2",
 "Cai Eq.(21) amplitude": "|B|_NL = (10/3) A/sum k_i^3   [identical to Li Eq.(4.20) f_NL = (10/3) A_tot/sum k_i^3]",
 "consistency": "with <zz>=(2pi)^3 delta P, P=2pi^2 Delta^2/k^3 and (2pi)^7 Delta^4 A/prod k^3, the local ansatz gives A=(3/10) f sum k^3, i.e. f=(10/3)A/sum k^3: the 6/5 Wick factor is already inside 10/3; no P-vs-2P slip is possible at the definition level",
 "Cai Eq.(23) 2pt": "<zeta*(k) zeta(k')> = (2pi)^4 k^-3 delta^3(k+k') P_zeta(k)  [verbatim]"}
json.dump(out, open(__file__.replace('.py','.json'),'w'), indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
