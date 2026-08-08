#!/usr/bin/env python3
"""One-off ApJS-framed Gemini INT review of the P3 ApJS variant (directive L test).

Reuses call_gemini / loadenv / parse_verdict from int_api_review_2026-07-08.py so
the upload path, model resolution, and verdict parsing are identical to the
production INT leg. The ONLY differences are:
  (1) the PDF is submissions/P3_apjs/paper3_apjs_v3.1.155.pdf (the ApJS variant), and
  (2) the referee prompt/system-instruction says "The Astrophysical Journal
      Supplement Series (ApJS)" instead of "Physical Review D".

Hypothesis under test: the venue-class REJECT the three PRD referees returned
flips when the venue matches the paper's true type (catalog / data release).

Saves raw verbatim response + verdict to
project-context/peer-reviews/INT_api/H17_2026-07-10/API_P3apjs_gemini.md
"""
import os, sys, json, time, datetime, pathlib
import importlib.util

from bigbounce_preflight import DEFAULT_RULES, PortfolioError, verify_receipt

REPO = pathlib.Path("/Users/houstongolden/Desktop/CODE_YOU/bigbounce")
PDF = REPO / "submissions/P3_apjs/paper3_apjs_v3.1.155.pdf"
OUTDIR = REPO / "project-context/peer-reviews/INT_api/H17_2026-07-10"
OUTFILE = OUTDIR / "API_P3apjs_gemini.md"

# import the production script as a module to reuse its functions verbatim
spec = importlib.util.spec_from_file_location(
    "int_api", str(REPO / "tools/int_api_review_2026-07-08.py"))
int_api = importlib.util.module_from_spec(spec)
spec.loader.exec_module(int_api)

# ApJS-adapted referee prompt (structurally identical to the PRD prompt, venue swapped)
APJS_PROMPT = (
    "You are an expert referee for The Astrophysical Journal Supplement Series "
    "(ApJS). ApJS is the AAS catalog / data-release / methods journal: it exists "
    "for exactly this kind of paper --- large released catalogs, data-mining "
    "pipelines, and machine-readable data products with reproducibility scripts. "
    "Review this manuscript to the standard of a real ApJS submission. Respond "
    "with exactly: "
    "(1) VERDICT: ACCEPT / MINOR REVISIONS / MAJOR REVISIONS / REJECT. "
    "(2) ISSUES: numbered, each prefixed [MAJOR] or [MINOR], naming the specific "
    "section/claim and concrete problem. "
    "(3) One sentence: is the central claim (the released multi-survey anomaly "
    "catalog) supported and appropriate for ApJS?"
)

# monkeypatch the module PROMPT + system instruction to the ApJS framing.
int_api.PROMPT = APJS_PROMPT
# call_gemini hard-codes a "Physical Review D referee" system instruction; wrap it.
_orig_call_gemini = int_api.call_gemini


def apjs_call_gemini(pdf_path):
    import requests, base64
    key = int_api.ENV["GEMINI_API_KEY"]
    model = int_api._gemini_model()
    size = os.path.getsize(pdf_path)
    if size <= int_api.GEMINI_INLINE_MAX:
        b64 = base64.b64encode(open(pdf_path, "rb").read()).decode()
        part = {"inline_data": {"mime_type": "application/pdf", "data": b64}}
        modality = "native-PDF (inline_data base64)"
    else:
        uri, _ = int_api._gemini_upload(pdf_path, key)
        part = {"file_data": {"mime_type": "application/pdf", "file_uri": uri}}
        modality = "native-PDF (Files/media upload file_uri)"
    payload = {
        "systemInstruction": {"parts": [{"text":
            "You are an expert referee for The Astrophysical Journal Supplement Series (ApJS)."}]},
        "contents": [{"role": "user", "parts": [part, {"text": APJS_PROMPT}]}],
    }
    r = requests.post(
        f"{int_api.GEMINI_BASE}/v1beta/models/{model}:generateContent",
        headers={"x-goog-api-key": key, "Content-Type": "application/json"},
        json=payload, timeout=int_api.REQ_TIMEOUT,
    )
    if r.status_code != 200:
        raise RuntimeError(f"generateContent HTTP {r.status_code}: {r.text[:400]}")
    j = r.json()
    parts = []
    for cand in j.get("candidates", []):
        for c in cand.get("content", {}).get("parts", []):
            if c.get("text"):
                parts.append(c["text"])
    txt = "\n".join(parts)
    return txt, {"usage": j.get("usageMetadata", {}), "modality": modality, "model": model}


