# P4 R52 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `unknown` [FALLBACK from sonar-pro]
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p2_chirality/chirality_catalog_paper.pdf` md5=c47abc18 pages=23
**Input format**: TEXT + web search
**Wall time**: 4.5s

---

## Reviewer call FAILED

```
AuthenticationError("Error code: 401 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information, visit https://www.perplexity.ai/settings/api.', 'type': 'insufficient_quota', 'code': 401}}")
Traceback (most recent call last):
  File "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/tools/v3_native_pdf_review.py", line 596, in run_reviewer
    content, model_used = _dispatch_one_call(vendor, keys, fallback_model, prompt, pdf_path, paper_text)
  File "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/tools/v3_native_pdf_review.py", line 563, in _dispatch_one_call
    return call_perplexity(keys, model, prompt, paper_text)
  File "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/tools/v3_native_pdf_review.py", line 541, in call_perplexity
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
