# Absorbed skill: shopping-shorts-ops

This file preserves the class workflow from the former `shopping-shorts-ops` sibling, consolidated into the broader `ai-content-ops` umbrella. Use when the user is researching, operating, validating, or tooling Korean shopping-shorts / Coupang Partners / Inpock / 생활꿀템 workflows.

## Core principle

Do **not** pick products by intuition. Product selection must be evidence-based:

1. Find already-performing source videos/products from Korean Shorts/Reels/TikTok, Douyin, Xiaohongshu, Taobao/1688/AliExpress, or competitor Inpock pages.
2. Identify the product **or functional group** and the exact usage/benefit being demonstrated.
3. Verify there is a Coupang/Naver/In-pock-mappable product or product set.
4. Score candidates before scripting or producing videos.
5. Track results so the future tool is backed by real operating data.

## Product sourcing workflow

### 1. Start from evidence, not ideas

Good sources:

- Korean YouTube Shorts shopping/lifehack accounts
- TikTok/Reels product/lifehack accounts
- Douyin and Xiaohongshu recent hot videos
- Taobao/1688/AliExpress product pages with usage videos
- Competitor Inpock pages, especially numbered product lists

For Korean competitor analysis, separate:

- **View/Hook data:** video title, first 1–3 seconds, views/comments, whether it is face/hand/product-only, what curiosity gap is used.
- **Sales data:** Inpock/link-in-bio product names, numbering system, product bundles/sets, Coupang vs Naver links.

### 2. Prefer usage/function over raw product names

The user corrected that finding “the same product 5 times” is too hard and often unnecessary. Treat source collection as:

- **Same exact product** when possible.
- Otherwise **same functional group / same usage promise** is acceptable.

Examples:

- `냉각판 핸디선풍기` rather than one exact fan model.
- `압축봉 수납 활용법` rather than one exact 압축봉 SKU.
- `단방향 창문 필름` rather than one exact film brand.

Only require strict matching for core advertised functions. If the source shows a 냉각판, 판매 링크 제품 also needs a 냉각판. If source shows 클립형, linked product must also be clip-type. Avoid claiming model-specific specs unless verified.

### 3. Look for “usage scenes,” not just product photos

Strong source videos usually show at least one of:

- Hand/body/installation/착용/use scene
- Problem → solution
- Before/after visual change
- An unexpected alternative use
- Real home context: kitchen, bath, laundry, storage, window, car, bag, desk

A face is not required. Product-only can work if the **idea/hack** is strong enough, but plain catalog/product-spin videos are weak.

### 4. Score candidates before production

Use a 100-point score. Make only 70+ candidates; prioritize 80+.

- **Reaction evidence — 30**
  - Recency: within 7 days best; 2 weeks acceptable; old viral videos are weaker.
  - Likes/comments: especially purchase intent (`링크?`, `어디서 사요?`, `제품명?`).
  - Repeat evidence: same product/function appears across multiple videos/sources.
- **Source-video fit — 20**
  - Usage scene, problem/solution, before/after, 15-second explainability.
- **Coupang/link fit — 20**
  - Same/similar product exists, 5,000–30,000 KRW ideal, reviews/sellers exist, bundleable products get extra value.
- **Korean target fit — 15**
  - Korean homes/lifestyle, 30–60 female/salim/self-care/family/camping/car relevance, seasonal timing.
- **Risk — 15**
  - Low IP/brand dependence, low medical/health claims, can be transformed and mixed from multiple sources.

Reject or defer products that require long explanation, have no clear Korean purchase path, rely on famous brands/IP, or make health/medical claims.

## Inpock/link-bio mining

Competitor Inpock pages are product databases. When available, parse them to discover what the creator actually sells.

Look for:

- Numbered items like `[119] 후크 스테인리스 집게`.
- Bundles under one video number, e.g. 압축봉 + 선반 + 고정걸이.
- Repeated categories: 압축봉, 메쉬망, S자 고리, 전선 몰딩, 단방향 필름, 두꺼비집 가리개, 클리너, 수납장.

Recommended model:

- Video sells a **usage idea**.
- Inpock sells the **product set** needed to reproduce it.
- CTA uses a number: `프로필 링크 117번에 모아뒀어요`.

This is often stronger than one-product hard selling.

## Content positioning patterns

Prefer `활용법/꿀팁/재발견` framing over plain `추천/구매` framing.

Strong title/hook formulas:

- `다이소 기획자도 감탄한 미친 활용법`
- `제조사도 예상 못한 뜻밖의 사용법`
- `이케아 직원도 당황한 천재의 활용법`
- `집에 이런 포인트 어때요?`
- `창문에 이거 붙이기만 하면`
- `시누이네서 이거보고 진짜 충격받았어요`
- `결벽증 언니가 추천한 청소꿀템`
- `요즘 맘카페에서 난리 난 올여름 필수템`

Avoid starting with product names unless the product name itself has search demand.

## Operational sequence

1. Collect 5–20 source candidates.
2. Score and shortlist 1–3 product/function groups.
3. For each selected group, gather 3–10 usage clips or references. Same function group is OK when exact model matching is too hard.
4. Verify Coupang/Naver products and note exact functions to avoid mismatch.
5. Build Inpock numbering/bundle.
6. Write 3–5 Korean hooks/scripts/CTAs per product/function group.
7. Publish across chosen platforms.
8. Track views, comments, profile visits, link clicks, and sales.
9. Turn repeated operational pain points into internal tools only after real operation reveals them.

## Tool/MVP implications

Do not pitch an external tool before the user has operational proof. First build internal helpers for:

- Source video/product/function scoring
- Product/function matching against Coupang keywords
- Chinese/English/Korean search keyword generation
- Inpock item naming and bundle planning
- Hook/script/CTA generation
- Result tracking

External product positioning should eventually be: `I used this while operating my own shopping-shorts workflow`, not generic AI automation.
