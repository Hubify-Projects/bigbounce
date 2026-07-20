export const config = { runtime: 'edge' };

const CONVEX_URL = 'https://impressive-quail-879.convex.cloud';

// ── System Prompt ──
function getSystemPrompt(pageContext) {
  const currentPage = pageContext
    ? `The user is currently viewing: "${pageContext.title}" at ${pageContext.path}`
    : 'The user is on the BigBounce research site.';

  return `You are Astro, the AI research assistant for the BigBounce spin-torsion cosmology research site (bigbounce.hubify.app). You help visitors understand the research, navigate the site, and explore the science.

## Identity & Behavior
- You are knowledgeable, precise, and honest about what the research has and hasn't achieved.
- Use concise, clear language. Match the visitor's technical level.
- When citing site pages, use markdown links to the current Next.js routes: [page name](/path) — NOT legacy .html paths.
- If asked about topics outside this research, briefly acknowledge and redirect.
- Never fabricate results or claims not supported by the research.
- Prefer simple Unicode for math (e.g. "f_NL = −35/16 = −2.1875", "σ", "×", "≈"). Light LaTeX (\\(inline\\), \\[display\\], \\frac{}{}) is rendered, but plain Unicode is most reliable. Use "###"/"##" for headers and "-" for bullets — Markdown is rendered.

## Current Page
${currentPage}

## Site Map (current Next.js routes)
| Page | Path | Description |
|------|------|-------------|
| Homepage | / | Program overview, the six papers, top contributions, live readiness |
| Papers | /paper | Paper index with live readiness %, versions, PDFs |
| Explainer | /explained | Non-technical explanation of the research |
| Contributions | /contributions | Novel results ranked on the N1–N4 novelty scale (self-claim ceiling N3) |
| Predictions | /predictions | The falsifiable signatures and the experiments that settle them |
| Reviews | /reviews | The adversarial internal/external review loop, verdict trajectories, in the open |
| Data Explorer | /data-explorer | Interactive tables: barriers, MCMC, f_NL derivation, forecasts |
| Figures | /figures | Gallery of ~75 research figures |
| Glossary | /glossary | 17-entry searchable glossary |
| Articles | /articles | Deep-dive articles |
| Surveys | /surveys | The archival surveys mined, per-survey QC |
| Activity | /activity | Live machine event feed (version bumps, rounds, pods) |
| Anomaly Explorer | /anomaly-explorer | Interactive view of the DESI DR1 autoencoder anomaly-detection pipeline candidates |
| Galaxy Explorer | /galaxy-explorer | Explore the 8.47M-galaxy chirality catalog |
| Architecture | /architecture | Convex data model + MCP tool catalog |
| Astro Chat | /chat | Full-page chat (that's me!) |

## The Six Papers (current state)
- **P1A** (v1A.0.124, ~62% ready) — Minimal Einstein–Cartan–Holst gravity: axial four-fermion contact term + zero-spin scalar transparency. A narrow algebraic CQG Note.
- **P1B** (v2B.0.11, ~56%) — namaster-proof: exact pseudo-Cℓ window inference + tamper-evident provenance. A software metapaper (software/reproducibility claims only).
- **P2** (v1.7.125, ~80%) — The matter-contraction non-Gaussian amplitude: derives **f_NL = −35/16 = −2.1875** and maps it conditionally to LSS sensitivity. Forecasts are illustrative, not a detection.
- **P3** (v3.2.0-r10, ~56%) — Public-ID recovery of 181 DESI DR1 TARGETIDs from a frozen historical anomaly list (170 high-coordinate-consistency core + 11 lower-confidence). An **archive-recovery / provenance product — explicitly NOT a purity, novelty, or detection claim.**
- **P4** (v1.0.268, ~80%) — 8.47M-galaxy chirality catalog; the strict safe-sample observed-label dipole is null-consistent (z=+0.63465, p=0.23768).
- **P5** (v0.1.141, ~74%) — DESIVAST void/non-void chirality: a bounded catalog-native non-detection (does not establish physical environment independence).

## Key Scientific Results

### Two Surviving Predictions
1. **Matter-bounce f_NL = −35/16 = −2.1875** (Paper 2): the corrected squeezed-limit non-Gaussianity from matter-dominated contraction, ~300× larger than standard inflation and opposite sign. SPHEREx (~2028) tests it at ~3–5σ. (The older −35/8 = −4.375 value was a single-time-ordering convention and is SUPERSEDED — the canonical value is −35/16.)
2. **ALP birefringence β = 0.27°** (Paper 1A/2): Planck-scale ALP predicts cosmic birefringence, within ~0.5σ of the published 0.342 ± 0.094° (3.6σ) observation. LiteBIRD (~2030) tests at ~9σ. Bounce-independent.

### 14 Structural Barriers
Systematically tested every minimal route from bounce to dark energy across 7 foundations (A–G) and 17 branches (H–W); all closed under stated assumptions. Key results: perturbation-transparency theorem, mass-coupling lock, Topological-Shift Duality.

### MCMC Verification (Paper 1B)
~309K posterior samples across frozen dataset combinations. Result: ΔN_eff ≈ 0, H₀ = 67.68 (standard ΛCDM). Cobaya 3.6.1 + CAMB.

### Honest Caveats
- The ECH bounce framework mostly did not connect a bounce to dark energy — the enumerated routes are closed.
- The f_NL prediction is bounce-generic, not ECH-specific.
- The birefringence prediction is bounce-independent.
- Paper 3 is an archive-recovery/provenance product, NOT a detection or discovery claim — do not describe it as "378,280 anomalies across 7 surveys" or "12 z>6 QSO discoveries" as a current result.
- No claim reaches STRONG evidence yet; the best bounce-dependent prediction (f_NL) is MODERATE, testable ~2028–2030.
- All six papers remain IN REVISION; automated-model review labels are not journal acceptance.

## Author
Houston Golden (houston@hubify.com)`;
}

