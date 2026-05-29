---
name: youtube-channel-success-report
description: "Generate a deep Korean YouTube channel success-formula report from a channel URL: collect top non-Shorts videos, transcripts, and metadata, then synthesize hook, narrative, CTR, persona, and reusable strategy at reference-report quality."
---

# YouTube Channel Success Report

Use this skill when the user gives a YouTube channel URL/name and wants a benchmark/channel-level success formula report. In the user's terminology, this is **1번 / 골채널분석 스킬**.

Keep this separate from:

- **2번 / 타겟영상분석 스킬** (`youtube-source-video-analysis`): one specific source video feasibility/structure analysis.
- **3번 / 대본생성 스킬** (`youtube-benchmark-script-writer`): final script synthesis using 골채널분석 + 타겟영상분석 + 투두TV positioning.

Do not turn a channel report directly into a final script unless the user asks for 대본생성 after a target video has been analyzed.

## Saved outputs

Default local storage:

```text
/home/coka/youtube-channel-reports/[channel_slug]/
  [channel_slug]_success_report.md
  videos_all.json
  selected_videos.json
  caption_summary.json
  transcripts/
```

When saving to Notion, use the `투두TV 콘텐츠 분석 시스템` structure:

- Store this result in **골채널분석 DB**.
- Put filterable fields in DB properties: 채널명, 채널 URL, 분석일, 니치, 분석 영상 수, 코퍼스 규모, 핵심 성공 공식, 후크 공식, 제목 공식, 투두TV 적용 가능성, 리포트 파일 경로.
- Put a concise readable summary in the page body.
- Keep the full report in local Markdown and link its file path.
- Later 타겟영상분석 and 최종대본 rows should relate back to this row.

See `youtube-benchmark-script-writer/references/todotv-analysis-system-notion-workflow.md` for the cross-DB workflow and known Notion DB URLs.

User-facing alias for this workflow: **1번 골채널분석 스킬**. Use this wording when explaining the modular YouTube workflow to the user.

Use this skill when the user wants a YouTube channel / rival channel / benchmark channel analyzed into a high-quality strategic report similar to:

- `채널 핵심 성장 전략 리포트`
- `골/라이벌 채널의 서사 구조 및 성공 공식 정밀 분석`
- sections like `분석 대상 영상`, `채널 분석 Overview`, `후크 공식`, `내러티브 구조`, `언어 및 톤앤매너`, `CTR 전략`, `추천 타이틀 샘플`

Default language: Korean. The user wants depth and quality comparable to a polished analyst report, not a brief summary.

## Core promise

Input: YouTube channel URL or handle.

Output: A deep report that explains **why the channel works**, based on its best-performing long-form videos, excluding Shorts by default.

The report should feel like a competitive intelligence / creator strategy memo, not a generic YouTube summary.

If the user asks casually in Korean like `이 채널 뭐야?`, `400만명이야?`, or `해당 채널 분석해줘`, start the final answer with a **plain one-line identity answer** and quick scale confirmation before the deeper report. The user often wants to first understand “what kind of channel this is,” so do not bury the basic answer under methodology.

## Local/Notion saving convention

When a benchmark/gold channel is analyzed, save the report and raw artifacts locally, not only in chat:

```text
/home/coka/youtube-channel-reports/{channel_slug}/
  videos_all.json
  selected_videos.json
  caption_summary.json
  transcripts/
  {channel_slug}_success_report.md
```

If the user asks for Notion organization, store each benchmark channel as one row/page in `골채널분석 DB` and relate it to target-video analyses and final scripts. See `ai-content-ops/references/youtube-analysis-notion-system.md` for the recommended schema.

## Mandatory workflow

### 1. Clarify only if necessary

If the user does not specify, use these defaults:

- Analyze top 10 long-form videos.
- Exclude Shorts.
- Rank by view count, but also mention if a newer video overperforms relative to channel baseline.
- Target output: deep Korean report.
- If the user's own application context is known, include `내 채널 적용 포인트`.

Ask only if ambiguity changes execution materially, e.g. the user wants a paid client report vs quick internal memo.

### 2. Collect channel/video data

Use tools, not memory. Use `yt-dlp` from terminal/execute_code when possible.

Recommended collection command patterns:

```bash
yt-dlp --flat-playlist --dump-json --playlist-end 80 --no-warnings "CHANNEL_URL"
```

Then fetch metadata for candidates:

```bash
yt-dlp --dump-json --skip-download --no-warnings VIDEO_URLS...
```

Collect at least:

- channel name
- video title
- URL
- video id
- duration
- view_count
- like_count
- comment_count if available
- upload_date
- description
- thumbnail URL
- subtitles / automatic captions availability

Robust `yt-dlp` metadata pitfall: full `--dump-json` output can be huge. If parsing via tool stdout fails, write each video's JSON directly to a local file and parse the file, rather than parsing a capped/truncated tool output. Also, YouTube popular-sort URLs such as `?sort=p` may not be reliable through flat playlist extraction; if all-time popular ranking matters, fetch a broad candidate sample and sort locally by `view_count`, stating the sampling window.

