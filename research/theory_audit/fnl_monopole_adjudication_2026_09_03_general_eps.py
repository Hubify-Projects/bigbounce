# general constant-eps contraction: a = c (-eta)^p, p = 1/(eps-1); growing mode zeta ~ (-eta)^(1-2p)
import sympy as sp, importlib.util, sys, os, json
sys.argv=['x']
spec = importlib.util.spec_from_file_location("adj", "fnl_monopole_adjudication_2026_09_03.py")
# we re-implement compactly rather than import (import would run the whole script)
eta = sp.Symbol('eta', negative=True)
k1,k2,k3 = sp.symbols('k1 k2 k3', positive=True); KS=[k1,k2,k3]
kk, dl = sp.symbols('k delta', positive=True); mu = sp.Symbol('mu', real=True)
ep = sp.Symbol('epsilon', positive=True)
p = 1/(ep-1)
c = sp.Symbol('c', positive=True)
a = c*(-eta)**p
a2 = a**2; e = ep; calH = sp.simplify(sp.diff(a,eta)/a)
a2eps = a2*e
g = 1-2*p                       # growing-mode exponent
z1 = (-eta)**g
assert sp.simplify(sp.diff(a2eps*sp.diff(z1,eta),eta)) == 0
def dot(P,Q,R): return (R**2-P**2-Q**2)/2
verts = {
 'T1': dict(coef=a2*(e**2-e**3/2), legs=[(0,False),(1,False),(1,False)], V=lambda P,Q,R: sp.Integer(1)),
 'T3': dict(coef=-2*a2*e**2, legs=[(1,False),(0,False),(1,True)], V=lambda P,Q,R: dot(Q,R,P)/R**2),
 'T4': dict(coef=a2*e**3/2, legs=[(0,False),(1,True),(1,True)], V=lambda P,Q,R: dot(Q,R,P)**2/(Q**2*R**2)),
}
def mode1(al): return z1 if al==0 else sp.diff(z1,eta)
Fs = sp.Symbol('F')
def kern(vert,j,k,P,Q):
    legs=vert['legs']; others=[i for i in range(3) if i!=j]
    mom=[None]*3; mom[j]=k; mom[others[0]]=P; mom[others[1]]=Q
    prod = vert['coef']*vert['V'](*mom)*mode1(legs[others[0]][0])*mode1(legs[others[1]][0])
    src = prod if legs[j][0]==0 else -sp.diff(prod,eta)
    lhs = 2*sp.diff(a2eps*sp.diff(Fs*(-eta)**(2*g),eta),eta)
    ratio = sp.simplify(sp.powsimp(sp.expand_power_base(sp.powsimp(src/lhs, force=True), force=True), force=True))
    ratio = sp.simplify(ratio.subs(eta, -sp.Symbol('t', positive=True)))
    ratio = sp.simplify(sp.powsimp(sp.powdenest(ratio, force=True), force=True))
    assert not ratio.has(sp.Symbol('t', positive=True)), ratio
    return sp.simplify(sp.solve(sp.Eq(lhs,src),Fs)[0])
def redef(k,P,Q):
    pq=dot(P,Q,k); kp=(k**2+P**2-Q**2)/2; kq=(k**2+Q**2-P**2)/2
    fa = sp.simplify(mode1(0)*mode1(1)/calH/(-eta)**(2*g))
    fb = sp.simplify((e/(2*calH))*(pq/Q**2-kp*kq/(k**2*Q**2))*mode1(0)*mode1(1)/(-eta)**(2*g))
    return {'fa':sp.simplify(fa),'fb':sp.simplify(fb)}
def pieces(k,P,Q):
    out={}
    for vn,vert in verts.items():
        for j in range(3):
            for order,(pp,qq) in enumerate([(P,Q),(Q,P)]):
                others=[i for i in range(3) if i!=j]
                leg_of_long = others[0] if order==0 else others[1]
                on_chi = vert['legs'][leg_of_long][1]
                cls = 'L' if not on_chi else ('K' if vn=='T4' else 'X')
                out[(vn,j,order)] = (kern(vert,j,k,pp,qq)/2, cls)
    for order,(pp,qq) in enumerate([(P,Q),(Q,P)]):
        r = redef(k,pp,qq)
        out[('fa','r',order)] = (r['fa']/2,'L')
        out[('fb','r',order)] = (r['fb']/2, 'X' if order==1 else 'L')
    return out
Pw = {k1:k1**-3,k2:k2**-3,k3:k3**-3}
den = Pw[k1]*Pw[k2]+Pw[k1]*Pw[k3]+Pw[k2]*Pw[k3]
classes={'L':0,'K':0,'X':0}
for (kS,kO,wt) in [(k2,k3,Pw[k1]*Pw[k3]),(k3,k2,Pw[k1]*Pw[k2])]:
    for key,(F,cls) in pieces(kS,k1,kO).items():
        contrib = sp.Rational(5,6)*2*F*wt/den
        ser = sp.series(contrib.subs({k1:dl,k2:kk,k3:sp.sqrt(kk**2+dl**2+2*kk*dl*mu)}), dl, 0, 1).removeO()
        classes[cls] += sp.simplify(sp.expand(ser).coeff(dl,0))
res={}
for cls in classes:
    f = sp.factor(sp.simplify(classes[cls]))
    m = sp.factor(sp.simplify(sp.integrate(sp.expand(f),(mu,-1,1))/2)); q = sp.factor(sp.expand(f).coeff(mu,2))
    print(cls, ':', f, '| mono', m, '| mu2', q)
    res[cls]={'f_mu':str(f),'monopole':str(m),'mu2':str(q)}
tot = sp.factor(sp.simplify(sum(classes.values())))
print('TOTAL f(mu, eps) =', tot, '  at eps=3/2:', sp.expand(tot.subs(ep,sp.Rational(3,2))))
mono_tot = sp.factor(sp.simplify(sp.integrate(sp.expand(tot),(mu,-1,1))/2))
print('monopole(eps) =', mono_tot, '  isoceles(eps) =', sp.factor(tot.subs(mu,0)), '  mu2(eps) =', sp.factor(sp.expand(tot).coeff(mu,2)))
print('in-in monopole - deltaN_c(-5) =', sp.factor(mono_tot+5))
print('[L] - (-5) =', sp.factor(sp.simplify(classes['L']+5)))
print('threading factor deltaN_c/zeta =', 1-ep/3)
res['total']={'f_mu_eps':str(tot),'monopole_eps':str(mono_tot),'isoceles_eps':str(sp.factor(tot.subs(mu,0))),'mu2_eps':str(sp.factor(sp.expand(tot).coeff(mu,2)))}
json.dump(res, open('fnl_monopole_adjudication_2026_09_03_general_eps.json','w'), indent=2)
