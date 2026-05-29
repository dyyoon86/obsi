---
name: youtube-source-video-analysis
description: "Analyze a single YouTube video as source material: collect metadata/transcript, extract concept, hook, structure, claims, required assets/tools, feasibility, and reusable script angles."
---

# YouTube Source Video Analysis

User-facing alias for this workflow: **2번 타겟영상분석 스킬**. Use this wording when explaining the modular YouTube workflow to the user.

Use this skill when the user gives a single YouTube video URL and wants to understand whether/how to use it as source material for their own video, script, experiment, or remake.

Default language: Korean.

## Purpose

This is separate from `youtube-channel-success-report` and should be referred to as **타겟영상분석 스킬** when talking with the user.

- `youtube-channel-success-report` / **골채널분석 스킬**: benchmark/channel-level analysis. Finds a channel's repeated success formula across many videos.
- `youtube-source-video-analysis` / **타겟영상분석 스킬**: single-video/source-level analysis. Extracts what this one video is about, whether the user can reproduce it, and what angle to use.
- `youtube-benchmark-script-writer` / **대본생성 스킬**: final synthesis. Takes source-video analysis + benchmark-channel formula + 투두TV positioning and writes the final script.

Do not merge 타겟영상분석 with 골채널분석. The user wants one result per target video, then a separate final script result.

## Mandatory workflow

When a YouTube URL is provided:

1. Use `yt-dlp` to collect metadata:
   - title, channel, URL, duration, view_count, like_count, comment_count, upload_date, description, thumbnail.
2. Use `yt-dlp` to fetch captions/transcript when possible:

```bash
yt-dlp --skip-download --write-subs --write-auto-subs --sub-lang ko,en --sub-format vtt VIDEO_URL
```

3. Clean captions:
   - remove VTT tags/timestamps for full transcript if needed
   - preserve rough time anchors for hook/structure
   - dedupe repeated auto-caption lines
4. Analyze the video as source material, not as a whole channel.
5. If the user asks whether to follow/remake it, include a feasibility score.

## Default output structure

```markdown
# 단일 영상 소스 분석

## 00. 영상 기본 정보
- 제목:
- 채널:
- URL:
- 길이:
- 조회수/좋아요/댓글:
- 업로드일:
- 자막 수집 여부:

## 01. 한 줄 요약
[이 영상의 핵심 아이디어]

## 02. 영상 구조 분석
### 훅
- 실제 훅:
- 작동 원리:

### 본문
- 전개 단계:
- 데모/증거:
- 설명 방식:

### 클로징/CTA
- 마무리 방식:
- CTA:

## 03. 따라할 수 있는 핵심 메커니즘
- [복제 가능한 구조]
- [그대로 베끼면 안 되는 부분]

## 04. 투두TV 적합성
- 맞는 점:
- 안 맞는 점:
- 투두TV식으로 바꿔야 할 각도:

## 05. 제작 가능성 점수
총점: NN/100
- 실현 가능성:
- 데모 가능성:
- 무료배포/파일화 가능성:
- 차별화 가능성:
- 리스크:

## 06. 추천 각도
- 바로 만들 제목 후보:
- 훅 방향:
- 필요한 준비물:
- 촬영/화면 녹화 컷:
```

## Local/Notion saving convention

When a target video is analyzed for 투두TV, save the result as a reusable artifact, not only in chat:

```text
/home/coka/youtube-channel-reports/source_videos/{video_id}/
  metadata.json
  summary.json
  transcript.txt
  todotv_fit_analysis.md
```

If the user asks for Notion organization, store each target-video analysis as one row/page in `타겟영상분석 DB` and relate it to the relevant `골채널분석 DB` and `최종대본 DB` entries. See `ai-content-ops/references/youtube-analysis-notion-system.md` for the DB schema.

## Feasibility scoring for 투두TV

Total: 100.

### 1. 투두TV fit — 25
- Concrete practical problem: 8
- Can be turned into 직접 만든 스킬/파일/워크플로우: 10
- Matches Korean practical/work/creator context: 5
- Avoids broad macro/news-only angle: 2

### 2. Reproducibility — 25
- User can actually implement/demo it: 10
- Tools are accessible and not too unstable: 6
- Result can be visually shown: 5
- Reasonable production time: 4

### 3. Audience value — 20
- Saves time/money or reduces painful work: 8
- Viewer can copy/use immediately: 6
- Free asset/template possible: 4
- Clear target viewer: 2

### 4. Differentiation — 15
- User can add lived experience: 5
- Not just a copy of the original: 5
- Strong Korean/localized angle: 5

### 5. Risk — 15
- Low copyright risk: 4
- Low tool failure risk: 4
- Low privacy/ethics risk: 4
- Low overclaim risk: 3

Interpretation:
- 85+: make now
- 70–84: make after angle adjustment
- 50–69: not priority
- <50: skip

## 투두TV adaptation rules

For 투두TV, prefer framing around:

- `제가 직접 해봤습니다`
- `이 부분에서 막혔습니다`
- `그래서 파일/스킬/워크플로우로 만들었습니다`
- `고정 댓글에 무료로 공유합니다`
- `되는 점/안 되는 점 솔직히 말합니다`

Avoid:

- broad AI future claims
- pure tool 소개
- copying source video's wording or title too closely
- overpromising automation results

## Saved files

Good local paths:

```text
/home/coka/youtube-channel-reports/source_videos/[video_id]/metadata.json
/home/coka/youtube-channel-reports/source_videos/[video_id]/summary.json
/home/coka/youtube-channel-reports/source_videos/[video_id]/transcript.txt
/home/coka/youtube-channel-reports/source_videos/[video_id]/todotv_fit_analysis.md
/home/coka/youtube-channel-reports/source_videos/[video_id]/todotv_final_script.md
```

When the user asks to save analysis results to Notion, use the `투두TV 콘텐츠 분석 시스템` Notion structure:

- 타겟영상분석 DB for this skill's result.
- Relate the row to the relevant 골채널분석 DB row when available.
- Keep full long analysis in local Markdown and put a concise readable summary + file path in Notion.

For details, see `youtube-benchmark-script-writer/references/todotv-analysis-system-notion-workflow.md`.
