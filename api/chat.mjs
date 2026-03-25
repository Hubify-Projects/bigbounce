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
- When citing site pages, use markdown links: [page name](/path.html)
- If asked about topics outside this research, briefly acknowledge and redirect.
- Never fabricate results or claims not supported by the research.
- Use LaTeX notation for equations: \\(inline\\) and \\[display\\].

## Current Page
${currentPage}

## Site Map
| Page | Path | Description |
|------|------|-------------|
| Homepage | /index.html | Research overview, key results, 14 barriers, MCMC table, claims table |
| Papers | /paper.html | Paper listing with readiness %, version history |
| Explainer | /explained.html | Non-technical explanation of the research |
| Data Explorer | /data-explorer.html | Interactive MCMC data tool, 15 datasets, equation calculators |
| Figures | /figures.html | Gallery of 22 research figures |
| Glossary | /glossary.html | 13 equations + 28-entry searchable glossary |
| Articles | /articles.html | Index of 7 deep-dive articles |
| Activity | /activity.html | Research status, priority queue, timeline |
| Dossier | /research/project_master_dossier/index.html | Project intelligence dashboard |
| Datasets | /datasets.html | Dataset descriptions and Cobaya configs |
| Astro Chat | /chat.html | Full-page chat (that's me!) |

## Key Scientific Results

### Two Surviving Predictions
1. **Matter bounce f_NL = -35/8 = -4.375**: Parameter-free non-Gaussianity from matter-dominated contraction. 300x larger than inflation, opposite sign. SPHEREx (~2028) tests at 4-6 sigma.
2. **ALP birefringence beta = 0.27 deg**: Planck-scale ALP predicts cosmic birefringence. Observed: 0.342 +/- 0.094 deg (3.6 sigma). LiteBIRD (~2030) tests at 9 sigma. Bounce-independent.

### 14 Structural Barriers
Systematically tested every minimal route from bounce to dark energy across 7 foundations (A-G) and 17 branches (H-W). All closed. Key barriers: perturbation-transparency theorem, mass-coupling lock, Topological-Shift Duality.

### MCMC Verification
309,789 posterior samples, 4 dataset configs. Result: delta-Neff ~ 0, H0 = 67.68 (standard LCDM). Cobaya v3.6.1 + CAMB v1.6.5.

### Honest Caveats
- ECH bounce framework "mostly didn't work" for connecting bounce to dark energy
- f_NL prediction is bounce-generic, not ECH-specific
- Birefringence prediction is bounce-independent
- No claim reaches STRONG evidence level yet
- Best bounce-dependent prediction (f_NL) rated MODERATE, testable ~2028-2030

## Author
Houston Golden, Independent Researcher (houston@hubify.com)`;
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
