# P1A exact-convention closure manifest

- Closure: `P1A v1A.0.117`
- Paper date: `July 14, 2026`
- Source: `arxiv/paper1a_ech_nogo.tex`
- Compiled paper: `arxiv/paper1a_ech_nogo.pdf`
- Compile engine: Tectonic 0.15.0 with the locally cached TeX bundle
- Compile command: `tectonic -b /tmp/tectonic-p1a-bundle -k --keep-logs -r 2 paper1a_ech_nogo.tex`
- PDF pages: `7`
- PDF size: `149500 bytes`
- PDF SHA-256: `a5dcf033306c3b949a4a16d834a6fa39875d3da8af8d3c69cabba48ca4876fee`
- PDF MD5: `1a34a9d378d0877a20e764caefdfb867`
- Source SHA-256: `db0982af9e1377a14feee62fb8793aecf7667258975db6b74153483373b23637`

## Frozen proof files

| File | SHA-256 |
|---|---|
| `proof/paper1a_ech_nogo.v1A.0.117.tex` | `db0982af9e1377a14feee62fb8793aecf7667258975db6b74153483373b23637` |
| `proof/paper1a_ech_nogo.v1A.0.117.pdf` | `a5dcf033306c3b949a4a16d834a6fa39875d3da8af8d3c69cabba48ca4876fee` |
| `proof/njl_gap_equation_route1.v1A.0.117.py` | `a0b89159950d34f37558fff7af0ce5741d5baea331c28068f5596572c0388c7c` |
| `proof/njl_gap_equation_route1_results.v1A.0.117.json` | `123ec9f10ee05056231efef43f4093c787996acfd15b9d2704f836fabc5a136b` |
| `proof/njl_gap_equation_route1.v1A.0.117.md` | `e0fe2f0425627511bdd2f1f96a26ca21ee0636ceb22b5cca1c188f670406f829` |
| `audit/paper1a_ech_nogo.v1A.0.117.log` | `1deb67f0d877878fb555ca446577dc7f4b7db97f494edb0b58f06a1fd7269b8f` |
| `audit/paper1a_ech_nogo.v1A.0.117.blg` | `b0e97af3bcb65443e2a0852e23fd2e8e5f56cad448889fd63b4130f389b119ff` |

The frozen TeX and PDF are byte-identical to their live `arxiv/` counterparts.
The calculation script, generated JSON, and derivation note are likewise
byte-identical to the live reproducibility artifacts.

## Scope statement

This bundle records only the bounded P1A exact-convention closure. It does not
update the site, SSOT, Convex, `version.json`, another paper, or review state.
No Git staging, commit, push, tag, or review dispatch is part of this closure.
