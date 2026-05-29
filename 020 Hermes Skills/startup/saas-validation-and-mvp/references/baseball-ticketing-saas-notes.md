# Baseball ticketing / 직관 캘린더 SaaS notes

Use these notes when the user explores a baseball-ticketing SaaS, especially around KBO ticket transfer/cancellation pain. This is not a ticket-bot or resale-platform pattern; keep the product framed as safe information organization and risk checking.

## Product framing

Recommended framing:

> 직관캘린더: Threads/communities에 흩어진 야구 양도글을 날짜별로 정리하고, 좌석 위치와 위험 신호를 보여주는 가족/친구 직관러용 안전 캘린더.

Avoid framing as:

- Ticket buying bot.
- TicketLink/Interpark automation.
- Resale marketplace or 양도 거래방.
- Premium/암표 aggregator.

Use language like:

- “공개 양도글의 정보를 정리하고 위험 신호를 안내합니다.”
- “거래를 중개하지 않습니다.”
- “원문에서 양도 완료 여부를 반드시 확인하세요.”

## First customer / wedge

Most promising initial segment from the session:

- Families or small groups looking for 3–4 adjacent seats after presales/priority sales have already taken good seats.
- They search Threads/communities for transfer posts, but need to know date, team/stadium, seat count, adjacent-seat likelihood, price/face-value status, and scam/risk signals.

MVP should likely start narrower than all KBO:

- One stadium first, likely Jamsil if sample volume supports it.
- One or two teams/venues if data suggests concentration.
- Operator-curated data before full user-generated/community automation.

## Safe boundaries

Do not suggest or build:

- Auto-refreshing official ticketing sites.
- Automatic seat selection/reservation.
- Queue bypasses.
- TicketLink/Interpark scraping or automation.
- Cancellation-ticket bots.
- Premium/above-face-value resale facilitation.

Safer scope:

- User/operator-submitted public post links.
- Minimal metadata extraction.
- Risk-signal summaries.
- Original-source links only.
- Status updates and reports.
- Seat-location visualization using original simplified SVG maps, not copied official seating charts.

## Data model fields to consider

For `transfer_posts`:

- source_platform
- source_url
- source_post_id / canonical URL
- post_type: 양도 / 구함 / 양도+구함 / 불명확
- raw_text_redacted, not full unredacted body
- summary
- game_date
- stadium_id
- home_team / away_team
- seat_count
- is_consecutive_seats
- section_raw
- zone_id
- delivery_method
- price_text
- price_status: 명시 / 미기재 / 정가언급 / 웃돈의심
- risk_level: 낮음 / 확인필요 / 높음
- risk_reasons
- check_questions
- status: unknown / active_unverified / ended / expired / reported / hidden
- report_count, ended_report_count

For `submissions`:

- transfer_post_id
- submitter identifier if available
- submitted_via: kakao_openchat / kakao_channel / telegram / web / pwa / shortcut
- submitted_at

For `stadium_zones`:

- stadium_id
- zone_id
- zone_name
- aliases, e.g. “중스상 12”, “3스상 25구역”
- svg_path_id
- side: 1루 / 3루 / 중앙 / 외야
- level
- family_score, view_score, cheering_score
- notes

## Collection strategy

Use staged collection:

1. Operator-curated MVP:
   - User/operator finds Threads posts manually.
   - Sends links to an operator tool, Telegram bot, iOS Shortcut, or admin form.
   - AI extracts metadata.
   - Admin reviews/edits/approves.
   - Public calendar shows summaries + original links.

2. Kakao OpenChat validation:
   - Good for Korean users and early community validation.
   - Position as “양도글 제보/위험체크방,” not a 거래방.
   - Operator watches the room and processes links manually/semiautomatically.
   - Use room rules: no direct trading, no 계좌/전화번호/예매번호/QR, no premium/정가 이상 유도, original links only.

