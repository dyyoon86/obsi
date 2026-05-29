---
name: ai-content-ops
description: "Operate creator content workflows for the user's AI/content businesses: AI news-to-Shorts packages, YouTube/Threads/community repurposing, Notion/content DB storage, competitor/video analysis, and shopping-shorts evidence-based sourcing/validation."
---

# AI Content Ops

Use this umbrella skill when the user wants to operate content workflows around AI/channel growth or evidence-based shortform commerce. This includes:

- AI news/trends turned into reusable assets for YouTube Shorts, Threads, community posts, Instagram, or a Notion content database.
- Daily/current AI Shorts news research and one-source multi-use packages.
- YouTube competitor/source-video analysis for channel strategy.
- Korean shopping-shorts / Coupang Partners / Inpock / 생활꿀템 sourcing, scripting, and validation.

This skill intentionally absorbs narrower siblings such as `ai-shorts-news-research` and `shopping-shorts-ops`; use the labeled sections and references rather than looking for one-session micro-skills.

## User context

- The user runs a YouTube AI channel.
- The user gathers AI-related news as source material for Shorts.
- The user wants **원소스 멀티유즈**: one AI news/source item repurposed into Shorts, Threads, community posts, and a Notion DB entry.
- The user primarily communicates in Korean; default to Korean unless they ask otherwise.

## Core principle

Do not merely summarize AI news. Convert it into a **content package**:

1. What happened
2. Why viewers should care
3. A strong 1–3 second hook
4. A 30–45 second Shorts script
5. Titles and thumbnail text
6. Threads short post and/or thread
7. Community/Instagram caption
8. Hashtags
9. Fact-check notes
10. Notion-ready fields when requested

The user’s goal is content production, not passive news reading.

## Daily AI Shorts workflow

This section replaces the former narrow `ai-shorts-news-research` skill. For the preserved detailed checklist/output style, see `references/absorbed-ai-shorts-news-research.md`.

1. Get current date/time with a tool when current-day relevance matters.
2. Collect recent AI items from reliable sources:
   - Official blogs: OpenAI, Anthropic, Google/DeepMind, Meta AI, NVIDIA, Hugging Face
   - Tech/business news: Reuters, Bloomberg, The Verge, TechCrunch, Ars Technica, CNBC
   - Community/trend sources: Hacker News, Reddit LocalLLaMA, Hugging Face Papers, GitHub Trending
3. Filter for Shorts potential:
   - General audience can understand it quickly
   - Strong emotion: surprise, fear, money, opportunity, usefulness, controversy
   - Visualizable with B-roll/demo/screenshots
   - Direct relevance to creators, workers, students, developers, or everyday users
4. Rank 3–5 candidates and choose a clear 1순위.
5. Produce a content package, not just a news list.

## Good Shorts angles

Prefer framing around viewer impact:

- “이제 사람이 직접 안 해도 될 수 있습니다”
- “AI 때문에 돈 버는 회사가 따로 있습니다”
- “이 기술 때문에 가짜 영상 구분이 어려워질 수 있습니다”
- “유튜버/직장인/학생이 바로 써먹을 수 있습니다”
- “AI 경쟁이 챗봇에서 영상/칩/에이전트로 넘어가고 있습니다”

Avoid weak news-anchor starts:

- “구글이 Gemini Omni를 공개했습니다”
- “OpenAI가 새로운 발표를 했습니다”

Instead, lead with the consequence:

- “이제 유튜브 쇼츠도 직접 찍지 않아도 될 수 있습니다.”
- “AI 시대에 진짜 돈을 버는 회사가 숫자로 드러났습니다.”

## Default content package format

Use this structure unless the user asks for something else:

```text
[소재명]

1. 핵심 요약
2. 왜 먹힐 만한지
3. 쇼츠용 훅
4. 쇼츠 대본
5. 쇼츠 제목 후보
6. 썸네일 문구
7. B-roll 아이디어
8. Threads 짧은 글
9. Threads 타래
10. 유튜브 커뮤니티/인스타 캡션
11. 해시태그
12. 팩트체크 포인트
```

