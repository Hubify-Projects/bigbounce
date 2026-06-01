"""
Apply truth-audit verdicts from the 2026-06-01 subagent pass.

Three subagents independently audited the 48 open findings from the
2026-06-01 R-rounds on P1B/P2/P5 against the actual .tex files +
version-comment-block closure histories. This script applies their
verdicts via the Convex findings.truthAudit + findings.close mutations.

Per feedback_peer_review_truth_audit_protocol: FALSIFIED/STALE/OPINION/
OUT-OF-SCOPE verdicts close with closureStatus = closed-by-truth-audit-
falsification. VERIFIED verdicts stay open for real-action closure.
"""
import json
import os
import ssl
import sys
import urllib.error
import urllib.request

try:
    import certifi
    _CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    _CTX = ssl.create_default_context()

CONVEX_URL = os.environ.get("CONVEX_URL", "https://brilliant-panther-471.convex.cloud")

# Encoded verdicts from the 3 subagent passes (P1B, P2, P5).
VERDICTS = [
    # P1B — all 12 closeable, no VERIFIED
    {"_id": "jh7fskttv621pjjpcc5tnta8ax87v36v", "verdict": "STALE", "evidence": "Abstract L298-301 + scope L341-344 + §IV.B L668-673 + conclusions L980-982: pipeline-vs-sky disclaimer present in 4 places.", "note": "Pipeline-validation-not-sky-detection disclaimer present in abstract, intro scope, §IV.B header, and conclusions."},
    {"_id": "jh79j6te9fs9rx5ytawejjj79587t2d4", "verdict": "STALE", "evidence": "L554-570, L752-766, L1051, L975: paper explicitly states ln B not reported, queues PolyChord/MultiNest.", "note": "Paper does not claim a Bayes factor; explicitly states ln B omitted with technical reason and queues nested sampling."},
    {"_id": "jh73bdkd43r5sgrtvem5rbe90h87tad8", "verdict": "STALE", "evidence": "Abstract L304-306, intro L346-352, §VI L778-784, conclusions L990-991, claims table L1083: 'not a distinctive ECH prediction' in 5 locations.", "note": "ALP-not-distinctive disclaimer in 5 separate locations."},
    {"_id": "jh71mrqfwn0pqg24wqxayvrpn987tv76", "verdict": "STALE", "evidence": "§V.B L752-766 + Appendix A L1051 + claims table L1078: AIC/BIC/lnB explicitly listed as 'Omitted (pending) - v1B.0.18+ Nested Sampling'.", "note": "Duplicate of GPT-B2; paper explicitly does not report and documents the reason."},
    {"_id": "jh7cea6sb3xxx93wzsygjj901d87vg42", "verdict": "STALE", "evidence": "Table 1B L509 fn:wcaveat + physics interp L536-538 'disfavors (in marg-tail sense; see fn:wcaveat)'.", "note": "+4.3σ table cell carries explicit footnote stating it is NOT Bayes-factor/frequentist tension."},
    {"_id": "jh7ebtjh0bvxcc8qhtr9zc29h987thqc", "verdict": "OPINION", "evidence": "§IV.B L683-691 (purify_b=True, mode-coupling) + L711-723 bias quantification 0.032-0.040°.", "note": "Apodized-mask treatment + quantified bias already present; reviewer asks for stylistic 'more detail'."},
    {"_id": "jh77pfndsmdh6zqe8yaa8hdtfs87ty0t", "verdict": "OPINION", "evidence": "Lines 1-265 are %-prefixed TeX comments not rendered in PDF; v1B.0.28 closure block L126-128 documents pre-arXiv strip as Houston-sign-off-gated.", "note": "TeX-source comments not rendered in PDF; pre-arXiv scrub documented as gated task."},
    {"_id": "jh7ckak8yv6kttcwf456a44n9x87ttsn", "verdict": "OPINION", "evidence": "Abstract L297-301 carries SNR figure with 'pipeline-recovery bias 0.032°' framing + explicit 'not a sky-detection significance claim' adjacent.", "note": "Reframe-with-disclaimer vs remove is a stylistic editorial choice the paper has made."},
    {"_id": "jh7215rqjsep3dnb4129hwk0p987tcpe", "verdict": "STALE", "evidence": "Table 1B L509 σ column carries fn:wcaveat + '(marg.-tail, +4.3σ)' inline qualifier.", "note": "σ cell already qualified inline + explicit no-evidence-metric footnote."},
    {"_id": "jh705z132f6kftf01se6msrg4x87t8mk", "verdict": "OPINION", "evidence": "Title literally 'Technical Verification Companion ... for the ECH Spin-Torsion Program' + intro §1 L330-360 'Scope of this paper' three-bullet scope-limitation list.", "note": "'Companion' framing explicitly admits this paper does not test ECH directly."},
    {"_id": "jh7c1ykxhkymnzn9nxwmsfvvrd87vmdh", "verdict": "STALE", "evidence": "L884 mcmc_inventory caption + L920-933 'ln B recompute queued for v1B.0.16+' + L944-946 'in flight for Paper I(a)'.", "note": "Anchor language already qualified as 'parameter posterior available; ln B queued'."},
    {"_id": "jh79f4p1zq944sgwxem5t68aan87v540", "verdict": "OPINION", "evidence": "§III §V L437-453: 'compatibility check' (positive consistency) vs 'not a discriminator' (negative null) are logically complementary not contradictory.", "note": "Two framings describe different aspects of the same null result."},

    # P2 — 17 closeable, 1 VERIFIED (PER-M2)
    {"_id": "jh793gg8jv97dvxjr2ac7w9y3987vtaa", "verdict": "STALE", "evidence": "v1.7.37 abstract L99 'headline envelope is therefore BF~10-17 at the broad-multifield competitor (a curvaton-natural [-5,+5] competitor narrows this to a lower-envelope sensitivity check of BF~4)'.", "note": "Exact Resolution A already applied in v1.7.37 R-next-f-MAJ-1."},
    {"_id": "jh7bxa80600hjpm97menvxvsp587t6r9", "verdict": "STALE", "evidence": "v1.7.37 conclusion L489 already states '|-35/16|/σ(fNL)≈3.1 → r=0.84 template overlap → 1.5-2.5σ post-systematic'.", "note": "Conclusion 3.1 → 1.5-2.5σ chain already rewritten in v1.7.37 R-next-f-MIN-1."},
    {"_id": "jh7cw8d3jdqq09p180mvf1n5dx87tn0m", "verdict": "STALE", "evidence": "§6 + Table 2 four-corner prior grid: σ_theory ∈ {0.5, 1.0, 2.0, delta} × narrow/broad competitor; scipy.stats.norm recomputes 4.01/9.80/13.91/5.65/7.00/17.10; explicit 'upper bounds given current theoretical uncertainty' L325.", "note": "Prior sensitivity is the most thoroughly mapped section of the paper."},
    {"_id": "jh75f85g9ar6v5neqn0yn7tc6587t1eq", "verdict": "STALE", "evidence": "§3.2 L223-228: 10 weighting schemes; range [0.829, 0.876]; ℓ-space Fisher + 200 MC injections + 10000-sample null-space scan with all 4 numerical anchors.", "note": "r=0.84±0.02 methodology exhaustively documented across §2.1 and §3.2."},
    {"_id": "jh7ckd0jd3fky67at4gdhewp8187t84x", "verdict": "STALE", "evidence": "§7.2 L369: 'widens by O(20-50%) → ~4.0-4.5σ at central 30% degradation, ~3.5-3.7σ at conservative 50% end'.", "note": "Universality-relaxation impact already quantified with central+conservative numbers."},
    {"_id": "jh76d5qt22rekdq7bzpgjqcqax87v2xj", "verdict": "STALE", "evidence": "§7.1-7.4 Tables + L414 'estimated O(10-30%) combined degradation; SPHEREx can test fNL=-35/8 at >3σ'.", "note": "Combined-systematic-budget estimate already on disk (10-30% joint degradation, headline 3-5σ post-budget)."},
    {"_id": "jh76ab9m0w9gcenypbmn1praqn87t6k6", "verdict": "OPINION", "evidence": "§4 L240 self-flags Fisher-invariance caveat as 'standard but non-trivial' + 'post-arXiv TODO' label.", "note": "Author-disclosed deferral; reviewer demands headline removal but with disclosure this is stylistic."},
    {"_id": "jh730qe3htx4v9j4nzhmaxkwrs87t3e8", "verdict": "STALE", "evidence": "Abstract L99 + §5 L259 + conclusion L445: MegaMapper σ(fNL)≈0.5 ideal (3-7σ realistic) flagged 'speculative motivation, not firm forecasts' in 3 places.", "note": "MegaMapper numbers already labeled speculative motivation in 3 locations."},
    {"_id": "jh7avv0c2jf3rg85bdrrk64mdd87tx34", "verdict": "STALE", "evidence": "Abstract L99: 'forecast survey estimators measure conventional Planck/local-template fNL in the gauge frame, not CFC physical-frame ... complementary theoretical discriminator, not on-sky observable'.", "note": "Exact clarifying sentence already in abstract."},
    {"_id": "jh7fmmfht9m0h11smf6yktbges87t4h3", "verdict": "FALSIFIED", "evidence": "Table 3 narrow-competitor [-5,+5] column BF=7.9-10.9 vs Table 2 broad-competitor [-15,+15] envelope BF=10-17 are separate quantities; abstract L99 explicitly notes the BF≈8-11 GR-variation spread is on the delta-prior row, distinct from the 10-17 envelope.", "note": "Reviewer conflated narrow-competitor (Table 3) with broad-competitor envelope (Table 2)."},
    {"_id": "jh74kdr328ah482kaxsvycng7h87t1e2", "verdict": "STALE", "evidence": "§7.2 L369: '20-50% widening → 5.2-5.5σ optimistic → ~4.0-4.5σ central 30% degradation → ~3.5-3.7σ conservative 50%'.", "note": "Per-tracer b_phi marginalization upper end already mapped; 3-5σ headline brackets the central case."},
    {"_id": "jh704fzpw4mh9jmex1gpvhae7d87tr26", "verdict": "OPINION", "evidence": "§3.2 L228 'no prior quantification of this overlap exists for the matter-bounce bispectrum (2009-2024)' already implicitly scopes the claim.", "note": "Stylistic preference for 'known to the authors' qualifier; 2009-2024 already scopes."},
    {"_id": "jh78vy3v9fwpawzg1bd90rawg187tv00", "verdict": "OUT-OF-SCOPE", "evidence": "Abstract L99 + §4 L240-242 cite Heinrich et al. 2024 with sensitivity-recast framing + Fisher-fiducial-shift caveat disclosure.", "note": "Reviewer-side citation-verification failure is not a paper defect; recast is documented."},
    {"_id": "jh79cg2ye846500kbn97e37a0587tvys", "verdict": "STALE", "evidence": "§4 L240: 'leading-order linearization ... standard but non-trivial Fisher-forecast assumption ... post-arXiv TODO'.", "note": "Author-disclosed deferral with explicit TODO label; not a hidden assumption."},
    {"_id": "jh7dvje5dp75364kysqh1dy4e587vwq6", "verdict": "STALE", "evidence": "Conclusion L489 + Abstract L99 + Intro L108 all use 'O(slow-roll) residuals' framing; v1.7.34 R-next-a-MAJ-2 closure documented in comment block.", "note": "Three-place CFC-residual softening already applied in v1.7.34."},
    {"_id": "jh7c3efma7jn9cxmjz55p5e2ph87tnd6", "verdict": "VERIFIED", "evidence": "§2.1 L140-144 uses (c1...c6) = (2,7,3,-12,-69,19); footnote treats Cai (3,1,-9,5,-66,9) as 'a different valid solution', but prose does not explicitly disclaim that underdetermination is internal to this paper's basis vs property of Cai's treatment.", "note": ""},
    {"_id": "jh7ex3j0sq48wtmnfn8bd1n1jx87vkqc", "verdict": "STALE", "evidence": "Appendix A L506-518: c=1 vs c=2 convention difference scales B_ζ linearly; L518 'detection significance |fNL|/σ(fNL) is convention-independent, since σ(fNL) scales inversely with c'.", "note": "App.A.1 explicitly addresses convention-independence."},
    {"_id": "jh737b6zvz2qasqp1gpw5wmk6x87v69k", "verdict": "STALE", "evidence": "§4 L240: 'Seljak ... McDonald & Seljak ... Karagiannis et al. underwrites Heinrich bispectrum-channel forecast, not original power-spectrum cancellation alone'.", "note": "Provenance attribution and Karagiannis vs Seljak distinction already explicit."},

    # P5 — 16 closeable, 2 VERIFIED (GRO-M1, PER-M1)
    {"_id": "jh7dscbtd81athwaxkbtcjwfr187v8rz", "verdict": "OPINION", "evidence": "§XI.B L1601-1626: operator def, dimensional analysis g_φ |∇φ|/H_0, EFT cites (AlexanderYunes2009, LueWangKamionkowski1999), self-labels as first-order parameterization not full ALP-coupling exclusion. v0.1.32 GEM-M2 closure L33-42.", "note": "Reviewer asks for more rigor on a section the paper already labels first-order parameterization."},
    {"_id": "jh72bbjk3txjjfk7xz052kkx3587tr1t", "verdict": "OPINION", "evidence": "L1296-1305 reports mean +0.020, std 1.184, skewness +0.044, kurtosis +0.825 on 1821 valid pixels as shot-noise diagnostic + companion JSON.", "note": "Shot-noise diagnostic already at moments-of-distribution level; reviewer's 'enhance' is vague."},
    {"_id": "jh76ft4v0nv8sqz1cwsdhptgdh87tt0j", "verdict": "FALSIFIED", "evidence": "§VIII Phase 2 sweep L774-837 + Table II L784-805: 9-cell R_s × λ_th scan already reports max f_CW range 0.22 pp invariant.", "note": "Sensitivity analysis already exists at exactly the requested granularity."},
    {"_id": "jh7dezczkm5shzvh6haw7312md87vvye", "verdict": "STALE", "evidence": "v0.1.31 R-ext-GRO-M2 closure: Tempel rewritten as 'supporting rather than load-bearing'; abstract L177-184 + §IX confirm in v0.1.32; Jeffreys 95% CIs in Table III L869 and figure L919-933.", "note": "Tempel already downgraded from cross-validation to supporting consistency check."},
    {"_id": "jh787et6hf9p9mkddap15b5dn987tqvj", "verdict": "OPINION", "evidence": "Jeffreys 95% binomial CIs (Tempel, density) + Bonferroni-LEE on multi-bin §V.A L451-467 + P4-monopole residual decomp L1296-1305.", "note": "Uncertainty budget threaded per-test rather than centralized; stylistic restructuring ask."},
    {"_id": "jh7e7r4mpkza7pac0q9qw78wa187tqs0", "verdict": "FALSIFIED", "evidence": "Grep for 'Bayes', 'likelihood ratio', 'nuisance' across .tex returns zero hits; paper reports binomial σ-from-half and Bonferroni-LEE.", "note": "Reviewer critiques framing the paper never adopts."},
    {"_id": "jh729whkrmd2gzrb7wcr6xqbc187t988", "verdict": "STALE", "evidence": "v0.1.31 GRO-B1 closure L54-60: V-Web headline because the paper is about V-Web environmental classification; DESIVAST Δf_CW=0.0007, n=56981 already in abstract L185-210.", "note": "Documented stylistic decision in prior round; DESIVAST result already carried right after V-Web headline."},
    {"_id": "jh777mc3wt09w1d2xn19j8c6md87tcrt", "verdict": "OPINION", "evidence": "§XI.B L1601-1626 self-labels as first-order parameterization + explicit scope-bound 'fully model-dependent transfer-function calculations beyond scope of this companion paper'; EFT cites are real.", "note": "Reviewer asks for deletion of a section the paper already correctly bounds in scope."},
    {"_id": "jh7b6g4059ehkx3hh3w8fb8nzs87vvmp", "verdict": "VERIFIED", "evidence": "§ density quintile and §VIII voids-vs-chirality use 727-pixel pre-selected subset L1316; per-quintile |σ_obs-σ_pred| table deferred per v0.1.31 GRO-min2 L76-78; HEALPix robustness grid reported L1328-1339 but per-quintile residual σ table not.", "note": ""},
    {"_id": "jh75c0r3h286qe33j4yq1zct0n87v0wh", "verdict": "STALE", "evidence": "v0.1.32 GEM-M1 closure L27-32: Limitations §XII anisotropy paragraph L1550-1562 added (Kaiser+FoG anisotropic eigenvalue deformation, sub-percent contamination expectation).", "note": "Anisotropy caveat present in §XII Limitations as of v0.1.32 with quantitative contamination estimate."},
    {"_id": "jh730ecpt05n3gawp3ayy1bg5h87t36x", "verdict": "STALE", "evidence": "Abstract L177-184 + §IX: Tempel relabeled 'supporting rather than load-bearing per R-ext-GRO-M2'; v0.1.31 closure L66-70.", "note": "Already relabeled to qualitative sanity check in prior round."},
    {"_id": "jh78tsvk56sdw6086a3fe1nx2s87txtx", "verdict": "STALE", "evidence": "Abstract L186-189 already concedes 'methodologically correlated by construction because they reuse the same matched-spiral subsample'.", "note": "Correlation already stated; four DESIVAST tests vary on distinct axes."},
    {"_id": "jh70j4jkp3fe4rehwyndj9d38h87td8h", "verdict": "FALSIFIED", "evidence": "Bibitem TWebDESI2026 L1723-1726 cites arXiv:2604.02463 (April 2026). Today is 2026-06-01; April 2026 arXiv IDs are not future.", "note": "Reviewer's 'future arXiv ID' premise is wrong against current date."},
    {"_id": "jh790c0jp3458j4v6c2a2pajyh87v9r9", "verdict": "FALSIFIED", "evidence": "ASTRADESI2026 L1728-1732 cites arXiv:2604.01456 (April 2026). Same date-arithmetic error as PER-B1.", "note": "April 2026 arXiv IDs are in the past relative to 2026-06-01."},
    {"_id": "jh7d3vf0dcx0tm8vjsvfpr8ayh87vmbe", "verdict": "FALSIFIED", "evidence": "DESIVAST2025 L1734-1738 cites ApJ 982, 38 (2025) and arXiv:2411.00148 (Nov 2024). Both past dates relative to 2026-06-01.", "note": "Reviewer's date arithmetic is wrong; both ApJ 982 and 2411.00148 are past."},
    {"_id": "jh75av73kas29e29cfqcgc82jh87v91v", "verdict": "VERIFIED", "evidence": "Bibitems golden_chirality_2026 L1669-1675 and golden_fnl_2026 L1677-1682 formatted as journal-style citations with 'companion paper (Paper IV/II), 2026' but only artifact paths and version tags — no arXiv ID, DOI, or submission venue.", "note": ""},
    {"_id": "jh78tmtsmedhmwmf8d9xt4xazx87tw7h", "verdict": "FALSIFIED", "evidence": "Depends on PER-B1/B2/B3 which are FALSIFIED on date arithmetic; §VII.E discussion consistent with bibliography entries.", "note": "Mischaracterization downstream of fabricated-citation claim which fails on date arithmetic."},
    {"_id": "jh7dq209b26y3txee9kr2m4gqn87twaj", "verdict": "OPINION", "evidence": "Hahn2007, Hoffman2012, Cautun2014, Planck2018cosmoparams all have title+journal+volume+arXiv; DOIs missing but arXiv IDs make all four independently verifiable.", "note": "Stylistic preference for DOI-augmented metadata; existing entries are sufficient."},
]


