# Shopping Shorts Competitor/Sourcing Notes

Session-derived notes for analyzing Korean shopping-shorts/life-hack accounts and translating findings into an operating experiment or future tool.

## User correction: do not pick products by intuition

For shopping-shorts experiments, product selection must be evidence-based. Do not suggest products just because they seem plausible. The workflow should start from videos/products that already show traction, then reverse-engineer.

Preferred sequence:

1. Collect high-performing Korean shopping/life-hack Shorts accounts and videos.
2. Sort by view count and engagement, not recency alone.
3. Identify whether the video is face-led, hand/use-scene led, or faceless life-hack led.
4. Extract the product or usage idea.
5. Generate Korean/English/Chinese search terms for the same or similar product.
6. Check whether the product exists on Coupang or a Korean buyer-accessible marketplace.
7. Score for: viral evidence, visual clarity, Korean household relevance, conversion likelihood, sourcing feasibility, and IP/policy risk.
8. Only then write hooks/scripts/CTA.

## Important distinction: face vs human-use scene

The user observed that many successful shopping shorts are not necessarily creator-face videos. What matters is often the source video containing a believable use scene:

- hands installing/holding/using the item
- body/foot/waist/closet/kitchen context
- before/after transformation
- problem-to-solution sequence
- real household context rather than product-only white-background shots

Do not conclude “face reveal is required.” Better framing:

> Face is optional; visible usage context is often the signal.

## But faceless can still work: utilization-hack accounts

A Korean account like `@bgs_pick1` / 방구석꿀템 showed high views without people/face when the content is framed as a surprising life-hack or unexpected use case rather than an ad.

Observed title patterns:

- 다이소 기획자도 감탄한 미친 활용법
- 다이소 개발진도 당황한 미친 활용법
- 이케아 직원도 당황한 천재의 활용법
- 제조사도 예상 못한 미친 사용법
- 이케아 개발자도 예상 못한 구멍의 정체
- 살림 생태계 파괴 중인 미친 아이템

Takeaway:

> For faceless shopping shorts, sell the “unexpected use / utilization hack,” not the product.

This makes the content feel like a useful discovery instead of a direct product ad.

## Accounts saved during the session

Initial Korean YouTube source accounts:

- `UCOUGVptqq1C_iQ5HBFNQ-9w` — 홈캐치
- `@homestory_official` — HomeStory
- `UClGmMCacsvj7TZb0zeC6csA` — 살림메모 (face/personality-led; use mostly for product/source ideas, not direct format copying)
- `UClDVrsWD6ef9wuq-1BovYuw` — 홈잇
- `@bgs_pick1` — 방구석꿀템 (faceless utilization-hack style)

## Patterns found

### Product-name hiding

Successful titles often hide the product name and create curiosity:

- 이걸 붙여보세요
- 이걸 깔아보세요
- 창문에 이거 붙이기만 하면
- 다이소 가도 이런 건 없어요
- 이 구멍의 정체

### Social-proof/authority framing

- 다이소 기획자도 감탄한
- 이케아 직원도 당황한
- 요즘 맘카페에서 난리 난
- 일본 다이소에서 난리 난
- 친구/시누이/언니/엄마/남편이 알려준

### Strong product classes

- cleaning / dust / water stains / grease
- storage / wasted-space utilization
- self-interior / peel, stick, install, cover
- laundry and detergent organization
- kitchen organization and dishwashing accessories
- seasonal summer/rain/privacy/heat-blocking items

### Good video-source criteria

Prioritize source videos with:

- clear first-second visual payoff
- use scene, installation, or transformation
- problem and resolution visible without long explanation
- low brand dependency
- Korean household relevance
- likely Coupang equivalent
- low medical/health-claim risk

Avoid starting with:

- pure product spins or catalog slides
- heavily branded products
- medical/health efficacy claims
- expensive products with weak impulse-purchase fit
- clips where the whole value depends on a creator’s face/personality

## Example reverse-engineered videos from 홈잇

- `rQsoT1Elgck`: worry stone / fidget stone keychain. Strong story hook but health/anxiety claims require caution.
- `580kXWXO-ZI`: flower wall/tile decoration. Massive views; strong transformation, but harder to source/shoot.
- `2Nt2WFPiHM8`: reflective/privacy/heat-insulation window film. Strong seasonal/privacy hook.
- `K_Wv6FEZHCA`: under-shelf storage rack. Lower views but highly practical, easy to source, and easy to shoot.

## Output format when user sends source videos/accounts

For each candidate video, return:

```text
제품명 추정:
영상 유형: 얼굴/손사용/무인활용법/제품전시
핵심 장면:
문제 상황:
해결 장면:
쿠팡 검색어:
영어 검색어:
중국어 검색어:
한국식 훅 후보:
15초 재구성 가능성:
우선순위: 상/중/하
주의점:
```
