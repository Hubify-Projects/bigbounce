# P4 FINALHASH_2026-08-03_P4_v1.0.273 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `unknown` [FALLBACK from sonar-pro]
**Input PDF**: `pipelines/p2_chirality/chirality_catalog_paper.pdf` sha256=88bb513284db6adf4c6cf22ee7e08be2787cf8c3ebf43ffdcc289f2d369cee05 pages=32
**Review packet(s)**: `e40aa39a3de6b746dccbea4dc94bd69d8d42faee8b56ec875956fc950f214374`
**Input format**: TEXT + web search
**Wall time**: 280.8s

---

## Reviewer call FAILED

```
AuthenticationError("Error code: 401 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information, visit https://www.perplexity.ai/settings/api.', 'type': 'insufficient_quota', 'code': 401}}")
Traceback (most recent call last):
  File "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/tools/v3_native_pdf_review.py", line 488, in run_reviewer
    content, model_used = packetized_dispatch(fallback_model, prompt)
  File "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/tools/v3_native_pdf_review.py", line 478, in packetized_dispatch
    return _dispatch_one_call(vendor, keys, model, dispatch_prompt, snapshot, paper_text)
  File "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/tools/v3_native_pdf_review.py", line 438, in _dispatch_one_call
    return call_perplexity(keys, model, prompt, paper_text)
  File "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/tools/v3_native_pdf_review.py", line 410, in call_perplexity
    resp = client.chat.completions.create(
  File "/Users/houstongolden/Library/Python/3.9/lib/python/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
  File "/Users/houstongolden/Library/Python/3.9/lib/python/site-packages/openai/resources/chat/completions/completions.py", line 1251, in create
    return self._post(
  File "/Users/houstongolden/Library/Python/3.9/lib/python/site-packages/openai/_base_client.py", line 1332, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
  File "/Users/houstongolden/Library/Python/3.9/lib/python/site-packages/openai/_base_client.py", line 1105, in request
    raise self._make_status_error_from_response(err.response) from None
openai.AuthenticationError: Error code: 401 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information, visit https://www.perplexity.ai/settings/api.', 'type': 'insufficient_quota', 'code': 401}}

```
