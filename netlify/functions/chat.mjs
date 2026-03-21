import Anthropic from '@anthropic-ai/sdk';
import { getSystemPrompt } from '../../astro/system-prompt.mjs';

// In-memory rate limiter (resets on cold start — fine for soft limiting)
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

export default async (request) => {
  if (request.method !== 'POST') {
    return new Response(JSON.stringify({ error: 'Method not allowed' }), {
      status: 405,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  // Rate limit by IP
  const ip = request.headers.get('x-forwarded-for') || request.headers.get('client-ip') || 'unknown';
  if (!checkRateLimit(ip)) {
    return new Response(JSON.stringify({ error: 'Rate limit exceeded. Please wait a moment.' }), {
      status: 429,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  // Parse request
  let messages, pageContext;
  try {
    const body = await request.json();
    messages = body.messages;
    pageContext = body.pageContext;
    if (!Array.isArray(messages) || messages.length === 0) {
      throw new Error('messages required');
    }
  } catch (e) {
    return new Response(JSON.stringify({ error: 'Invalid request: ' + e.message }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  // Sanitize messages
  const sanitized = messages.map(m => ({
    role: m.role === 'assistant' ? 'assistant' : 'user',
    content: String(m.content).slice(0, 4000)
  }));

  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) {
    return new Response(JSON.stringify({ error: 'Server configuration error' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  const client = new Anthropic({ apiKey });

  try {
    const stream = client.messages.stream({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 1024,
      system: getSystemPrompt(pageContext),
      messages: sanitized
    });

    const encoder = new TextEncoder();

    const readable = new ReadableStream({
      async start(controller) {
        try {
          for await (const event of stream) {
            if (event.type === 'content_block_delta' && event.delta?.text) {
              const data = JSON.stringify({ text: event.delta.text });
              controller.enqueue(encoder.encode(`data: ${data}\n\n`));
            }
          }
          controller.enqueue(encoder.encode('data: [DONE]\n\n'));
          controller.close();
        } catch (err) {
          const data = JSON.stringify({ error: err.message });
          controller.enqueue(encoder.encode(`data: ${data}\n\n`));
          controller.close();
        }
      }
    });

    return new Response(readable, {
      headers: {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive'
      }
    });
  } catch (err) {
    return new Response(JSON.stringify({ error: 'Failed to get response. Please try again.' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
};
