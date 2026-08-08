# P3 EXT20 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `unknown` [FALLBACK from sonar-pro]
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=62d7b294 pages=30
**Input format**: TEXT + web search
**Wall time**: 2.0s

---

## Reviewer call FAILED

```
BadRequestError("Error code: 400 - {'error': {'message': 'validation failed: message 0: content exceeds maximum length of 100KB', 'type': 'invalid_request', 'code': 400}}")
Traceback (most recent call last):
  File "/Users/houstongolden/Desktop/CODE_2025/bigbounce/tools/v3_native_pdf_review.py", line 596, in run_reviewer
    content, model_used = _dispatch_one_call(vendor, keys, fallback_model, prompt, pdf_path, paper_text)
  File "/Users/houstongolden/Desktop/CODE_2025/bigbounce/tools/v3_native_pdf_review.py", line 563, in _dispatch_one_call
    return call_perplexity(keys, model, prompt, paper_text)
  File "/Users/houstongolden/Desktop/CODE_2025/bigbounce/tools/v3_native_pdf_review.py", line 541, in call_perplexity
    resp = client.chat.completions.create(
  File "/Users/houstongolden/Library/Python/3.10/lib/python/site-packages/openai/_utils/_utils.py", line 287, in wrapper
    return func(*args, **kwargs)
  File "/Users/houstongolden/Library/Python/3.10/lib/python/site-packages/openai/resources/chat/completions/completions.py", line 1211, in create
    return self._post(
  File "/Users/houstongolden/Library/Python/3.10/lib/python/site-packages/openai/_base_client.py", line 1314, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
  File "/Users/houstongolden/Library/Python/3.10/lib/python/site-packages/openai/_base_client.py", line 1087, in request
    raise self._make_status_error_from_response(err.response) from None
openai.BadRequestError: Error code: 400 - {'error': {'message': 'validation failed: message 0: content exceeds maximum length of 100KB', 'type': 'invalid_request', 'code': 400}}

```
