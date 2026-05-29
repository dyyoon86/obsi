---
name: youtube-benchmark-script-writer
description: "Turn a user-provided source video/topic into a finished Korean YouTube script by applying a benchmark channel success report/formula to the user's own channel positioning. Outputs hook, body, closing, and CTA."
---

# YouTube Benchmark Script Writer

Use this skill when the user wants to create a YouTube script from a source video/topic while imitating/adapting the success formula of a benchmark channel (e.g. RouteAI, 에딭초이), but fitting the user's own channel `투두TV`.

Default language: Korean.

## Core goal

Input:

- Source video URL or topic/material.
- Benchmark channel name/report/formula: e.g. "RouteAI처럼", "에딭초이식으로".
- User channel context: `투두TV` is positioned around 직접 만든 AI 실무 자동화 스킬/파일/워크플로우 무료배포 and Korean practical work problems.

Output:

- A finished script, not just ideas.
- Structure must include: `훅 → 본문 → 클로징 → CTA`.
- Also provide title candidates and thumbnail text when useful.

## Required context loading

Before writing the final script:

1. If benchmark channel report exists locally, read/use it.
   - RouteAI report: `/home/coka/youtube-channel-reports/routeai/routeai_success_report.md`
   - 투두TV data: `/home/coka/youtube-channel-reports/todo_chn/`
2. If the benchmark report does not exist, first run or ask to run the `youtube-channel-success-report` workflow.
3. If source is a YouTube URL, analyze it with the separate `youtube-source-video-analysis` workflow: collect source metadata/transcript with `yt-dlp`, then extract hook/body/closing/CTA, feasibility, and 투두TV adaptation angle.
4. Do not write from memory if source/transcript can be retrieved.

## Skill separation

Keep the pipeline modular. The user explicitly named the workflow this way:

- **1번 / 골채널분석 스킬**: `youtube-channel-success-report` = benchmark/channel formula extraction.
- **2번 / 타겟영상분석 스킬**: `youtube-source-video-analysis` = one source video analysis and feasibility check.
- **3번 / 대본생성 스킬**: `youtube-benchmark-script-writer` = final script generation using benchmark formula + source video + 투두TV positioning.

Do not collapse 골채널분석 and 타겟영상분석 into one report. First extract the benchmark channel formula, then analyze the target video, then synthesize the final script.

See `references/todotv-analysis-system-notion-workflow.md` for the user's preferred terminology, local/Notion storage structure, and session-derived workflow notes.

When asked for the final output, produce an **all-in-one production package**, not only narration text: title candidates, thumbnail text, final spoken script, face-cam/demo directing, screen-recording cues, pinned comment, description, and downloadable/free asset checklist where relevant.

## 투두TV positioning constraints

투두TV should not become a broad AI news/전망 channel. Default positioning:

> AI로 귀찮은 일을 자동화하고, 제가 만든 파일/스킬/워크플로우를 공유합니다.

Strong content zones:

- Claude Skills / CLAUDE.md / Claude Code practical setup
- HWPX, 한글 보고서, 회의록, 제안서, 한국 실무 문서 자동화
- 유튜브 채널 분석 리포트, 콘텐츠 DB, AI 뉴스 → Shorts/Threads workflow
- 직접 만든 자동화 파일/스킬 무료배포
- 실패담/실험기: 직접 해봤는데 막힌 점, 고친 점, 무료 배포

Avoid unless explicitly requested:

- broad AI macro 전망 (`18개월 뒤 사무직 사라짐`, AGI 담론)
- generic tool roundup (`Claude 완전정복`, `Gemini 총정리`) without a concrete user-made asset
- news-only summaries without a practical artifact
- copying a benchmark channel's wording too closely

## Benchmark adaptation principle

Do not clone the benchmark. Extract its reusable mechanism, then translate to 투두TV.

Example:

- RouteAI mechanism: `최신 AI 도구 → 업무 산출물 → A to Z 가이드 → 무료 자료 CTA`
- 투두TV translation: `한국 실무 문제 → 내가 만든 AI 스킬/파일 → 실제 결과물 시연 → 한계 솔직 공개 → 무료 배포 CTA`