## Threads style

Threads should not read like a news article or Instagram carousel copy. It should sound like a compact explainer with a personal interpretation, similar to creator-style Threads posts.

Preferred pattern:

```text
[뉴스 핵심 한 줄]

이게 무슨 말이냐면

[기존 상황 / 사람들이 하던 방식]

근데 이제
[바뀐 점]

핵심은
[오해 방지: "대체"가 아니라 "역할 변화" 등]

결국
[앞으로의 변화 / 내 해석]

[필요하면 짧은 주의문: 검증 필요, 과장 금지]
```

Example:

```text
OpenAI 모델이 80년 된 수학 추측에 반례를 찾았다고 발표함

이게 무슨 말이냐면

수학자들이 오랫동안
“이 정도가 한계일 거다”라고 생각했던 문제를

AI가 수많은 경우의 수를 탐색하다가
다른 가능성을 찾아낸 거임

핵심은
AI가 수학자를 대체했다는 게 아니라

사람이 문제를 정의하고
AI가 인간이 놓쳤을 수 있는 후보를 찾아주는 식으로
연구 방식이 바뀌고 있다는 점

앞으로 AI 경쟁은
말 잘하는 챗봇보다
이런 “발견하는 AI” 쪽이 더 중요해질 수도 있음

물론 세부 검증은 계속 봐야 함
```

Threads tone:

- concise, casual Korean; avoid sounding like a press release
- first line states the news directly
- use line breaks generously for readability
- use `이게 무슨 말이냐면`, `핵심은`, `결국` to guide readers
- explain workflow/impact in plain language rather than dumping facts
- end with a short interpretation or caution
- avoid too many facts/numbers unless they support the point

Threads image rule:

- Prefer **one real/source-adjacent image**, not a 5–8 page card뉴스, when the user is asking for Threads-style posting.
- Good options: official article screenshot, product/demo screenshot, source article image, logo/announcement image, or a relevant public-domain/CC image when the original article image is unavailable.
- Do not over-design Threads images; the text is the main content. One image + short explainer is usually enough.
- If using a substitute image, provide source and license info, and avoid implying it is the article’s official image.

## Local SQLite / LLM Wiki workflow

When the user asks about `LLM Wiki`, `Graphify`, non-Notion DBs, SQLite/RDB/vector DB, or making Hermes use a knowledge base, frame it as a practical staged architecture:

- Notion = 사람이 보는 콘텐츠 운영판
- SQLite = Hermes가 쓰는 내부 지식창고 / FTS 검색 / 관계 테이블
- Markdown = 긴 리포트·대본·자막 원본
- LanceDB/Chroma/pgvector = later semantic search
- Neo4j/Kuzu = later true graph visualization/traversal

Prefer starting with SQLite + Markdown rather than overbuilding with graph DBs. For the current environment, see `references/local-sqlite-llm-wiki.md` for the existing `/home/coka/todotv_knowledge/` wiki files, schema, search commands, and rebuild pattern.

## Notion DB workflow

When the user wants DB storage, recommend starting simple for general AI-news content. For the user's YouTube channel-analysis/script pipeline, use the dedicated **투두TV 콘텐츠 분석 시스템** instead of forcing everything into `AI 콘텐츠 소재 DB`.

YouTube analysis system structure:

- `골채널분석 DB`: benchmark/channel success formula reports.
- `타겟영상분석 DB`: one source video analysis + 투두TV fit score.
- `최종대본 DB`: final upload-ready script packages.

Known DB URLs from the 2026-05 setup:

- 골채널분석 DB: `https://www.notion.so/36b2186db1af81398257f3dfc878864f`
- 타겟영상분석 DB: `https://www.notion.so/36b2186db1af81ec89c3c68af7eab12f`
- 최종대본 DB: `https://www.notion.so/36b2186db1af81aa8645ef265b1ad97f`

For long analysis/deep scripts, store full Markdown locally and put concise summaries + file paths in Notion pages. Long Notion body writes may time out; the durable pattern is properties + readable summary + local path.

