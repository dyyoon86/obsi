---
name: saas-validation-and-mvp
description: "Validate and plan a small SaaS before building: force a specific user/problem/wedge, create landing-page and social validation assets, then define the smallest MVP only after demand signals. Use when the user says they want to build a SaaS, copy an indie-hacker/AI-SaaS workflow, use gstack/office-hours, validate an app idea, create a landing page, or decide what to build first."
---

# SaaS Validation and MVP

Use this skill when the user wants to build a SaaS or AI product, especially from a vague idea or from seeing someone else build a SaaS. The default posture is **startup office-hours first, implementation second**.

## Core rule

Do **not** jump straight to scaffolding code. First determine:

1. Who has the problem.
2. What they do now.
3. What it costs them.
4. What the smallest paid wedge is.
5. What signal proves demand.

If the user is impatient, ask only the two highest-leverage questions, then give a concrete next action.

## Tone for this user

- Respond in Korean unless the user asks otherwise.
- Be direct and casual.
- Keep the SaaS advice practical, not motivational.
- If the user says they want to build a SaaS, do not keep treating the topic as content for Threads/Shorts. Explicitly switch from “content angle” to “startup/product angle.”

## Startup diagnostic sequence

Ask one question at a time when possible. Push for specifics, not categories.

### Q1. Demand reality

Ask:

> 이걸 진짜 필요로 하는 증거가 뭐야? “있으면 좋겠다” 말고, 없으면 짜증나거나 돈 낼 정도의 증거.

Look for:

- Someone paying.
- Someone manually doing the workflow repeatedly.
- Someone spending hours or money on the workaround.
- Someone asking for access, not just liking the idea.

Red flags:

- “콘텐츠 제작자들 다 필요할 듯.”
- “AI 시대니까 수요 많을 듯.”
- “대기자 명단 있으면 되지 않을까.”

### Q2. Status quo

Ask:

> 지금 그 사람은 이 문제를 어떻게 해결하고 있어? ChatGPT 복붙, Notion 정리, 외주, 스프레드시트, 편집자한테 맡김 중 뭐야? 하루/주 몇 분 걸려?

The current workaround is the real competitor.

### Q3. Desperate specificity

Ask:

> “콘텐츠 제작자” 말고 실제로 가장 아픈 사람은 누구야? 예: AI 뉴스 쇼츠를 매일 올리는 1인 운영자, 콘텐츠 대행사 직원, 유튜브 편집자, B2B 마케터.

Force one narrow first customer.

### Q4. Narrowest paid wedge

Ask:

> 이번 주 안에 돈 받을 수 있는 제일 작은 버전은 뭐야? 로그인/대시보드/자동발행 없이도 돈 낼 기능 하나만 고르면?

Prefer a wedge like:

- URL/text → Shorts hook + 30s script + Threads post + Instagram caption.
- YouTube link/transcript → 조회수형 short-form script variations.
- Manual concierge version where the user sends a link and receives a content pack.

### Q5. Observation

Ask:

> 실제 사용자가 이걸 하는 걸 옆에서 본 적 있어? 어디서 막히고, 뭐가 제일 귀찮아 보였어?

If not, assignment #1 is to watch or interview 3 target users.

### Q6. Future fit

Ask:

> 3년 뒤 AI가 더 좋아지면 이 제품은 더 필요해져, 덜 필요해져? 왜 네 제품만 남아?

Avoid generic “AI grows, so we grow.” Need a thesis.

## Recommended path for the user's likely SaaS

For this user, three strong starting directions have emerged:

1. AI/tech news or video source → platform-specific content package for Shorts, Threads, Instagram, images, hashtags.
2. Baseball “직관 캘린더” → public baseball ticket-transfer posts organized by date, seat count, stadium zone, and risk signals for fans/families seeking adjacent seats.
3. Shopping-shorts operator tools → first directly operate a Korean shopping-shorts/Coupang Partners account, then turn the repeated sourcing/script/CTA/tracking pain points into internal tools and only later sell them as proven tools.

Do not assume any is correct. Validate against actual users and willingness to pay. If the user brings up baseball ticketing, switch fully into startup/product mode — do not treat it as content strategy. If the user brings up shopping-shorts tools, do **not** jump straight to SaaS: the user explicitly prefers building operating proof first.

For baseball-ticketing details, see `references/baseball-ticketing-saas-notes.md`. For the shopping-shorts tool direction, see `references/shopping-shorts-tool-validation.md`.

### Alternate explored wedge: baseball ticketing

If the user mentions baseball ticketing, presales, family seats, cancellation tickets, or transfer-ticket safety, use the notes in `references/baseball-ticketing-validation.md`.

Default framing:

> Family baseball fans who miss presales need a safer way to find 3-4 adjacent seats through cancellations or legitimate transfers.

Hard boundary: do not propose ticket-buying macros, automated queue/click bots, platform-rule bypasses, or scalping/premium-resale automation. Keep the wedge around safety checks, family-seat matching, legal public alerts, and manual concierge validation before software.

### Shopping-shorts tool caveat

If the user wants to build tools for shopping-shorts / Coupang Partners / hot-item short-form creators, do **not** jump straight to a generic script generator. The user explicitly corrected the sequence: first operate a real account and build proof/data; otherwise the tool is hard to sell. Recommend: run the account as a lab, track sourcing→production→views→clicks→revenue, build internal helpers around actual bottlenecks, then sell the verified system/tool. Product selection should be data-based from Douyin/TikTok/Taobao/Korean source-account evidence, not intuition.