### 3. Exclude Shorts

Default exclusion rules:

- Exclude videos with `/shorts/` URL.
- Exclude duration <= 60 seconds.
- Exclude obviously vertical Shorts if metadata/URL reveals it.
- If a 61–180s video is ambiguous, keep only if it functions as long-form/tutorial content; otherwise exclude.

### 4. Select analysis set

Default:

1. Sort non-Shorts by view_count descending.
2. Pick top 10.
3. If the channel has recent strong performers, optionally add a short note: `최근 성과 신호`.

If the channel has fewer than 10 usable videos, analyze all available and clearly state the sample size limitation.

### 5. Fetch transcripts/captions

Preferred order for now:

1. **`yt-dlp` caption fetch** for internal prototyping and current Hermes usage. The user explicitly prefers using `yt-dlp` first because it is easier/better for this stage.
2. User-provided/custom transcript API only later if needed for productization or if `yt-dlp` fails repeatedly.
3. Metadata-only analysis if captions fail.

Use `yt-dlp` to attempt Korean captions first, then English/original language, including auto captions:

```bash
yt-dlp --skip-download --write-subs --write-auto-subs --sub-lang ko,en --sub-format vtt VIDEO_URL
```

Clean returned captions/VTT by:

- removing timestamps/tags when making the full transcript
- preserving rough time anchors for hook/narrative analysis
- deduplicating repeated automatic caption lines
- splitting into intro / body / conclusion chunks

If no transcript exists, analyze from title/description/thumbnail metadata and clearly mark `자막 없음 — 메타 기반 분석`.

YouTube API caveat for later: the official YouTube Data API `captions.download` generally requires authorization for captions owned by the authenticated channel and may not expose arbitrary videos' auto captions, so do not switch to YouTube v3 unless the user explicitly asks or provides a working custom endpoint.

### 6. Multi-pass analysis is required

Do not produce the final report in one shallow pass if transcript data exists. Use this structure:

1. **Per-video pass:** summarize each video's topic, promise, hook, proof/result, narrative flow, CTA, title pattern.
2. **Corpus synthesis pass:** compare all selected videos to find repeated formulas.
3. **Report writing pass:** produce polished structured report.

The final report should not merely list videos; it must identify reusable patterns.

## Desired output structure

Use this structure unless the user asks otherwise.

```markdown
# 채널 핵심 성장 전략 리포트

📺 Channel: [채널명]
🎬 [N]개 영상 분석
📝 [approx chars/tokens/transcript corpus] 코퍼스

## 00. 분석 대상 영상
1. [제목]
   - URL:
   - 조회수:
   - 업로드일:
   - 길이:
   - 분석 메모: [왜 선정됐는지]

## 01. 채널 분석 Overview
### 🧬 채널 정체성
[아키타입, 포지셔닝, 시청자가 기대하는 역할]

### 🎯 시청자 페르소나
[누가 보는지, 밤에 잠 못 자는 고민, 욕망, 두려움, 구매/시청 동기]

### 📁 카테고리 / 하위 니치
[표면 니치와 실제 하위 니치 구분]

### 💎 차별화 가치
[다른 채널과 다른 점, 복제 어려운 자산]

## 02. 후크 공식
### 초반 30초 승부수
[채널의 공통 훅 전략 요약]

#### 01. [후크 패턴명]
- 설명:
- 심리 기제:
- 실제 예시:
- 재사용 템플릿:

#### 02. [후크 패턴명]
...

#### 03. [후크 패턴명]
...

## 03. 내러티브 구조
### 콘텐츠 서사 구조
[전체 내러티브 요약]

#### STEP 1. 도입부 ([time])
- 역할:
- 기법:
- 실제 예시:

#### STEP 2. 초기 설명 ([time])
...

#### STEP 3. 실전/전개 ([time])
...

#### STEP 4. 결론/확장 ([time])
...

## 04. 언어 및 톤앤매너
### 핵심 화법 및 전달 스타일
- 화법 스타일:
- 페이싱 스타일:
- 정보 밀도:
- 신뢰 형성 방식:

### 감정 유발 키워드
[키워드 나열]

### 시그니처 표현
[반복 표현]

## 05. 클릭률(CTR) 극대화 전략
### 썸네일 & 타이틀 전략
[제목/썸네일의 공통 대비, 숫자, 시간, 난이도, 결과물, 권위 장치]

### 검증된 제목 패턴
1. `[패턴]`
2. `[패턴]`
3. `[패턴]`

### 추천 타이틀 샘플
#1 ...
#2 ...
#3 ...

## 06. 반복되는 성공 공식
### 공식 1. [공식명]
- 구조:
- 왜 먹히는지:
- 적용 예시:

### 공식 2. ...

## 07. 약점 / 빈틈 / 기회
- 채널이 아직 덜 다루는 영역
- 후발주자가 비집고 들어갈 각도
- 콘텐츠 포맷 확장 기회

## 08. 내 채널/사용자 적용 전략
[사용자의 known context에 맞춰 적용. 예: AI 채널, ionflow, Threads, Shorts]

### 바로 만들 수 있는 영상 아이디어 10개
1. [제목] — [훅/구성]
...

## 09. 최종 요약
[이 채널의 성공 공식 3~5줄]
```

