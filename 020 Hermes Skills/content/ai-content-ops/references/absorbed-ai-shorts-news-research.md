# Absorbed skill: ai-shorts-news-research

This file preserves the narrow session-derived AI Shorts news research skill that was consolidated into the broader `ai-content-ops` umbrella. Use it for exact output shapes and style notes when the user asks for daily AI news/Shorts packages.

---

# AI Shorts News Research

## When to use
Use this workflow when the user asks for AI-related news or trends to use as material for YouTube Shorts or related social repurposing, e.g. “오늘 AI 쇼츠 소재 찾아줘”, “AI 뉴스 쇼츠 대본 만들어줘”, “AI 채널용 오늘 이슈 찾아줘”, “쓰레드 글도 써줘”, “원소스 멀티유즈 패키지 만들어줘”, or “Notion DB에 넣을 수 있게 정리해줘”.

## User context
The user operates a YouTube AI channel and gathers AI-related news as source material for creating Shorts. The deliverable should be creator-ready, not just a news briefing. The user also wants one-source multi-use output: one AI news item should become a Shorts script, Threads post, Threads thread, YouTube community/Instagram caption, and a structured Notion DB record for future tracking and performance analysis.

## Core workflow
1. Establish the date/time 기준 first. For current date/time, use a tool rather than guessing.
2. Collect candidates from multiple source types:
   - Official AI company blogs/newsrooms: OpenAI, Google/DeepMind, Anthropic, Meta AI, NVIDIA, Hugging Face.
   - Fast trend/news aggregators: Google News RSS/search, Hacker News, Reddit/LocalLLaMA where available.
   - Research feeds when useful: Hugging Face Papers, arXiv, Papers with Code.
   - Business/impact sources: Reuters, CNBC, Bloomberg, The Verge, TechCrunch, Axios, MIT Tech Review, ZDNet Korea/AI Times for Korean framing.
3. Prefer items with at least one authoritative/primary source, especially official blogs or major outlets.
4. Select 3–5 candidates, then rank by Shorts value:
   - Strong 1–3 second hook.
   - Easy for general viewers to understand.
   - Visual/demo potential.
   - Direct relevance to creators, productivity, money, jobs, safety, or big-tech rivalry.
   - Clear “why it matters” in 1–2 sentences.
5. Package the output in Korean unless the user asks otherwise.

## Output format
For a daily request, provide:

1. **오늘의 1순위 소재**
   - Topic/title
   - Source(s)
   - 한 줄 요약
   - 왜 쇼츠에 좋은지
   - 쇼츠 훅
   - 30–45초 대본
   - 제목 후보 2–3개
   - 썸네일 문구
   - 해시태그 if relevant

2. **후보 3–5개**
   For each:
   - Topic
   - Source(s)
   - 소재력 / 추천도
   - 한 줄 요약
   - 훅
   - Short script or script skeleton
   - 제목 후보
   - 썸네일 문구

3. **오늘 바로 만들 추천 순서**
   Rank the best 2–3 options and explain briefly why.

For a one-source multi-use request, produce a **콘텐츠 패키지**:
- 소재명
- 날짜
- 카테고리
- 출처 / 원문 링크
- 우선순위
- 쇼츠 적합도
- 핵심 한 줄
- 핵심 관점: news translated into the user’s own creator POV
- 쇼츠 훅
- 쇼츠 대본
- 제목 후보
- 썸네일 문구
- B-roll 아이디어
- Threads 짧은 글
- Threads 타래
- 유튜브 커뮤니티 글 / 인스타 캡션
- 해시태그
- 팩트체크 필요 / 주의할 점
- 메모

## Writing style
- The user wants practical material for Shorts creation, not a broad essay about AI news.
- Keep the language punchy and creator-oriented.
- Translate technical news into simple Korean.
- Do not over-explain mathematical/research details; simplify to “what changed” and “why viewers care”.
- Use bullets and labeled sections; avoid Markdown tables because the user is on Telegram.
- For Shorts/YouTube openings, preserve strong hook energy even when removing AI-ish phrasing. The user may prefer a slightly exaggerated YouTube hook if it improves retention. Do not over-sanitize the first 3–10 seconds into a mild explainer. Instead: keep the curiosity/money/result hook strong, then add realism/caveats in the body.
- For Shorts, frame the first line around viewer impact, fear, opportunity, money, or creator utility rather than the company announcement. Weak: “구글이 Gemini Omni를 공개했습니다.” Strong: “이제 유튜브 쇼츠도 직접 찍지 않아도 될 수 있습니다.”
- For AI-tool tutorial scripts, remove generic AI-copywriting phrases such as “강력한”, “혁신적인”, “엄청난 가능성”, “완벽한 대안”, but keep concrete claims that create curiosity: “이 영상, 사실 제 목소리가 아닙니다”, “목소리 샘플 몇 초”, “유료 TTS 없이 어디까지 가능한지”.
- For Threads, use a calmer insight/POV tone. Threads should not merely repeat the Shorts hook; it should turn the news into an observation about AI, work, content creation, money, or culture.
- When the user asks how to shoot a face-reveal AI tutorial at home, provide a concrete capture list and staging plan: face-cam trust shots, screen recordings, actual vs AI voice comparison, reactions, before/after result clips, and simple background control.

## Verification and sourcing
- Current facts require tool-backed lookup.
- Do not invent features from headlines alone. If the headline is vague, mark it as “보도 기준” or use cautious wording.
- When possible, verify numbers from primary sources. For financial results, prefer company newsroom/SEC/official release.
- If a source is behind a paywall or inaccessible, cite the accessible source and note that it is based on reporting.

## Common Shorts categories
- Big feature launches: “AI가 이제 영상/음성/앱을 만든다”.
- Big-tech rivalry: OpenAI vs Google vs Anthropic vs Meta.
- Creator/productivity tools: video, image, voice, editing, automation.
- Money/infrastructure: NVIDIA, AI chips, data centers, cloud.
- Safety/controversy: watermarking, deepfakes, copyright, jobs, regulation.
- Research breakthroughs: AI contributing to math/science, but explain simply.

## Pitfalls
- Do not return only a list of links; convert news into Shorts-ready assets.
- Do not choose only technically important items if they lack a strong viewer hook.
- Do not make the script too long. Aim for a spoken 30–45 second script.
- Do not rely on a single unverified social post for factual claims unless clearly labeled as rumor/trend.
- Do not present “AI news summary” as the channel concept. The stronger positioning is: translate AI news into what changes for ordinary viewers, creators, work, money, or content production.
- Do not make Threads posts too long or too article-like unless the user explicitly asks for a thread. For a single Threads post, prefer concise insight with line breaks.
- For Notion automation, do not ask the user to paste secrets into chat if avoidable. Recommend environment variables for `NOTION_TOKEN` and ask only for the database ID unless credentials must be configured interactively.
