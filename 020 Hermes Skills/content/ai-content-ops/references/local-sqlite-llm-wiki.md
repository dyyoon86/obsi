# Local SQLite LLM Wiki for 투두TV/Hermes

Use this reference when the user asks to build or use a non-Notion DB/LLM Wiki/Graphify layer for 투두TV, ionflow, or Hermes knowledge.

## Session-derived default architecture

Recommended split:

- **Notion**: human-facing operating board for status, priorities, summaries, links, publish dates.
- **SQLite**: Hermes-facing local knowledge DB for fast structured search, document chunks, relations, metadata, automation logs.
- **Markdown files**: long reports/scripts/transcripts that are too large or awkward for Notion bodies.
- **Vector DB later**: LanceDB/Chroma/pgvector for semantic “similar 소재/대본” search.
- **Graph DB later**: Neo4j/Kuzu only if relationship traversal/visualization becomes complex; start with an RDB `relations` table.

## Existing local wiki created in this environment

Current files:

```text
/home/coka/todotv_knowledge/todotv_wiki.sqlite
/home/coka/todotv_knowledge/build_todotv_wiki.py
/home/coka/todotv_knowledge/sync_notion_to_sqlite.py
/home/coka/todotv_knowledge/search_wiki.py
/home/coka/todotv_knowledge/README.md
```

Current contents:

- Hermes skills and references under `/home/coka/.hermes/skills/`
- local YouTube/channel analysis reports under `/home/coka/youtube-channel-reports/`
- raw heavy metadata/transcripts intentionally excluded in the first pass
- Notion DB pages from `AI 콘텐츠 소재 DB`, `골채널분석 DB`, `타겟영상분석 DB`, `최종대본 DB`
- core tables: `documents`, `skills`, `chunks`, `relations`, `documents_fts`, `chunks_fts`, `runs`
- Notion sync tables: `notion_databases`, `notion_pages`, `notion_blocks`
- FTS5 keyword search enabled at document and chunk level

Example queries:

```bash
python3 /home/coka/todotv_knowledge/search_wiki.py 'Threads OR OpenClaw' --limit 5
python3 /home/coka/todotv_knowledge/search_wiki.py '골채널' --chunks --limit 5
python3 /home/coka/todotv_knowledge/search_wiki.py 'Claude Skills HWPX' --chunks
```

Rebuild after adding skills/reports:

```bash
python3 /home/coka/todotv_knowledge/build_todotv_wiki.py
```

Sync Notion databases into SQLite:

```bash
set -a && source ~/.config/hermes/notion.env && set +a
python3 /home/coka/todotv_knowledge/sync_notion_to_sqlite.py
```

The Notion sync script is read-only against Notion. It reads `NOTION_TOKEN` and `NOTION_DATABASE_ID` from `~/.config/hermes/notion.env`, also attempts the three known 투두TV DB IDs, upserts pages into both Notion-specific tables and the generic `documents`/`chunks`/FTS indexes, and records a `sync_notion_to_sqlite` row in `runs`.

## Schema pattern

Minimum useful schema:

- `documents`: source_type, category, title, path, content, sha, metadata_json
- `skills`: skill name/category/description/path, linked document_id
- `chunks`: document_id, chunk_index, heading, content, title/source/path denormalized for FTS
- `relations`: from_document_id/from_label, relation_type, to_document_id/to_label, evidence
- `notion_databases`: Notion DB id/key/name/schema metadata and last sync time
- `notion_pages`: page id, database id, linked document_id, title/url/timestamps, raw and plain properties, page content
- `notion_blocks`: page block text/raw JSON for body-level inspection
- `documents_fts`, `chunks_fts`: FTS5 indexes
- `runs`: build/import/sync history

For Graphify-like relationships, start with `relations` rows such as:

- `document has_reference reference_file`
- `document mentions_topic Threads`
- `소재 -> generates -> Threads 글`
- `골채널 -> provides_formula -> 제목 공식`
- `타겟영상 -> used_for -> 최종대본`
- `최종대본 -> produced -> 업로드 성과`

## Workflow guidance

1. Keep Notion as the user-visible board until automation/search needs dominate.
2. Put long text, scripts, transcripts, metadata, and search indexes into SQLite/Markdown.
3. Add Notion sync only after the local SQLite core is stable.
4. Add vector search only when keyword search fails for “비슷한 소재/대본” tasks.
5. Add a real graph DB only when the `relations` table is no longer enough.

## User-facing framing

When explaining this to the user, use simple Korean:

- “노션 = 사람이 보는 운영판”
- “SQLite = Hermes가 쓰는 내부 지식창고”
- “Markdown = 긴 리포트/대본 원본 저장”
- “나중에 유사검색은 벡터DB, 관계 시각화는 그래프DB”

Avoid over-engineering early. For this user, the practical default is `Notion + SQLite + Markdown`, not immediate Neo4j/Pinecone.