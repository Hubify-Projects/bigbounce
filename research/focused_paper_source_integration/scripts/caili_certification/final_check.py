import sympy as sp
cs=sp.symbols('c_s',positive=True)
# Li Eq (5.1): f_NL^local = -165/16 + 65/(8 cs^2)
li_local = -sp.Rational(165,16)+sp.Rational(65,8)/cs**2
print("Li local at c_s=1:", li_local.subs(cs,1), " = -35/16?", li_local.subs(cs,1)==sp.Rational(-35,16))

# And verify the local limit from vertices is a clean limit AND matches isoceles reduction
k1,k2,k3=sp.symbols('k1 k2 k3',positive=True); ks=[k1,k2,k3]; k=sp.symbols('k',positive=True)
eps=sp.Rational(3,2)
def s1(p): return sum(x**p for x in ks)
def s2(a,b): return sum(ks[i]**a*ks[j]**b for i in range(3) for j in range(3) if i!=j)
def s3(a,b,c): return sum(ks[i]**a*ks[j]**b*ks[kk]**c for i in range(3) for j in range(3) for kk in range(3) if i!=j and j!=kk and i!=kk)
prodk2=(k1*k2*k3)**2
A_red=-eps/2*s1(3)-eps**2/(32*prodk2)*(s2(7,2)+s2(6,3)-2*s2(5,4)-2*s3(5,2,2)-s3(4,3,2))
A_zz=(-eps**2/12+eps**3/24)*s1(3)
A_zdchi=eps**2/(24*prodk2)*(2*s2(7,2)-2*s2(5,4)-s3(5,2,2))
A_chi2=eps**3/(96*prodk2)*(s1(9)-3*s2(7,2)-s2(6,3)+3*s2(5,4)-s3(5,2,2)+s3(4,3,2))
A=sp.together(A_red+A_zz+A_zdchi+A_chi2)
f=sp.Rational(10,3)*A/s1(3)
fiso=f.subs({k2:k,k3:k})
print("f_NL isoceles series k1->0:", sp.series(sp.simplify(fiso),k1,0,3).removeO())
print("clean limit:", sp.limit(fiso,k1,0))