For AI news/source-to-content packages, the existing `AI 콘텐츠 소재 DB` remains appropriate. Essential fields:

- 소재명: Title
- 날짜: Date
- 상태: Status
- 우선순위: Select
- 카테고리: Multi-select
- 출처: Text or Select
- 원문 링크: URL
- 쇼츠 훅: Text
- 쇼츠 대본: Text
- Threads 짧은 글: Text

Useful expanded fields:

- 팩트체크 필요: Checkbox
- 핵심 한 줄: Text
- 쇼츠 적합도: Number
- 제목 후보: Text
- 썸네일 문구: Text
- B-roll 아이디어: Text
- Threads 타래: Text
- 유튜브 커뮤니티 글: Text
- 해시태그: Text
- 쇼츠 발행일: Date
- Threads 발행일: Date
- 유튜브 URL: URL
- Threads URL: URL
- 조회수/좋아요/댓글/저장·공유: Number
- 성과 메모: Text

## Notion API setup pattern

For a single user’s own Notion workspace, use **Internal Integration Secret**, not OAuth.

Before writing to Notion, always inspect the live database schema and select/status options. CSV imports and manual edits often leave properties as `rich_text`, while later user edits may change them to `status`, `select`, `multi_select`, `date`, or `number`. Do not assume the documented schema is current. Generate Notion property payloads from the live property types.

Important pitfall: Notion `status` and `select` writes fail if the option name does not exist (e.g. writing `수집됨` when the DB only has `시작 전`, `진행 중`, `완료`). If options differ, either use the existing option names or ask the user to rename/add options before writing. `object_not_found` usually means the integration is not connected to the actual database page or is in the wrong workspace.

For quick verification, use `scripts/notion_probe.py` in this skill to print the DB schema/options and optionally create a small test page.

For a single user’s own Notion workspace, use **Internal Integration Secret**, not OAuth.

Steps:

1. Create an integration at `https://www.notion.so/profile/integrations`.
2. Give at least read/insert/update content permissions.
3. Open the actual Notion database page.
4. Use `...` → Connections/Add connections → add the integration.
5. Get database ID from the DB URL.
6. Store env vars in WSL:

```bash
mkdir -p ~/.config/hermes
cat > ~/.config/hermes/notion.env <<'EOF'
export NOTION_TOKEN='secret_xxx'
export NOTION_DATABASE_ID='database_id_xxx'
EOF

printf '\n[ -f ~/.config/hermes/notion.env ] && source ~/.config/hermes/notion.env\n' >> ~/.bashrc
source ~/.config/hermes/notion.env
```

Verify without revealing the token:

```bash
echo $NOTION_DATABASE_ID
echo ${NOTION_TOKEN:0:10}
```

If Notion returns `object_not_found` for a DB ID, the common fix is to reconnect/share the **actual database page** with the integration and confirm the integration is in the same workspace as the database.

## YouTube competitor/link analysis

When the user sends YouTube links for analysis, treat it as content strategy work, not just video summarization. Use `yt-dlp` metadata + captions when available, analyze each video's hook/structure/proof/CTA, and translate the reusable pattern into the user's AI channel context. For multiple videos, synthesize common formulas only after analyzing the individual links.

For shopping-shorts/account analysis specifically, do **not** pick products by intuition. Start from high-performing videos/accounts, sort by traction, identify whether the format is face-led, use-scene-led, or faceless utilization-hack-led, then reverse-engineer product/search terms/CTA. The user explicitly corrected that product selection must be evidence-based from hot videos/products, not guessed. Also distinguish “human face” from “human-use context”: face is optional, but hand/body/use scenes or surprising utilization hooks often drive performance.

See `references/youtube-competitor-analysis-workflow.md` for the proven workflow, output shape, and May 2026 examples of shopping-shorts/growth-video patterns adapted into AI-channel formats.
See `references/shopping-shorts-competitor-sourcing.md` for session-derived notes on Korean shopping-shorts source accounts, hot-item reverse engineering, human-use-scene vs faceless utilization-hack formats, and output templates.sed. Also distinguish “human face” from “human-use context”: face is optional, but hand/body/use scenes or surprising utilization hooks often drive performance.

