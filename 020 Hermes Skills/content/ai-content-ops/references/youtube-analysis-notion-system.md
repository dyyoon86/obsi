# YouTube analysis → Notion storage system for 투두TV

Use this reference when the user wants 골채널분석, 타겟영상분석, and 최종대본 results saved/organized in Notion rather than only as local Markdown files.

## User terminology

- **골채널분석**: benchmark/gold channel analysis. Analyze a channel like RouteAI or 에딭초이 to extract success formulas.
- **타겟영상분석**: single target/source video analysis. Score whether one video is worth adapting for 투두TV.
- **최종대본**: final upload-ready script generated from 골채널분석 + 타겟영상분석 + 투두TV positioning.

## Recommended Notion structure

Prefer three related databases under one Notion page, e.g. `투두TV 콘텐츠 분석 시스템`:

1. `골채널분석 DB`
2. `타겟영상분석 DB`
3. `최종대본 DB`

Use Relations:

```text
골채널분석 DB
  ↕ related to
타겟영상분석 DB
  ↕ related to
최종대본 DB
```

This lets the user later see which benchmark channel formula produced which target-video adaptations and which final scripts/actual uploads.

## 1. 골채널분석 DB fields

- `채널명` — Title
- `채널 URL` — URL
- `분석일` — Date
- `니치` — Select or Multi-select, e.g. AI 자동화, AI 콘텐츠, 바이브코딩, 생산성
- `분석 영상 수` — Number
- `코퍼스 규모` — Text
- `핵심 성공 공식` — Rich text
- `후크 공식` — Rich text
- `제목 공식` — Rich text
- `투두TV 적용 가능성` — Select: 높음 / 중간 / 낮음
- `리포트 파일 경로` — Rich text or URL if cloud synced
- `관련 타겟영상` — Relation → 타겟영상분석 DB
- `관련 최종대본` — Relation → 최종대본 DB

Page body should include the full channel success report: overview, persona, hook formulas, narrative structure, CTR patterns, repeatable formulas, weaknesses/opportunities, and 투두TV application.

## 2. 타겟영상분석 DB fields

- `영상명` — Title
- `영상 URL` — URL
- `원본 채널` — Text or Select
- `분석일` — Date
- `골채널분석` — Relation → 골채널분석 DB
- `투두TV 적용 점수` — Number
- `판정` — Select: 바로 제작 / 각도 수정 후 제작 / 보류 / 비추천
- `핵심 각도` — Rich text
- `추천 제목` — Rich text
- `썸네일 문구` — Rich text
- `리스크` — Multi-select: 설치 리스크 / 저작권 / 윤리 / 과장 / 품질 불안정
- `최종대본` — Relation → 최종대본 DB
- `분석 파일 경로` — Rich text

Page body should include: video metadata, one-line summary, hook/body/closing/CTA breakdown, reusable mechanism, 투두TV fit/non-fit, score table, and recommended adaptation angle.

## 3. 최종대본 DB fields

- `콘텐츠 제목` — Title
- `상태` — Status: 아이디어 / 대본완료 / 촬영예정 / 촬영완료 / 편집중 / 업로드완료
- `타겟영상분석` — Relation → 타겟영상분석 DB
- `골채널분석` — Relation → 골채널분석 DB
- `예상 영상 길이` — Text
- `추천 제목` — Rich text
- `썸네일 문구` — Rich text
- `CTA` — Rich text
- `배포 자료 있음` — Checkbox
- `촬영 예정일` — Date
- `업로드 URL` — URL
- `최종대본 파일 경로` — Rich text

Page body should include the upload-ready package: title candidates, thumbnail copy, hook, body, closing, CTA, face-cam/demo directing, screen-recording checklist, pinned comment, description, and downloadable asset list.

## Views

Recommended views:

- 골채널분석: `전체 채널`, `AI 자동화`, `투두TV 적용 가능성 높음`
- 타겟영상분석: `제작 후보`, `점수 높은 순`, `보류 영상`
- 최종대본: `대본완료`, `촬영예정 캘린더`, `업로드완료`

## If using the existing `AI 콘텐츠 소재 DB`

The existing DB can be used as a quick temporary store by setting `카테고리` to one of `골채널분석`, `타겟영상분석`, `최종대본` and putting the full report/script in the page body. But for long-term legibility, create the three related databases above.

## Local file convention

Continue saving local artifacts as well:

```text
/home/coka/youtube-channel-reports/
  {benchmark_channel}/
    {channel}_success_report.md
  source_videos/{video_id}/
    metadata.json
    summary.json
    transcript.txt
    todotv_fit_analysis.md
    todotv_final_script.md
```

When writing to Notion, include the local file path in the relevant DB property so the user can recover the raw transcript/Markdown package later.
