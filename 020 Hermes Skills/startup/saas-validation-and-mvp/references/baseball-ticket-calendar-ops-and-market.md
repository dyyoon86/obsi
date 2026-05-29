# Baseball 직관 calendar: operations, naming, and competitor notes

Session-specific detail for the user's `직캘` / `직관캘린더` SaaS exploration. Use with the umbrella SaaS validation skill when the user discusses baseball tickets, public transfer posts, or 직관 planning.

## Naming and positioning

Preferred project name:

- Short service name: `직캘`
- Full name: `직관캘린더`
- Category: `야구 직관 준비 캘린더`

Safe one-line definition:

> 공식 예매 정보, 좌석 위치, 공개 양도글의 확인 필요 항목을 날짜별로 정리해주는 야구 직관 준비 서비스.

Avoid language that frames the product as a broker or resale venue:

- `티켓양도 페이지`
- `양도표 모음`
- `티켓 거래소`
- `표 구해주는 앱`
- `취소표 자동 알림` if it implies ticketing-site automation

Use safer labels:

- `공개 양도글 체크`
- `양도글 위험 신호 확인`
- `좌석 위치 보기`
- `공식 예매 정보`
- `직관 준비 캘린더`

## Product scope refined in session

The product should not be only a transfer-post page. It should look like a broader 직관-prep information product:

- Official team/ticketing-site links and presale/general-sale notes.
- Stadium/seat guide pages.
- Date-first calendar for public transfer-post metadata.
- Original-source links only; no full reposting of sensitive content.
- Seat-zone visualization using self-made simplified SVG maps, not copied official seat maps.
- Risk-signal checks for posts and ticket-proof screenshots.
- User reports for ended items, duplicates, incorrect info, and risky posts.

## Important operational mechanics

### Already-ended posts

Problem: a post can remain on the calendar before game day even after the transfer is over.

MVP handling:

- Default status should be `확인 필요`, not `거래 가능`.
- Add card actions: `양도 종료됨`, `정보가 틀려요`, `위험해 보여요`.
- Track `ended_report_count`; after threshold, show `종료 제보 있음` or hide pending admin review.
- Auto-expire after game start, but do not rely on this for pre-game completion.
- If feasible, periodically re-fetch the source and detect terms like `양도완료`, `완료`, `마감`, `거래완료`, `구했습니다`.

### Duplicate submissions

Same Threads post can be shared by multiple people.

- Normalize source URLs by removing tracking query parameters and converting threads.net/com variants.
- Extract/store `source_post_id` from `/post/<id>` when possible.
- Make `(source_platform, source_post_id)` unique.
- Keep one public `transfer_post` record; append each contributor to `submissions`.
- Treat duplicate count as a signal: interest/popularity or consensus that an item is ended/risky.

### Contributor identity and rewards

If submissions happen through Kakao/Telegram/share flows outside the logged-in web app, rewards require identity design.

Options:

- Operator-only collection first: no rewards.
- Kakao login + web submission: simple reward tracking.
- Kakao Channel/chatbot: likely best later for Korean users because it can identify sender and send alerts, but implementation/policy is heavier.
- Telegram bot: easy identity technically, but poor mainstream Korean perception; suitable for operator or power users, not main consumer UX.
- PWA/native share: best long-term UX but requires install/app and login.
- Lightweight `제보 코드` can work for early tests but is weak and clunky.

Suggested sequence:

1. v0: operator-curated, no rewards.
2. v1: Kakao login + web submission + `내 제보함`.
3. v2: Kakao Channel/chatbot for link submissions and contributor tracking.

## Kakao Open Chat as MVP intake

The user proposed watching a Kakao Open Chat room and manually processing submissions. This is acceptable for early validation.

Recommended framing:

- Room is a `제보방/위험체크방`, not a `거래방`.
- Users submit public source links, ended reports, risk reports, or date/team requests.
- The operator copies links into the admin page; AI extracts metadata; admin approves before public display.

Open Chat rules should say:

```text
이 방은 야구 티켓 거래방이 아닙니다.
공개 양도글을 제보하고 날짜·좌석수·위험 신호를 정리하기 위한 방입니다.
계좌번호/전화번호/예매번호/QR 공유 금지.
정가 이상 거래 유도 금지.
직접 거래 금지.
원문 링크만 제보해주세요.
```