### Operate-first proof before tool-selling

When the user wants to sell tools to people following a current online money-making trend, do not jump straight to SaaS. The user explicitly corrected that a tool is hard to sell without proof/results; first run the workflow directly, collect operating data, and build internal helpers around observed bottlenecks. Then position the product as “the system/tool I built while doing this myself,” not a generic AI tool.

For the shopping-shorts version of this pattern, see `references/operate-first-tool-validation-shopping-shorts.md`.

### MVP v0

Avoid accounts, payments, Notion OAuth, auto-posting, and complex dashboards at first.

Minimal flow:

1. Input: URL, transcript, or pasted article text.
2. Button: generate content package.
3. Output:
   - 조회수형 첫 줄/hook
   - 30초 Shorts script
   - Threads post
   - Instagram caption
   - image prompt or image direction
   - hashtags
4. Copy buttons.

### Concierge version

Before building full SaaS, offer a manual/AI-assisted service:

> 링크 하나 보내면 쇼츠 대본 + Threads + 인스타 캡션까지 10분 안에 만들어드립니다.

This can test demand faster than code.

## Validation assets to produce

When asked to help validate, generate:

1. One-line positioning.
2. Landing-page hero copy.
3. Waitlist CTA.
4. Three sample outputs from real sources.
5. Korean Threads validation post.
6. English X/Threads validation post.
7. A tiny ad test plan.

### Korean validation post template

```text
AI 뉴스 콘텐츠 만드는 사람들은 알 거임

뉴스 하나 찾는 것보다
그걸 쇼츠, Threads, 인스타용으로
각각 바꾸는 게 더 오래 걸림

그래서 뉴스 URL 하나 넣으면

- 쇼츠 훅
- 30초 대본
- Threads 글
- 인스타 캡션
- 이미지 프롬프트

까지 한 번에 뽑아주는 툴을 만들고 있음

이거 필요하면 댓글/DM 줘
먼저 써볼 수 있게 보내드림
```

### English validation post template

```text
I'm building a tool that turns one AI news link into a full content package:

- Shorts hook
- 30-sec video script
- Threads post
- Instagram caption
- image prompt
- hashtags

Finding AI news is easy.
Turning it into platform-specific content every day is the annoying part.

Would you use this if you create AI/tech content?
Comment "AI" and I'll send early access.
```

## Demand thresholds

Recommend building MVP only if one of these happens:

- 30+ waitlist emails from target users.
- 5+ DMs asking to try it.
- 3+ users send real links for sample conversion.
- 1+ person agrees to pay for a manual/concierge version.

Likes alone do not count as demand.

## gstack / office-hours pattern

If the user mentions `gstack`, Garry Tan, Claude Code office-hours, or asks whether an idea is worth building, apply the office-hours style:

- Specificity over broad market talk.
- Status quo is the competitor.
- Narrow wedge before platform vision.
- Interest is not demand.
- Watch users rather than demoing.

See `references/gstack-office-hours-notes.md` for the repo-specific notes captured from the session.

Also see `references/baseball-ticket-transfer-calendar.md` for a session-derived SaaS direction around a legal/safe baseball ticket-transfer calendar: families seeking 3–4 adjacent seats, Threads link submissions, risk-signal extraction, calendar UI, Telegram/iOS Shortcut mobile collection, and strict boundaries against ticket bots, queue bypassing, scalping, or reposting sensitive third-party content.

For the refined `직캘` / `직관캘린더` direction, see `references/baseball-ticket-calendar-ops-and-market.md`: naming/positioning rules, Kakao Open Chat intake, ended-post handling, duplicate submissions, contributor identity/rewards, seat-map visualization, fake screenshot risk checks, adjacent competitor/substitute scan, and the newer one-off `/check` URL analysis wedge where users paste a transfer-post URL to get seat-location/risk-signal guidance without automatically publishing it.

## Pitfalls

## Pitfalls

- Do not keep proposing Threads/Shorts content when the user has clarified they want to build a SaaS.
- Do not recommend building Notion OAuth, auto-publishing, dashboards, teams, or billing before validating demand.
- Do not treat “AI content creators” as a specific customer. Force a narrower user.
- Do not over-index on the user's own pain only. Their workflow is a good seed, but the product needs other paying users.
- For shopping-shorts tooling, do not propose selling the tool before operating proof exists. The user's preferred sequence is: operate account → collect performance/pain data → build internal tool → sell the proven system/tool.
- For shopping-shorts product sourcing, do not choose products by intuition. Use hot-item evidence from Douyin/TikTok/Taobao or Korean competitor accounts, then validate Coupang availability and purchase-intent comments.
- Do not call a prompt pack a SaaS unless there is a repeat workflow, saved state, integration, or distribution advantage.
- For baseball-ticketing ideas, never drift into ticket bots, official ticketing-site automation, queue bypassing, or premium resale. Keep the product framed as information organization, risk-signal checking, and original-link navigation.
- For user-generated/community collection ideas, force the operational questions early: already-ended items, duplicate submissions, contributor identity/rewards, reporting, and moderation. These are core product mechanics, not edge cases.

## Output shape

For early SaaS conversations, prefer this compact structure:

```text
결론: [one direct take]

1. 지금 만들면 안 되는 것
2. 먼저 검증할 고객/문제
3. 가장 작은 유료 버전
4. 오늘 할 검증 액션
5. 반응 있으면 만들 MVP
```
