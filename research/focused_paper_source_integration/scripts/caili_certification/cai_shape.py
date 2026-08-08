import sympy as sp

k1,k2,k3 = sp.symbols('k1 k2 k3', positive=True)
ks = [k1,k2,k3]

# Convention definitions
def sum_single(p):
    # sum_i k_i^p  -> 3 terms
    return sum(k**p for k in ks)

def sum_ineqj(pa,pb):
    # sum_{i != j} k_i^pa k_j^pb : ORDERED pairs, 6 terms
    tot = 0
    for i in range(3):
        for j in range(3):
            if i!=j:
                tot += ks[i]**pa * ks[j]**pb
    return tot

def sum_ineqjneqk(pa,pb,pc):
    # sum_{i!=j!=k} : the paper's triple sum. Interpret as all i,j,k distinct = 6 permutations
    tot = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i!=j and j!=k and i!=k:
                    tot += ks[i]**pa * ks[j]**pb * ks[k]**pc
    return tot

prodk2 = (k1*k2*k3)**2

# Cai Eq (result), A_T, epsilon=3/2 already substituted:
A_T = sp.Rational(3,256)/prodk2 * (
      3*sum_single(9)
    + sum_ineqj(7,2)
    - 9*sum_ineqj(6,3)
    + 5*sum_ineqj(5,4)
    - 66*sum_ineqjneqk(5,2,2)
    + 9*sum_ineqjneqk(4,3,2)
)

# f_NL normalization: |B|_NL = (10/3) A / sum_i k_i^3
def fNL(expr):
    return sp.Rational(10,3)*expr/sum_single(3)

# Equilateral: k1=k2=k3=k
Aeq = sp.simplify(A_T.subs({k2:k1,k3:k1}))
feq = sp.simplify(fNL(A_T).subs({k2:k1,k3:k1}))
print("Equilateral A_T =", Aeq)
print("Equilateral f_NL =", feq, "   (Cai published -255/64 =", sp.Rational(-255,64),")")

# Local isoceles k1<<k2=k3=k : set k2=k3=k, expand small k1, leading nonvanishing term
k = sp.symbols('k', positive=True)
expr = fNL(A_T).subs({k2:k,k3:k})
# series in k1 around 0
ser = sp.series(sp.simplify(expr), k1, 0, 4).removeO()
print("f_NL local series in k1:", sp.simplify(ser))
lim = sp.limit(expr, k1, 0)
print("f_NL local limit k1->0 =", sp.simplify(lim), "  (Cai published -35/8 =", sp.Rational(-35,8),")")
