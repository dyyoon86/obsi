# YouTube competitor/link analysis workflow

Use when the user sends one or more YouTube links and asks/implicitly expects analysis for their content strategy.

## Retrieval pattern

1. Use `yt-dlp --dump-json --skip-download <url>` to collect title, channel, duration, views, upload date, description, and subtitle availability.
2. If captions exist as auto-captions, download Korean VTT with:
   ```bash
   yt-dlp --skip-download --write-auto-subs --sub-lang ko --sub-format vtt <url>
   ```
3. Parse the VTT into time chunks. Auto-captions often duplicate phrases; dedupe consecutive identical cue text before summarizing.
4. If analyzing multiple links, analyze each individually first, then synthesize cross-video patterns after the final link.

## Output shape that worked well for this user

For each video, answer in Korean with concise but useful sections:

- 기본 정보: title, channel, length, views if available, topic, target viewer
- 한 줄 요약
- 구조 분석: opening hook, problem/friction, method/steps, proof/data, CTA
- 왜 먹히는지: title/hook psychology, proof, beginner barrier removal, practical screens/data
- 약점/주의점: especially copyright, policy, income overclaiming, reproducibility
- 네 채널에 적용할 포인트: translate the structure into the user's AI content/channel context

For 3+ videos, add a synthesis:

- 각 영상의 역할/성격 비교
- 공통 성공 공식
- user's channel adaptation formulas: title examples, opening script template, CTA template, experiment/content-series ideas

## Patterns observed in May 2026 creator-analysis session

The user shared three Korean videos about shopping Shorts/YouTube growth. The useful transferable pattern was not the shopping-shorts tactic itself, but the long-form lead-generation structure:

1. **Outcome-first title**: money/result + time compression + “free/no paid course needed”.
2. **Beginner barrier removal**: 구독자 0명, 자본금 0원, 얼굴 없음, 왕초보 가능, 처음부터 보여줌.
3. **Proof before theory**: revenue screenshots, views, YouTube Studio analytics, account setup screens, prompts, editing/link setup.
4. **Step-by-step 실습 화면**: tools and clicks make long videos feel like a course rather than an essay.
5. **Risk/plot twist increases retention**: e.g. copyright strike -> counter-notification -> recovery.
6. **Free-value lead magnet CTA**: comment keyword, free materials, webinar/waiting room/community.

## Applying to the user's AI channel

Recommend adapting the structure, not copying risky tactics. Good AI-channel formats:

- “AI 강의 듣지마세요. 뉴스 하나로 쇼츠 5개 만드는 법 다 보여드립니다”
- “AI 뉴스 쇼츠 7일 동안 매일 3개 올려봤습니다. 살아남은 포맷은 딱 2개였습니다”
- “제가 AI 뉴스 하나를 쇼츠/Threads/롱폼으로 바꾸는 실제 과정”

Template:

1. Strong hook around saved time/money/result.
2. State the pain: news overload, 소재 부족, bland GPT output.
3. Promise a full workflow.
4. Show actual sourcing -> summarizing -> hook generation -> Shorts script -> Threads post -> Notion DB -> upload/result tracking.
5. Share data or before/after examples.
6. CTA: comment keyword for a prompt/template/checklist.

## Pitfalls

- Do not endorse reuploading/downloading others' video sources as a safe tactic. Mention copyright/platform/duplicate-content risk clearly.
- Do not overfocus on transcript minutiae; the user wants channel strategy and reusable formulas.
- Avoid Markdown tables in Telegram; use bullets and labeled sections.
