# Separate-universe failure criterion (novelty lift #2, 2026-09-04). Closed forms only; inputs frozen from
# threading_map_second_order_2026_09_04.json (constant-eps kernels) and fnl_monopole_adjudication_2026_09_03 (in-in).
import sympy as sp, json, time, os
t0=time.time(); H=os.path.dirname(os.path.abspath(__file__))
eps,mu,w=sp.symbols('epsilon mu w',real=True); eta=sp.Symbol('eta',negative=True)
es,ef=sp.symbols('epsilon_s epsilon_f',positive=True)
J=json.load(open(os.path.join(H,'threading_map_second_order_2026_09_04.json')))
S=lambda s: sp.sympify(s,locals={'epsilon':eps,'mu':mu})
out={}
# --- constant-eps background: a ~ (-eta)^p, non-constant zeta mode ~ (-eta)^g ; r = zetadot/(H zeta)
p=1/(eps-1); g=1-2*p; a=(-eta)**p; z=(-eta)**g
aH=sp.diff(a,eta)/a; r=sp.simplify(sp.diff(z,eta)/(aH*z))
assert sp.simplify(r-(eps-3))==0
Theta=sp.simplify(eps*r); lam_const=sp.simplify(1-sp.Rational(1,3)*eps)  # <eps>_zeta = eps for constant eps
out['constant_eps']=dict(growing_mode_exponent_g=str(sp.simplify(g)),zetadot_over_Hzeta=str(r),Theta=str(Theta),
    lambda_=str(lam_const),deltaK_over_Hzeta=str(-Theta),delta_rho_c_over_rho_per_zeta=str(sp.simplify(-sp.Rational(2,3)*Theta)))
# --- USR exact (linear): eps = es (a/as)^-6, zeta = zf (a/af)^3, integrate int eps dzeta / zf from as to af
x=sp.Symbol('x',positive=True)                      # x = a/a_f, from x_s to 1 ; eps = ef x^-6 ; zeta = zf x^3
xs=(ef/es)**sp.Rational(1,6)                        # a_s/a_f
mean_eps=sp.simplify(sp.integrate(ef*x**-6*sp.diff(x**3,x),(x,xs,1)))
lam_usr=sp.simplify(1-mean_eps/3)
assert sp.simplify(lam_usr-(1+ef/3-sp.sqrt(es*ef)/3))==0
out['USR_exact_linear']=dict(mean_eps_zeta=str(mean_eps),lambda_USR_exact=str(lam_usr),Theta='3*epsilon',
    numeric={f'es={a_},ef={b_}':float(lam_usr.subs({es:a_,ef:b_})) for a_,b_ in [(1e-2,1e-6),(1e-2,1e-4),(1e-3,1e-9)]})
# --- second order (frozen kernels) and general w
fm=S(J['map_fNL_pieces']['total_final_label']['const'])+S(J['map_fNL_pieces']['total_final_label']['mu2'])*mu**2
fin=sp.Rational(5,12)*(eps**2*mu**2-eps**2+6*eps-12)
fdN_final=sp.simplify(fin/lam_const+fm)
fdN_init=S(J['prediction']['initial_label']['const'])+S(J['prediction']['initial_label']['mu2'])*mu**2
assert sp.simplify(fm+sp.Rational(5,4)*eps*(1-mu**2))==0 and sp.simplify(fdN_init+5)==0
assert sp.simplify(fdN_final-(-sp.Rational(15,4)*(eps-4)/(eps-3)+sp.Rational(15,4)*eps/(3-eps)*mu**2))==0
mono=lambda f: sp.simplify(sp.integrate(f,(mu,-1,1))/2)
gap=sp.simplify(mono(fin)-(-5)); assert sp.simplify(gap-5*eps*(9-eps)/18)==0
sub={eps:sp.Rational(3,2)*(1+w)}
gw=lambda f: sp.factor(sp.simplify(f.subs(sub)))
out['second_order']=dict(f_map=str(fm),f_map_monopole=str(mono(fm)),f_inin=str(fin),f_dN_initial_label=str(fdN_init),
    f_dN_final_label=str(fdN_final),inin_minus_dN_monopole=str(gap),
    all_map_pieces_carry_eps=all(sp.simplify(S(v['const']).subs(eps,0))==0 and sp.simplify(S(v['mu2']).subs(eps,0))==0
        for k,v in J['map_fNL_pieces'].items()))
