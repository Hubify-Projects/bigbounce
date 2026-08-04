# P3 v3.2.0-r16 flat ApJS portal package

This directory is the checksum-bound, flat upload staging package for the P3
ApJS manuscript. All uploadable files are at this one directory level.

`paper3_apjs.tex` is the r16 source with only its three figure paths flattened.
It uses the bundled AASTeX 7.0.2 class and retains line numbers. The expected
rendered manuscript is 17 pages. `SHA256SUMS` binds every payload file; verify
it before upload with `shasum -a 256 -c SHA256SUMS`.

The source tar and full audit evidence are one directory above:

- `paper3_apjs_arxiv_v3.2.0-r16.tar.gz`
- `FINAL_PACKAGE_RECEIPT_v3.2.0-r16_2026-08-03.md`
- `APJS_PORTAL_SUBMISSION_KIT_v3.2.0-r16_2026-08-03.md`

This package is prepared for Houston's review only. It does not represent a
journal upload or submission.
