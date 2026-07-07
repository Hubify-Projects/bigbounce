import sympy as sp

k1, k2, k3 = sp.symbols('k1 k2 k3', positive=True)
ks = [k1, k2, k3]
eps = sp.Rational(3, 2)

sumk3 = sum(k**3 for k in ks)
Pik2 = (k1*k2*k3)**2

def Sig(a, b):
    # ordered pairs i != j (6 terms)
    return sum(ks[i]**a * ks[j]**b for i in range(3) for j in range(3) if i != j)

def Sig_single(a):
    return sum(k**a for k in ks)

def Sig_triple_perms(a, b, c):
    # sum over all 6 permutations of (i,j,l) all distinct = perms of (1,2,3)
    from itertools import permutations
    return sum(ks[i]**a * ks[j]**b * ks[l]**c for (i, j, l) in permutations(range(3)))

def Sig_triple_distinct(a, b, c):
    # distinct-monomial interpretation: each distinct product once
    from itertools import permutations
    seen = set()
    total = 0
    for (i, j, l) in permutations(range(3)):
        key = tuple(sorted([(i, a), (j, b), (l, c)]))
        if key in seen:
            continue
        seen.add(key)
        total += ks[i]**a * ks[j]**b * ks[l]**c
    return total

def build_A(Sig_triple):
    # vertex 1: field redef
    v1 = -sp.Rational(1,2)*eps*sumk3 - eps**2/(32*Pik2)*(
        Sig(7,2) + Sig(6,3) - 2*Sig(5,4)
        - 2*Sig_triple(5,2,2) - Sig_triple(4,3,2))
    # vertex 2
    v2 = (-eps**2/12 + eps**3/24)*sumk3
    # vertex 3
    v3 = eps**2/(24*Pik2)*(2*Sig(7,2) - 2*Sig(5,4) - Sig_triple(5,2,2))
    # vertex 4
    v4 = eps**3/(96*Pik2)*(
        Sig_single(9) - 3*Sig(7,2) - Sig(6,3)
        + 3*Sig(5,4) - Sig_triple(5,2,2) + Sig_triple(4,3,2))
    return v1 + v2 + v3 + v4

def squeezed(A):
    k = sp.symbols('k', positive=True)
    fNL = sp.Rational(10,3)*A/sumk3
    fNL_sub = fNL.subs({k2: k, k3: k})
    fNL_sub = sp.simplify(fNL_sub)
    # expand in small k1
    ser = sp.series(fNL_sub, k1, 0, 3).removeO()
    lead = sp.limit(fNL_sub, k1, 0)
    return lead, sp.expand(ser)

for name, trip in [("6-perms", Sig_triple_perms), ("distinct-monomial", Sig_triple_distinct)]:
    A = build_A(trip)
    lead, ser = squeezed(A)
    print(f"=== {name} ===")
    print("  squeezed leading (k1->0):", lead)
    print("  series in k1:", ser)
    # equilateral
    A_eq = A.subs({k2: k1, k3: k1})
    fNL_eq = sp.simplify(sp.Rational(10,3)*A_eq/(3*k1**3))
    print("  equilateral fNL:", fNL_eq)
    print()

# Li cross-check
cs = sp.symbols('c_s', positive=True)
fNL_Li = -sp.Rational(165,16) + sp.Rational(65,8)/cs**2
print("Li at c_s=1:", fNL_Li.subs(cs, 1))