## Script output format

Use this as default. For the user, prefer an **올인원 패키지** format when the video includes face-cam/demo:

```markdown
# 최종 영상 패키지

## 콘셉트 / 핵심 메시지
...

## 제목 후보
1. ...
2. ...
3. ...

## 썸네일 구성
- 문구:
- 이미지 구도:
- 색감/강조:

## 영상 전체 구조
예상: [N]분
- 0:00 ...
- 0:30 ...

## 촬영 전 준비물
- 작업 폴더:
- 샘플 파일:
- 배포 자료:

## 최종 촬영 대본 + 디렉팅
### 0. 오프닝 결과물
- 화면:
- 음성/대본:
- 자막:

### 1. 얼굴 등장 훅
- 화면:
- 대본:
- 편집:

### 2. 본문 ...
- 화면:
- 대본:
- 자막/편집:

## 고정 댓글 초안
...

## 설명란 초안
...

## 촬영 체크리스트
- 얼굴 촬영:
- 화면 녹화:
- 오디오/결과물 샘플:
## Script output format

Use this as default. The user prefers an **all-in-one package**, especially when they plan to film with face-cam plus screen demo:

```markdown
# 최종 대본 패키지

## 제목 후보
1. ...
2. ...
3. ...

## 추천 제목
...

## 썸네일 문구 후보
- ...
- ...

## 영상 콘셉트
...

## 영상 길이
예상: [N]분

## 촬영 전 준비물
- 작업 폴더:
- 테스트 파일/샘플:
- 배포 자료:

## 0. 오프닝 결과물
- 화면:
- 음성/대본:
- 자막:

## 1. 훅 (0:00~0:30)
- 화면/얼굴 캠 디렉팅:
- 완성 대본:

## 2. 본문 1 — 문제 제기 / 왜 필요한가
- 화면:
- 완성 대본:

## 3. 본문 2 — 해결 구조 / 도구 소개
- 화면:
- 완성 대본:

## 4. 본문 3 — 실전 시연 / 단계별 흐름
- 화면 녹화:
- 완성 대본:

## 5. 본문 4 — 결과물 확인 / 한계
- 비교 컷/점수 그래픽:
- 완성 대본:

## 6. 클로징
[완성 대본]

## 7. CTA
[완성 대본]

## 고정 댓글 초안
...

## 설명란 초안
...

