#!/usr/bin/env python3
"""Backgrounds for row 9b, each exposing exactly what the Bardeen (Phi, Xi) system needs.

A background is a list of CHARTS.  Each chart gives, as a function of its own integration variable s:
    a(s), Hc(s) = a'/a, Q(s) = Hc^2 - Hc' = -a^2 Hdot,  and the Jacobian J(s) = d eta / d s.
eta itself is carried as an ODE state variable, so no interpolation of the background is ever used.

The three backgrounds are the ones committed in `../a2_transmission_linear.py` and
`../lane9b2_s2_rawadm/lane9b2_s2_rawadm.py`, reproduced here in closed form (verified against those
modules by the gates in row9b_numeric.py):

  QUINTIN   piecewise: Hdot = Upsilon inside |t| <= tm, -3/2 H^2 outside.  Q NEVER vanishes (Hdot jumps
            between the two signs), so this background has no smooth NEC crossing.  Chart = cosmic time.
  LQC       effective dust, rho_c = 1: H^2 = (x/3)(1-x), a = x^{-1/3}, Hdot = -x(1-2x)/2.
            Q = x^{1/3}(1/2 - x) has a SIMPLE zero at x = 1/2 on each side.  Charts: w = sgn(eta) sqrt(1-x)
            through the core (regular at the bounce), y = ln x in the two dust tails.
  POLY      a = 1 + eta^2 (eta_b = 1).  Q = 2(3 eta^2 - 1)/(1 + eta^2)^2, simple zeros at eta = +-1/sqrt(3).
            Chart = eta itself.
"""
import numpy as np
from scipy.integrate import quad
from scipy.special import erf

SQ3 = np.sqrt(3.0)


class Chart:
    def __init__(self, s0, s1, fields, name):
        self.s0, self.s1, self.fields, self.name = float(s0), float(s1), fields, name


# --------------------------------------------------------------------------- Quintin (control)
class Quintin:
    label = "Quintin2015-type"
    has_crossing = False

    def __init__(self, dtB=1.0, t_far=400.0):
        self.Ups = 8.0 / (3.0 * dtB**2)
        self.tm = dtB / 2.0
        self.am = np.exp(self.Ups * self.tm**2 / 2.0)
        self.eta_B = float(np.sqrt(np.pi / (2 * self.Ups)) * erf(self.tm * np.sqrt(self.Ups / 2)))
        self.A = self.am**3 / (9.0 * self.tm**2)
        self.eta_off = 3.0 * self.tm / self.am - self.eta_B     # eta = eta_m + sgn * eta_off
        self.t_far = float(t_far)
        self.eta_start = float(self._eta(-t_far))
        self.eta_m_start = self.eta_start + self.eta_off        # sgn = -1
        self.eta_end = -self.eta_start
        self.eta_m_end = self.eta_end - self.eta_off
        # crossings of Q: none.  NEC boundary (Hdot sign change) at |t| = tm, i.e. |eta| = eta_B.
        self.crossings_eta = []
        self.crossings_s = []
        self.first_crossing = None
        self.eta_NEC = self.eta_B

    def _a(self, t):
        return np.exp(self.Ups * t * t / 2) if abs(t) <= self.tm else self.am * (abs(t) / self.tm) ** (2.0 / 3.0)

    def _H(self, t):
        return self.Ups * t if abs(t) <= self.tm else 2.0 / (3.0 * t)

    def _Hd(self, t):
        return self.Ups if abs(t) <= self.tm else -1.5 * self._H(t) ** 2

    def _eta(self, t):
        if abs(t) <= self.tm:
            return float(np.sqrt(np.pi / (2 * self.Ups)) * erf(t * np.sqrt(self.Ups / 2)))
        em = np.sign(t) * 3.0 * self.tm ** (2.0 / 3.0) * abs(t) ** (1.0 / 3.0) / self.am
        return float(em + np.sign(t) * self.eta_off)

    def _f(self, t):
        a, H, Hd = self._a(t), self._H(t), self._Hd(t)
        return a, a * H, -a * a * Hd, 1.0 / a          # a, Hc, Q, J = deta/dt

    def charts(self):
        # split at the two Hdot jumps so the solver never straddles a discontinuity
        return [Chart(-self.t_far, -self.tm, self._f, "contraction"),
                Chart(-self.tm, self.tm, self._f, "window"),
                Chart(self.tm, self.t_far, self._f, "expansion")]

    def eta_of_chart(self, ichart, s):                 # analytic, used only for reporting
        return self._eta(s)

    def wronskian_window(self):
        """Sub-domain for the Wronskian gate: |t| <= 2 tm, spanning both Hdot jumps and H = 0.
        The gate must be run on a BOUNDED sub-domain -- over the full dust tails the two basis
        solutions differ by many orders of magnitude and W is a catastrophic cancellation."""
        return [(0, -2 * self.tm, -self.tm), (1, -self.tm, self.tm), (2, self.tm, 2 * self.tm)]


