# P3 FINALHASH_2026-08-03_P3_v3.2.0-r15 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `unknown` [FALLBACK from sonar-pro]
**Input PDF**: `pipelines/p3_anomaly_engine/paper3_apjs.pdf` sha256=793575f5705c421a3c75bfa2fe66b9f3c07aed327a2a75e01f835f952aee47ef pages=17
**Review packet(s)**: `packet-build-failed`
**Input format**: TEXT + web search
**Wall time**: 92.8s

---

## Reviewer call FAILED

```
PortfolioError('portfolio receipt is stale: HEAD, registry, rules, source, or PDF changed')
Traceback (most recent call last):
  File "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/tools/v3_native_pdf_review.py", line 484, in run_reviewer
    content, model_used = packetized_dispatch(primary_model, prompt)
  File "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/tools/v3_native_pdf_review.py", line 468, in packetized_dispatch
    packet = build_packet(
  File "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/tools/review_packet.py", line 145, in build_packet
    preflight = verify_receipt(
  File "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/tools/bigbounce_preflight.py", line 371, in verify_receipt
    raise PortfolioError("portfolio receipt is stale: HEAD, registry, rules, source, or PDF changed")
bigbounce_preflight.PortfolioError: portfolio receipt is stale: HEAD, registry, rules, source, or PDF changed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/tools/v3_native_pdf_review.py", line 488, in run_reviewer
    content, model_used = packetized_dispatch(fallback_model, prompt)
  File "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/tools/v3_native_pdf_review.py", line 468, in packetized_dispatch
    packet = build_packet(
  File "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/tools/review_packet.py", line 145, in build_packet
    preflight = verify_receipt(
  File "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/tools/bigbounce_preflight.py", line 371, in verify_receipt
    raise PortfolioError("portfolio receipt is stale: HEAD, registry, rules, source, or PDF changed")
bigbounce_preflight.PortfolioError: portfolio receipt is stale: HEAD, registry, rules, source, or PDF changed

```
