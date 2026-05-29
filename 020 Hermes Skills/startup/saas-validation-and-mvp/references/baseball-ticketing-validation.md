# Baseball ticketing SaaS validation notes

Session context: user shifted from AI-content SaaS ideas to a possible baseball-ticketing product after observing that baseball is hot and ticketing is hard.

## Problem framing

Strongest current framing:

> Family baseball fans who miss team/member presales struggle to safely find 3-4 adjacent seats through cancellations or legitimate transfers.

This is better than a generic "baseball ticket app" because the wedge is specific:

- Presale / early-presale access can remove good seats before general sale.
- Single tickets are easier; 3-4 adjacent seats for family outings are much harder.
- Families care about sitting together, price ceilings, child safety, schedule certainty, and scam risk.
- Current workaround likely involves repeated refreshes, X/Twitter search, fan cafes, open chat rooms, resale posts, DMs, and manual scam checking.

## Hard boundaries

Do not propose or build:

- Ticket-buying macros or automated click bots.
- Systems that bypass ticketing-platform rules or queues.
- Scalping / premium resale automation.
- Dark-pattern resale marketplaces.

Keep the product in the safer space:

- Cancellation/transfer discovery assistance.
- Safety/scam-risk checking.
- Price and seat-condition sanity checks.
- Family adjacent-seat request organization.
- Notifications that respect platform rules and data access limits.

## Candidate wedges

Best first wedge candidates:

1. **Transfer-post safety checker**
   - User uploads a screenshot/link/text of a ticket transfer post.
   - Output: scam-risk score, price sanity check, red flags, questions to ask, safe transaction checklist.
   - Lower legal/platform risk than direct ticket brokerage.

2. **Family adjacent-seat finder waitlist / concierge**
   - User submits: team, date, 3-4 seats, section preference, budget, must-sit-together flag.
   - Initially manual: monitor legal public sources and notify when plausible matches appear.
   - Tests willingness to pay before building automation.

3. **Cancellation/transfer alert room for family fans**
   - Kakao open chat / Telegram / email alerts first.
   - Paid monthly if users repeatedly need weekend/popular games.

Avoid starting with a full marketplace. It introduces trust, dispute, payment, fraud, moderation, and legal responsibility before demand is proven.

## Validation copy seed

Korean validation post:

```text
요즘 야구 티켓팅 진짜 빡센데
특히 가족 단위로 3~4연석 구하는 건 거의 미션 수준인 듯

선예매/선선예매에서 좋은 자리는 거의 빠지고
일반 예매 들어가면 연석은 이미 없고

결국 취소표나 양도표 찾아보게 되는데
문제는 이게 또 너무 불안함

정가인지
사기 아닌지
진짜 양도 가능한 표인지
아이랑 같이 앉을 수 있는 자리인지

확인할 게 너무 많음

그래서 가족 단위 야구 직관러를 위한
“취소표/양도표 안전 체크 + 연석 알림” 같은 걸 만들어볼까 하는데

이런 거 있으면 쓸 사람 있음?
특히 3~4연석 구해본 사람들 의견 궁금함
```

## Demand tests

Build only after at least one strong signal:

- 10+ target users describe the same family-seat pain in comments/DMs.
- 5+ users send real ticket-transfer screenshots asking for safety checks.
- 3+ users submit real upcoming games and seat constraints.
- 1+ user agrees to pay for a concierge search/check service.

Likes alone do not count.

## Office-hours questions for next session

Ask one at a time:

1. Which team/stadium has the worst first wedge and why?
2. Where exactly do family fans currently search for transfer/cancellation tickets?
3. What scam or bad-transaction stories have they experienced or heard?
4. How much would a family pay to avoid wasting hours or getting scammed?
5. Can the first version be a manual Kakao/Telegram concierge rather than software?
