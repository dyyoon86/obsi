# 투두TV VoiceBox target-video adaptation package

This reference captures the reusable pattern from adapting 에딭초이's VoiceBox/HyperFrames video for 투두TV.

## Source video

- Title: `이게 무료? 5분만에 내 목소리 복제해서 영상 자동화하기 | 클로드코드 + 보이스박스 + 하이퍼프레임`
- Channel: `에딭초이 | 콘텐츠 빌더•AI`
- Video ID: `aaiEg5ZniyQ`
- Local source folder: `/home/coka/youtube-channel-reports/source_videos/aaiEg5ZniyQ/`

## Final feasibility judgment

- Score: about `85/100`
- Decision: 제작 추천
- Why: strong result-first hook (`이 나레이션, 제가 직접 녹음한 게 아닙니다`), VoiceBox quality was better than expected, and the workflow fits 투두TV's 콘텐츠 제작 자동화 lane.
- Caveat: not core Korean office-work automation like HWPX/report/meeting notes, so position it as an `AI 콘텐츠 제작 자동화 실험`.

## User correction that changed the angle

The user said VoiceBox quality was actually good. The script should therefore not overemphasize poor voice quality. The durable nuance:

> VoiceBox short-sentence quality can be good, but long scripts may fail or become unstable when pasted in all at once.

So the winning angle is not `품질이 별로다`; it is:

> 짧은 문장은 생각보다 좋다. 긴 대본은 통째로 넣지 말고 20~40초 단위로 쪼개 생성해야 실전에서 쓸 수 있다.

## Recommended title

`이 나레이션, 제가 직접 녹음한 게 아닙니다 | 무료 AI 음성복제 직접 해봤습니다`

## Thumbnail copy

```text
직접 녹음 아님
내 목소리 AI 복제
```

## Core message

`무료 AI 음성복제는 생각보다 쓸 만하다. 다만 긴 대본을 통째로 넣는 게 아니라, 짧게 나눠서 디렉팅해야 실전에서 쓸 수 있다.`

## Face-cam/demo package structure

Use an all-in-one upload package when the user plans to film their face and screen demo:

1. Opening AI voice sample/result first
2. Face-cam reaction: reveal it was not manually recorded
3. Why test it: recording is a bottleneck for creators
4. Workflow diagram: voice sample → VoiceBox → AI narration → chunking → video draft
5. Claude Code install/demo screen recording
6. Voice sample recording on camera
7. Short-sentence quality test
8. Long-script failure/instability test
9. Practical workflow: split script into 20–40 second chunks
10. Optional HyperFrames/video-draft connection
11. Final score/evaluation
12. CTA with checklist/prompt files

## Practical chunking rule

For VoiceBox-style voice generation:

- Do not paste an entire 5–10 minute script at once.
- Split into 20–40 second chunks.
- Keep each chunk to roughly 2–5 sentences.
- Cut at natural pauses or emotional shifts.
- Regenerate only bad chunks.
- Stitch generated audio in the editor.

Example files:

```text
chunk_01_hook.txt
chunk_02_problem.txt
chunk_03_demo.txt
chunk_04_result.txt
chunk_05_closing.txt
```

## Asset/freebie CTA

For 투두TV, include downloadable/checklist assets:

- VoiceBox 설치 체크리스트
- Claude Code 설치 프롬프트
- 긴 대본을 짧게 나누는 기준
- AI 음성 생성 테스트 문장
- 음성복제 윤리/주의사항 체크리스트

Always include a warning: use only the user's own voice or explicitly permitted voices; do not clone others without consent.

## Local saved outputs from the session

- Target-video fit analysis: `/home/coka/youtube-channel-reports/source_videos/aaiEg5ZniyQ/todotv_fit_analysis.md`
- Final script package: `/home/coka/youtube-channel-reports/source_videos/aaiEg5ZniyQ/todotv_final_script.md`
