#!/usr/bin/env python3
"""Hardened single-leg INT API review — native-PDF upload (OpenAI Files API / XAI /v1/files).
Runs EXACTLY ONE (paper, vendor) leg per invocation so a hang loses one leg, not the round.
Keys from .env.local by NAME (first token before inline comments; never printed).
Per-request timeout 300s. One retry, then FAILED with the error string.
Usage: int_api_review_2026-07-08.py <PAPER> <openai|grok>
"""
import os, sys, json, time, warnings, datetime, pathlib
warnings.filterwarnings("ignore")

REPO = pathlib.Path("/Users/houstongolden/Desktop/CODE_YOU/bigbounce")
OUTDIR = REPO / "project-context/peer-reviews/INT_v3/ROUND_2026-07-08"
OUTDIR.mkdir(parents=True, exist_ok=True)
MANIFEST = OUTDIR / "manifest.jsonl"

# paper -> (version, pdf path relative to repo)
PAPERS = {
    "P1A": ("v1A.0.115", "arxiv/paper1a_ech_nogo.pdf"),
    "P1B": ("v1B.0.104", "arxiv/paper1b_mcmc_companion.pdf"),
    "P2":  ("v1.7.102",  "research/focused_paper_source_integration/02_full_draft.pdf"),
    "P3":  ("v3.1.144",  "pipelines/p3_anomaly_engine/paper3_draft.pdf"),
    "P4":  ("v1.0.223",  "pipelines/p2_chirality/chirality_catalog_paper.pdf"),
    "P5":  ("v0.1.107",  "pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf"),
}

OPENAI_MODEL = "gpt-5.5"
XAI_MODEL = "grok-4.3"
REQ_TIMEOUT = 300

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
        tok = v.split()[0] if v else ""
        d[k] = tok
    return d


ENV = loadenv()
import requests


def parse_verdict(text):
    if not text:
        return None
    for line in text.splitlines():
        s = line.strip()
        if "verdict:" in s.lower():
            after = s.split(":", 1)[1].strip().upper()
            for v in ("MAJOR REVISIONS", "MINOR REVISIONS", "ACCEPT", "REJECT"):
                if v in after:
                    return v
            if "MAJOR" in after:
                return "MAJOR REVISIONS"
            if "MINOR" in after:
                return "MINOR REVISIONS"
    # fallback: scan whole text for first verdict token
    up = text.upper()
    for v in ("MAJOR REVISIONS", "MINOR REVISIONS", "ACCEPT", "REJECT"):
        if v in up:
            return v
    return None


# ---------- OpenAI: Files API (purpose user_data) + Responses input_file ----------
def call_openai(pdf_path):
    key = ENV["OPENAI_API_KEY"]
    with open(pdf_path, "rb") as fh:
        up = requests.post(
            "https://api.openai.com/v1/files",
            headers={"Authorization": f"Bearer {key}"},
            files={"file": (os.path.basename(pdf_path), fh, "application/pdf")},
            data={"purpose": "user_data"},
            timeout=REQ_TIMEOUT,
        )
    if up.status_code != 200:
        raise RuntimeError(f"upload HTTP {up.status_code}: {up.text[:400]}")
    file_id = up.json()["id"]
    payload = {
        "model": OPENAI_MODEL,
        "input": [
            {"role": "system", "content": "You are an expert Physical Review D referee."},
            {"role": "user", "content": [
                {"type": "input_file", "file_id": file_id},
                {"type": "input_text", "text": PROMPT},
            ]},
        ],
    }
    r = requests.post(
        "https://api.openai.com/v1/responses",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        json=payload, timeout=REQ_TIMEOUT,
    )
    if r.status_code != 200:
        raise RuntimeError(f"responses HTTP {r.status_code}: {r.text[:400]}")
    j = r.json()
    # extract text from responses output
    txt = j.get("output_text")
    if not txt:
        parts = []
        for item in j.get("output", []):
            for c in item.get("content", []):
                if c.get("type") in ("output_text", "text") and c.get("text"):
                    parts.append(c["text"])
        txt = "\n".join(parts)
    return txt, {"file_id": file_id, "usage": j.get("usage", {}), "modality": "native-PDF (Files API input_file)"}