3. User-submitted links:
   - Web submission with Kakao login or lightweight identity.
   - Later Kakao Channel/chatbot if product shows demand.
   - PWA/native share-sheet later; web paste is fallback only.

Avoid making Telegram the main user-facing channel for Korean consumers. It can be useful for the operator or power users, but user perception may be negative.

## Status/ending problem

A major problem: posts may already be transferred even if the game date is still in the future. Treat every post as unverified unless recently confirmed.

Recommended mechanics:

- Display status as “확인 필요” or “모집중 추정,” never “거래 가능” by default.
- Add buttons: “양도 종료됨,” “정보가 틀려요,” “위험해 보여요.”
- Use ended-report counts to mark “종료 제보 있음” or auto-hide after threshold/admin review.
- Auto-expire after game start.
- Optionally re-fetch public metadata for “완료/마감/양도완료/구했습니다” keywords, but don’t rely on it.

## Duplicate submissions

Normalize Threads URLs by removing tracking query params and extracting `/post/<id>` as canonical `source_post_id`.

If multiple people submit the same post:

- Store one `transfer_posts` row.
- Store multiple `submissions` rows.
- Use duplicate submissions as signals: popularity, confidence, or faster ending/risk reports.

## Contributor incentives and identity

If contributions should earn rewards, the system needs identity. Anonymous Kakao/Telegram shares won’t map cleanly to a logged-in web account.

Options by stage:

- v0: no rewards; operator-only collection.
- v1: Kakao login + web submission + “내 제보함.”
- v2: Kakao Channel/chatbot identity if feasible.
- v3: PWA/native app share target with login state.
- Lightweight fallback: nickname/code, but weak and easy to abuse.

Possible incentives:

- Approved submissions count.
- Weekly/team-specific 제보왕.
- Priority alerts for interest games.
- “This helped N people” feedback.

## Seat map feature

A strong differentiator is turning cryptic section text into visual location:

- Extract section aliases from posts.
- Map to normalized stadium zones.
- Highlight zones on original simplified SVG stadium maps.
- Do not copy official seating chart images.
- Start with one stadium.

Show family-relevant context:

- family_score / “가족 적합도”
- view_score
- cheering/noise intensity
- possible shade/stairs/restroom notes if known

## Screenshot / AI-generated fake ticket risk check

Users reported scams where sellers use ChatGPT/AI or editing tools to create fake booking-history screenshots. Do not claim perfect fake detection.

Safe product language:

- “예매내역 캡처의 위험 신호를 체크합니다.”
- “캡처만으로는 진위 확인이 어렵습니다.”
- “공식 앱에서 새로고침하는 짧은 화면 녹화를 요청해보세요.”

Possible checks:

- OCR text extraction.
- Game date / stadium / teams cross-check with official schedule data.
- Presence of expected booking fields: event, date/time, venue, seat section, count, price, booking time, ticket status.
- Suspicious missing or inconsistent fields.
- Seller behavior flags: refuses live app verification, insists on 선입금, avoids face-value questions, asks for account info, etc.

Never say:

- “사기입니다.”
- “AI 생성 이미지입니다.”
- “100% 안전합니다.”

Say:

- “공식 예매내역으로 확인하기 어려운 항목이 있습니다.”
- “추가 확인이 필요합니다.”

## Recommended MVP sequence

1. Collect 30–50 Threads/community sample links.
2. Test metadata extraction from public pages, especially `og:description`, but assume coverage may vary.
3. Build operator/admin ingestion and AI extraction.
4. Add calendar UI + original links + risk summary.
5. Add status/report buttons for ended/wrong/risky posts.
6. Add one-stadium seat SVG mapping.
7. Validate via Kakao OpenChat or small audience.
8. Add user submissions and identity only after the utility is proven.

Demand signals to watch:

- People submit links without being asked repeatedly.
- People ask for specific game/team alerts.
- People report ended/risky posts.
- People share the calendar page with other fans.
- Repeat visits around popular game dates.
