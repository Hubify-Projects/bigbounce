import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const bump = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-a3m",
  version: "v3M.0.25",
  datestamp: "2026-09-18",
  texCommit: process.env.A3M_TEX_COMMIT ?? "pending",
  pdfMd5: "d46166cb88b32009cdc6be59bb620547",
  pdfPages: 20,
  pdfSizeBytes: 775652,
  sitePdfPath: "/papers/a3_multichannel_arxiv_v3M.0.25.pdf",
  changelog: "R9 closure (first board since the directive-R2 stop was lifted by ledger row 19 / D-A3-14). INT legs on exact v3M.0.24: Grok REJECT, Gemini minor-revisions, Claude Fable 5.1 major-revisions; truth-audit found 24 genuinely-new-real items (3 MAJOR, 1 MAJOR-lite, 17 minor, 3 nit) against 14 source-cited falsifications. MAJOR 1: the reproducibility statement pinned to commit 68309c8, which contains NONE of the ~12 artifacts it names (both published tree URLs returned 200 only because the parent directories exist) -- re-pointed to the repository main-branch trees, with the frozen-release DOI named as the required packaging-stage action. MAJOR 2: Eq. (15) was Li+2016 Eq. (5.1), not (4.19), and already carried lambda at its P-propto-X^n value, so the Sec. VIII lambda-scan double-counted lambda on the matter-contraction line -- the general-lambda amplitude f_NL^pre = -245/16 + 105/(8c_s^2) - 30*Lambda is now printed as the primary equation with the X^n line as its specialization, and every scan number is stated as measured from the Lambda=0 baseline. MAJOR 3: f_NL^after = 1.0-1.4e11 was printed in the abstract, Sec. VIII and Table VII with no statement that tree-level control is lost ~6.9 decades earlier; a new committed computation (r9_perturbativity) applies the paper's own Sec. V B criterion 1.2|f_NL|zeta_rms<=1 to give a floor c_s >~ 0.073-0.079 where r >~ 1.8 is already 49x BICEP/Keck, and the exclusion is now rested on r=24c_s plus loss of control rather than on the 10^11 figure. MAJOR-lite: v3M.0.19 had dropped the whole 'lambda = s = 0' qualifier when D-A3-14 proved lambda-independence ONLY; the constant-sound-speed (s=0) restriction is restored to the abstract and the claim sentence, with time-dependent c_s(eta) stated as outside the computation. Also added the Planck 95% edge (c_s >= 0.525, r >= 12.6, disjointness 350x) as the headline alongside the 68% one; corrected the squeezed LQC deficit 2.1-4.4 -> 3.1-4.4 dex against lane9c2 abs_comparison; corrected the T_B / k*eta_B pairing in Sec. IV D; disclosed that the PTA injection test establishes bias but not coverage; noted the left-skew (-1.10) that makes the gamma marginal's sigma exceed its 68% half-width; cited row11_pbh_residuals as the source of the headline 1.84+-0.03; defined the bispectrum amplitude A, T_3/T_4, the sound-speed running s, and the quasar response parameter p; removed a drafting-history parenthetical (directive Q1) and four internal ledger-row/lane labels; moved 9 raw artifact paths out of body prose and captions into the reproducibility statement; added four explicitly disclosed limitations to Sec. IX; abstract re-trimmed 341 -> 307 words. SEPARATELY DISCOVERED DURING CLOSURE: the committed v3M.0.24 main.tex did not compile at all on a clean toolchain (a raw Unicode rho at line 1754), so the served v3M.0.24 PDF was not reproducible from its own committed source; fixed. Directive G: 4-pass pdflatex, 0 errors, 0 undefined refs/citations, 20 pages, max overfull hbox 3.9pt (0 above 10pt), three-way md5 d46166cb88b32009cdc6be59bb620547 (fresh compile == site/public/papers == public/papers). arXiv tarball rebuilt and standalone smoke-compiled clean (0 undef, 20pp), sha256 403f6b1f. Readiness stays at the computed cap 75 pending the one confirmation board permitted by directive R2.",
});
console.log("paperVersions.bump:", bump);

const activity = await client.mutation(api.activityFeed.add, {
  type: "r-round",
  date: "2026-09-18",
  title: "A3M R9 board + closure -- v3M.0.25 (rounds resumed, row 19 CLOSED)",
  body: "First board since the directive-R2 stop was lifted. INT-only (Grok API, Gemini API, Claude Fable 5.1 referee) on exact v3M.0.24: REJECT / minor-revisions / major-revisions. Truth-audit: 24 genuinely-new-real, 14 falsified with source citations. Three MAJORs closed in v3M.0.25 -- the reproducibility pin resolved to a commit containing none of the cited artifacts; Eq. (15) was misattributed and double-counted lambda; and the 10^11 f_NL figure was printed without noting that tree-level control expires 6.9 decades earlier. A new committed computation (r9_perturbativity) supplies the validity floor. Also found and fixed during closure: the committed v3M.0.24 source did not compile on a clean toolchain. Readiness held at the computed cap 75 pending the confirmation board.",
  tags: [
    { label: "paper-a3m", kind: "paper" },
    { label: "v3M.0.25", kind: "version" },
    { label: "campaign-2026-09-18", kind: "campaign" },
  ],
});
console.log("activityFeed.add:", activity);