See `references/youtube-competitor-analysis-workflow.md` for the proven workflow, output shape, and May 2026 examples of shopping-shorts/growth-video patterns adapted into AI-channel formats.
See `references/shopping-shorts-competitor-sourcing.md` for session-derived notes on Korean shopping-shorts source accounts, hot-item reverse engineering, human-use-scene vs faceless utilization-hack formats, and output templates.

For shopping-shorts operation/tool-building work, also see `references/shopping-shorts-operation-and-tool-notes.md`. Important durable lesson: do **not** pick products by intuition. Source from Douyin/TikTok/Taobao/Korean shopping-shorts evidence, validate Coupang availability and buyer-intent signals, and distinguish face-led creator trust from faceless but human-use-context footage. For this user, the preferred sequence is operate first → collect proof/data → build internal tools → sell the verified system/tool. See `references/shopping-shorts-competitor-workflow.md` for the newer shopping-shorts source-account/product-sourcing workflow and initial Korean source accounts.

## Shopping-shorts / affiliate-short validation

This section absorbs the former `shopping-shorts-ops` skill. For the full product-sourcing scorecard, Inpock mining pattern, usage/function matching guidance, and hook formulas, see `references/absorbed-shopping-shorts-ops.md`.

When the user asks whether Korean shopping-shorts income videos are worth trying, or wants to run the experiment together, frame it as a validation workflow rather than guaranteed income. Separate reusable production patterns from exaggerated revenue claims, estimate probability with the full funnel (`views → profile/comment/DM → link click → purchase → commission`), and recommend a small 2-week test before scaling.

Default experiment: `살림템/생활꿀템` for 40–60대 household audience, 3 shorts/day for 14 days, cross-posted to Instagram Reels/TikTok/YouTube Shorts, with explicit Coupang Partners disclosure and tracked metrics: views, profile visits, link clicks, comments/DMs asking where to buy, and actual commission.

See `references/shopping-shorts-validation-workflow.md` for the detailed reality-check model, product heuristics, 15-second script formula, safety notes, and how Hermes should package product candidates.

## Media handling for social posts

When the user asks what image/video to use for Instagram or Threads:

- Threads-style posts: prefer one source-adjacent image or screenshot plus the text. Do not default to multi-card images unless the user asks for Instagram/card뉴스.
- Instagram feed: use a 4:5 image/carousel when the user wants a polished post; 5 cards is often cleaner than 8 for complex technical topics.
- If official article images cannot be extracted, use a relevant public-domain/CC image or a simple generated abstract background, and explicitly provide source/license info so the user can post safely.
- For YouTube Shorts/video references, `yt-dlp` can download public/unlisted Shorts into MP4. If it reports `Private video`, ask the user to make it public/unlisted or send the file; then retry the same URL. Do not spend time on browser-cookie workarounds unless the user specifically needs a private video downloaded.

See `references/ionflow-social-style.md` for examples from the ionflow setup session.

## Fact-check discipline

- Prefer official source links for model/product announcements.
- Use Reuters/Bloomberg/CNBC/etc. for business claims.
- For numeric claims, cite exact numbers and source.
- Mark uncertain items as `팩트체크 필요` rather than overstating them.

## References

- See `references/notion-ai-content-db.md` for the initial Notion DB schema and setup details from the first user workflow.
- See `references/local-sqlite-llm-wiki.md` for the local non-Notion knowledge-base pattern: Notion as human-facing board, SQLite as Hermes-facing internal DB, Markdown for long reports, then vector/graph DB only when needed.
- See `references/threads-real-image-workflow.md` for the user-preferred Threads pattern: one real/source-adjacent image plus concise Korean explainer copy, not default carousel/card뉴스.
See `references/threads-api-and-browser-automation.md` when the user asks about Threads/Meta API, OpenClaw/browser-agent posting, or multi-account promotion. Key lesson: Threads API exists for legitimate owned-account publishing/insights, but OpenClaw-style multi-account promotional posting should be framed as technically possible yet high-risk; recommend approval-based owned-account workflows instead.