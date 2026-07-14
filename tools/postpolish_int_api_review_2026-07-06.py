#!/usr/bin/env python3
"""POST-POLISH INT API-vendor round (native-PDF) on all 6 POLISHED bigbounce papers.

Per canonical spec §1.2-1.3:
  - XAI/Grok native-PDF: /v1/files upload + /v1/responses input_file        (grok-4.3)
  - Gemini API = known 403 -> skip + note (NOT run here)

Keys loaded from .env.local by NAME only (first token before inline comments; never printed).
Same PRD-referee prompt as prior rounds (VERDICT / ISSUES / central-claim).
Every raw response saved. A failed call = FAILED leg (recorded with error), never invented.
NEVER fabricate.
"""
import os, sys, json, time, warnings, datetime, pathlib
warnings.filterwarnings("ignore")

REPO = pathlib.Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
OUTDIR = REPO / "project-context/peer-reviews/INT_v3/POSTPOLISH_2026-07-06"
OUTDIR.mkdir(parents=True, exist_ok=True)
MANIFEST = OUTDIR / "manifest.jsonl"

# (version, polished PDF path) — the POLISHED papers
PAPERS = {
    "P4":  ("v1.0.219",  "/tmp/polished_P4.pdf"),
    "P1B": ("v1B.0.102", "/tmp/polished_P1B.pdf"),
    "P3":  ("v3.1.140",  "/tmp/polished_P3.pdf"),
    "P2":  ("v1.7.98",   "/tmp/polished_P2.pdf"),
    "P5":  ("v0.1.103",  "/tmp/polished_P5.pdf"),
    "P1A": ("v1A.0.111", "/tmp/polished_P1A.pdf"),
}

XAI_MODEL = "grok-4.3"

PROMPT = (
    "You are an expert referee for Physical Review D. Review this manuscript to the "
    "standard of a real submission. Respond with exactly: "
    "(1) VERDICT: ACCEPT / MINOR REVISIONS / MAJOR REVISIONS / REJECT. "
    "(2) ISSUES: numbered, each prefixed [MAJOR] or [MINOR], naming the specific "
    "section/claim and concrete problem. "
    "(3) One sentence: is the central claim supported?"
)


def loadenv(p=REPO / ".env.local"):
    d = {}
    for line in open(p):
        line = line.rstrip("\n")
        if not line or line.lstrip().startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        tok = v.split()[0] if v else ""  # strip trailing inline comment/note
        d[k] = tok
    return d


ENV = loadenv()
from openai import OpenAI

xai = OpenAI(api_key=ENV["XAI_API_KEY"], base_url="https://api.x.ai/v1")


def parse_verdict(text):
    if not text:
        return None
    for line in text.splitlines():
        s = line.strip()
        low = s.lower()
        if "verdict:" in low:
            after = s.split(":", 1)[1].strip().upper()
            for v in ("MAJOR REVISIONS", "MINOR REVISIONS", "ACCEPT", "REJECT"):
                if v in after:
                    return v
            if "MAJOR" in after:
                return "MAJOR REVISIONS"
            if "MINOR" in after:
                return "MINOR REVISIONS"
    return None


def usage_to_dict(usage):
    if usage is None:
        return {}
    try:
        return usage.model_dump()
    except Exception:
        try:
            return dict(usage)
        except Exception:
            return {"raw": str(usage)}


def review_native(client, model, pdf_path):
    """Upload PDF (purpose=user_data), then Responses input_file. Returns (text, usage, modality)."""
    with open(pdf_path, "rb") as fh:
        f = client.files.create(file=fh, purpose="user_data")
    file_id = f.id
    kwargs = dict(
        model=model,
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_file", "file_id": file_id},
                    {"type": "input_text", "text": PROMPT},
                ],
            }
        ],
        max_output_tokens=8000,
    )
    r = client.responses.create(**kwargs)
    text = r.output_text
    usage = usage_to_dict(getattr(r, "usage", None))
    return text, usage, file_id


VENDORS = {
    "grok":   (XAI_MODEL,    xai, "native-pdf (/v1/files upload + /v1/responses input_file)"),
}


def run_one(paper, vendor):
    ver, pdfpath = PAPERS[paper]
    model, client, modality = VENDORS[vendor]
    ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
    rec = {"paper": paper, "version": ver, "vendor": vendor, "model": model,
           "modality": modality, "ts": ts}
    outfile = OUTDIR / f"API_{paper}_{vendor}.md"
    try:
        t0 = time.time()
        content, usage, file_id = review_native(client, model, pdfpath)
        dt = round(time.time() - t0, 1)
        verdict = parse_verdict(content)
        rec.update({"status": "ok", "verdict": verdict, "seconds": dt,
                    "usage": usage, "file_id": file_id})
        with open(outfile, "w") as f:
            f.write(f"# INT API POST-POLISH (native-PDF) — {paper} {ver} — {vendor} ({model})\n")
            f.write(f"PAPER: {paper}  |  VERSION: {ver}  |  MODEL: {model}\n")
            f.write(f"MODALITY: {modality}\n")
            f.write(f"UTC: {ts}  |  latency: {dt}s\n")
            f.write(f"USAGE: {json.dumps(usage)}\n")
            f.write(f"PARSED VERDICT: {verdict}\n\n")
            f.write("=" * 70 + "\nRAW RESPONSE (verbatim):\n" + "=" * 70 + "\n\n")
            f.write(content)
        print(f"[OK]   {paper:4s} {vendor:6s} -> {verdict}  ({dt}s)")
    except Exception as e:
        rec.update({"status": "FAILED", "verdict": None, "error": str(e)[:1000]})
        with open(outfile, "w") as f:
            f.write(f"# INT API POST-POLISH (native-PDF) — {paper} {ver} — {vendor} ({model}) — FAILED\n")
            f.write(f"PAPER: {paper}  |  VERSION: {ver}  |  MODEL: {model}\n")
            f.write(f"MODALITY: {modality}\n")
            f.write(f"UTC: {ts}\nERROR: {e}\n")
        print(f"[FAIL] {paper:4s} {vendor:6s} -> {str(e)[:160]}")
    with open(MANIFEST, "a") as mf:
        mf.write(json.dumps(rec) + "\n")
    return rec


def main():
    if MANIFEST.exists():
        MANIFEST.unlink()
    order = sys.argv[1:] if len(sys.argv) > 1 else list(PAPERS.keys())
    results = []
    for paper in order:
        for vendor in ("grok",):
            results.append(run_one(paper, vendor))
    print("\n===== VERDICT TABLE (native-PDF) =====")
    print(f"{'paper':5s} {'grok(grok-4.3)':18s}")
    for paper in order:
        g = next((r for r in results if r["paper"] == paper and r["vendor"] == "grok"), {})
        print(f"{paper:5s} {str(g.get('verdict') or g.get('status')):18s}")


if __name__ == "__main__":
    main()
