# Shopping Shorts Competitor and Hot-Item Analysis Workflow

Use this when the user provides YouTube/TikTok/Instagram/Douyin shopping-shorts accounts or videos and wants to find products to operate an account or build tools around.

## Core rule

Do not pick products by intuition. The user specifically corrected this. Product candidates must be evidence-led:

- high-view competitor videos,
- repeated products across accounts,
- purchase-intent comments,
- hot-item signals from Douyin/TikTok/Taobao,
- and Coupang availability / similar-product availability.

If suggesting products without this evidence, label them as unvalidated hypotheses.

## YouTube account analysis steps

1. Use `yt-dlp --flat-playlist --dump-json --playlist-end N <channel>` to list recent Shorts/videos.
2. For promising videos, fetch metadata with `yt-dlp --dump-json --skip-download <video_url>`.
3. Sort by `view_count` when available.
4. Extract:
   - title/hook pattern,
   - visible/likely product,
   - category,
   - proof metric (views/comments/likes if available),
   - URL,
   - whether it fits the user's target niche.
5. Prioritize videos with strong views relative to that account’s baseline.
6. If captions are needed, download Korean auto-captions with yt-dlp and parse as in existing YouTube analysis workflow.

## Initial Korean source accounts from session

- 홈캐치 — `UCOUGVptqq1C_iQ5HBFNQ-9w`
  - Strong themes: self-interior, repair, 붙이는/깔아보는/칠해보는 products, deck tiles, deco tiles, 시트지, grout/줄눈, silicon/bangchung repair.
- HomeStory — `@homestory_official`
  - Strong hooks: 일본 다이소, 아는 사람만, 뽕뽑는, 절대 쓰지마세요, 미리 준비해야 하는 이유.
- 살림메모 — `UClGmMCacsvj7TZb0zeC6csA`
  - Strong high-view household/idea items. Important initial videos included “이걸 세탁기에 붙인다고?..” (~3.7M views) and “한 끗이 다른 아이디어템” (~1.4M views).
- 홈잇 — `UClDVrsWD6ef9wuq-1BovYuw`
  - Strong hooks: 시누이네서 보고, 결벽증 언니, 엄마한테 혼날 뻔, 남편이 알고 있어서 충격, 다이소에도 없는, 미국에서 대박.

## Observed reusable hook patterns

- Hide product name; lead with curiosity/problem.
- Frequent phrases: “이걸…”, “이거…”, “붙여보세요”, “깔아보세요”, “세탁기에 붙인다고?”, “아는 사람만”, “다이소에도 없는”, “일본/미국에서 대박”.
- Relationship/social proof hooks fit Korean household audiences: 시누이, 언니, 엄마, 남편.
- Problem → tool → visible result is stronger than generic product recommendation.

## Product scoring rubric

Use before recommending production:

- Viral evidence: 30
  - High-view source, repeated product, purchase-intent comments.
- Coupang conversion potential: 25
  - Similar product exists, price is impulse-friendly, reviews/sales proof, low friction.
- Video demonstration strength: 20
  - Feature visible in 1 second, before/after possible, 15-second script possible.
- Target fit: 15
  - Fits chosen niche such as Korean 40–60 household/salim audience.
- Risk: 10
  - Avoid brand/IP dependency, health/medical claims, heavy copyright reuse exposure.

Default: only produce videos for 70+ candidates.

## Beginner-friendly sourcing sequence

1. Start with Korean competitor account reverse-engineering.
2. Collect 20–30 high-view product videos.
3. Identify products and hooks.
4. Validate on Coupang.
5. Only then use Douyin/Taobao/TikTok to find more source variants and adjacent products.

This is easier than cold-searching Douyin first.