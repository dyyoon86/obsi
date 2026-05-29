# Baseball ticket transfer calendar concept

Session-derived notes for validating a non-content SaaS idea around Korean baseball ticketing.

## Problem framing

User explored a legal/safe "직관 캘린더" concept:

- Baseball is hot, but ticketing is hard because presales/early presales exhaust good seats.
- The acute user is not just any fan. The narrowest first customer is families seeking 3–4 adjacent seats.
- Current workaround: manually searching Threads/communities for transfer posts, cancellations, and safe 양도 options.
- Pain is strongest where the user needs adjacent seats, has kids/family constraints, and fears scams or inflated prices.

## Hard boundary

Do **not** design anything that:

- Automates Ticketlink/Interpark/KBO ticket acquisition.
- Auto-clicks, auto-refreshes, bypasses queues, or selects seats.
- Encourages scalping/price premiums or direct ticket brokering.
- Reposts full third-party post bodies, contact details, account numbers, ticket numbers, or screenshots.

Position the product as an information organization and safety-check tool, not a ticket procurement service.

## Safer product shape

A safer framing:

> Threads에 흩어진 야구 양도글을 날짜별 캘린더로 정리하고, 가족 연석 여부와 위험 신호를 체크해주는 서비스.

Store/display minimal metadata:

- Source URL
- Collection time
- Inferred game date
- Stadium / teams if inferable
- Seat count
- Adjacent-seat signal
- Price signal, not necessarily exact price
- Risk level: low / medium / high / needs-check
- Redacted one-line summary
- Public source link

Avoid displaying:

- Full post text
- Phone numbers
- Kakao IDs/open chat details if sensitive
- Bank/account details
- Full seat/ticket numbers
- Profile images or unnecessary author metadata

## MVP path

1. Manual operator collection first.
   - User manually finds Threads transfer posts and sends links into the system.
   - Goal is to see whether a calendar page is useful before automating collection.
2. User/operator submission.
   - Provide "양도글 제보하기" with link submission.
   - Prefer admin review before public display.
3. AI extraction.
   - Extract date, teams/stadium, seat count, adjacent-seat likelihood, price signal, and risk signals.
   - Phrase risk as "확인 필요" or "위험 신호 있음", not definitive fraud accusations.
4. Calendar UI.
   - Date-first interface, with filters for team, stadium, 2/3/4 seats, risk level, and adjacent-seat candidates.
5. Only later consider approved automation.
   - Prefer official APIs, user-submitted links, browser extension/share flows, or permitted social listening over scraping.

## Mobile collection insight

For early data collection, browser paste UX is too high-friction:

Bad early UX:

> Threads → copy link → open browser → open service page → paste → submit

Better operator/user collection options:

- Threads share → Telegram bot → DB → AI analysis → admin review.
- iOS share sheet shortcut → POST to `/api/submit` → saved.
- PWA Web Share Target later, but do not rely on it first because install/support varies.
- Web paste remains a fallback, not the primary mobile collection workflow.

## Technical sketch

Suggested stack:

- Next.js frontend and API routes
- Supabase DB
- Telegram bot webhook for operator submissions
- OpenAI/Claude extraction step
- Admin review page
- Public calendar page

Core pipeline:

```text
Threads post
→ share to Telegram bot / shortcut / submit page
→ source URL saved
→ text/link analyzed and redacted
→ parsed fields stored
→ admin approval
→ public calendar listing with source link only
```

Example DB fields:

```text
id
source_platform
source_url
source_author_hash
raw_text_redacted
summary
game_date
stadium
home_team
away_team
seat_count
is_consecutive_seats
price_signal
risk_level
risk_reasons
check_questions
status: collected/analyzed/approved/rejected/expired
created_at
updated_at
```

## Participation and monetization

Participation mechanisms:

- "양도글 제보하기" button everywhere.
- Reward useful submissions with priority alerts, badges, or free interest-game alerts.
- Show impact: "이 경기 찾는 사람 N명에게 도움이 될 수 있어요."
- Team/fandom leaderboards can encourage participation.

Ad/monetization fit:

- Ads/affiliate links fit because users have strong 직관 intent.
- Good ad surfaces: date pages, stadium pages, team pages, family 직관 guide pages.
- Relevant ads: stadium parking, nearby restaurants, accommodation, merch, kid supplies, cheering goods.
- Premium alerts may monetize better later: interest-game alerts, 3–4 adjacent-seat candidates, low-risk candidates.

## Validation signals

Do not count likes alone. Look for:

- People submitting transfer links.
- People asking for specific team/date alerts.
- Families saying they need 3–4 seats.
- Repeat visits during ticketing periods.
- Users sharing the calendar with fan groups.
- Someone willing to pay for alerts or a concierge check.
