import sympy as sp
k1,k2,k3=sp.symbols('k1 k2 k3',positive=True)
ks=[k1,k2,k3]; k=sp.symbols('k',positive=True)
eps=sp.Rational(3,2)

def s1(p): return sum(x**p for x in ks)
def s2(a,b):  # sum_{i!=j} ordered, 6 terms
    return sum(ks[i]**a*ks[j]**b for i in range(3) for j in range(3) if i!=j)
def s3(a,b,c): # sum_{i!=j!=k} all distinct, 6 terms
    return sum(ks[i]**a*ks[j]**b*ks[kk]**c for i in range(3) for j in range(3) for kk in range(3) if i!=j and j!=kk and i!=kk)
prodk2=(k1*k2*k3)**2

# A_red : Cai first form (before the algebraic re-split)
A_red = -eps/2*s1(3) - eps**2/(32*prodk2)*( s2(7,2)+s2(6,3)-2*s2(5,4)-2*s3(5,2,2)-s3(4,3,2) )
# A_zzdot2
A_zz = (-eps**2/12+eps**3/24)*s1(3)
# A_zdot zeta chi
A_zdchi = eps**2/(24*prodk2)*( 2*s2(7,2)-2*s2(5,4)-s3(5,2,2) )
# A_zeta(didjchi)^2
A_chi2 = eps**3/(96*prodk2)*( s1(9)-3*s2(7,2)-s2(6,3)+3*s2(5,4)-s3(5,2,2)+s3(4,3,2) )

A_total = sp.together(A_red+A_zz+A_zdchi+A_chi2)

def fNL(A): return sp.Rational(10,3)*A/s1(3)

feq=sp.nsimplify(sp.simplify(fNL(A_total).subs({k2:k1,k3:k1})))
floc=sp.simplify(sp.limit(fNL(A_total).subs({k2:k,k3:k}),k1,0))
print("Sum-of-vertices  f_eq =",feq,"  f_loc=",floc)

# compare with printed A_T (result)
A_T = sp.Rational(3,256)/prodk2*(3*s1(9)+s2(7,2)-9*s2(6,3)+5*s2(5,4)-66*s3(5,2,2)+9*s3(4,3,2))
print("A_total - A_T (should be 0 if printed sum is consistent):", sp.simplify(A_total-A_T))
