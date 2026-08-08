import sympy as sp
from itertools import product

k1,k2,k3 = sp.symbols('k1 k2 k3', positive=True)
ks=[k1,k2,k3]
k=sp.symbols('k',positive=True)

def s_single(p): return sum(x**p for x in ks)

def s_pair(pa,pb,ordered):
    tot=0
    for i in range(3):
        for j in range(3):
            if i!=j:
                if ordered: tot+=ks[i]**pa*ks[j]**pb
                else:
                    if i<j: tot+=ks[i]**pa*ks[j]**pb + ks[j]**pa*ks[i]**pb
    return tot

def s_triple(pa,pb,pc,mode):
    # mode: 'perm6' all distinct ordered (6 terms); 'sym' symmetric over the two equal-ish; 'single' one rep
    tot=0
    for i in range(3):
        for j in range(3):
            for kk in range(3):
                if i!=j and j!=kk and i!=kk:
                    tot+=ks[i]**pa*ks[j]**pb*ks[kk]**pc
    if mode=='perm6': return tot
    if mode=='half': return tot/2  # if the two equal exponents double-count
    return tot

def build(pair_ord, trip_mode):
    prodk2=(k1*k2*k3)**2
    return sp.Rational(3,256)/prodk2*(
        3*s_single(9)
        + s_pair(7,2,pair_ord)
        - 9*s_pair(6,3,pair_ord)
        + 5*s_pair(5,4,pair_ord)
        - 66*s_triple(5,2,2,trip_mode)
        + 9*s_triple(4,3,2,trip_mode)
    )

def fNL(A): return sp.Rational(10,3)*A/s_single(3)

target_eq=sp.Rational(-255,64)
target_loc=sp.Rational(-35,8)
for po in [True,False]:
    for tm in ['perm6','half']:
        A=build(po,tm)
        feq=sp.nsimplify(sp.simplify(fNL(A).subs({k2:k1,k3:k1})))
        floc=sp.simplify(sp.limit(fNL(A).subs({k2:k,k3:k}),k1,0))
        print(f"pair_ordered={po} triple={tm}:  f_eq={feq}  f_loc={floc}",
              "  <-- EQ MATCH" if feq==target_eq else "",
              " LOC MATCH" if floc==target_loc else "")
