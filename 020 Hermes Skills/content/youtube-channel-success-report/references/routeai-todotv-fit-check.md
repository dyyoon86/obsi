# Session reference: RouteAI benchmark + 투두TV fit check

Use this reference when the user asks whether their channel should follow a benchmark AI/automation channel, especially RouteAI-style channels.

## Data collection pattern proven in session

- Use `yt-dlp` for channel listing, metadata, and captions.
- Default path pattern:
  - `/home/coka/youtube-channel-reports/<channel_slug>/videos_all.json`
  - `/home/coka/youtube-channel-reports/<channel_slug>/selected_videos.json`
  - `/home/coka/youtube-channel-reports/<channel_slug>/caption_summary.json`
  - `/home/coka/youtube-channel-reports/<channel_slug>/transcripts/`
- For RouteAI, collected 39 videos, 20 long-form, selected top 10 by views, captions succeeded for all 10, approx 309k caption chars.
- For 투두TV/@todo_chn, collected 5 videos, 4 long-form + 1 short, captions succeeded for all 4 long-form.

## RouteAI success formula observed

RouteAI is not just an AI news/tool channel. It is a practical guide channel that translates AI tools into work automation systems.

Core formulas:

1. **Completeness packaging**
   - Repeated title language: `A to Z`, `이 영상 하나로 끝`, `15분 만에`, `300% 활용법`, `업무 10배`.
   - Viewer promise: one video reduces AI-update overwhelm.

2. **Proof/result first**
   - Open with working outputs: receipt image → expense Excel/report, AI browser automation, competitor site → analysis report.
   - Strong hook template: `지금 보시는 이 결과물, 제가 직접 만든 게 아닙니다. AI가 한 줄 지시로 만든 겁니다.`

3. **FOMO / loss aversion**
   - `대부분 제대로 못 쓰고 있다`, `업데이트가 너무 빠르다`, `99%가 모르는`, `늦게 알면 손해`.
   - Works because AI users fear falling behind.

4. **Tool → job output translation**
   - Claude/Gemini/NotebookLM/n8n are positioned through concrete work outputs: reports, data analysis, sales/PM/SEO workflows, browser automation.

5. **Free resource CTA**
   - Repeated `영상속 자료 무료 받아가세요` / open-chat lead capture.

## 투두TV fit check from session

User’s channel: `투두TV` / `@todo_chn`.

Observed early signals:

- Best short: `구글이 공개한 새로운 영상 AI 쓰고 개빡침` (~1.8k views). Signal: direct use + emotion beats neutral tool news.
- Best long-form: `보고서 5분 컷! 클로드 스킬로 한글(HWPX) 문서 자동 작성하는 법 (스킬 무료배포)` (~889 views). Signal: concrete Korean office pain + direct build + free skill/file distribution works.
- Lower-performing broad/future topic: `딱 18개월 남았습니다 아무도 말해주지 않는 AI의 진짜 현실` (~29 views). Signal: avoid broad AI-future/AGI/job-loss punditry for now.

## Recommendation pattern for the user

Do **not** advise copying RouteAI wholesale. Recommend borrowing structure, not topic breadth.

Good adaptation:

- RouteAI: `AI tools → work automation`
- 투두TV: `directly built AI skills/files/workflows → Korean practical work/content problems solved`

Positioning:

> AI로 직접 만든 실무 자동화 스킬과 파일을 무료로 나눠주는 채널.

Strong content pillars:

- HWPX/Hangul reports
- meeting notes → report
- YouTube channel/transcript analysis report
- AI news → Shorts/Threads/Notion DB workflow
- Claude Skills
- CLAUDE.md practical setup
- direct build/failure retrospectives
- free templates/files/skills

Avoid for now:

- broad AI future prediction / AGI/job-loss takes
- generic `Claude 완전정복` / `Gemini 완전정복` unless tied to a concrete output
- pure news summary without a direct artifact or workflow

## Title rewrites that matched session conclusions

- Weak: `카파시 65줄 CLAUDE.md, 깃허브 스타 10만의 진짜 이유`
- Stronger: `클로드 코드 자꾸 이상하게 짜면 이 65줄 먼저 넣으세요`
- Stronger: `클로드 코드 실수 줄이는 CLAUDE.md 65줄 세팅법`

- Weak-ish: `바이브코딩으로 만든 서비스가 망하는 진짜 이유`
- Stronger: `클로드 코드로 36,000줄짜리 서비스를 만들었는데 아무도 안 썼습니다`

- Strong next video: `유튜브 채널 링크만 넣으면 성공 공식 뽑는 분석기를 만들었습니다`
  - Hook: `경쟁 채널을 감으로 보지 말고, 조회수 높은 영상 10개의 자막을 모아서 성공 공식을 뽑아봤습니다.`

## Report behavior note

When asked “이 채널 따라해도 될까?” combine:

1. benchmark channel formula extraction,
2. user’s own channel data and traction signals,
3. direct verdict: what to copy / what not to copy,
4. concrete next video ideas and title rewrites.

Do not only produce a generic competitor report; answer the strategic fit question.