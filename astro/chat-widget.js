/**
 * Astro — BigBounce Research Chat Widget
 * Self-contained: injects its own CSS, creates all DOM elements.
 * Supports floating bubble mode and full-page mode (#astro-full-chat).
 */
(function () {
  'use strict';

  // ── Config ──
  const API_URL = '/.netlify/functions/chat';
  const MAX_HISTORY = 20; // max message pairs to send

  // ── State ──
  let messages = [];
  let isStreaming = false;
  let isOpen = false;
  let isFullPage = false;
  let abortController = null;

  // ── Detect full-page mode ──
  const fullPageMount = document.getElementById('astro-full-chat');
  if (fullPageMount) isFullPage = true;

  // ── Inject CSS ──
  const style = document.createElement('style');
  style.textContent = `
    /* Astro Chat Widget */
    .astro-bubble {
      position: fixed;
      bottom: 24px;
      right: 24px;
      width: 48px;
      height: 48px;
      background: #1a1a1a;
      border: 1px solid #333;
      border-radius: 0;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 9999;
      transition: background 0.15s;
      box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    }
    .astro-bubble:hover { background: #2a2a2a; }
    .astro-bubble-icon {
      color: #fff;
      font-family: 'JetBrains Mono', 'IBM Plex Mono', 'Courier New', monospace;
      font-size: 13px;
      font-weight: 700;
      user-select: none;
      line-height: 1;
    }

    .astro-panel {
      position: fixed;
      bottom: 84px;
      right: 24px;
      width: 400px;
      max-height: 520px;
      background: #fff;
      border: 1px solid #eaeaea;
      border-radius: 0;
      z-index: 9998;
      display: none;
      flex-direction: column;
      box-shadow: 0 4px 24px rgba(0,0,0,0.10);
    }
    .astro-panel.open { display: flex; }

    .astro-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 16px;
      border-bottom: 1px solid #eaeaea;
      flex-shrink: 0;
    }
    .astro-header-title {
      font-family: 'JetBrains Mono', 'IBM Plex Mono', monospace;
      font-size: 13px;
      font-weight: 700;
      color: #1a1a1a;
      letter-spacing: 0.02em;
    }
    .astro-close {
      background: none;
      border: none;
      font-size: 18px;
      cursor: pointer;
      color: #999;
      padding: 0 4px;
      line-height: 1;
    }
    .astro-close:hover { color: #333; }

    .astro-messages {
      flex: 1;
      overflow-y: auto;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      min-height: 0;
    }

    .astro-msg {
      font-family: 'Inter', -apple-system, sans-serif;
      font-size: 14px;
      line-height: 1.6;
      color: #1a1a1a;
      max-width: 100%;
      word-wrap: break-word;
      overflow-wrap: break-word;
    }
    .astro-msg.user {
      align-self: flex-end;
      background: #f5f5f5;
      padding: 8px 12px;
      border-radius: 2px;
      max-width: 85%;
    }
    .astro-msg.assistant {
      border-left: 2px solid #1a1a1a;
      padding-left: 12px;
    }
    .astro-msg.assistant p { margin: 0 0 8px 0; }
    .astro-msg.assistant p:last-child { margin-bottom: 0; }
    .astro-msg.assistant code {
      background: #f5f5f5;
      padding: 1px 4px;
      border-radius: 2px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 12.5px;
    }
    .astro-msg.assistant pre {
      background: #f5f5f5;
      padding: 10px 12px;
      overflow-x: auto;
      font-family: 'JetBrains Mono', monospace;
      font-size: 12.5px;
      margin: 8px 0;
      border-radius: 2px;
    }
    .astro-msg.assistant pre code {
      background: none;
      padding: 0;
    }
    .astro-msg.assistant ul, .astro-msg.assistant ol {
      padding-left: 20px;
      margin: 4px 0 8px 0;
    }
    .astro-msg.assistant li { margin-bottom: 2px; }
    .astro-msg.assistant a { color: #2563eb; }
    .astro-msg.assistant strong { font-weight: 600; }
    .astro-msg.assistant blockquote {
      border-left: 2px solid #ddd;
      padding-left: 10px;
      color: #666;
      margin: 8px 0;
    }

    .astro-msg.error {
      color: #dc2626;
      font-size: 13px;
      font-style: italic;
    }

    .astro-welcome {
      color: #999;
      font-size: 13px;
      font-family: 'Inter', sans-serif;
      text-align: center;
      padding: 32px 16px;
    }
    .astro-welcome strong { color: #666; }

    .astro-input-row {
      display: flex;
      align-items: center;
      border-top: 1px solid #eaeaea;
      padding: 0;
      flex-shrink: 0;
    }
    .astro-prompt-prefix {
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      color: #999;
      padding: 12px 0 12px 14px;
      user-select: none;
      flex-shrink: 0;
    }
    .astro-input {
      flex: 1;
      border: none;
      outline: none;
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      padding: 12px 14px 12px 6px;
      background: transparent;
      color: #1a1a1a;
    }
    .astro-input::placeholder { color: #bbb; }
    .astro-input:disabled { opacity: 0.5; }

    .astro-typing {
      display: inline-block;
      width: 6px;
      height: 14px;
      background: #1a1a1a;
      animation: astro-blink 0.8s infinite;
      vertical-align: text-bottom;
      margin-left: 1px;
    }
    @keyframes astro-blink {
      0%, 50% { opacity: 1; }
      51%, 100% { opacity: 0; }
    }

    /* Full-page mode overrides */
    .astro-full {
      position: relative;
      width: 100%;
      height: calc(100vh - 140px);
      max-height: none;
      border: 1px solid #eaeaea;
      display: flex;
      flex-direction: column;
      background: #fff;
      bottom: auto;
      right: auto;
      box-shadow: none;
    }
    .astro-full .astro-messages {
      padding: 24px 32px;
    }
    .astro-full .astro-msg { max-width: 700px; }
    .astro-full .astro-msg.user { max-width: 600px; }
    .astro-full .astro-input-row { padding: 0 8px; }

    /* Mobile */
    @media (max-width: 600px) {
      .astro-panel {
        width: calc(100vw - 16px);
        right: 8px;
        bottom: 76px;
        max-height: calc(100vh - 100px);
      }
      .astro-bubble { bottom: 16px; right: 16px; }
      .astro-full { height: calc(100vh - 120px); }
      .astro-full .astro-messages { padding: 16px; }
    }
  `;
  document.head.appendChild(style);

  // ── Simple Markdown Parser ──
  function renderMarkdown(text) {
    // Escape HTML
    let html = text
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');

    // Code blocks (``` ... ```)
    html = html.replace(/```(\w*)\n([\s\S]*?)```/g, (_, lang, code) =>
      `<pre><code>${code.trim()}</code></pre>`
    );

    // Inline code
    html = html.replace(/`([^`]+)`/g, '<code>$1</code>');

    // Bold
    html = html.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');

    // Italic
    html = html.replace(/\*([^*]+)\*/g, '<em>$1</em>');

    // Links [text](url)
    html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');

    // Fix internal links — don't open in new tab
    html = html.replace(/href="\/([^"]*)" target="_blank" rel="noopener"/g, 'href="/$1"');

    // Blockquotes
    html = html.replace(/^&gt; (.+)$/gm, '<blockquote>$1</blockquote>');

    // Unordered lists
    html = html.replace(/^[-*] (.+)$/gm, '<li>$1</li>');
    html = html.replace(/(<li>[\s\S]*?<\/li>)/g, (match) => {
      if (!match.startsWith('<ul>')) return '<ul>' + match + '</ul>';
      return match;
    });
    // Merge adjacent <ul> tags
    html = html.replace(/<\/ul>\s*<ul>/g, '');

    // Ordered lists
    html = html.replace(/^\d+\. (.+)$/gm, '<li>$1</li>');

    // Paragraphs (double newlines)
    html = html.replace(/\n\n+/g, '</p><p>');
    html = '<p>' + html + '</p>';

    // Clean up empty paragraphs and fix nesting
    html = html.replace(/<p>\s*<\/p>/g, '');
    html = html.replace(/<p>\s*(<pre>)/g, '$1');
    html = html.replace(/(<\/pre>)\s*<\/p>/g, '$1');
    html = html.replace(/<p>\s*(<ul>)/g, '$1');
    html = html.replace(/(<\/ul>)\s*<\/p>/g, '$1');
    html = html.replace(/<p>\s*(<blockquote>)/g, '$1');
    html = html.replace(/(<\/blockquote>)\s*<\/p>/g, '$1');

    return html;
  }

  // ── Page Context ──
  function getPageContext() {
    return {
      title: document.title,
      path: location.pathname
    };
  }

  // ── Build DOM ──
  function buildPanel(container) {
    // Header
    const header = document.createElement('div');
    header.className = 'astro-header';
    header.innerHTML = `<span class="astro-header-title">astro</span>`;

    if (!isFullPage) {
      const closeBtn = document.createElement('button');
      closeBtn.className = 'astro-close';
      closeBtn.textContent = '×';
      closeBtn.addEventListener('click', togglePanel);
      header.appendChild(closeBtn);
    }
    container.appendChild(header);

    // Messages area
    const msgArea = document.createElement('div');
    msgArea.className = 'astro-messages';
    msgArea.innerHTML = `<div class="astro-welcome">
      <strong>astro</strong> — BigBounce research assistant<br><br>
      Ask me about the research, the science,<br>or anything on this site.
    </div>`;
    container.appendChild(msgArea);

    // Input row
    const inputRow = document.createElement('div');
    inputRow.className = 'astro-input-row';
    inputRow.innerHTML = `<span class="astro-prompt-prefix">&gt;</span>`;

    const input = document.createElement('input');
    input.className = 'astro-input';
    input.type = 'text';
    input.placeholder = 'ask astro...';
    input.autocomplete = 'off';
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage(input, msgArea);
      }
    });
    inputRow.appendChild(input);
    container.appendChild(inputRow);

    return { msgArea, input };
  }

  // ── Send Message ──
  async function sendMessage(input, msgArea) {
    const text = input.value.trim();
    if (!text || isStreaming) return;

    // Clear welcome message
    const welcome = msgArea.querySelector('.astro-welcome');
    if (welcome) welcome.remove();

    // Add user message
    messages.push({ role: 'user', content: text });
    const userEl = document.createElement('div');
    userEl.className = 'astro-msg user';
    userEl.textContent = text;
    msgArea.appendChild(userEl);

    input.value = '';
    input.disabled = true;
    isStreaming = true;

    // Add assistant message placeholder
    const assistantEl = document.createElement('div');
    assistantEl.className = 'astro-msg assistant';
    const cursor = document.createElement('span');
    cursor.className = 'astro-typing';
    assistantEl.appendChild(cursor);
    msgArea.appendChild(assistantEl);
    msgArea.scrollTop = msgArea.scrollHeight;

    // Prepare messages (trim to MAX_HISTORY)
    const sendMsgs = messages.slice(-MAX_HISTORY * 2);

    let fullText = '';
    abortController = new AbortController();

    try {
      const res = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          messages: sendMsgs,
          pageContext: getPageContext()
        }),
        signal: abortController.signal
      });

      if (!res.ok) {
        const err = await res.json().catch(() => ({ error: 'Something went wrong' }));
        throw new Error(err.error || `Error ${res.status}`);
      }

      // Read SSE stream
      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n');
        buffer = lines.pop() || '';

        for (const line of lines) {
          if (!line.startsWith('data: ')) continue;
          const data = line.slice(6);
          if (data === '[DONE]') break;

          try {
            const parsed = JSON.parse(data);
            if (parsed.error) throw new Error(parsed.error);
            if (parsed.text) {
              fullText += parsed.text;
              // Remove cursor, render current text, re-add cursor
              if (cursor.parentNode) cursor.remove();
              assistantEl.innerHTML = renderMarkdown(fullText);
              assistantEl.appendChild(cursor);
              msgArea.scrollTop = msgArea.scrollHeight;
            }
          } catch (e) {
            if (e.message && !e.message.includes('JSON')) throw e;
          }
        }
      }

      // Finalize
      if (cursor.parentNode) cursor.remove();
      assistantEl.innerHTML = renderMarkdown(fullText);
      messages.push({ role: 'assistant', content: fullText });

      // Trigger MathJax if available
      if (window.MathJax && window.MathJax.typesetPromise) {
        window.MathJax.typesetPromise([assistantEl]).catch(() => {});
      }
    } catch (err) {
      if (cursor.parentNode) cursor.remove();
      if (err.name === 'AbortError') {
        assistantEl.innerHTML = renderMarkdown(fullText || '*Cancelled.*');
      } else {
        assistantEl.innerHTML = '';
        assistantEl.className = 'astro-msg error';
        assistantEl.textContent = err.message || 'Something went wrong. Please try again.';
      }
    } finally {
      isStreaming = false;
      input.disabled = false;
      input.focus();
      msgArea.scrollTop = msgArea.scrollHeight;
      abortController = null;
    }
  }

  // ── Toggle Panel ──
  function togglePanel() {
    const panel = document.querySelector('.astro-panel');
    if (!panel) return;
    isOpen = !isOpen;
    panel.classList.toggle('open', isOpen);
    if (isOpen) {
      const input = panel.querySelector('.astro-input');
      if (input) setTimeout(() => input.focus(), 100);
    }
  }

  // ── Initialize ──
  function init() {
    if (isFullPage) {
      // Full-page mode
      fullPageMount.classList.add('astro-full');
      buildPanel(fullPageMount);
      const input = fullPageMount.querySelector('.astro-input');
      if (input) setTimeout(() => input.focus(), 200);
    } else {
      // Floating widget mode
      // Create bubble
      const bubble = document.createElement('div');
      bubble.className = 'astro-bubble';
      bubble.innerHTML = '<span class="astro-bubble-icon">&gt;_</span>';
      bubble.addEventListener('click', togglePanel);
      document.body.appendChild(bubble);

      // Create panel
      const panel = document.createElement('div');
      panel.className = 'astro-panel';
      buildPanel(panel);
      document.body.appendChild(panel);

      // Close on Escape
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && isOpen) togglePanel();
      });
    }
  }

  // Wait for DOM
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