Do not propose scraping Kakao Open Chat automatically as the default. Use manual monitoring first; later evaluate official Kakao Channel/chatbot routes.

## Seat-location visualization

High-value differentiator: parse raw seat-zone text and show approximate location on a stadium graphic.

- Use simplified, self-made SVG stadium maps.
- Do not copy official seat-map images.
- Start with one stadium, likely Jamsil or whichever appears most in collected posts.
- Maintain `stadium_zones` with aliases, SVG path IDs, side/level, and qualitative notes.

Example fields:

```text
stadium_id
zone_id
zone_name
aliases
svg_path_id
side: 1루/3루/중앙/외야
level: 하단/상단/테이블/외야
family_score
view_score
cheering_score
notes
```

## Fake ticket-proof screenshot risk checks

User reported scams where sellers use ChatGPT/AI to create fake booking-history screenshots.

Position as risk-signal checking, not definitive authenticity detection.

Possible checks:

- OCR the screenshot.
- Extract game date, teams, stadium, seat section/count, price, booking time/number presence.
- Compare date/team/stadium against KBO schedule when available.
- Check for missing or inconsistent fields.
- Generate safe verification questions.

Recommended output language:

- `공식 예매내역으로 확인하기 어려운 항목이 있습니다.`
- `캡처만으로는 진위 확인이 어렵습니다.`
- `예매처 앱에서 티켓 화면을 열고 새로고침/뒤로가기 후 재진입하는 짧은 화면 녹화를 요청해보세요. 개인정보/QR/예매번호는 가려도 됩니다.`

Avoid:

- `사기입니다`
- `AI 생성 이미지입니다`
- `가짜 예매내역입니다`

## Competitor and substitute scan

Search did not reveal an exact direct competitor combining KBO-specific official ticketing info, public transfer-post calendar, seat map visualization, and risk-signal checks.

Adjacent substitutes:

- Ticketbay: ticket resale/transfer marketplace. Competes for transfer demand, but `직캘` should avoid marketplace positioning.
- Ticketlink / Interpark / NOL Ticket: official ticketing sources. `직캘` should link to and explain them, not compete with or automate them.
- TheCheat: financial scam prevention/account lookup. Complementary; include in safety checklist rather than compete directly.
- Kakao Open Chat / Threads / X / fan cafes: the real status quo is manual searching and community monitoring.
- SeatGeek / StubHub / Gametime abroad: large resale marketplaces with seat maps; useful as inspiration for map UX but different from the safe-info-checking wedge.

Validation should focus on current user routines:

- Where do fans search after missing presales?
- Are 3–4 adjacent seats actually common enough in posts?
- Do fans understand raw seat-zone abbreviations?
- Do ended posts cause wasted effort?
- Are users worried about fake screenshots or seller proof?
- Would they submit links or ask for alerts?

## Suggested MVP phases

### v0: URL-check utility + operator-curated proof of usefulness

Include a public one-off URL check flow as an early wedge, not only a browsable calendar:

- Homepage should have a quick input: user pastes a public transfer Threads/X/community URL and clicks `확인하기`.
- `/check` analyzes the URL or pasted text and returns a one-time result: estimated game/date, teams/stadium, seat count, seat-zone text, approximate SVG seat location, price expression, ended/completed keywords, risk signals, and safe verification questions.
- `/check` results should **not** automatically become public calendar items or `transfer_posts`; only save minimal anonymous logs if needed. If the user clicks `이 링크 제보하기`, then create a pending submission for admin review.
- This flow is useful for immediate consumer value and validation even before the calendar has enough curated inventory.

Then build the operator-curated calendar:

- Collect 30–100 public links manually from Threads/Kakao/community sources.
- Extract metadata using AI.
- Admin approve/edit.
- Publish calendar with source links, status, risk checks, and one stadium SVG.
- Add ended/risky/incorrect report buttons.

### v1: lightweight participation

- Kakao Open Chat 제보방 for links and ended/risk reports.
- Web fallback submission.
- Optional Kakao login and `내 제보함` if rewards matter.

### v2: mainstream Korean UX

- Kakao Channel/chatbot for submissions and alerts.
- Contributor identity and rewards.
- Interest-game alerts.
- More stadium maps and official ticketing info pages.