// ── IP Hashing (non-reversible, privacy-safe) ──
function hashIP(ip) {
  let h = 0x9e3779b9;
  for (let i = 0; i < ip.length; i++) {
    h ^= ip.charCodeAt(i);
    h = (h << 5) | (h >>> 27);
    h = Math.imul(h, 0x5bd1e995);
    h ^= h >>> 15;
  }
  return (h >>> 0).toString(16).padStart(8, '0');
}

// ── Session ID: hash of IP + daily salt ──
function makeSessionId(ip) {
  const daySalt = new Date().toISOString().slice(0, 10); // YYYY-MM-DD
  const raw = ip + ':' + daySalt;
  let h = 0x811c9dc5;
  for (let i = 0; i < raw.length; i++) {
    h ^= raw.charCodeAt(i);
    h = Math.imul(h, 0x01000193);
  }
  return (h >>> 0).toString(16).padStart(8, '0');
}

// ── Convex Logging (fire-and-forget) ──
function logToConvex(args) {
  fetch(`${CONVEX_URL}/api/mutation`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      path: 'chatMessages:log',
      args: args,
    }),
  }).catch(() => {});
}

// ── Rate Limiter ──
const rateLimits = new Map();
const RATE_LIMIT = 20;
const RATE_WINDOW = 60_000;

function checkRateLimit(ip) {
  const now = Date.now();
  const entry = rateLimits.get(ip);
  if (!entry || now - entry.start > RATE_WINDOW) {
    rateLimits.set(ip, { start: now, count: 1 });
    return true;
  }
  entry.count++;
  return entry.count <= RATE_LIMIT;
}

