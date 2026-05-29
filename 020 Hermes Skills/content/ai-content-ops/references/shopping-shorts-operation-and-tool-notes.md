# Shopping Shorts Operation + Tool Opportunity Notes

Session context: user analyzed 4 Korean/English-ish YouTube shopping-shorts/commerce content videos plus Korean source accounts, with the goal of first operating an account, then turning the workflow pain into a tool.

## Strategic thesis

Do **not** jump straight to selling a tool for shopping-shorts creators. The user correctly noted: without proof/results, selling a tool is weak. Sequence should be:

1. Operate a shopping-shorts account directly.
2. Use the operation as a lab to collect proof: views, comments, link clicks, affiliate revenue, failed products, time spent.
3. Build small internal tools for the workflow bottlenecks encountered while operating.
4. Only after some evidence, sell the system/tool as "what I actually used to run this."

Gold-rush framing: if many people are trying to earn from shopping shorts, a durable opportunity may be selling the picks/shovels — but only after the user has credible operational evidence.

## Durable user correction

Avoid suggesting products from intuition. Product selection must be evidence-based:

- Start from hot-item evidence on Douyin/TikTok/Taobao/Korean shopping-shorts accounts.
- Reverse-engineer already-performing products and hooks.
- Validate the product on Coupang or another target commerce source.
- Score candidates before making content.

Bad: "These products feel like good kitchen items: vegetable chopper, storage box..."
Good: "This product appears in multiple performing Shorts/Reels, has buyer-intent comments, exists on Coupang, and can be shown in 1 second."

## Source account analysis pattern

When the user sends Korean shopping-shorts accounts:

1. Save/source the accounts for future reference.
2. Pull latest/top Shorts metadata with `yt-dlp --flat-playlist` and per-video metadata when available.
3. Sort by view count, not upload recency alone.
4. Identify:
   - product category
   - title/hook formula
   - whether there is a human/hand/body/use-context in the frame
   - whether it is face-led, hand/use-led, or product-only
   - whether the product is suitable for a faceless account
   - whether it is for sourcing only or format replication
5. Prioritize accounts where product usage can be replicated without face reveal.

## Key insight: face reveal vs human-use context

The user refined the insight: it is not necessarily "real creator face reveal" that wins; recent shopping shorts often perform better when the video contains **human usage context**:

- hands using the product
- body/feet/waist wearing or testing it
- real kitchen/bathroom/laundry/closet context
- before/after transformation
- a lived-in scene that feels like a real user, not a pure product render

Implication for operation:

- Faceless is still possible.
- But avoid pure product-only slideshow/reused source footage when possible.
- Better workflow: hot-item sourcing → buy a few validated cheap items → shoot hands/usage at home → add AI script/captions/CTA.

## Product scoring rubric

Score candidates before production.

- Viral evidence (30): high views, repeated across accounts, buyer-intent comments like "where to buy/link/product name?"
- Coupang/commerce fit (25): exists or has close substitutes, fair price, reviews/sales signs, impulse-buy range.
- Visual clarity (20): function clear in 1 second, before/after, 15-second explanation possible.
- Target fit (15): 40–60 Korean household/living audience, clear household pain.
- Risk (10): low brand/IP/medical-claims risk, not too dependent on copyrighted source footage.
- Direct shooting feasibility (bonus/decision gate): can shoot hands/use-context at home, cheap enough to buy, one item can produce multiple angles.

Only produce high-scoring candidates; discard weak ones even if they "sound useful."

## Korean account examples saved during session

Initial YouTube source accounts:

- `UCOUGVptqq1C_iQ5HBFNQ-9w` — 홈캐치; strong in self-interior/repair/transformation: deck tiles, deco tiles, sink sheets, grout cleaning.
- `@homestory_official` — HomeStory; curiosity hooks: "일본 다이소에서 난리", "아는 사람만", "도마 절대 쓰지마세요".
- `UClGmMCacsvj7TZb0zeC6csA` — 살림메모; strong product ideas but user noted it is face/creator-trust led, so use mainly for sourcing/trend insight rather than direct format copying.
- `UClDVrsWD6ef9wuq-1BovYuw` — 홈잇; strong relationship/social-proof hooks and human-use context.

A local note was also created in the session at `/home/coka/shopping-shorts-research/source_accounts.md` and sample metadata JSON under `/home/coka/shopping-shorts-research/`.

## Hook patterns observed

Common high-performing Korean shopping-short title frames:

- "이걸 붙여보세요 / 깔아보세요 / 칠해보세요"
- "이걸 세탁기에 붙인다고?.."
- "아는 사람만 쓴다는 OOO"
- "다이소 가도 이런 건 없어요"
- "요즘 맘카페에서 난리 난"
- "요즘 일본/미국에서 대박 난"
- "시누이네서 이거보고 충격받았어요"
- "결벽증 언니가 추천한 청소꿀템"
- "이거 한번 써보면 일반 OOO 못 써요"

Avoid product-name-first titles unless the user explicitly asks for SEO style.

## Operational recommendation

For the user's lab phase:

1. Collect 20–30 candidates from Korean shopping-shorts accounts and/or Douyin/TikTok/Taobao hot items.
2. Validate Coupang availability and shooting feasibility.
3. Buy only 3–5 cheap, high-scoring products.
4. Produce multiple angles per product using hands/body/real context.
5. Track per-video metrics: product, hook, human-use context type, platform, views, comments, profile visits, link clicks, revenue, notes.
6. Use the resulting bottlenecks to decide internal tool features.

Likely internal tools after operation starts:

- hot-item validation board
- product-to-hooks/script/CTA generator
- sourcing keyword generator (Korean/Chinese/English)
- performance tracking sheet/dashboard

Do not start with auto-download, auto-upload, or heavy SaaS integrations; these add policy/complexity before proof.