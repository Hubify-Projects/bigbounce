# P1B v1B.0.112 exact-PDF confirmation truth audit

Exact artifact: commit `72812cf63cc124ec0c203fc43f5dfde0f509953f`,
PDF SHA-256
`d420a7f5be48f1fa5f9fc1b2cf57206708881ffe29c782ea6cdf4d65eb20331c`.

## Transport and policy status

- Grok direct API: valid receipt, wrapper verdict **REJECT**.
- Gemini direct API: valid receipt, wrapper verdict **REJECT**.
- Codex/ChatGPT subscription: two attempts, both recorded **FAILED** with no
  verdict. The first stream disconnected and remained idle without a network
  socket; the subscription-only retry stalled at the remote plugin-catalog
  boundary for more than two hours. Both processes were terminated and
  retained as failed receipts.
- OpenAI API and Anthropic were not used.

This is an incomplete three-leg confirmation board. The two successful legs
are evidence; the missing Codex verdict is not silently converted to ACCEPT,
MINOR, or a zero-finding result.

## Scientific truth audit

Both successful reviewers affirm that the bounded central claim—technical
reproducibility of the three explicitly limited exercises—is supported. Neither
identifies a numerical, provenance, estimator, prior, artifact, or internal
consistency regression in v1B.0.112.

All Grok and Gemini major findings are the standing venue/scope objection:
stock-code analyses, idealized synthetic NaMaster validation, generic ALP
summary likelihood, and fragmentation from Paper I(a) are judged insufficient
as a standalone JCAP research article. These are genuine editorial risks and
must remain visible, but they do not falsify the calculations or reopen the
three v1B.0.111 defects that v1B.0.112 closed.

## Verdict

- **Known-defect confirmation:** PASS on the two successful independent legs;
  zero known-pattern escape and zero new verified scientific defect.
- **Full board:** INCOMPLETE because both Codex-subscription transports failed.
- **Venue posture:** REJECT-modal on the two successful legs, driven entirely
  by standing novelty/fragmentation judgments.
- **Readiness:** HOLDS 56. No submission, acceptance, or minor-only convergence
  is claimed.

The next efficient action is not another identical Grok/Gemini wave. It is
either a successful Codex-subscription confirmation after the CLI transport is
healthy, or a deliberate venue/article-architecture decision that resolves the
standing standalone-JCAP objection.
