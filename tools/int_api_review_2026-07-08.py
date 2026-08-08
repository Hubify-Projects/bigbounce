#!/usr/bin/env python3
"""Hardened single-leg INT API review for xAI/Grok and Google/Gemini.
Runs EXACTLY ONE (paper, vendor) leg per invocation so a hang loses one leg, not the round.
Keys from .env.local by NAME (first token before inline comments; never printed).
Per-request timeout 300s. One retry, then FAILED with the error string.
OpenAI is deliberately blocked here: OpenAI reviews run through the authenticated
Codex CLI/ChatGPT subscription, never an API endpoint or OPENAI_API_KEY.
Usage: int_api_review_2026-07-08.py <P1A|P1B|P2|P3|P4|P5> <grok|gemini>
"""
from __future__ import annotations

import os, sys, json, time, warnings, datetime, pathlib, hashlib
warnings.filterwarnings("ignore")

from paper_registry import CANONICAL_IDS, load_registry, repo_root
from bigbounce_preflight import DEFAULT_RULES, verify_receipt
from review_packet import (
    build_packet,
    publish_packet,
    resolve_pdf_snapshot,
    review_cache_root,
)

REPO = repo_root()
REGISTRY = load_registry(REPO)
# Output dir is overridable (INT_OUTDIR env) so variant waves (e.g. the P3 ApJS
# review-of-record) can write their raws to a clearly-labeled sibling round dir
# without clobbering the canonical PRD round. Default = the canonical PRD round.
OUTDIR = pathlib.Path(os.environ.get("INT_OUTDIR")
                      or (REPO / "project-context/peer-reviews/INT_v3/ROUND_2026-07-09"))
MANIFEST = OUTDIR / "manifest.jsonl"


def archive_existing_raw(outfile: pathlib.Path) -> pathlib.Path | None:
    """Preserve a rolling provider raw before a retry overwrites it.

    The manifest is append-only, so every manifest row must be able to retain
    a distinct raw body.  The stable API_<paper>_<vendor>.md path remains the
    newest result for existing parsers, while earlier bodies move into a
    content-addressed sibling archive.
    """
    if not outfile.exists():
        return None
    data = outfile.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    archive_dir = outfile.parent / "provider-raw-archive"
    archive_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    archived = archive_dir / f"{outfile.stem}__{stamp}__{digest[:12]}{outfile.suffix}"
    if not archived.exists():
        archived.write_bytes(data)
    return archived


def live_version(tex_rel: str) -> str:
    import re as _re
    tex = REPO / tex_rel
    try:
        txt = tex.read_text()
        m = _re.search(r"\\newcommand\{\\paperVersion\}\{([^}]+)\}", txt)
        if m:
            return m.group(1)
        # fallback: version comment on the \date line (P3 style)
        m = _re.search(r"\\date\{[^}]*\}\s*%\s*(v[\w.\-]+)", txt)
        if m:
            return m.group(1)
        # fallback: first changelog comment "% vX.Y.Z (" (P2 style)
        m = _re.search(r"^%\s*(v[\w.]+)\s*\(", txt, _re.M)
        if m:
            return m.group(1)
    except Exception:
        pass
    return "unknown-version"

XAI_MODEL = "grok-4.3"
# Gemini INT leg (keyed 2026-07-11). Newest pro-tier model with native-PDF input,
# probed live from generativelanguage.googleapis.com/v1beta/models. The default
# below is what the models-list endpoint reported as the latest pro preview; an
# override env GEMINI_MODEL wins if Houston pins a different one.
GEMINI_MODEL = "gemini-3.1-pro-preview"
GEMINI_BASE = "https://generativelanguage.googleapis.com"
REQ_TIMEOUT = 300

PROMPT = ""
SYSTEM_MSG = ""


def review_messages(entry):
    venue = os.environ.get("INT_VENUE") or entry["target_journal"]
    prompt = os.environ.get("INT_PROMPT") or (
        f"You are an expert referee for {venue}. Review this {entry['article_type']} "
        f"manuscript under profile {entry['review_profile']} to the standard of a real "
        "submission. Respond with exactly: (1) VERDICT: ACCEPT / MINOR REVISIONS / "
        "MAJOR REVISIONS / REJECT. (2) ISSUES: numbered, each prefixed [MAJOR] or "
        "[MINOR], naming the specific section/claim and concrete problem. "
        "(3) One sentence: is the central claim supported?"
    )
    system = os.environ.get("INT_SYSTEM") or f"You are an expert {venue} referee."
    return system, prompt