out['general_w']=dict(lambda_=str(gw(lam_const)),Theta=str(gw(Theta)),f_map=str(gw(fm)),f_map_monopole=str(gw(mono(fm))),
    f_inin=str(sp.expand(fin.subs(sub))),f_dN_initial_label='-5',f_dN_final_label=str(gw(fdN_final)),
    w0_check=str(sp.expand(fin.subs(eps,sp.Rational(3,2)))),w_minus1=dict(lambda_=str(lam_const.subs(eps,0)),f_map=str(fm.subs(eps,0))),
    w_plus1=dict(lambda_=str(lam_const.subs(eps,3)),f_inin_monopole=str(mono(fin).subs(eps,3))))
# --- validations
val={}
val['dust_eps_3_2']=dict(f_inin=str(sp.expand(fin.subs(eps,sp.Rational(3,2)))),f_dN=str(fdN_init),lambda_=str(lam_const.subs(eps,sp.Rational(3,2))),
    Theta=str(Theta.subs(eps,sp.Rational(3,2))),mean_eps_zeta='3/2',monopole_gap=str(gap.subs(eps,sp.Rational(3,2))),verdict='O(1) failure, as computed')
val['USR']=dict(lambda_minus_1=str(sp.simplify(lam_usr-1)),f_map_eps_to_0=str(fm.subs(eps,0)),
    kernels_eps_to_0=J['usr_limit']['cross_kernels_eps_to_0'],verdict='agreement to O(eps): consistent with delta N(phi,pi) = in-in = 5/2 (NFS 2013)')
val['attractor']=dict(zetadot=0,Theta=0,lambda_=1,div_cross_from_input=J['attractor_limit']['div_cross'],verdict='identity map; Maldacena consistency relation untouched')
ek={}
for e_ in [5,10,30,100]:
    gg=sp.simplify(g.subs(eps,e_)); ek[f'eps={e_}']=dict(nonconstant_mode_exponent_g=str(gg),nonconstant_mode='decays as eta->0-' if gg>0 else 'grows',
        dominant_mode='constant zeta -> Theta=0, lambda=1, identity map',Theta_if_on_nonconstant_mode=str(Theta.subs(eps,e_)),
        lambda_if_on_nonconstant_mode=str(lam_const.subs(eps,e_)),constant_eps_kernels_applicable=bool(sp.simplify((3/sp.Integer(e_)-1))>0))
val['ekpyrotic']=dict(cases=ek,verdict='dominant (constant) mode: separate universe valid (consistent with Creminelli-Nicolis-Zaldarriaga 2004); the growing-Bardeen-potential mode has Theta=eps(eps-3)>>1 and lambda<0 but decays in zeta, so it never sets zeta_L(t_f)')
out['validations']=val
out['criterion']='isotropic delta N (with N(phi,pi)) reproduces the squeezed bispectrum of comoving zeta iff <eps/c_s^2>_zeta = (1/zeta_Lf) int (eps/c_s^2) dzeta_L -> 0; failure is O(<eps>_zeta): lambda = 1 - <eps>_zeta/3, f_map = -(5 eps/4)(1-mu^2) at constant eps'
out['wall_clock_s']=round(time.time()-t0,2); out['sympy']=sp.__version__
json.dump(out,open(os.path.join(H,'separate_universe_failure_criterion_2026_09_04.json'),'w'),indent=1,default=str)
print(json.dumps(out,indent=1,default=str))