// ── Handler ──
export default async function handler(request) {
  if (request.method !== 'POST') {
    return new Response(JSON.stringify({ error: 'Method not allowed' }), {
      status: 405,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  const ip = request.headers.get('x-forwarded-for') || request.headers.get('x-real-ip') || 'unknown';
  if (!checkRateLimit(ip)) {
    return new Response(JSON.stringify({ error: 'Rate limit exceeded. Please wait a moment.' }), {
      status: 429,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  let messages, pageContext, clientSessionId;
  try {
    const body = await request.json();
    messages = body.messages;
    pageContext = body.pageContext;
    clientSessionId = body.sessionId;
    if (!Array.isArray(messages) || messages.length === 0) {
      throw new Error('messages required');
    }
  } catch (e) {
    return new Response(JSON.stringify({ error: 'Invalid request: ' + e.message }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  const sanitized = messages.map(m => ({
    role: m.role === 'assistant' ? 'assistant' : 'user',
    content: String(m.content).slice(0, 4000)
  }));

  // ── Generate session ID and IP hash for logging ──
  // Prefer client-provided sessionId (for cross-page persistence), fall back to IP-based
  const sessionId = (typeof clientSessionId === 'string' && clientSessionId.length > 0) ? clientSessionId : makeSessionId(ip);
  const ipHash = hashIP(ip);
  const pageCtx = pageContext
    ? { title: pageContext.title || undefined, path: pageContext.path || undefined }
    : undefined;

  // ── Log the user message (fire-and-forget) ──
  const lastUserMsg = sanitized.filter(m => m.role === 'user').pop();
  if (lastUserMsg) {
    logToConvex({
      sessionId,
      role: 'user',
      content: lastUserMsg.content,
      pageContext: pageCtx,
      ipHash,
      timestamp: Date.now(),
    });
  }

  const apiKey = process.env.OPENROUTER_API_KEY;
  if (!apiKey) {
    return new Response(JSON.stringify({ error: 'OPENROUTER_API_KEY not configured' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  try {
    const orResponse = await fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
        'HTTP-Referer': 'https://bigbounce.hubify.app',
        'X-Title': 'BigBounce Astro Chat'
      },
      body: JSON.stringify({
        model: 'anthropic/claude-sonnet-4.6',
        max_tokens: 1024,
        stream: true,
        messages: [
          { role: 'system', content: getSystemPrompt(pageContext) },
          ...sanitized
        ]
      })
    });

    if (!orResponse.ok) {
      const errText = await orResponse.text();
      return new Response(JSON.stringify({ error: `API error ${orResponse.status}: ${errText.slice(0, 200)}` }), {
        status: 502,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    const encoder = new TextEncoder();
    const decoder = new TextDecoder();
    const reader = orResponse.body.getReader();

    // Accumulate assistant response for logging
    let assistantText = '';

    const readable = new ReadableStream({
      async start(controller) {
        let buffer = '';
        try {
          while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            buffer += decoder.decode(value, { stream: true });
            const lines = buffer.split('\n');
            buffer = lines.pop() || '';

            for (const line of lines) {
              if (!line.startsWith('data: ')) continue;
              const data = line.slice(6).trim();
              if (data === '[DONE]') continue;

              try {
                const parsed = JSON.parse(data);
                const text = parsed.choices?.[0]?.delta?.content;
                if (text) {
                  assistantText += text;
                  controller.enqueue(encoder.encode(`data: ${JSON.stringify({ text })}\n\n`));
                }
              } catch {}
            }
          }
          controller.enqueue(encoder.encode('data: [DONE]\n\n'));
          controller.close();

          // ── Log the assistant response (fire-and-forget) ──
          if (assistantText) {
            logToConvex({
              sessionId,
              role: 'assistant',
              content: assistantText.slice(0, 10000),
              pageContext: pageCtx,
              ipHash,
              timestamp: Date.now(),
            });
          }
        } catch (err) {
          controller.enqueue(encoder.encode(`data: ${JSON.stringify({ error: err.message })}\n\n`));
          controller.close();
        }
      }
    });

    return new Response(readable, {
      headers: {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache'
      }
    });
  } catch (err) {
    return new Response(JSON.stringify({ error: err.message || 'Unknown error' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}
