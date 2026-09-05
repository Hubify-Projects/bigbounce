# Row 18(b) — A3-cs-bounce: c_s-dependence of the bounce cubic term Δf_NL^bounce(c_s)

**Date:** 2026-09-04 · **Lane:** row18b_cs_bounce_cubic · **Status:** IN PROGRESS (plan header)

## Question
Row 14 established the joint (r, f_NL) window using f_NL^pre(c_s) = −165/16 + 65/(8 c_s²)
and a c_s-independent transmission T, with the bounce's own cubic contribution taken at
c_s = 1 (Δf_NL^bounce = −(5/24) ρ_B, lane-b S1 in-in). This lane asks whether the bounce
term itself carries c_s, so that

    f_NL^after(c_s) = T · f_NL^pre(c_s) + Δf_NL^bounce(c_s)

is evaluated consistently at a single c_s.

## Plan
1. c_s-scaling of each S1 cubic vertex (Seery–Lidsey/Chen form; (1/c_s²−1) factors);
   state exactly how c_s enters the S1 mode functions (z², sound horizon) and vertices.
2. Extend the lane-b integrator minimally to carry c_s; keep the c_s=1 regression gate
   (Quintin −0.1398 / LQC-dust −0.1043 / poly −0.1271 at kη_B = 1e−3).
3. Evaluate Δf_NL^bounce at c_s ∈ {0.44, 0.6, 0.8876, 1} on all three backgrounds.
4. Combine to f_NL^after(c_s); restate the |f_NL^after| ≤ 5.1 window and r = 24 c_s;
   report whether the bounce term moves the no-go boundary.

No tuning. Results, table, and paper-ready sentences appended below on completion.