def convex_call(path: str, args: dict, kind: str = "mutation") -> dict:
    url = f"{CONVEX_URL}/api/{kind}"
    body = json.dumps({"path": path, "args": args, "format": "json"}).encode("utf-8")
    req = urllib.request.Request(
        url, data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30, context=_CTX) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return {"error": e.read().decode("utf-8", errors="replace")[:400]}


def main():
    audited = 0
    closed = 0
    kept_open = 0
    fail = 0

    for v in VERDICTS:
        # 1) Apply truth-audit verdict
        r = convex_call("findings:truthAudit", {
            "findingId": v["_id"],
            "verdict": v["verdict"],
            "evidence": v["evidence"][:1000],
        })
        if isinstance(r, dict) and "error" in r:
            print(f"FAIL audit {v['_id']}: {r['error'][:200]}", file=sys.stderr)
            fail += 1
            continue
        audited += 1

        # 2) If not VERIFIED, close
        if v["verdict"] != "VERIFIED":
            r2 = convex_call("findings:close", {
                "findingId": v["_id"],
                "closureStatus": "closed-by-truth-audit-falsification",
                "closureNote": f"truth-audit {v['verdict']}: {v.get('note', '')[:500]}",
            })
            if isinstance(r2, dict) and "error" in r2:
                print(f"FAIL close {v['_id']}: {r2['error'][:200]}", file=sys.stderr)
                fail += 1
            else:
                closed += 1
        else:
            kept_open += 1
            print(f"  KEPT OPEN (VERIFIED): {v['_id']} → real-action closure needed")

    print(f"\n=== Summary ===")
    print(f"  Audited: {audited}")
    print(f"  Closed (FALSIFIED/STALE/OPINION/OUT-OF-SCOPE): {closed}")
    print(f"  Kept open (VERIFIED): {kept_open}")
    print(f"  Failures: {fail}")

    # Print final state
    states = convex_call("papers:listAllPaperStates", {}, kind="query")
    if isinstance(states, dict) and "value" in states:
        states = states["value"]
    print(f"\n=== Final Convex paper state ===")
    for s in states:
        print(f"  {s['number']:<3} {(s.get('currentVersion') or '?'):<10} "
              f"readiness={s['readinessComputed']:>3}  "
              f"open: {s.get('openBlockers', 0)}B/{s.get('openMajors', 0)}M/"
              f"{s.get('openMinors', 0)}m/{s.get('openCaveats', 0)}C")


if __name__ == "__main__":
    main()