def loadenv(p=REPO / ".env.local"):
    d = dict(os.environ)
    if not p.is_file():
        return d
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


def _request_id(response):
    """Return only known provider request-id headers; never persist all headers."""
    headers = getattr(response, "headers", {}) or {}
    for name in ("x-request-id", "request-id", "x-goog-request-id"):
        value = headers.get(name) or headers.get(name.title())
        if value:
            return str(value)
    return "unavailable"


def _provider_cost(payload):
    """Preserve provider-reported cost only; never estimate or invent a charge."""
    usage = payload.get("usage") or payload.get("usageMetadata") or {}
    for source in (payload, usage):
        if not isinstance(source, dict):
            continue
        for name in ("cost", "total_cost", "totalCost", "estimated_cost"):
            if name in source and source[name] is not None:
                return source[name]
    return "unavailable"


def _provider_meta(provider, requested_model, payload, response, modality):
    """Build a strict allowlisted receipt fragment from a provider response."""
    resolved = (
        payload.get("model")
        or payload.get("modelVersion")
        or payload.get("model_version")
        or "unavailable"
    )
    response_id = payload.get("id") or payload.get("responseId") or "unavailable"
    usage = payload.get("usage") or payload.get("usageMetadata") or {}
    return {
        "provider": provider,
        "requested_model": requested_model,
        "resolved_model": resolved,
        "response_id": response_id,
        "request_id": _request_id(response),
        "usage": usage,
        "provider_reported_cost": _provider_cost(payload),
        "modality": modality,
    }


def _complete_receipt(meta, latency_seconds, attempt):
    """Add local timing fields while retaining only the receipt allowlist."""
    return {
        "provider": meta.get("provider", "unavailable"),
        "requested_model": meta.get("requested_model", "unavailable"),
        "resolved_model": meta.get("resolved_model", "unavailable"),
        "response_id": meta.get("response_id", "unavailable"),
        "request_id": meta.get("request_id", "unavailable"),
        "usage": meta.get("usage") or {},
        "provider_reported_cost": meta.get("provider_reported_cost", "unavailable"),
        "modality": meta.get("modality", "unavailable"),
        "latency_seconds": latency_seconds,
        "attempt": attempt,
    }


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
            {"role": "system", "content": SYSTEM_MSG},
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
    modality = "native-PDF (/v1/files file_id)"
    return txt, _provider_meta("xai", XAI_MODEL, j, r, modality)


# ---------- Gemini: Google Generative Language API, native-PDF ----------
# Files/media resumable upload (handles any size incl. P4's 32MB) -> generateContent
# with file_data.file_uri. Inline base64 (inline_data) is used for small PDFs
# (<=18MB, leaving headroom under the ~20MB request cap) to save a round-trip.
# Model probed live: the newest pro-tier model reporting generateContent from the
# models-list endpoint (GEMINI_MODEL env override wins).
GEMINI_INLINE_MAX = 18 * 1024 * 1024


def _gemini_model():
    return ENV.get("GEMINI_MODEL") or os.environ.get("GEMINI_MODEL") or GEMINI_MODEL


def _gemini_upload(pdf_path, key):
    data = open(pdf_path, "rb").read()
    n = len(data)
    start = requests.post(
        f"{GEMINI_BASE}/upload/v1beta/files",
        headers={
            "x-goog-api-key": key,
            "X-Goog-Upload-Protocol": "resumable",
            "X-Goog-Upload-Command": "start",
            "X-Goog-Upload-Header-Content-Length": str(n),
            "X-Goog-Upload-Header-Content-Type": "application/pdf",
            "Content-Type": "application/json",
        },
        json={"file": {"display_name": os.path.basename(pdf_path)}},
        timeout=REQ_TIMEOUT,
    )
    if start.status_code != 200:
        raise RuntimeError(f"upload-start HTTP {start.status_code}: {start.text[:400]}")
    upload_url = start.headers.get("X-Goog-Upload-URL")
    if not upload_url:
        raise RuntimeError("upload-start missing X-Goog-Upload-URL")
    fin = requests.post(
        upload_url,
        headers={
            "Content-Length": str(n),
            "X-Goog-Upload-Offset": "0",
            "X-Goog-Upload-Command": "upload, finalize",
        },
        data=data, timeout=REQ_TIMEOUT,
    )
    if fin.status_code != 200:
        raise RuntimeError(f"upload-finalize HTTP {fin.status_code}: {fin.text[:400]}")
    f = fin.json()["file"]
    fname, uri, state = f["name"], f["uri"], f.get("state")
    # poll until ACTIVE (PDF processing) — cap ~40s so a stuck file fails, not hangs.
    for _ in range(20):
        if state == "ACTIVE":
            break
        if state == "FAILED":
            raise RuntimeError(f"file processing FAILED: {fname}")
        time.sleep(2)
        g = requests.get(f"{GEMINI_BASE}/v1beta/{fname}",
                         headers={"x-goog-api-key": key}, timeout=60)
        state = g.json().get("state") if g.status_code == 200 else state
    if state != "ACTIVE":
        raise RuntimeError(f"file not ACTIVE after poll (state={state})")
    return uri, fname