def require_verified_preflight():
    """Fail closed unless a current PASS receipt binds all six canonical papers."""
    value = os.environ.get("BIGBOUNCE_PREFLIGHT_RECEIPT", "").strip()
    if not value:
        raise PortfolioError(
            "BIGBOUNCE_PREFLIGHT_RECEIPT is required before Gemini review dispatch"
        )
    receipt = verify_receipt(
        REPO, REPO / DEFAULT_RULES, pathlib.Path(value).expanduser()
    )
    canonical_papers = [
        item
        for item in receipt.get("papers", [])
        if not (isinstance(item, dict) and item.get("draft"))
    ]
    if receipt.get("paper_count") != 6 or len(canonical_papers) != 6:
        raise PortfolioError("preflight receipt does not bind all six canonical papers")
    return receipt


def main():
    try:
        preflight = require_verified_preflight()
    except (PortfolioError, OSError) as exc:
        print(f"[FAIL] portfolio preflight: {exc}")
        return 2
    if not PDF.exists():
        print(f"[FAIL] PDF not found: {PDF}")
        return 1
    OUTDIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.datetime.utcnow().isoformat() + "Z"
    model = int_api._gemini_model()
    last_err = None
    for attempt in (1, 2):
        try:
            t0 = time.time()
            content, meta = apjs_call_gemini(str(PDF))
            dt = round(time.time() - t0, 1)
            eff_model = meta.get("model", model)
            verdict = int_api.parse_verdict(content)
            with open(OUTFILE, "w") as f:
                f.write(f"# INT API Review (ApJS-framed) — P3 ApJS variant v3.1.155 — gemini ({eff_model})\n")
                f.write(f"paper: P3apjs  version: v3.1.155  model: {eff_model}\n")
                f.write(f"venue-framing: The Astrophysical Journal Supplement Series (ApJS)\n")
                f.write(f"pdf: submissions/P3_apjs/paper3_apjs_v3.1.155.pdf\n")
                f.write(f"modality: {meta.get('modality')}\n")
                f.write(f"UTC: {ts}  |  latency: {dt}s  |  attempt: {attempt}\n")
                f.write(f"usage: {json.dumps(meta.get('usage', {}))}\n")
                f.write(
                    "preflight: "
                    f"schema={preflight['schema']} "
                    f"core_sha256={preflight['core_sha256']} "
                    f"receipt_sha256={preflight['receipt_sha256']} "
                    f"paper_count={preflight['paper_count']}\n"
                )
                f.write(f"PARSED VERDICT: {verdict}\n\n")
                f.write("PROMPT (verbatim):\n" + APJS_PROMPT + "\n\n")
                f.write("=" * 70 + "\nRAW RESPONSE (verbatim):\n" + "=" * 70 + "\n\n")
                f.write(content or "(empty response)")
            print(f"[OK] P3apjs gemini -> {verdict}  ({dt}s, attempt {attempt})  model={eff_model}")
            print(f"saved: {OUTFILE}")
            return 0
        except Exception as e:
            last_err = str(e)[:800]
            print(f"[retry {attempt}] {last_err[:200]}")
            time.sleep(3)
    with open(OUTFILE, "w") as f:
        f.write(f"# INT API Review (ApJS-framed) — P3 ApJS variant v3.1.155 — gemini — FAILED\n")
        f.write(f"UTC: {ts}\nERROR: {last_err}\n")
    print(f"[FAIL] {last_err[:200]}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