## 편집 메모
- 얼굴 캠:
- B-roll / 화면 녹화:
- 자막 강조:
- 자료 배포 위치:
```

## Hook requirements

The hook must be concrete and result-first whenever possible.

Good hook patterns for 투두TV:

- `이 [결과물], 제가 직접 쓴 게 아닙니다.`
- `[귀찮은 실무] 때문에 시간 버리는 분들, 이걸 스킬로 만들어봤습니다.`
- `저도 처음엔 [문제]에서 막혔는데, 결국 [자동화/스킬]로 해결했습니다.`
- `[잘나가는 채널/영상]을 감으로 따라하지 말고, 자막 10개를 모아서 공식으로 뽑아봤습니다.`
- `[AI 도구]가 좋다는 말은 많은데, 실제로 [한국 실무 문제]에 붙이면 여기서 막힙니다.`

Avoid opening with generic news:

- `오늘은 [도구명]에 대해 알아보겠습니다.`
- `[회사]가 [제품]을 공개했습니다.`
- `요즘 AI가 정말 빠르게 발전하고 있습니다.`

## Body structure

Use the user's lived-use tone. The script should sound like the creator actually tried it.

Recommended body flow:

1. **현실 문제:** 내가/시청자가 겪는 구체적 불편.
2. **기존 방식 실패:** ChatGPT/Gemini/수작업으로는 왜 부족했는지.
3. **내가 만든 해결책:** 스킬/템플릿/워크플로우 소개.
4. **시연:** 단계별로 짧고 명확하게.
5. **결과 확인:** 전후 비교 / 실제 산출물.
6. **한계 솔직 공개:** 되는 것과 안 되는 것.
7. **적용 제안:** 누가 쓰면 좋은지.

## CTA rules

CTA should match 투두TV's asset-sharing positioning.

Good CTAs:

- `제가 만든 파일은 고정 댓글에 올려둘게요.`
- `일단 무료로 받아서 본인 양식에 맞게 바꿔보세요.`
- `써보시고 막히는 부분 댓글로 남겨주시면 후속편에서 고쳐보겠습니다.`
- `다음 편에서는 이걸 [다음 자동화]까지 연결해보겠습니다.`

Avoid pushy CTAs:

- `무조건 구독하세요.`
- `이거 안 보면 손해입니다.`
- `지금 당장 구매하세요.`

## Scoring / feasibility check

When the user asks whether to follow a specific video, score it before writing the final script.

Total: 100 points.

### 1. 투두TV fit — 25점

- Concrete Korean practical problem: 10
- Can be framed as 직접 만든 스킬/파일/워크플로우: 10
- Avoids broad macro/news-only angle: 5

### 2. Benchmark formula transferability — 20점

- Has clear result-first hook potential: 7
- Can follow benchmark narrative structure: 7
- Has reusable title/CTR pattern: 6

### 3. Production feasibility — 20점

- User can actually make/demo it: 8
- Needed tools accessible: 5
- Result can be shown visually: 5
- Reasonable production time: 2

### 4. Audience value — 20점

- Saves time/money or reduces painful work: 8
- Viewer can copy/use it immediately: 6
- Free asset/template possible: 4
- Clear target viewer: 2

### 5. Risk / differentiation — 15점

- Low copyright/platform risk: 4
- Not too close to benchmark copy: 4
- Differentiated by user's experience: 4
- Low overclaim risk: 3

Interpretation:

- 85+: make now
- 70–84: make after adjusting angle
- 50–69: maybe, but not priority
- <50: skip

## Final decision output

Before script, include:

```markdown
# 가능성 체크
총점: NN/100
판정: [바로 제작 / 각도 수정 후 제작 / 보류 / 비추천]
핵심 이유:
- ...
- ...
수정해야 할 각도:
- ...
```

Then provide the final script.

## References

- `references/voicebox-video-package.md`: session-specific reference for the VoiceBox / AI voice-cloning video package, including the updated 85/100 fit score, final angle, title/thumbnail, directing beats, ethics note, and pinned-comment assets.

## Session-specific references

- For the VoiceBox/HyperFrames target-video adaptation, see `references/todotv-voicebox-script-package.md`. Durable lesson: if the voice quality is good, do not frame the video as `품질이 별로다`; frame it as `짧은 문장은 좋지만 긴 대본은 20~40초 단위로 쪼개야 실전에서 안정적이다`.

## Paid-script comparison lesson

When a user provides a paid/generated reference script for the same target, compare it against the Hermes script and absorb proven strengths. See `references/paid-vs-hermes-script-comparison.md`.

For VoiceBox/HyperFrames-like automation videos, use a hybrid standard:

1. Result-first hook with a bold, cinematic promise.
2. Face-cam trust reset: `직접 해보니 되는 점/막히는 점이 있었다`.
3. Named pipeline preview: Tool 1 → Tool 2 → Orchestrator → Revision → Practical workflow.
4. Tool-context authority: why this tool matters, privacy/cost/workflow advantage, but verify specific dates/stars/licenses before claiming.
5. Orchestrator metaphor: Claude Code as `지휘자/오케스트레이터` connecting tools.
6. Design iteration demo: after first result, request color/font/layout/tone changes in natural language and rerender.
7. Keep practical 투두TV insight: long scripts should be chunked into 20–40 second segments for stable AI voice generation.
8. End with a series bridge / next automation extension.

## Quality bar

- The final script should be upload-ready, not a summary.
- Write in natural spoken Korean.
- Prefer first-person experience: `제가 해보니까`, `여기서 막혔습니다`, `그래서 이렇게 바꿨습니다`.
- Include concrete screen/action cues.
- Make claims verifiable and avoid exaggeration.
- If source video transcript is available, adapt the concept, not the wording.
- Do not omit the user's channel identity: direct experiment, realistic caveats, free files/templates/workflows shared in pinned comment.
