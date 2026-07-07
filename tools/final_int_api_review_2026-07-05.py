#!/usr/bin/env python3
"""FINAL pre-sign-off INT API-vendor review (OpenAI + XAI/Grok) on 6 bigbounce papers.
Loads keys from .env.local by NAME (never prints values). Sends pdftotext text.
Saves EVERY raw response. A failed call = FAILED leg (recorded with error), never invented.
"""
import os, sys, json, time, warnings, datetime, pathlib
warnings.filterwarnings("ignore")

REPO = pathlib.Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
OUTDIR = REPO / "project-context/peer-reviews/INT_v3/FINAL_ROUND_2026-07-05"
OUTDIR.mkdir(parents=True, exist_ok=True)
MANIFEST = OUTDIR / "manifest.jsonl"

PAPERS = {
    "P4":  ("v1.0.217",  "/tmp/txt_P4.txt"),
    "P1B": ("v1B.0.101", "/tmp/txt_P1B.txt"),
    "P3":  ("v3.1.138",  "/tmp/txt_P3.txt"),
    "P2":  ("v1.7.95",   "/tmp/txt_P2.txt"),
    "P5":  ("v0.1.102",  "/tmp/txt_P5.txt"),
    "P1A": ("v1A.0.110", "/tmp/txt_P1A.txt"),
}

OPENAI_MODEL = "gpt-5.2"
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
        tok = v.split()[0] if v else ""   # strip trailing inline comment/note
        d[k] = tok
    return d


ENV = loadenv()
import requests


def parse_verdict(text):
    """Extract verdict only from a line beginning with '(1) VERDICT:' (per spec)."""
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
            # handle "MAJOR" / "MINOR" bare
            if "MAJOR" in after:
                return "MAJOR REVISIONS"
            if "MINOR" in after:
                return "MINOR REVISIONS"
    return None


def call_openai(text):
    payload = {
        "model": OPENAI_MODEL,
        "messages": [
            {"role": "system", "content": "You are an expert Physical Review D referee."},
            {"role": "user", "content": PROMPT + "\n\n===== MANUSCRIPT (pdftotext) =====\n\n" + text},
        ],
    }
    r = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {ENV['OPENAI_API_KEY']}", "Content-Type": "application/json"},
        json=payload, timeout=1200,
    )
    if r.status_code != 200:
        raise RuntimeError(f"HTTP {r.status_code}: {r.text[:500]}")
    j = r.json()
    return j["choices"][0]["message"]["content"], j.get("usage", {})


def call_xai(text):
    payload = {
        "model": XAI_MODEL,
        "messages": [
            {"role": "system", "content": "You are an expert Physical Review D referee."},
            {"role": "user", "content": PROMPT + "\n\n===== MANUSCRIPT (pdftotext) =====\n\n" + text},
        ],
    }
    r = requests.post(
        "https://api.x.ai/v1/chat/completions",
        headers={"Authorization": f"Bearer {ENV['XAI_API_KEY']}", "Content-Type": "application/json"},
        json=payload, timeout=1200,
    )
    if r.status_code != 200:
        raise RuntimeError(f"HTTP {r.status_code}: {r.text[:500]}")
    j = r.json()
    return j["choices"][0]["message"]["content"], j.get("usage", {})


VENDORS = {"openai": (OPENAI_MODEL, call_openai), "grok": (XAI_MODEL, call_xai)}


def run_one(paper, vendor):
    ver, txtpath = PAPERS[paper]
    model, fn = VENDORS[vendor]
    text = open(txtpath).read()
    ts = datetime.datetime.utcnow().isoformat() + "Z"
    rec = {"paper": paper, "version": ver, "vendor": vendor, "model": model, "ts": ts}
    outfile = OUTDIR / f"API_{paper}_{vendor}.md"
    try:
        t0 = time.time()
        content, usage = fn(text)
        dt = round(time.time() - t0, 1)
        verdict = parse_verdict(content)
        rec.update({"status": "ok", "verdict": verdict, "seconds": dt, "usage": usage})
        with open(outfile, "w") as f:
            f.write(f"# INT API Review — {paper} {ver} — {vendor} ({model})\n")
            f.write(f"UTC: {ts}  |  latency: {dt}s  |  usage: {json.dumps(usage)}\n")
            f.write(f"PARSED VERDICT: {verdict}\n\n")
            f.write("=" * 70 + "\nRAW RESPONSE (verbatim):\n" + "=" * 70 + "\n\n")
            f.write(content)
        print(f"[OK]   {paper:4s} {vendor:6s} -> {verdict}  ({dt}s)")
    except Exception as e:
        rec.update({"status": "FAILED", "verdict": None, "error": str(e)[:800]})
        with open(outfile, "w") as f:
            f.write(f"# INT API Review — {paper} {ver} — {vendor} ({model}) — FAILED\n")
            f.write(f"UTC: {ts}\nERROR: {e}\n")
        print(f"[FAIL] {paper:4s} {vendor:6s} -> {str(e)[:120]}")
    with open(MANIFEST, "a") as mf:
        mf.write(json.dumps(rec) + "\n")
    return rec


def main():
    # fresh manifest
    if MANIFEST.exists():
        MANIFEST.unlink()
    order = sys.argv[1:] if len(sys.argv) > 1 else list(PAPERS.keys())
    results = []
    for paper in order:
        for vendor in ("openai", "grok"):
            results.append(run_one(paper, vendor))
    print("\n===== VERDICT TABLE =====")
    print(f"{'paper':5s} {'openai':16s} {'grok':16s}")
    for paper in order:
        o = next((r for r in results if r["paper"] == paper and r["vendor"] == "openai"), {})
        g = next((r for r in results if r["paper"] == paper and r["vendor"] == "grok"), {})
        print(f"{paper:5s} {str(o.get('verdict') or o.get('status')):16s} {str(g.get('verdict') or g.get('status')):16s}")


if __name__ == "__main__":
    main()