## Quality bar

The user specifically wants reference-level quality. Follow these standards:

- Write with confident strategic interpretation, not vague statements.
- Tie every major claim to observed titles, transcripts, or recurring patterns.
- Include actual examples from analyzed videos whenever possible.
- Use psychological/content strategy terms when helpful, but explain them plainly.
- Avoid generic phrases like `꾸준함이 중요합니다`, `좋은 콘텐츠를 만듭니다` unless converted into a specific mechanism.
- Distinguish surface topic from deeper viewer desire.
- Extract reusable formulas, not just summaries.
- Include `왜 이게 먹히는지` for each formula.
- Use Korean section labels and polished report language.

## Analysis dimensions

### Channel identity

Look for:

- role/archetype: mentor, builder, experimenter, curator, critic, insider, storyteller
- promise: time saving, money saving, mastery, confidence, access, entertainment, status
- repeated transformation: `before viewer state → after viewer state`

### Viewer persona

Infer:

- job/life situation
- pain points
- aspirations
- fears
- what they want to avoid wasting: time, money, attention, opportunity
- what self-image they want: creator, expert, early adopter, efficient worker, smart consumer

### Hook formulas

Common hook types:

- impossible-result hook: `이게 가능해?`
- time compression: `1시간짜리를 5분 만에`
- cost removal: `무료로`
- effort removal: `코딩 없이`, `말 한마디로`
- fear/loss hook: `돈 낭비하지 마세요`
- contrarian hook: `감으로 분석하지 마세요`
- proof-first hook: show final result before process
- challenge hook: `직접 만들어봤습니다`

### Narrative structures

Identify whether videos follow:

- problem → promise → tool stack → demo → proof → takeaway
- myth/old way → new way → demonstration → implications
- result-first → reverse-engineer process → apply to viewer
- comparison → recommendation → decision rule

### CTR/title formulas

Extract reusable title templates including:

- `[결과물] + [시간 단축] + [도구]`
- `[고통/비용] 끝? [AI/방법]으로 [결과]`
- `[경고] + [선택/실수] + [대안]`
- `[누구나/코딩없이] + [desired output] + 만들기`

For each title pattern, include why it works.

## Handling long reports

If the final report would exceed chat comfort, do not degrade quality. Instead:

- Provide a strong first report in chat.
- Also write a full Markdown report to a file if useful.
- Offer to expand specific sections.

Good file paths:

```text
/home/coka/youtube-channel-reports/[channel_slug]_success_report.md
/home/coka/youtube-channel-reports/[channel_slug]_videos.json
/home/coka/youtube-channel-reports/[channel_slug]_transcripts/
```

If delivering on Telegram, avoid markdown tables. Prefer a concise top summary first, then sections with bullets. For casual Korean channel questions, explicitly answer `뭐 하는 채널인지`, `구독자/규모`, and `왜 큰지` before the full framework.

## Case references

- `references/routeai-todotv-fit-check.md` — session-specific RouteAI vs 투두TV notes and title recommendations.
- `references/evancarmichael-case-notes.md` — Evan Carmichael large English self-help/authority-curation channel precedent, 투두TV adaptation angles, and yt-dlp metadata parsing pitfall.

## Verification

Before final answer:

- Confirm the number of videos analyzed.
- Confirm Shorts were excluded or state if not.
- Confirm whether transcripts were available.
- Mention saved file path if a report was written.

## User-context adaptation

For this user, when relevant, include an application section for:

- AI YouTube channel topics
- Shorts/long-form hooks
- Threads-style posts for ionflow
- Notion content DB / source-to-multiformat workflow
- creator/tool-building angle
- fit checks comparing a benchmark channel against the user's own channel `투두TV` / `@todo_chn`

When the user asks whether they should follow/copy a benchmark channel, answer as a strategic fit check: what to copy, what not to copy, why their own channel data suggests that, and concrete next video/title recommendations. Do not only output a generic competitor report.

For session-specific RouteAI vs 투두TV notes and title recommendations, see `references/routeai-todotv-fit-check.md`.
For Evan Carmichael / @evancarmichael, see `references/evan-carmichael-todotv-fit-check.md`: classify it as a format-only reference, not a primary 투두TV 골채널. Copy packaging patterns like `Top 10 Rules`, `ALL OF X Explained`, and `No BS, No Fluff`; do not copy broad motivational/famous-person curation as the channel core.

Do not force shopping-shorts unless the user explicitly asks; it was put on hold.
