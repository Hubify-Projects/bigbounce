# P1B v2B.0.2 Exact-PDF Confirmation Truth Audit

## Binding

- Commit: `8ad6b00faeb423931b04e4748b57fe532933eba8`
- Exact PDF SHA-256:
  `18b97ac5ffc48d03a60d84822b74562ccd10202430a13054ef2dabf3f267d46c`
- Providers: Codex CLI through ChatGPT subscription, direct xAI/Grok API, and
  direct Google/Gemini API.
- OpenAI API used: **no**
- Anthropic used: **no**

## Verdict-first audit

The board is not clean, but only one raised item is a genuine major software
defect. The exact-window numerical claims were not contradicted.

| Finding | Disposition | Evidence / closure |
|---|---|---|
| Missing persistent archive identifier | **OPEN EXTERNAL GATE → DP1B-15** | Explicitly disclosed in the manuscript; package 0.1.2 still requires an immutable archive before submission. |
| Repository URL absent/inaccessible | **FALSIFIED** | The PDF contains a live repository annotation and direct artifact annotations. v2B.0.3 additionally renders the repository URL as text for extraction robustness. |
| Paper `v2B.0.2` conflicts with package `0.1.1` | **FALSIFIED** | These are explicitly distinct manuscript and software version namespaces. |
| Embedded runnable code is required in the paper | **EDITORIAL** | Executable examples and installation commands are retained in the linked package README and CI. |
| Separate License heading | **EDITORIAL, ADOPTED** | MIT was already stated, but v2B.0.3 adds a dedicated heading for JORS scanability. |
| Receipt verification TOCTOU race | **VERIFIED MAJOR → DP1B-13** | `verify_json_receipt` parsed one result generation, then re-read the path when hashing. A concurrent publish could return the old payload while accepting the new receipt/current file. Package 0.1.2 reads result and receipt once and hashes the exact result bytes returned; a race regression is mandatory. |
| Canonical README repeats superseded recoveries | **VERIFIED MINOR → DP1B-14** | The old table contradicted the preceding physical-production status and is removed from the canonical section. |
| Operating-system independence unsupported | **VERIFIED MINOR → DP1B-14** | Directory `fsync` is POSIX-specific and prior CI covered Ubuntu only. The code now scopes directory synchronization to POSIX; CI adds Windows 3.12; the manuscript claims only tested Linux/Windows support. |
| “Content-addressed sidecar” terminology | **VERIFIED MINOR → DP1B-14** | The sidecar path is filename-derived, while its protected field is digest-bound. “Content-bound” replaces the inaccurate term. |
| Reference/page-number collision | **VERIFIED MINOR → DP1B-14** | The forced page enlargement rendered the footer inside Reference 4. v2B.0.3 removes the enlargement and uses a compact bibliography. |
| “Because … so” grammar | **VERIFIED MINOR → DP1B-14** | Corrected directly. |

## Recursive-improvement consequence

This round adds a new mechanically detectable software-integrity class:
validation must never parse bytes from one generation and authenticate bytes
from another. The closure includes a deterministic race regression rather than
only manuscript wording. No readiness increase is taken before exact-PDF
confirmation of v2B.0.3 and completion of the archive/human gates.
