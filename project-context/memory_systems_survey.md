# Memory Systems Survey for Hubify Labs

**Date:** 2026-04-07
**Status:** Research draft
**Author:** Background research agent

## TL;DR

- **Build, don't fork.** None of the surveyed OSS projects map cleanly onto Hubify's 4-layer (user → agent → lab → global) requirement AND Convex-native storage. Most of them assume Postgres/Neo4j/Qdrant, and adapting them to Convex is as much work as just writing the layer directly.
- **Bootstrap on the `@convex-dev/agent` component.** Convex already ships an official Agent component ([get-convex/agent](https://github.com/get-convex/agent), Apache-2.0, 318★) that implements threads, messages, streaming, file refs, a `memories` table, and hybrid vector+text search — including 10 pre-built `embeddings_{dim}` tables for 128-4096 dim vectors. This is a 70% head start that's already isomorphic to Convex's data model.
- **Steal ideas, not code, from mem0 + Letta + Graphiti + Cognee.** mem0's `(user_id, agent_id, run_id)` filter scheme and `infer` pattern, Letta's core/recall/archival tiering, Graphiti's temporal edge invalidation, and Cognee's `add → cognify → search` pipeline are all reusable design ideas. None of their codebases are worth forking because they all carry heavy dependencies (Postgres/Neo4j/LanceDB/Kuzu) Hubify doesn't want.

## Requirements Recap

Hubify Labs needs a memory system with **four layers**:

1. **User memory** — verbatim user messages + AI summaries + tags + timestamps. Agents never make Houston repeat himself.
2. **Agent memory** — per-agent working + long-term memory. Agents remember everything across sessions.
3. **Lab memory** — everything done in a research lab. The lab agent never forgets experiments, plans, blockers.
4. **Global memory** — cross-lab knowledge graph. New labs see relevant datasets, learnings, and models from other labs.

**Required features** (repeated here as a checklist for evaluation):

- [ ] Vector embeddings for semantic search
- [ ] Hybrid retrieval (keyword + vector)
- [ ] Markdown-friendly storage (Houston likes plain files)
- [ ] Convex DB integration (Hubify already uses Convex)
- [ ] Per-user, per-agent, per-lab, global namespacing
- [ ] Memory writes triggered by agent actions (not user-driven)
- [ ] Cross-session persistence
- [ ] Time-decay or relevance scoring for hot vs cold memories
- [ ] Audit trail (when was a memory created, who wrote it, has it been verified?)

**Current baseline in Hubify** (`hubify/convex/agentMemory.ts` + `hubify/convex/schema.ts:3329-3393`):

- `agent_memory` table with `squad_id`, `agent_id`, `mission_id`, `memory_type` (7 literals), `topic`, `content`, `importance` (1-10), `source`, `expires_at`, `created_at`
- Convex full-text search index on `content`, filtered by `squad_id`, `agent_id`, `memory_type`
- `agent_workspace_files` table with content-hash dedup and file-type filtering
- Missing: vector embeddings, user layer, global layer, explicit audit trail, AI-written summaries, verified-status flag, time-decay ranking
- `storeMemory` / `storeMemories` / `updateImportance` / `searchMemories` / `pruneMemories` mutations + queries already exist

This baseline is the skeleton to extend; the rest of this document is about what to add and what to borrow.

---

## Project Evaluations

### 1. mem0 (mem0ai/mem0)

- **Repo:** https://github.com/mem0ai/mem0
- **Stars:** 52,249 (largest in space)
- **Forks:** 5,854
- **License:** Apache-2.0
- **Language:** Python (61%) + TypeScript (29%)
- **Last commit:** 2026-04-07 (active)
- **Open issues:** 232

**Architecture.** `Memory` class from `mem0/memory/main.py` composes a vector store, an LLM client, an embedding model, a SQLite "history" manager (for mutation audit trail), and an optional graph store. `AsyncMemory` is the async twin. Both inherit from `MemoryBase`. Method signatures (verified from source):

```python
add(messages, *, user_id, agent_id, run_id, metadata, infer, memory_type, prompt)
search(query, *, user_id, agent_id, run_id, limit, filters, threshold, rerank)
get(memory_id)
update(memory_id, data, metadata)
delete(memory_id)
```

A `_build_filters_and_metadata()` helper enforces "at least one of user_id / agent_id / run_id must be provided." Embeddings happen in `_add_to_vector_store()` with a `new_message_embeddings` cache to avoid redundant calls; search path runs `self.embedding_model.embed(query, "search")` then `self.vector_store.search(...)` with the same scope filters applied as metadata. Optional reranker at the end.

**Storage backends.** The mem0 vectorDB registry supports Qdrant (default), Chroma, PGVector, Upstash Vector, Milvus, Pinecone, MongoDB, Azure, Redis, Valkey, Elasticsearch, OpenSearch, Supabase, Vertex AI, Weaviate, FAISS, Amazon S3 Vectors, Databricks, Turbopuffer. The TypeScript SDK only supports Qdrant, Redis, Valkey, Cloudflare Vectorize, and in-memory. **No Convex adapter exists.** No SQLite or plain-file option either. A SQLite table tracks mutation history as the audit trail.

**Embedding providers.** Swappable via `EmbedderFactory.create()` — OpenAI default, plus HuggingFace, Ollama, Vertex AI, Azure, etc.

**Namespacing.** Three-level: `user_id`, `agent_id`, `run_id`. Flat, no nesting. No concept of "lab" or "global" — you'd fake it by sharing `user_id="lab_X"`.

**Audit trail.** Yes, SQLite history log (`db.add_history()` / `db.get_history()`) records previous value, new value, action type, actor_id, timestamps. This is the cleanest audit pattern in the set.

**Pros**
- Battle-tested, biggest community, active daily, framework-agnostic
- `infer` flag controls whether to run an LLM over messages before storing — the clearest "AI summary" pattern
- Clean mutation audit log in SQLite
- Excellent reference for `add()` / `search()` / `update()` semantics

**Cons**
- No Convex adapter, no plans for one
- Graph features paywalled on the hosted product (open source still has the code but the hosted story matters for marketing)
- Only 49% on LongMemEval benchmark ([vectorize.io](https://vectorize.io/articles/best-ai-agent-memory-systems)) — strong for personalization, weak for institutional knowledge
- Only 3 scopes (user/agent/run). No lab/org layer natively.
- Python-heavy; TypeScript SDK is a thinner port

**Hubify fit:** 6/10. Don't fork, but study `main.py` carefully when implementing Hubify's `add`/`search`/`update`/`delete` shapes. The `(user_id, agent_id, run_id)` filter pattern is the one to copy.

**Verdict:** Reference architecture. Study the API surface and audit log design; ignore the storage layer.

---

### 2. Letta (letta-ai/letta) — formerly MemGPT

- **Repo:** https://github.com/letta-ai/letta
- **Stars:** 21,937
- **Forks:** 2,320
- **License:** Apache-2.0
- **Language:** Python (99.5%)
- **Last commit:** 2026-04-08 (active)
- **Open issues:** 97
- **Repo size:** 294 MB — heavy

**Architecture.** Letta is a **full agent runtime**, not a memory library. The `Agent` class in `letta/agent.py` extends `BaseAgent` and manages three distinct memory layers:

1. **Core memory** — structured `Memory` blocks ("human", "persona", etc.) that are *always* in the LLM context window. Editable by the agent itself via tool calls. Managed by `BlockManager`.
2. **Recall memory** — full historical message archive, searchable but not always in context. Managed by `MessageManager`.
3. **Archival memory** — external searchable passages (the closest thing to "vector memory"). Managed by `PassageManager` → `PostgreSQL + pgvector` (or Turbopuffer for cloud).

`PassageManager` (from `letta/services/passage_manager.py`) handles embedding generation via an `LLMClient`, pads embeddings to `MAX_EMBEDDING_DIM` for pgvector compatibility, and uses a dual-write pattern (SQL first, then vector store) when Turbopuffer is enabled. Passages have tags, stored in both JSON columns and a `PassageTag` junction table.

**Storage backends.** Postgres is the only supported backend — `alembic` migrations, `init.sql`, dual-write to Turbopuffer for cloud. No SQLite, no Convex, no filesystem.

**Embedding providers.** Abstracted via `LLMClient`; OpenAI default, also supports Anthropic, Azure, Ollama, etc.

**Namespacing.** Per-agent memory is the primary scope; users are a secondary concept. Shared "organization" scope exists but is coarse. No native lab/global layer.

**Audit trail.** `StepManager` logs every agent step; `JobManager` tracks executions. Pretty detailed, but wired into the Letta runtime — hard to extract standalone.

**Pros**
- The cleanest conceptual model for agent memory in the space (core/recall/archival is genuinely the right abstraction)
- Self-improving agents: the agent edits its own core memory via tool calls
- Full streaming, checkpointing, tool registry — if you wanted an agent *runtime*, this would be it
- Active daily development, well-funded company

**Cons**
- Forking is practically impossible — you'd inherit 294 MB of code and a Postgres+Alembic dependency
- No Convex path
- It's a platform, not a component
- Heavy learning curve (steep per [vectorize.io](https://vectorize.io/articles/best-ai-agent-memory-systems))
- User-layer is an afterthought; org-layer is coarse

**Hubify fit:** 4/10 as code. 9/10 as conceptual reference.

**Verdict:** Don't fork. **Steal the core/recall/archival tiering idea** and map it to Hubify: core = lab dossier summary always in context; recall = raw message log searchable; archival = embedding-searchable long-term facts.

---

### 3. Zep (getzep/zep) + Graphiti (getzep/graphiti)

- **Zep repo:** https://github.com/getzep/zep
- **Zep stars:** 4,383 | forks: 600 | license: Apache-2.0
- **Graphiti repo:** https://github.com/getzep/graphiti
- **Graphiti stars:** 24,618 | forks: 2,451 | license: Apache-2.0
- **Last commit (Graphiti):** 2026-04-05
- **Zep OSS status:** **deprecated.** The community edition has been moved to `legacy/` and Zep is now cloud-only. Graphiti is the open-source engine underneath.

**Architecture (Graphiti).** Temporal knowledge graph. The `Graphiti` class (`graphiti_core/graphiti.py`) takes a `graph_driver` (Neo4j, FalkorDB, Kuzu, or Amazon Neptune), `llm_client`, `embedder`, `cross_encoder`, and `tracer`. Main methods:

```python
add_episode(name, content, source_description, reference_time, valid_at, source, ...)
add_episode_bulk(episodes)
remove_episode(uuid)
retrieve_episodes()
search(query, group_ids, ...) -> list[EntityEdge]
search_(query, group_ids, config, search_filter) -> SearchResults  # advanced
build_communities()
summarize_saga()
add_triplet(source_node, edge, target_node)
```

**Episodes** are the atomic unit — raw ingested data (text, message, JSON) with a `reference_time` and optional `valid_at`. The LLM extracts entities and relationships from each episode and writes them to the graph. Every edge (fact) has a **bi-temporal validity window** — facts aren't deleted when they become stale, they're invalidated with an `invalid_at` timestamp. This lets you query "what was true on 2026-01-15."

**Namespacing.** `group_id` partitions the graph; when omitted it defaults. Multi-tenancy is achieved by switching the driver's active database on a per-request basis. This is the most explicit multi-tenancy story in the survey, though still flat (no hierarchy).

**Hybrid search.** Best-in-class. `graphiti_core/search/search.py` exposes a search system combining:

- **BM25 full-text** (keyword)
- **Cosine similarity vector search** (semantic)
- **BFS graph traversal** (relational)
- Rerankers: RRF, MMR, cross-encoder, distance-based

`SearchConfig` is composed of `NodeSearchConfig`, `EdgeSearchConfig`, `EpisodeSearchConfig`, `CommunitySearchConfig`, each with its own method list + reranker + thresholds. Benchmarked at 63.8% LongMemEval vs mem0's 49.0% — the 15-point gap is attributed to temporal reasoning ([vectorize.io](https://vectorize.io/articles/best-ai-agent-memory-systems)).

**Embedding providers.** OpenAI default; Anthropic, Groq, Gemini, Azure all supported. Warns "works best with LLM services that support Structured Output."

**Pros**
- Temporal reasoning is a category winner — nobody else models edge invalidation with bi-temporal windows
- Hybrid search (BM25 + vector + graph BFS + reranker) is exactly what Hubify wants
- Apache 2.0, permissive
- Active daily development (24k stars)

**Cons**
- **Requires a graph database**: Neo4j, FalkorDB, Kuzu, or Neptune. Hubify would have to stand up and operate one of these, or port Graphiti's search engine to Convex (non-trivial).
- Zep's OSS self-hostable server is deprecated, so the "out of the box" path is Zep Cloud
- Python-only
- LLM cost is non-trivial because every episode runs through entity extraction
- Graph extraction is slow compared to straight vector insert

**Hubify fit:** 5/10. Great ideas, wrong backend.

**Verdict:** Don't fork. **Steal the temporal edge invalidation pattern** (facts get a `valid_at`/`invalid_at` not a delete) and the hybrid search recipe (BM25 + vector + reranker + optional BFS). The group_id scheme is also worth borrowing as the name for Hubify's namespace key.

---

### 4. cognee (topoteretes/cognee)

- **Repo:** https://github.com/topoteretes/cognee
- **Stars:** 15,021
- **Forks:** 1,529
- **License:** Apache-2.0
- **Language:** Python 3.10-3.13
- **Last commit:** 2026-04-07 (active daily)
- **Open issues:** 58
- **Commits:** 6,394+
- **Owner:** Author of the awesome-ai-memory list

**Architecture.** Three-stage pipeline: `add() → cognify() → search()`. From `cognee/api/v1/cognify/cognify.py`, `cognify()` takes `datasets`, `graph_model` (default `KnowledgeGraph`), `chunker`, `chunk_size`, `chunks_per_batch`, `temporal_cognify` flag, `custom_prompt`, and runs a sequential pipeline:

1. Document classification
2. Text chunking (via `TextChunker` or `LangchainChunker`)
3. Graph extraction (identifies key concepts + relationships)
4. Hierarchical text summarization
5. Data point addition (with optional triplet embeddings)
6. Edge extraction (foreign-key style relationships)

Returns `PipelineRunInfo` objects — this is a pipeline abstraction, not a single-shot API.

The `search()` function (`cognee/api/v1/search/search.py`) has a rich signature:

```python
async def search(
    query_text: str,
    query_type: SearchType = SearchType.GRAPH_COMPLETION,
    user: Optional[User] = None,
    datasets: Optional[Union[list[str], str]] = None,
    dataset_ids: Optional[Union[list[UUID], UUID]] = None,
    top_k: int = 10,
    node_type: Optional[Type] = NodeSet,
    node_name: Optional[List[str]] = None,
    node_name_filter_operator: str = "OR",
    only_context: bool = False,
    session_id: Optional[str] = None,
    wide_search_top_k: Optional[int] = 100,
    triplet_distance_penalty: Optional[float] = 6.5,
    feedback_influence: float = 0.0,
    ...
) -> List[SearchResult]
```

Supported query types: `GRAPH_COMPLETION` (default), `RAG_COMPLETION`, `CHUNKS`, `SUMMARIES`, `CODE`, `CYPHER`, `FEELING_LUCKY` (auto-route), `CHUNKS_LEXICAL`. The variety is the best in the survey — cognee treats "search" as a router over multiple retrieval strategies.

**Storage backends.** This is cognee's killer feature: runs **fully local with embedded defaults**: SQLite (relational) + LanceDB (vectors) + Kuzu (graph). Vector adapters also include ChromaDB, PGVector. Graph adapters include Neo4j, FalkorDB, Memgraph, Kuzu. This is the only surveyed project that works out of the box with zero external services ([medium.com top-10 AI memory 2026](https://medium.com/@bumurzaqov2/top-10-ai-memory-products-2026-09d7900b5ab1)).

**Namespacing.** `User` model + `datasets`. Search requires read permission on target datasets — explicit RBAC. The `session_id` parameter adds a sub-scope. This gets closer to Hubify's 4 layers than anyone else, but still no hierarchy.

**Embedding providers.** Multiple LLM/embedding providers via adapters.

**Pros**
- Fully local default (SQLite + LanceDB + Kuzu) — zero external services
- Richest search surface (8 query types, including CYPHER escape hatch)
- `datasets` + `User` = closest thing to multi-namespace RBAC in OSS
- Author owns the awesome-ai-memory list (so this is his own "ideal" design)
- Apache-2.0, active, permissive

**Cons**
- Python-only
- No Convex backend (LanceDB/Kuzu are the embedded stores)
- The `cognify()` pipeline is heavy per add — LLM calls for chunk → classify → extract → summarize
- Smaller community than mem0 / Letta
- Docs are thinner than stars suggest
- Pipeline abstraction is Python-idiomatic; wouldn't port cleanly to TypeScript

**Hubify fit:** 6/10. Great architectural ideas, wrong language + storage.

**Verdict:** Don't fork. **Steal:** (a) the `add → cognify → search` three-stage pipeline as Hubify's mental model; (b) the multi-query-type search router (`GRAPH_COMPLETION`, `CHUNKS`, `SUMMARIES`, `CODE`, `FEELING_LUCKY`); (c) the idea that ingestion is a pipeline, not a single write.

---

### 5. Memori (MemoriLabs/Memori)

- **Repo:** https://github.com/MemoriLabs/Memori
- **Stars:** 13,246
- **Forks:** 1,719
- **License:** Apache-2.0 (GitHub shows "NOASSERTION" in the metadata API, but the `LICENSE` file is full Apache 2.0 — verified)
- **Language:** Python
- **Last commit:** 2026-04-07 (active)
- **Open issues:** 8
- **Created:** 2025-07-24 (newest in the set)

**Architecture.** "SQL-native, LLM-agnostic" layer that intercepts LLM calls and automatically persists conversations to a structured database. The quickstart pattern:

```python
from memori import Memori
from openai import OpenAI

client = OpenAI()
mem = Memori().llm.register(client)
mem.attribution(entity_id="user_123", process_id="support_agent")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "My favorite color is blue."}],
)
```

After `register()`, every LLM call automatically writes memories. The `attribution(entity_id, process_id)` call sets the namespace — without attribution, "Memori cannot make memories."

**Storage.** **SQL-native** — the whole value prop is "no vector DB required." Hosted version is Memori Cloud; self-hosted is called **Memori BYODB** (Bring Your Own Database, so you point it at your own Postgres / MySQL / SQLite). Claims 81.95% on LoCoMo benchmark using only 1,294 tokens per query.

**Namespacing.** Three-level: `entity_id` + `process_id` + `session`. Maps to user + agent + run pattern from mem0 but with richer extraction layers (attributes, events, facts, people, preferences, relationships, rules, skills).

**Pros**
- Only project in the survey that's explicitly SQL-native and does NOT require a vector DB
- Automatic write triggered by LLM calls (matches the "memory writes triggered by agent actions, not user-driven" requirement exactly)
- Very low token cost at query time (1.3k tokens)
- MCP support for non-SDK agents
- Active daily development

**Cons**
- Newest project (July 2025) — less hardened than mem0/Letta/Zep
- "BYODB" isn't on Convex; the BYODB docs mention SQL databases like Postgres/MySQL/SQLite
- Entity/process/session is the entire namespace vocabulary — still no lab/global layer
- Less source-code transparency than mem0/cognee because the killer features live in the LLM interception layer which is tightly coupled to OpenAI/Anthropic SDKs
- The "no embeddings" story is a double-edged sword for Hubify which explicitly wants semantic search

**Hubify fit:** 5/10. Interesting as a counterpoint, but the "SQL-only" philosophy conflicts with Hubify's "hybrid vector + keyword" requirement.

**Verdict:** Don't fork. **Steal the LLM-call interception pattern** — wrapping the client so writes happen automatically — and the `attribution()` API for setting scope before a call. Skip the "no vectors" stance.

---

### 6. Memobase (memodb-io/memobase)

- **Repo:** https://github.com/memodb-io/memobase
- **Stars:** 2,668
- **Forks:** 208
- **License:** Apache-2.0
- **Last commit:** 2026-01-11 (slowing)

**Architecture.** Server-based: FastAPI + PostgreSQL + Redis, fully dockerized. Focus: **user profile-based long-term memory for chatbots.** Profiles are organized as `topic → sub-topic → content` — e.g., `basic_info → name → "Gus"`, `work → title → "Software Engineer"`, `interest → pets → "yorkshire terrier"`. User conversations get batched and processed periodically, updating the profile.

```python
from memobase import MemoBaseClient, ChatBlob
client = MemoBaseClient(project_url=PROJECT_URL, api_key=PROJECT_TOKEN)
```

Blobs (raw conversation chunks) are ingested, profiles are extracted, and blobs are then discarded by default (configurable). v0.0.40 shipped an optimization reducing LLM calls per run from 3-10 down to a fixed 3.

**Storage.** Postgres + Redis. Not replaceable.
**Namespacing.** Per-user only. That's the entire story.

**Pros**
- Super clear hierarchical profile schema (topic/sub-topic/content)
- Optimized LLM cost (3 calls fixed per run)
- Active, Apache 2.0

**Cons**
- **Per-user only** — no agent, no lab, no global layer. Hubify would use ~25% of it.
- Hard dependency on Postgres + Redis + FastAPI — cannot embed in Convex
- Slower commit cadence than mem0/cognee/Memori
- The "user profile" framing doesn't match Hubify's "lab memory" case

**Hubify fit:** 3/10. Too narrowly scoped.

**Verdict:** Skip. Only borrow the `topic → sub-topic → content` idea as a way to structure the user-memory layer.

---

### 7. Memary (kingjulio8238/Memary)

- **Repo:** https://github.com/kingjulio8238/Memary
- **Stars:** 2,577
- **Forks:** 192
- **License:** MIT (the only MIT project in the set — friendliest license)
- **Language:** Jupyter Notebook (a red flag for production use)
- **Last commit:** 2024-10-22 (**stalled for 18 months**)

**Architecture.** Graph-focused memory layer for ReAct agents. Uses LlamaIndex for knowledge graph node management, Neo4j or FalkorDB as the graph store, Perplexity (mistral-7b-instruct) for external queries. Memory updates happen automatically after the ReAct agent generates a response: responses are written back to the KG, entities are timestamped in a memory stream, and a separate "entity knowledge store" tracks frequency + recency.

**Pros**
- MIT license (weakest copyleft of the set)
- Explicit frequency + recency tracking — closest thing to "time decay" in the survey
- Auto-write on agent response is the right pattern

**Cons**
- **Stalled for 18 months** — last commit October 2024. Effectively dead.
- Jupyter Notebook as the primary language means the source is unstructured and not library-packaged
- Requires Neo4j or FalkorDB
- Small community
- ReAct-specific (agent loop tied to LlamaIndex)

**Hubify fit:** 3/10.

**Verdict:** Skip. Reference the frequency+recency design if you want a very specific time-decay formula, but that's it.

---

### 8. memonto (shihanwan/memonto)

- **Repo:** https://github.com/shihanwan/memonto
- **Stars:** 94 (too small)
- **License:** Apache-2.0
- **Last commit:** 2024-10-16 (stalled)

**Architecture.** RDF ontology-based memory. Uses Apache Jena Fuseki as the triple store, Chroma as the optional vector store. Three operational modes: ephemeral (in-memory), triple store only, hybrid (triples + vector). API: `retain()`, `recall()`, `retrieve()`. Supports SPARQL.

**Verdict:** Skip. Too niche (RDF/SPARQL), too small, stalled.

---

### 9. txtai (neuml/txtai)

- **Repo:** https://github.com/neuml/txtai
- **Stars:** 12,380
- **Forks:** 801
- **License:** Apache-2.0
- **Last commit:** 2026-04-07 (very active)
- **Created:** 2020 (oldest in the set)

**Architecture.** "All-in-one AI framework for semantic search, LLM orchestration, and language model workflows." Uses an **embeddings database** as the core — a union of vector indexes (sparse + dense), graph networks, and relational databases. Python 3.10+, built on HuggingFace Transformers and FastAPI.

It's **not a memory system per se**, more of a general-purpose embeddings DB + pipeline framework with bindings for JS/Java/Rust/Go.

**Pros**
- Mature, 5+ years of development
- Multi-language bindings
- Apache 2.0
- Excellent embeddings DB if you want one

**Cons**
- Not an agent memory system — no user/agent/session scoping model, no audit trail, no write-on-action
- Duplicates what Convex already does (vector search + text search + structured storage)
- Adopting txtai means running another service alongside Convex

**Hubify fit:** 2/10. Not the right category.

**Verdict:** Skip. If Hubify needs a standalone embeddings DB *outside* Convex (unlikely), this is the one. Otherwise, Convex covers it natively.

---

### 10. Convex Agent Component (get-convex/agent) — THE DARK HORSE

- **Repo:** https://github.com/get-convex/agent
- **Stars:** 318 (small but it's an official Convex component)
- **Forks:** 79
- **License:** Apache-2.0
- **Language:** TypeScript (98.5%)
- **Install:** `npm i @convex-dev/agent`
- **Docs:** https://docs.convex.dev/agents

Not on the awesome-ai-memory list because it's Convex-specific, but it is **by far the most relevant project for Hubify**.

**Architecture.** A Convex Component (installable as `components.agent` in `convex.config.ts`). Creates an `Agent` class you instantiate with a chat model, instructions, tools, and optionally embedding config:

```typescript
const supportAgent = new Agent(components.agent, {
  name: "Support Agent",
  chat: openai.chat("gpt-4o-mini"),
  instructions: "You are a helpful assistant.",
  tools: { accountLookup, fileTicket, sendEmail },
});
```

Agents work in **threads** — persistent message containers that can be shared across multiple users and agents. Threads auto-include conversation history in each LLM call. Supports streaming via WebSockets, tool calls, file storage with refcounting, rate limiting, multi-agent workflows, and usage tracking per provider/model/user/agent.

**Schema (from `src/component/schema.ts`).** Includes:

| Table | Purpose | Key indexes |
|---|---|---|
| `threads` | Conversation containers (userId, title, summary, status, parentThreadIds) | `by_userId`; search on title |
| `messages` | Individual messages (threadId, order, stepOrder, text, model, provider, usage, tool) | compound `threadId_status_tool_order_stepOrder`; text search on content |
| `streamingMessages` | Real-time streams (state: streaming/finished/aborted) | `threadId_state_order_stepOrder` |
| `streamDeltas` | Delta chunks for streaming | `streamId_start_end` |
| **`memories`** | **User/thread-scoped memory entries with embedding support** | `by_threadId`, `by_userId`, `by_embeddingId` |
| `files` | File metadata (storageId, mediaType, filename, hash, refcount) | `by_hash`, `by_refcount` |
| `vectorTables` | Per-dimension embedding tables (from `vector/tables.ts`) | see below |
| `apiKeys` | Auth keys | `by_name` |

**Vector tables (from `src/component/vector/tables.ts`).** Dynamically generates `embeddings_{dim}` tables for dimensions `128, 256, 512, 768, 1024, 1408, 1536, 2048, 3072, 4096`. Each row contains:

- `model: string` (e.g., `"text-embedding-3-small"`)
- `table: string` (`"messages"` or `"memories"`)
- `userId?: string`
- `threadId?: string`
- `vector: number[]` (of the matching dimension)
- Denormalized `model_table_userId` and `model_table_threadId` fields for vector-search filtering

Each dimension table has a **vector index** with filter fields on `model_table_userId` and `model_table_threadId`, plus a regular index on `["model", "table", "threadId", "_creationTime"]`.

**Hybrid search.** Per the docs: "Hybrid vector/text search capabilities for retrieving relevant messages." Text search on message content (Convex built-in searchIndex), vector search via `ctx.vectorSearch()`, combined in the query layer.

**Pros**
- Only project in the survey that is native to Convex
- Already handles 90% of what Hubify needs: threads, messages, memories, embeddings (10 pre-built dim tables), text search, file refs, streaming, tool calls, usage tracking, rate limiting
- Same auth model, same transaction guarantees, same reactive subscriptions as the rest of Hubify
- Published as an installable component, so upgrades are `npm update`
- Apache-2.0
- Official Convex-maintained

**Cons**
- Only 318 stars — much smaller community than mem0/Letta
- The namespace vocabulary is `userId + threadId`. No agent/lab/global layers out of the box — Hubify would add those.
- No explicit audit trail column (though `_creationTime` + usage tracking covers most of it)
- No LLM-driven summarization of memories (no equivalent of mem0's `infer=True`) — Hubify would bolt that on
- Memories table schema is opinionated (scoped by userId/threadId). Hubify wants squad/lab scoping.

**Hubify fit:** **9/10.** Not a fork — it's a **component you install** and extend.

**Verdict:** **This is the foundation to build on.** Hubify adds its 4-layer namespacing, AI summary pipeline, and audit columns on top. No fork, just composition.

---

### 11. HybridAGI (SynaLinks/HybridAGI)

- **Repo:** https://github.com/SynaLinks/HybridAGI
- **Note:** The original repo appears to have been renamed/redirected. The current `SynaLinks/synalinks-skills` repo is Claude skills for a commercial Synalinks product, not the memory system described on the awesome list.
- **Verdict:** Skip — either deprecated or pivoted away from open source.

---

### 12. Microsoft GraphRAG (microsoft/graphrag)

- **Repo:** https://github.com/microsoft/graphrag
- **Stars:** 32,056
- **License:** MIT
- **Last commit:** 2026-04-07

Not a memory system — a batch RAG pipeline using graph extraction. No session/thread/user concept, no cross-session state. Designed for "analyze this corpus and answer questions about it," not "agent remembers what happened last week."

**Verdict:** Skip — wrong category.

---

## Side-by-Side Comparison

| Project | License | Stars | Last commit | Storage backend | Embeddings | Layers supported | Hybrid retrieval | Audit trail | Convex-ready | Hubify Fit |
|---|---|---|---|---|---|---|---|---|---|---|
| **Convex Agent** | Apache 2.0 | 318 | 2026-04 | **Convex native** | 10 dim tables (128-4096) | user, thread | **yes** (vector + text) | via `_creationTime` + usage | **yes** | **9/10** |
| mem0 | Apache 2.0 | 52,249 | 2026-04 | Qdrant default, 20+ adapters, no Convex | Swappable factory | user, agent, run | partial | SQLite history log | no | 6/10 |
| Letta | Apache 2.0 | 21,937 | 2026-04 | Postgres + pgvector (+Turbopuffer) | Swappable LLMClient | agent, (user) | partial | StepManager + JobManager | no | 4/10 code, 9/10 ideas |
| Zep/Graphiti | Apache 2.0 | 24,618 | 2026-04 | Neo4j / FalkorDB / Kuzu / Neptune | OpenAI/Anthropic/Groq/Gemini | group_id (flat) | **yes** (BM25+vec+BFS+rerank) | via episode history | no | 5/10 |
| cognee | Apache 2.0 | 15,021 | 2026-04 | **SQLite+LanceDB+Kuzu (local default)** | Swappable | User + datasets | **yes** (8 query types) | graph audit | no | 6/10 |
| Memori | Apache 2.0 | 13,246 | 2026-04 | **SQL-native (BYODB)** | not required | entity, process, session | text-only | SQL audit | no (uses Postgres/MySQL/SQLite BYO) | 5/10 |
| Memobase | Apache 2.0 | 2,668 | 2026-01 | Postgres + Redis | configurable | user-only | partial | Postgres | no | 3/10 |
| Memary | MIT | 2,577 | **2024-10** | Neo4j / FalkorDB | LlamaIndex | user | via graph | frequency/recency | no | 3/10 |
| memonto | Apache 2.0 | 94 | 2024-10 | Apache Jena + Chroma | OpenAI/Anthropic | single | via SPARQL | triple store | no | 1/10 |
| txtai | Apache 2.0 | 12,380 | 2026-04 | Embedded (SQLite/DuckDB/RDBMS) | HuggingFace+ | none (not a memory sys) | **yes** (sparse+dense+graph) | no | no | 2/10 |

Legend: "Hubify Fit" is this agent's subjective 1-10 scoring based on license + Convex compatibility + 4-layer coverage + architectural fit.

---

## Recommendation

### 1. Don't fork anything wholesale.

Every project in this survey carries backend assumptions (Postgres+pgvector, Neo4j, Qdrant, LanceDB+Kuzu, SQLite+history-log) that would either run as a sidecar next to Convex or require a rewrite. The lift-and-shift cost of any of them is higher than the lift to build Hubify Memory v1 on Convex primitives directly.

### 2. Install `@convex-dev/agent` as the foundation.

It's already ~70% of what Hubify wants — threads, messages, a `memories` table, 10 pre-built `embeddings_{dim}` tables (128-4096 dimensions), text search on messages, file refcounting, streaming, tool calls, usage tracking, rate limiting, Apache-2.0. It's the only memory-adjacent OSS project in this survey that was written *for* Convex. Hubify adds 4-layer namespacing, AI summarization, and audit columns on top.

### 3. Borrow ideas from four projects, not code.

| From | What to steal |
|---|---|
| **mem0** | The `(user_id, agent_id, run_id)` filter key convention. The `infer=True` flag on `add()` that turns raw messages into AI summaries before storage. The SQLite mutation audit log pattern (mirror it as a Convex table `memory_history`). |
| **Letta** | The core/recall/archival three-tier model. Map to Hubify as: **core** = always-in-context lab dossier (tiny, <2k tokens); **recall** = message log (text search); **archival** = embedded long-term facts (vector search). |
| **Graphiti** | The temporal edge invalidation pattern — memories get `valid_at` / `invalid_at` instead of delete. The hybrid search recipe: BM25 + vector + optional graph BFS + reranker. The `group_id` name as the terminology for the namespace key. |
| **cognee** | The `add → cognify → search` three-stage pipeline as the mental model. The query-type router (`GRAPH_COMPLETION`, `CHUNKS`, `SUMMARIES`, `CODE`, `FEELING_LUCKY`). The idea that ingestion runs an LLM-driven pipeline, not a single write. |

### 4. Keep the Hubify baseline.

The existing `agent_memory` table in `hubify/convex/schema.ts` (lines 3329-3358) with the 7 memory types (learning, context, observation, decision, reflection, skill_result, collaboration) is well-designed and should be the base. It just needs: vector embeddings, a user layer, a lab layer, a global layer, an AI-summary field, an audit trail, and a verified-status flag.

---

## Architecture Sketch — Hubify Memory v1

### Design principles

1. **Convex is the one source of truth.** No sidecars, no Postgres, no Neo4j.
2. **Four layers = four scope keys on the same underlying `memories` table**, not four tables. Query-time filtering is efficient because Convex indexes compose.
3. **Markdown on disk is a backup + export format, not the primary store.** Houston gets plain files via a sync command; reads always go through Convex for consistency.
4. **Writes are agent-triggered.** Every `storeMemory` is called by an agent tool, never by a user typing into a form.
5. **The AI summary is the memory.** Verbatim user messages are also stored, but what gets indexed for recall is the AI-generated summary + tags.
6. **Audit is a separate append-only table.** Never modify a memory in place without writing a history row.

### File layout

```
hubify/
├── convex/
│   ├── schema.ts                      # extend with memories_v2, memory_history, memory_tags
│   ├── memory/
│   │   ├── core.ts                    # add / search / update / delete / summarize
│   │   ├── embeddings.ts               # wrapper over ctx.vectorSearch / embedding model calls
│   │   ├── audit.ts                    # append-only history writes
│   │   ├── summarize.ts                # LLM calls that produce ai_summary + tags
│   │   ├── prune.ts                    # cron: time-decay sweep, low-importance eviction
│   │   ├── export.ts                   # dump scope to markdown files for human review
│   │   └── triggers.ts                 # write hooks: "after message", "after experiment", "after branch close"
│   └── convex.config.ts                # registers @convex-dev/agent component
├── labs/
│   └── <lab_slug>/
│       └── memory/                     # markdown exports, one file per scope
│           ├── core.md                  # always-in-context lab dossier
│           ├── recall/2026-04/*.md     # monthly message log rollups
│           └── archival/*.md           # long-term facts, per topic
└── apps/
    └── memory/
        └── src/
            ├── write.ts                  # Agent SDK helper: mem.remember(scope, content)
            ├── search.ts                 # mem.search(scope, query, options)
            └── index.ts                  # re-exports
```

Markdown files under `labs/<slug>/memory/` are generated on a schedule (or on demand) from Convex. They are for Houston to grep, diff, and review — not for agents to read. Agents go through the Convex API every time.

### Convex schema (extending `hubify/convex/schema.ts`)

```typescript
// convex/schema.ts — additions for Memory v1

import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

// ── Scope: four layers, stored as four optional fields on the same table ──
const SCOPE = v.object({
  // layer 1: user
  user_id: v.optional(v.id("users")),
  // layer 2: agent (within a lab)
  agent_id: v.optional(v.string()),
  // layer 3: lab (squad in Hubify terminology)
  lab_id: v.optional(v.id("squads")),
  // layer 4: global (if all the above are null, memory is global)
  global: v.optional(v.boolean()),
});

const MEMORY_TYPE = v.union(
  v.literal("user_message"),      // verbatim user message
  v.literal("ai_summary"),         // LLM-produced summary of a conversation chunk
  v.literal("learning"),           // durable thing learned from research/work
  v.literal("context"),            // carried between sessions
  v.literal("observation"),        // raw observation from data/papers
  v.literal("decision"),           // decision + rationale
  v.literal("reflection"),         // meta-cognitive self-assessment
  v.literal("skill_result"),       // outcome of using a Hubify skill
  v.literal("collaboration"),      // notes from inter-agent work
  v.literal("experiment_run"),     // record of an experiment execution
  v.literal("dataset_ref"),        // pointer to a dataset + context
  v.literal("blocker"),            // something blocked, with reason
);

export default defineSchema({
  // ... existing tables ...

  memories_v2: defineTable({
    // scope keys — exactly one layer should be primary, but multiple can be set
    user_id: v.optional(v.id("users")),
    agent_id: v.optional(v.string()),
    lab_id: v.optional(v.id("squads")),
    is_global: v.boolean(),

    // content
    memory_type: MEMORY_TYPE,
    topic: v.string(),                        // short label for grouping
    content: v.string(),                      // verbatim content (may be long)
    ai_summary: v.optional(v.string()),       // LLM-produced short summary (<=500 chars)
    tags: v.array(v.string()),                // free-form tags ["quintom", "desi", "barrier"]

    // embeddings — link to the vector table row
    embedding_id: v.optional(v.id("memory_embeddings_1536")),
    embedding_model: v.optional(v.string()),  // e.g. "text-embedding-3-small"

    // temporal + relevance
    created_at: v.number(),
    valid_at: v.number(),                     // when the fact became true
    invalid_at: v.optional(v.number()),       // set when superseded (Graphiti pattern)
    last_accessed_at: v.number(),             // for hot/cold decay
    access_count: v.number(),                 // bump on each retrieval
    importance: v.number(),                   // 1-10, LLM-rated or user-set

    // provenance / audit
    source_type: v.string(),                  // "agent_tool" | "user" | "cron" | "llm_summary"
    source_actor: v.string(),                 // e.g. "agent:dossier-writer" | "user:houston"
    verified: v.boolean(),                    // has another agent or Houston signed off?
    verified_by: v.optional(v.string()),
    verified_at: v.optional(v.number()),

    // linkage
    parent_memory_id: v.optional(v.id("memories_v2")),  // summaries link to source
    supersedes: v.optional(v.id("memories_v2")),         // this memory replaces an older one
    related_mission_id: v.optional(v.id("squad_missions")),
    related_deliverable_id: v.optional(v.id("squad_deliverables")),

    // housekeeping
    expires_at: v.optional(v.number()),
  })
    .index("by_user", ["user_id", "created_at"])
    .index("by_agent", ["agent_id", "created_at"])
    .index("by_lab", ["lab_id", "created_at"])
    .index("by_global", ["is_global", "created_at"])
    .index("by_topic", ["topic", "created_at"])
    .index("by_importance", ["importance"])
    .index("by_last_accessed", ["last_accessed_at"])
    .index("by_mission", ["related_mission_id"])
    .searchIndex("search_content", {
      searchField: "content",
      filterFields: ["user_id", "agent_id", "lab_id", "is_global", "memory_type"],
    })
    .searchIndex("search_summary", {
      searchField: "ai_summary",
      filterFields: ["user_id", "agent_id", "lab_id", "is_global", "memory_type"],
    }),

  memory_embeddings_1536: defineTable({
    memory_id: v.id("memories_v2"),
    user_id: v.optional(v.id("users")),
    agent_id: v.optional(v.string()),
    lab_id: v.optional(v.id("squads")),
    is_global: v.boolean(),
    model: v.string(),
    vector: v.array(v.float64()),
  })
    .vectorIndex("by_vector", {
      vectorField: "vector",
      dimensions: 1536,
      filterFields: ["user_id", "agent_id", "lab_id", "is_global", "model"],
    }),

  memory_history: defineTable({
    memory_id: v.id("memories_v2"),
    action: v.union(
      v.literal("create"),
      v.literal("update_content"),
      v.literal("update_importance"),
      v.literal("verify"),
      v.literal("invalidate"),
      v.literal("supersede"),
      v.literal("delete"),
    ),
    actor: v.string(),              // "agent:X" | "user:Y" | "cron:prune"
    before: v.optional(v.string()), // JSON snapshot of prior state
    after: v.optional(v.string()),  // JSON snapshot of new state
    reason: v.optional(v.string()), // why this change happened
    at: v.number(),
  })
    .index("by_memory", ["memory_id", "at"])
    .index("by_actor", ["actor", "at"]),

  memory_tags: defineTable({
    tag: v.string(),
    memory_id: v.id("memories_v2"),
    scope_key: v.string(),          // concatenation like "lab:bigbounce" for fast filtering
    created_at: v.number(),
  })
    .index("by_tag", ["tag"])
    .index("by_tag_scope", ["tag", "scope_key"])
    .index("by_memory", ["memory_id"]),
});
```

**Design notes:**

- **One memories table, four scope fields.** `user_id`, `agent_id`, `lab_id`, `is_global` are all optional — a memory is assigned to the narrowest layer that owns it. Queries filter by exactly one layer or union multiple.
- **Global memories are not a separate table.** They're rows where `is_global = true` and all other scope keys are null. This means one `searchIndex` / `vectorIndex` covers all 4 layers.
- **Start with one embedding dimension (1536).** Matches `text-embedding-3-small`. Add `memory_embeddings_3072` later if Hubify switches to `-large`. This mirrors the Convex Agent component's pattern of per-dimension tables.
- **Separate embeddings table** (not inlined in `memories_v2`) because Convex's `vectorIndex` has different filter semantics than regular indexes and it keeps the main table row size down.
- **`memory_history` is append-only.** Never updated, never deleted except by explicit admin action. This is the audit trail.
- **`valid_at` / `invalid_at` from Graphiti.** A memory isn't deleted when it becomes stale — it gets `invalid_at` set and is filtered out of normal queries. Historical queries ("what did we think about X on April 1?") still work.

### Embedding provider

- **Default:** OpenAI `text-embedding-3-small` (1536 dim) — cheap, fast, Hubify already has an OpenAI key via the AI gateway
- **Abstracted:** `convex/memory/embeddings.ts` exports `embedText(texts: string[]): Promise<number[][]>` with a provider adapter pattern. First provider: OpenAI. Second (later): Voyage AI. Third (later): local Ollama for privacy-sensitive labs.
- **Batching:** Always batch embedding calls when inserting multiple memories (mem0 caches embeddings per `add()` call — Hubify should too, see `_add_to_vector_store` in `mem0/memory/main.py`).

### Search API surface

```typescript
// apps/memory/src/search.ts — Agent-facing SDK

import type { Id } from "../../../hubify/convex/_generated/dataModel";

export type Scope = {
  user_id?: Id<"users">;
  agent_id?: string;
  lab_id?: Id<"squads">;
  global?: boolean;
};

export type SearchOptions = {
  query: string;
  scope: Scope;
  limit?: number;              // default 20
  memory_types?: string[];     // filter by type
  tags?: string[];              // must include all these tags
  time_range?: { from?: number; to?: number };
  mode?: "hybrid" | "vector" | "text";   // default "hybrid"
  include_invalidated?: boolean;          // default false
  min_importance?: number;
};

export async function search(opts: SearchOptions): Promise<MemorySearchResult[]> {
  // Impl in convex/memory/core.ts:
  // 1. Run vector search via ctx.vectorSearch on memory_embeddings_{dim}
  //    with filter on scope fields + model
  // 2. Run text search via .withSearchIndex("search_content", ...)
  //    with same scope filter
  // 3. Run text search on "search_summary" (ai_summary field)
  // 4. Merge results with RRF (reciprocal rank fusion)
  // 5. Apply time-decay: score = base_score * exp(-lambda * days_since_last_access)
  //    with lambda configurable per scope
  // 6. Bump last_accessed_at + access_count on retrieved memories
  // 7. Return top K with computed relevance score
}

export async function remember(scope: Scope, input: {
  type: MemoryType;
  topic: string;
  content: string;
  tags?: string[];
  importance?: number;        // optional; LLM rates if omitted
  infer?: boolean;             // if true, run summarizer to produce ai_summary
  verified?: boolean;
  source_actor: string;
  parent_memory_id?: Id<"memories_v2">;
  supersedes?: Id<"memories_v2">;
}): Promise<Id<"memories_v2">> {
  // Impl:
  // 1. If infer=true, call summarize.ts to produce ai_summary + tags + importance
  // 2. Generate embedding from (ai_summary or content) via embeddings.ts
  // 3. Insert memories_v2 row
  // 4. Insert memory_embeddings_1536 row
  // 5. Insert memory_tags rows for each tag
  // 6. If supersedes, patch that memory's invalid_at = now
  // 7. Write memory_history row with action="create"
  // 8. Return new memory id
}

export async function verify(memory_id: Id<"memories_v2">, actor: string, reason?: string): Promise<void>;
export async function invalidate(memory_id: Id<"memories_v2">, actor: string, reason?: string): Promise<void>;
export async function supersede(old_id: Id<"memories_v2">, new_input: ...): Promise<Id<"memories_v2">>;
```

### Memory write triggers (agent-action-driven)

Every write goes through an agent tool, never through user-side code. Seven primary triggers:

| Trigger | Layer written to | Who writes | `infer` mode |
|---|---|---|---|
| **User sends message to lab chat** | User + Lab | chat frontend mutation | no (verbatim) |
| **LLM responds in chat** | User + Lab | chat frontend mutation | yes (summary of exchange) |
| **Agent completes a tool call** | Agent + Lab | agent runtime hook | yes (outcome summary) |
| **Experiment finishes** | Lab | squad runtime hook | yes (result summary) |
| **Research branch opens/closes** | Lab + Global | squad runtime hook | yes (decision summary) |
| **Periodic lab reflection (daily cron)** | Lab | scheduled action | yes (meta-summary of the day) |
| **Cross-lab learning promotion** | Global | manual review + agent | yes (generalized learning) |

No user typing in a form ever writes a memory directly. Houston's UI surfaces are read-only or go through agent tools.

### Memory read triggers

- **Every new agent turn** calls `search(scope=<agent's lab>, query=<last user message>)` and prepends the top-5 results to the system prompt
- **Every new lab session** loads the lab's `core.md` (always-in-context dossier) plus top-20 recent lab memories
- **Every new cross-lab query** searches `global` scope first, then the relevant `lab_id`
- **Every experiment plan** queries `(lab_id, memory_type="experiment_run")` to see what's already been tried

### Time-decay / relevance scoring

- **Time decay (soft):** query-time score multiplier `exp(-lambda * (now - last_accessed_at) / 86400000)` where lambda is 0.01 by default (half-life ~70 days). Tunable per scope.
- **Importance (hard):** `importance` field is multiplied into the final score. LLM assigns importance 1-10 on `infer=true` writes.
- **Access boost:** `access_count` contributes log-scaled to the score. Memories retrieved often stay hot.
- **Pruning cron (daily):**
  - Delete rows where `expires_at < now`
  - Delete rows where `importance < 2` AND `created_at < now - 90d` AND `access_count == 0`
  - Cap per-scope at N rows (default 500 per agent, 5,000 per lab, 20,000 global) — evict the oldest low-importance rows

### Markdown export workflow

Houston's "I want plain files" requirement is satisfied by a read-only export, not primary storage:

- `convex/memory/export.ts` has an action `exportLabToMarkdown(lab_id)` that dumps the scope to files under `labs/<slug>/memory/`
- Scheduled nightly via Convex cron
- Manual trigger via `npx convex run memory/export:exportLabToMarkdown '{"lab_id": "..."}'`
- Files are gitignored (not committed to the Hubify repo); they live in a separate `memory-exports` repo or an S3 bucket for backup

This gives Houston greppable markdown without the ACID complexity of markdown as primary storage.

### Namespacing scheme — full layer definition

| Layer | Scope fields set | Example use | Who reads | Who writes |
|---|---|---|---|---|
| **1. User** | `user_id` only | Houston said "I hate proton colliders" | Any agent Houston talks to | Chat runtime when Houston speaks |
| **2. Agent** | `user_id + agent_id` OR `agent_id + lab_id` | `bigbounce/agent:dossier-writer` learned that LaTeX compiles on H200 pods | Just that agent across sessions | Agent's own tool calls |
| **3. Lab** | `lab_id` only (or `lab_id + agent_id` for lab-internal agent facts) | Big Bounce lab has 14 closed barriers and 3 open branches | All agents in that lab | Any agent in the lab (verified by lab lead agent) |
| **4. Global** | `is_global = true`, all other scope keys null | "Cognee is an OSS memory system, Apache 2.0" | Every new lab on bootstrap | Cross-lab review agent |

When a new lab is created, a bootstrap action runs:

```typescript
// Pseudocode
async function bootstrapNewLab(lab_id: Id<"squads">) {
  // 1. Pull top-K most-accessed global memories and surface them as "prior knowledge" in the lab's core.md
  const globals = await search({ query: lab.topic, scope: { global: true }, limit: 50 });

  // 2. Write them as lab-scoped memories with parent_memory_id pointing back to the global originals
  for (const g of globals) {
    await remember({ lab_id }, {
      type: "learning",
      topic: "bootstrap:global_knowledge",
      content: g.content,
      ai_summary: g.ai_summary,
      tags: g.tags,
      importance: g.importance - 1,  // slightly lower than the originals
      parent_memory_id: g._id,
      source_actor: "cron:lab_bootstrap",
      verified: false,
    });
  }

  // 3. Write a lab core.md stub from these summaries
  await exportLabCore(lab_id);
}
```

### What to build in which order

1. **Week 1: Schema migration.** Add `memories_v2`, `memory_embeddings_1536`, `memory_history`, `memory_tags` to `hubify/convex/schema.ts`. Write a backfill that copies the existing `agent_memory` rows into `memories_v2` with `lab_id` = `squad_id`. Keep the old table read-only for 30 days.
2. **Week 1-2: Core API.** Implement `remember()`, `search()` (hybrid: text + vector + RRF), `verify()`, `invalidate()`, `supersede()` in `convex/memory/core.ts`. Wire in the OpenAI embedding provider.
3. **Week 2: Agent triggers.** Hook `remember()` into the existing squad runtime at the 7 trigger points listed above. Most of these are single-line additions to `squadCompute.ts` and related files.
4. **Week 3: Summarization pipeline.** Implement the `infer=true` path — LLM call that turns a raw exchange into (ai_summary, tags, importance) in one call. Use a cheap model (gpt-4o-mini or Claude Haiku).
5. **Week 3: Pruning cron + time-decay.** Daily cron that deletes expired + low-importance old rows. Query-time decay applied in `search()`.
6. **Week 4: Markdown export.** Nightly cron that dumps each lab's memories to `labs/<slug>/memory/*.md`. Read-only; gitignored.
7. **Week 4: Global bootstrap.** The `bootstrapNewLab()` action + admin UI for promoting lab memories to global.
8. **Week 5: @convex-dev/agent integration.** Install the Convex Agent component and use its threads/messages/streaming for the chat UI. The `memories_v2` table sits alongside the component's built-in `memories` table — Hubify's is the richer one; the component's is used only for automatic per-thread context.

### What NOT to build in v1

- Graph database — revisit after 6 months if entity/relationship queries become common
- Cypher / SPARQL escape hatch — overkill
- Multi-embedding-model support — pick one model, stick with it for 3 months
- Real-time streaming of new memories to clients — Convex does this for free via subscriptions, no extra work needed
- A GUI memory explorer — the markdown export covers this for v1
- Custom reranker — RRF is good enough; cross-encoder reranker is a v2 feature

---

## Open Questions

1. **Embedding cost accounting.** At what rate does Hubify hit OpenAI embedding quotas? Budget needs to be set before enabling auto-embed on every agent write. Needs a spike: measure current message volume × embedding cost.
2. **Vector search + text search merging.** Convex's `ctx.vectorSearch` runs only in actions, not queries. This means hybrid search has to be an `action` call, which has different latency characteristics. Is this acceptable for synchronous agent turns? Needs a bench.
3. **Per-embedding-dim table sprawl.** The Convex Agent component pre-declares 10 dim tables. Hubify starts with just 1 (1536). If the default embedding model changes, we need a migration story. Should we pre-declare 1536 + 3072 from day one?
4. **Search-index rebuild time.** Convex staged backfill for large tables is supported but untested at Hubify's scale. A migration of the existing `agent_memory` rows (how many?) into `memories_v2` may need to use `staged: true`.
5. **Global memory gatekeeping.** Who (or what) has write permission on `is_global = true`? Initial answer: only a dedicated cross-lab review agent, invoked manually by Houston, but this needs a real policy before going live.
6. **`valid_at` semantics.** Graphiti's temporal model is powerful but rarely used in practice by developers who pick it up. Is the additional complexity worth it for Hubify, or should v1 just use hard deletes + a `deleted_at` field?
7. **Cross-session summarization trigger.** Letta summarizes the message log when the context window fills up; Cognee summarizes hierarchically during cognify. What's the right heuristic for Hubify? Token count, conversation length, explicit user command?
8. **Relationship to the existing `agent_memory` table.** Keep it as a legacy read-only table for 30 days and then drop, or migrate in place? In-place migration is faster but riskier.
9. **Should the `@convex-dev/agent` component's built-in `memories` table be used at all?** The component has its own memories table with embedding support. Using both creates confusion. Decision needed: use theirs for thread-local short-term context, ours for cross-thread long-term memory? Or override theirs entirely?
10. **Testing strategy.** How do you unit-test a memory system? At minimum, need a deterministic embedding mock, a fixture lab with 10 known memories, and search accuracy tests (Recall@5, Recall@10).

---

## References

**Surveyed projects**

- https://github.com/topoteretes/awesome-ai-memory (the starting list)
- https://github.com/mem0ai/mem0 — mem0
- https://github.com/mem0ai/mem0/blob/main/mem0/memory/main.py — mem0 core source
- https://docs.mem0.ai/components/vectordbs/overview — mem0 vector backends
- https://docs.mem0.ai/quickstart — mem0 quickstart
- https://github.com/letta-ai/letta — Letta (MemGPT)
- https://github.com/letta-ai/letta/blob/main/letta/agent.py — Letta Agent class
- https://github.com/letta-ai/letta/blob/main/letta/services/passage_manager.py — Letta PassageManager
- https://github.com/getzep/zep — Zep (OSS deprecated)
- https://help.getzep.com/concepts — Zep concepts
- https://github.com/getzep/graphiti — Graphiti
- https://github.com/getzep/graphiti/blob/main/graphiti_core/graphiti.py — Graphiti core class
- https://github.com/getzep/graphiti/blob/main/graphiti_core/search/search.py — Graphiti hybrid search
- https://github.com/topoteretes/cognee — cognee
- https://github.com/topoteretes/cognee/blob/main/cognee/api/v1/cognify/cognify.py — cognee pipeline
- https://github.com/topoteretes/cognee/blob/main/cognee/api/v1/search/search.py — cognee search
- https://docs.cognee.ai/quickstart — cognee quickstart
- https://github.com/topoteretes/cognee/tree/main/cognee/infrastructure/databases/vector — cognee vector adapters
- https://github.com/MemoriLabs/Memori — Memori
- https://github.com/MemoriLabs/Memori/blob/main/LICENSE — Memori license (Apache 2.0)
- https://github.com/memodb-io/memobase — Memobase
- https://github.com/kingjulio8238/Memary — Memary
- https://github.com/shihanwan/memonto — memonto
- https://github.com/neuml/txtai — txtai
- https://github.com/microsoft/graphrag — Microsoft GraphRAG
- https://github.com/SynaLinks/HybridAGI — HybridAGI (deprecated/pivoted)

**Convex references**

- https://github.com/get-convex/agent — official Convex Agent component
- https://github.com/get-convex/agent/blob/main/src/component/schema.ts — component schema
- https://github.com/get-convex/agent/blob/main/src/component/vector/tables.ts — per-dim vector tables
- https://docs.convex.dev/agents — Convex Agent docs
- https://docs.convex.dev/search/vector-search — Convex vector search primitives
- https://docs.convex.dev/search/text-search — Convex full-text search primitives

**Comparison articles**

- https://vectorize.io/articles/best-ai-agent-memory-systems — 8-framework comparison (2026)
- https://vectorize.io/articles/cognee-alternatives — cognee alternatives survey
- https://vectorize.io/articles/supermemory-alternatives — supermemory alternatives survey
- https://vectorize.io/articles/zep-alternatives — Zep alternatives survey
- https://atlan.com/know/best-ai-agent-memory-frameworks-2026/ — best frameworks 2026
- https://medium.com/@bumurzaqov2/top-10-ai-memory-products-2026-09d7900b5ab1 — top 10 AI memory 2026
- https://dev.to/nebulagg/top-6-ai-agent-memory-frameworks-for-devs-2026-1fef — top 6 frameworks
- https://www.graphlit.com/blog/survey-of-ai-agent-memory-frameworks — Graphlit survey
- https://forum.letta.com/t/agent-memory-letta-vs-mem0-vs-zep-vs-cognee/88 — Letta forum comparison

**Internal Hubify baseline**

- `hubify/convex/schema.ts` lines 3329-3393 — existing `agent_memory`, `agent_messages`, `agent_workspace_files` tables
- `hubify/convex/agentMemory.ts` — existing store/search/prune/backup API surface
- `bigbounce/project-context/convex_integration_plan.md` — BigBounce's Convex integration plan (context on Hubify's Convex patterns)