# --------------------------------------------------------------------------- LQC effective dust
class LQC:
    label = "LQC-effective-dust"
    has_crossing = True

    def __init__(self, x_i=1e-10, x_split=0.1):
        self.x_i, self.x_split = float(x_i), float(x_split)
        self.w_split = float(np.sqrt(1.0 - x_split))
        # eta measured from the bounce (eta = 0 at x = 1)
        self.eta_core_half = float(quad(lambda w: 2.0 / (SQ3 * (1.0 - w * w) ** (7.0 / 6.0)),
                                        0.0, self.w_split, limit=400)[0])
        # int x^{-7/6}(1-x)^{-1/2} dx  =  6(x_i^{-1/6} - x_s^{-1/6})  +  R,  R regular at x -> 0
        self._R = float(quad(lambda xx: xx ** (-7.0 / 6.0) * (1.0 / np.sqrt(1.0 - xx) - 1.0),
                             self.x_i, self.x_split, limit=400)[0])
        self.eta_tail = float((6.0 * (self.x_i ** (-1.0 / 6.0) - self.x_split ** (-1.0 / 6.0))
                               + self._R) / SQ3)
        self.eta_start = -(self.eta_core_half + self.eta_tail)
        self.eta_end = -self.eta_start
        # dust-tail asymptote  a = (eta_c0 - eta)^2 / 12  (contracting);  A = 1/12 exactly
        self.A = 1.0 / 12.0
        #   eta_c0 = -eta_core_half + (6 x_split^{-1/6} - R)/sqrt(3)   (x_i-independent up to O(x_i^{5/6}))
        self.eta_c0 = float(-self.eta_core_half
                            + (6.0 * self.x_split ** (-1.0 / 6.0) - self._R) / SQ3)
        self.eta_m_start = self.eta_start - self.eta_c0     # negative
        self.eta_m_end = self.eta_end + self.eta_c0
        # Q = x^{1/3}(1/2 - x): simple zero at x = 1/2  ->  w = +-sqrt(1/2)
        self.w_c = float(np.sqrt(0.5))
        self.eta_B = float(quad(lambda w: 2.0 / (SQ3 * (1.0 - w * w) ** (7.0 / 6.0)),
                                0.0, self.w_c, limit=400)[0])
        self.crossings_eta = [-self.eta_B, self.eta_B]
        self.crossings_s = [(1, -self.w_c), (1, self.w_c)]
        self.first_crossing = (1, -self.w_c)
        self.eta_NEC = self.eta_B

    # ---- chart C (core): s = w = sgn(eta) sqrt(1-x)
    @staticmethod
    def _fw(w):
        x = 1.0 - w * w
        a = x ** (-1.0 / 3.0)
        Hc = x ** (1.0 / 6.0) * w / SQ3
        Q = x ** (1.0 / 3.0) * (0.5 - x)
        J = 2.0 / (SQ3 * x ** (7.0 / 6.0))
        return a, Hc, Q, J

    # ---- charts L/R (dust tails): s = y = ln x, sigma = -1 (contracting) / +1 (expanding)
    @staticmethod
    def _fy(y, sigma):
        x = np.exp(y)
        w = sigma * np.sqrt(1.0 - x)
        a = x ** (-1.0 / 3.0)
        Hc = x ** (1.0 / 6.0) * w / SQ3
        Q = x ** (1.0 / 3.0) * (0.5 - x)
        J = -1.0 / (3.0 * Hc)
        return a, Hc, Q, J

    def charts(self):
        ys, yi = np.log(self.x_split), np.log(self.x_i)
        return [Chart(yi, ys, lambda y: self._fy(y, -1.0), "tail-contracting"),
                Chart(-self.w_split, self.w_split, self._fw, "core"),
                Chart(ys, yi, lambda y: self._fy(y, +1.0), "tail-expanding")]

    def wronskian_window(self):
        """Core chart only, w in [-0.9, 0.9] (x from 0.19 to 1): spans both Q = 0 crossings and H = 0."""
        return [(1, -0.9, 0.9)]

    def Qprime_at_crossing(self):
        """dQ/deta at x = 1/2 (contracting branch, w = -w_c) in closed form:
        dQ/dx = x^{-2/3}(1 - 8x)/6 ;  dx/deta = -3 x Hc."""
        out = []
        for w in (-self.w_c, self.w_c):
            x = 1.0 - w * w
            Hc = x ** (1.0 / 6.0) * w / SQ3
            dQdx = x ** (-2.0 / 3.0) * (1.0 - 8.0 * x) / 6.0
            out.append(float(dQdx * (-3.0 * x * Hc)))
        return out


# --------------------------------------------------------------------------- poly (analytic non-LQC)
class Poly:
    label = "poly-analytic-nonLQC"
    has_crossing = True

    def __init__(self, eta_far=4000.0):
        self.eta_far = float(eta_far)
        self.eta_start, self.eta_end = -self.eta_far, self.eta_far
        # a = 1 + eta^2 -> dust asymptote a ~ eta^2, A = 1, eta_c0 = 0
        self.A = 1.0
        self.eta_c0 = 0.0
        self.eta_m_start, self.eta_m_end = self.eta_start, self.eta_end
        self.eta_B = float(1.0 / SQ3)
        self.crossings_eta = [-self.eta_B, self.eta_B]
        self.crossings_s = [(0, -self.eta_B), (0, self.eta_B)]
        self.first_crossing = (0, -self.eta_B)
        self.eta_NEC = self.eta_B

    @staticmethod
    def _f(e):
        a = 1.0 + e * e
        Hc = 2.0 * e / a
        Q = 2.0 * (3.0 * e * e - 1.0) / (a * a)
        return a, Hc, Q, 1.0

    def charts(self):
        return [Chart(self.eta_start, self.eta_end, self._f, "full")]

    def wronskian_window(self):
        """|eta| <= 5 eta_B: spans both Q = 0 crossings and H = 0."""
        return [(0, -5 * self.eta_B, 5 * self.eta_B)]

    def Qprime_at_crossing(self):
        out = []
        for e in (-self.eta_B, self.eta_B):
            a = 1.0 + e * e
            out.append(float(4.0 * e * (5.0 - 3.0 * e * e) / a ** 3))
        return out