def call_gemini(pdf_path):
    key = ENV["GEMINI_API_KEY"]
    model = _gemini_model()
    size = os.path.getsize(pdf_path)
    if size <= GEMINI_INLINE_MAX:
        import base64
        b64 = base64.b64encode(open(pdf_path, "rb").read()).decode()
        part = {"inline_data": {"mime_type": "application/pdf", "data": b64}}
        modality = "native-PDF (inline_data base64)"
    else:
        uri, _ = _gemini_upload(pdf_path, key)
        part = {"file_data": {"mime_type": "application/pdf", "file_uri": uri}}
        modality = "native-PDF (Files/media upload file_uri)"
    payload = {
        "systemInstruction": {"parts": [{"text": SYSTEM_MSG}]},
        "contents": [{"role": "user", "parts": [part, {"text": PROMPT}]}],
    }
    r = requests.post(
        f"{GEMINI_BASE}/v1beta/models/{model}:generateContent",
        headers={"x-goog-api-key": key, "Content-Type": "application/json"},
        json=payload, timeout=REQ_TIMEOUT,
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
    return txt, _provider_meta("google", model, j, r, modality)


VENDORS = {
    "grok": (XAI_MODEL, call_xai),
    "gemini": (GEMINI_MODEL, call_gemini),
}
BLOCKED_VENDORS = {"openai"}


def run_one(paper, vendor):
    global PROMPT, SYSTEM_MSG
    if vendor in BLOCKED_VENDORS:
        raise ValueError(
            "vendor=openai is disabled: use the Codex CLI with ChatGPT subscription "
            "authentication; OpenAI API billing is forbidden for reviews"
        )
    if paper not in REGISTRY:
        raise ValueError(f"paper must be one of {CANONICAL_IDS}")
    if vendor not in VENDORS:
        raise ValueError(f"vendor must be one of {tuple(VENDORS)}")
    preflight_value = os.environ.get("BIGBOUNCE_PREFLIGHT_RECEIPT", "").strip()
    if not preflight_value:
        raise ValueError(
            "BIGBOUNCE_PREFLIGHT_RECEIPT is required before any Grok/Gemini review dispatch"
        )
    preflight_path = pathlib.Path(preflight_value).expanduser()
    # Verify explicitly before model/provider selection. build_packet verifies a
    # second time while binding the same receipt into its immutable packet key.
    verify_receipt(REPO, REPO / DEFAULT_RULES, preflight_path)
    entry = REGISTRY[paper]
    rel = entry["pdf_path"]
    ver = live_version(entry["tex_path"])
    SYSTEM_MSG, PROMPT = review_messages(entry)
    expected_sha256 = os.environ.get("INT_EXPECTED_PDF_SHA256", "").strip().lower()
    model, fn = VENDORS[vendor]
    if vendor == "gemini":
        model = _gemini_model()
    context = os.environ.get("INT_CONTEXT", "").encode()
    packet_prompt = f"SYSTEM:\n{SYSTEM_MSG}\n\nUSER:\n{PROMPT}\n".encode()
    cache_root = review_cache_root()
    packet = build_packet(
        REPO, paper, entry, packet_prompt, context, model,
        os.environ.get("INT_EFFORT", "high"), expected_sha256 or None, cache_root,
        preflight_receipt=preflight_path,
    )
    packet_path, packet_reused = publish_packet(
        packet, cache_root / "packets", packet_prompt, context,
    )
    pdf_path = resolve_pdf_snapshot(packet, cache_root)
    pdf_sha256 = packet["pdf_sha256"]
    review_commit = packet["repository_head"]
    expected_commit = os.environ.get("INT_REVIEW_COMMIT", "").strip()
    if expected_commit and expected_commit != review_commit:
        raise RuntimeError(
            f"review commit mismatch: expected {expected_commit}, got {review_commit}"
        )
    if os.environ.get("BIGBOUNCE_REVIEW_DRY_RUN", "0") == "1":
        result = {
            "paper": paper, "vendor": vendor, "packet_key": packet["packet_key"],
            "packet_path": str(packet_path), "packet_reused": packet_reused,
            "pdf_sha256": pdf_sha256, "review_profile": entry["review_profile"],
            "target_journal": entry["target_journal"], "dispatch": False,
        }
        print(json.dumps(result, indent=2))
        return result
    OUTDIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.datetime.utcnow().isoformat() + "Z"
    rec = {"paper": paper, "version": ver, "vendor": vendor, "model": model, "ts": ts,
           "pdf_path": rel, "pdf_sha256": pdf_sha256, "review_commit": review_commit,
           "packet_key": packet["packet_key"], "review_profile": entry["review_profile"]}
    outfile = OUTDIR / f"API_{paper}_{vendor}.md"
    archived_raw = archive_existing_raw(outfile)
    if archived_raw is not None:
        rec["superseded_raw_archive"] = str(archived_raw.relative_to(OUTDIR))
        rec["superseded_raw_sha256"] = hashlib.sha256(archived_raw.read_bytes()).hexdigest()
    last_err = None
    last_latency = None
    last_attempt = 0
    for attempt in (1, 2):
        last_attempt = attempt
        t0 = time.time()
        try:
            content, meta = fn(pdf_path)
            dt = round(time.time() - t0, 1)
            resolved_model = meta.get("resolved_model", "unavailable")
            eff_model = resolved_model if resolved_model != "unavailable" else model
            receipt = _complete_receipt(meta, dt, attempt)
            verdict = parse_verdict(content)
            rec.update({"status": "ok", "verdict": verdict, "seconds": dt,
                        "model": eff_model,
                        "modality": meta.get("modality"), "attempt": attempt,
                        "provider_receipt": receipt})
            with open(outfile, "w") as f:
                f.write(f"# INT API Review — {paper} {ver} — {vendor} ({eff_model})\n")
                f.write(f"paper: {paper}  version: {ver}  model: {eff_model}\n")
                f.write(f"provenance: commit={review_commit}  pdf={rel}  sha256={pdf_sha256}\n")
                f.write(f"packet: key={packet['packet_key']}  profile={entry['review_profile']}\n")
                f.write(f"modality: {meta.get('modality')}\n")
                f.write(f"UTC: {ts}  |  latency: {dt}s  |  attempt: {attempt}\n")
                f.write(f"provider_receipt: {json.dumps(receipt, sort_keys=True)}\n")
                f.write(f"PARSED VERDICT: {verdict}\n\n")
                f.write("=" * 70 + "\nRAW RESPONSE (verbatim):\n" + "=" * 70 + "\n\n")
                f.write(content or "(empty response)")
            print(f"[OK]   {paper:4s} {vendor:6s} -> {verdict}  ({dt}s, attempt {attempt})")
            with open(MANIFEST, "a") as mf:
                mf.write(json.dumps(rec) + "\n")
            return rec
        except Exception as e:
            last_latency = round(time.time() - t0, 1)
            last_err = str(e)[:800]
            print(f"[retry {attempt}] {paper} {vendor}: {last_err[:160]}")
            time.sleep(3)
    failure_receipt = _complete_receipt(
        {"provider": "xai" if vendor == "grok" else "google",
         "requested_model": model},
        last_latency,
        last_attempt,
    )
    rec.update({"status": "FAILED", "verdict": None, "error": last_err,
                "provider_receipt": failure_receipt})
    with open(outfile, "w") as f:
        f.write(f"# INT API Review — {paper} {ver} — {vendor} ({model}) — FAILED\n")
        f.write(f"paper: {paper}  version: {ver}  model: {model}\n")
        f.write(f"provenance: commit={review_commit}  pdf={rel}  sha256={pdf_sha256}\n")
        f.write(f"packet: key={packet['packet_key']}  profile={entry['review_profile']}\n")
        f.write(f"provider_receipt: {json.dumps(failure_receipt, sort_keys=True)}\n")
        f.write(f"UTC: {ts}\nERROR: {last_err}\n")
    print(f"[FAIL] {paper:4s} {vendor:6s} -> {last_err[:160]}")
    with open(MANIFEST, "a") as mf:
        mf.write(json.dumps(rec) + "\n")
    return rec


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: int_api_review_2026-07-08.py <P1A|P1B|P2|P3|P4|P5> <grok|gemini>")
        sys.exit(2)
    try:
        run_one(sys.argv[1], sys.argv[2])
    except ValueError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(2)
