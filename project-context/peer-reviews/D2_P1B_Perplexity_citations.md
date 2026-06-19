# P1B D2 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `unknown` [FALLBACK from sonar-pro]
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=b166f4c0 pages=21
**Input format**: TEXT + web search
**Wall time**: 25.5s

---

## Reviewer call FAILED

```
AuthenticationError("Error code: 401 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information, visit https://www.perplexity.ai/settings/api.', 'type': 'insufficient_quota', 'code': 401}}")
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
openai.AuthenticationError: Error code: 401 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information, visit https://www.perplexity.ai/settings/api.', 'type': 'insufficient_quota', 'code': 401}}

```
