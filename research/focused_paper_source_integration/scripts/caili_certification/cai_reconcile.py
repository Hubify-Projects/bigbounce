import sympy as sp
k1,k2,k3=sp.symbols('k1 k2 k3',positive=True)
ks=[k1,k2,k3]; k=sp.symbols('k',positive=True)
eps=sp.Rational(3,2)
def s1(p): return sum(x**p for x in ks)
def s2(a,b): return sum(ks[i]**a*ks[j]**b for i in range(3) for j in range(3) if i!=j)
def s3(a,b,c): return sum(ks[i]**a*ks[j]**b*ks[kk]**c for i in range(3) for j in range(3) for kk in range(3) if i!=j and j!=kk and i!=kk)
prodk2=(k1*k2*k3)**2

# Cai groups by order in epsilon (lines 651-670). Rebuild THOSE, which is what feeds Eq(result).
# A^eps
A_e1 = -eps/2*s1(3)
# A^eps2  (Cai Eq): -eps^2/24 sum k^3 + eps^2/32 sum_{i!=j} k_i k_j^2 + eps^2/(96 prod) {5 s2(7,2) -3 s2(6,3) -2 s2(5,4)}
A_e2 = -eps**2/24*s1(3) + eps**2/32*s2(1,2) + eps**2/(96*prodk2)*(5*s2(7,2)-3*s2(6,3)-2*s2(5,4))
# A^eps3
A_e3 = eps**3/48*s1(3) + eps**3/96*s2(1,2) + eps**3/(96*prodk2)*(s1(9)-3*s2(7,2)-s2(6,3)+3*s2(5,4))
A_ordersum = sp.together(A_e1+A_e2+A_e3)

def fNL(A): return sp.Rational(10,3)*A/s1(3)
print("order-grouped (651-670) f_eq=",sp.nsimplify(sp.simplify(fNL(A_ordersum).subs({k2:k1,k3:k1}))),
      " f_loc=",sp.simplify(sp.limit(fNL(A_ordersum).subs({k2:k,k3:k}),k1,0)))

# NOW rebuild the per-vertex sum again but note: A^eps2 order-group is MISSING the eps^2 triple-sum s3 terms
#   from A_red (-2 s3(5,2,2) - s3(4,3,2)) and A_zdchi (-s3(5,2,2)).
# The order-grouped A^eps2 has NO triple sums at all -> Cai dropped them going from vertices to order-groups?
# Let's assemble A^eps2 from vertices:
Ared_e2 = -eps**2/(32*prodk2)*( s2(7,2)+s2(6,3)-2*s2(5,4)-2*s3(5,2,2)-s3(4,3,2) )
Azz_e2  = -eps**2/12*s1(3)
Azdchi_e2 = eps**2/(24*prodk2)*( 2*s2(7,2)-2*s2(5,4)-s3(5,2,2) )
A_e2_vertices = sp.together(Ared_e2+Azz_e2+Azdchi_e2)
print("A^eps2 vertices - A^eps2 printed:", sp.simplify(A_e2_vertices-A_e2))
