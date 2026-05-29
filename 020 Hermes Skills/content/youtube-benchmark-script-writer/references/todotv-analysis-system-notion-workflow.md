# 투두TV 유튜브 분석/대본 시스템 — session reference

## User-preferred terminology

Use these Korean labels in conversation and outputs:

1. **골채널분석 스킬** = benchmark/channel formula extraction
   - Actual skill: `youtube-channel-success-report`
   - Input: benchmark channel URL/name, e.g. RouteAI.
   - Output: channel success formula report.

2. **타겟영상분석 스킬** = single source/target video feasibility analysis
   - Actual skill: `youtube-source-video-analysis`
   - Input: one video URL the user may want to follow/remake.
   - Output: structure analysis, 투두TV fit score, adaptation angle.

3. **대본생성 스킬** = final synthesis
   - Actual skill: `youtube-benchmark-script-writer`
   - Input: 골채널분석 result + 타겟영상분석 result + 투두TV positioning.
   - Output: upload-ready script package: hook/body/closing/CTA, title, thumbnail, face-cam/screen-recording direction, pinned comment, description.

## Important workflow correction from user

The user wants **channel analysis and source video analysis separated**. Do not collapse them into one monolithic analysis.

Correct sequence:

```text
[1] 골채널분석
벤치마크 채널의 성공 공식 추출
        ↓
[2] 타겟영상분석
따라하고 싶은 영상 1개의 구조/가능성/점수 분석
        ↓
[3] 대본생성
1번 공식 + 2번 소재 + 투두TV 포지셔닝을 합쳐 최종 대본 작성
```

## Default storage pattern

Local files:

```text
/home/coka/youtube-channel-reports/
  [benchmark_channel]/
    *_success_report.md
    videos_all.json
    selected_videos.json
    caption_summary.json
    transcripts/

  source_videos/[video_id]/
    metadata.json
    summary.json
    transcript.txt
    todotv_fit_analysis.md
    todotv_final_script.md
```

Notion system created in this session:

- Parent page: `투두TV 콘텐츠 분석 시스템`
- Databases:
  - `골채널분석 DB`
  - `타겟영상분석 DB`
  - `최종대본 DB`

Known URLs created:

- 골채널분석 DB: `https://www.notion.so/36b2186db1af81398257f3dfc878864f`
- 타겟영상분석 DB: `https://www.notion.so/36b2186db1af81ec89c3c68af7eab12f`
- 최종대본 DB: `https://www.notion.so/36b2186db1af81aa8645ef265b1ad97f`

Sample pages inserted:

- RouteAI 골채널분석: `https://www.notion.so/RouteAI-36b2186db1af8198a45fc5bcc363f490`
- 에딭초이 VoiceBox 타겟영상분석: `https://www.notion.so/VoiceBox-36b2186db1af8176b110e9ac89cadcf4`
- VoiceBox 최종대본: `https://www.notion.so/VoiceBox-AI-36b2186db1af81efb655dbe9862421d6`

## Notion write pattern

When writing analysis results to Notion:

1. Put key metadata in DB properties for filtering/sorting.
2. Put readable summary blocks in the page body.
3. Keep full long Markdown locally and add the local path property.
4. Use relations:
   - 타겟영상분석 → 골채널분석
   - 최종대본 → 골채널분석 + 타겟영상분석
5. If Notion body insertion times out with long content, insert a concise body summary first and keep full content in local Markdown.

## 투두TV 대본 package requirements

When asked for final script, output an all-in-one package, not just dialogue:

- title candidates and recommended title
- thumbnail text
- video concept and target length
- full spoken Korean script
- face-cam direction
- screen recording/B-roll direction
- subtitle emphasis points
- pinned comment draft
- YouTube description draft
- downloadable/free asset list

The user specifically wants face-included demonstration direction when relevant.

## VoiceBox target-video lesson

For the 에딭초이 VoiceBox source video, the durable adaptation lesson is:

- VoiceBox quality can be good enough for a strong hook (`이 나레이션, 제가 직접 녹음한 게 아닙니다`).
- But long scripts may fail or degrade when pasted all at once.
- 투두TV angle should emphasize the practical workflow: split scripts into 20–40 second chunks, generate per chunk, regenerate only weak chunks, then assemble.
- Avoid overclaiming full automation. Frame as reducing recording burden and creating drafts.
- Include ethics warning: only use own voice or permitted voices.