# ---------- XAI/Grok: /v1/files upload + /v1/responses file_id ----------
def call_xai(pdf_path):
    key = ENV["XAI_API_KEY"]
    with open(pdf_path, "rb") as fh:
        up = requests.post(
            "https://api.x.ai/v1/files",
            headers={"Authorization": f"Bearer {key}"},
            files={"file": (os.path.basename(pdf_path), fh, "application/pdf")},
            data={"purpose": "user_data"},
            timeout=REQ_TIMEOUT,
        )
    if up.status_code != 200:
        raise RuntimeError(f"upload HTTP {up.status_code}: {up.text[:400]}")
    file_id = up.json()["id"]
    payload = {
        "model": XAI_MODEL,
        "input": [
            {"role": "system", "content": "You are an expert Physical Review D referee."},
            {"role": "user", "content": [
                {"type": "input_file", "file_id": file_id},
                {"type": "input_text", "text": PROMPT},
            ]},
        ],
    }
    r = requests.post(
        "https://api.x.ai/v1/responses",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        json=payload, timeout=REQ_TIMEOUT,
    )
    if r.status_code != 200:
        raise RuntimeError(f"responses HTTP {r.status_code}: {r.text[:400]}")
    j = r.json()
    txt = j.get("output_text")
    if not txt:
        parts = []
        for item in j.get("output", []):
            for c in item.get("content", []):
                if c.get("type") in ("output_text", "text") and c.get("text"):
                    parts.append(c["text"])
        txt = "\n".join(parts)
    return txt, {"file_id": file_id, "usage": j.get("usage", {}), "modality": "native-PDF (/v1/files file_id)"}


VENDORS = {"openai": (OPENAI_MODEL, call_openai), "grok": (XAI_MODEL, call_xai)}


def run_one(paper, vendor):
    ver, rel = PAPERS[paper]
    pdf_path = str(REPO / rel)
    model, fn = VENDORS[vendor]
    ts = datetime.datetime.utcnow().isoformat() + "Z"
    rec = {"paper": paper, "version": ver, "vendor": vendor, "model": model, "ts": ts}
    outfile = OUTDIR / f"API_{paper}_{vendor}.md"
    last_err = None
    for attempt in (1, 2):
        try:
            t0 = time.time()
            content, meta = fn(pdf_path)
            dt = round(time.time() - t0, 1)
            verdict = parse_verdict(content)
            rec.update({"status": "ok", "verdict": verdict, "seconds": dt,
                        "modality": meta.get("modality"), "attempt": attempt})
            with open(outfile, "w") as f:
                f.write(f"# INT API Review — {paper} {ver} — {vendor} ({model})\n")
                f.write(f"paper: {paper}  version: {ver}  model: {model}\n")
                f.write(f"modality: {meta.get('modality')}\n")
                f.write(f"UTC: {ts}  |  latency: {dt}s  |  attempt: {attempt}\n")
                f.write(f"usage: {json.dumps(meta.get('usage', {}))}\n")
                f.write(f"PARSED VERDICT: {verdict}\n\n")
                f.write("=" * 70 + "\nRAW RESPONSE (verbatim):\n" + "=" * 70 + "\n\n")
                f.write(content or "(empty response)")
            print(f"[OK]   {paper:4s} {vendor:6s} -> {verdict}  ({dt}s, attempt {attempt})")
            with open(MANIFEST, "a") as mf:
                mf.write(json.dumps(rec) + "\n")
            return rec
        except Exception as e:
            last_err = str(e)[:800]
            print(f"[retry {attempt}] {paper} {vendor}: {last_err[:160]}")
            time.sleep(3)
    rec.update({"status": "FAILED", "verdict": None, "error": last_err})
    with open(outfile, "w") as f:
        f.write(f"# INT API Review — {paper} {ver} — {vendor} ({model}) — FAILED\n")
        f.write(f"paper: {paper}  version: {ver}  model: {model}\n")
        f.write(f"UTC: {ts}\nERROR: {last_err}\n")
    print(f"[FAIL] {paper:4s} {vendor:6s} -> {last_err[:160]}")
    with open(MANIFEST, "a") as mf:
        mf.write(json.dumps(rec) + "\n")
    return rec


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: int_api_review_2026-07-08.py <PAPER> <openai|grok>")
        sys.exit(2)
    run_one(sys.argv[1], sys.argv[2])
