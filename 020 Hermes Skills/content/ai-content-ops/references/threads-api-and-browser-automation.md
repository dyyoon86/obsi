# Threads API vs Browser-Automation Posting Notes

Use when the user asks about Threads/Meta API, OpenClaw/browser agents, or multi-account social posting.

## Threads / Meta API

Threads has an official Meta developer API for normal automation use cases such as:

- Publishing Threads posts/media
- Managing replies/comments where permissions allow
- Reading basic profile/post data
- Reading insights/performance data

Common permission concepts include `threads_basic`, `threads_content_publish`, `threads_manage_replies`, and `threads_manage_insights`.

Treat this as the preferred long-term path for legitimate owned-account publishing and measurement, but expect setup friction:

- Meta developer app setup
- Account authorization and access tokens
- Possible business/creator account requirements
- App review / permission approval for broader use
- Rate limits and policy enforcement
- Token refresh/storage/security work

## Browser automation / OpenClaw-style posting

Browser-control agents can technically operate Threads like a human:

1. Open Threads
2. Use an authenticated session
3. Click compose
4. Paste text
5. Attach media
6. Click publish

This can be useful for early experiments or semi-automated workflows where APIs are unavailable. But distinguish **possible** from **safe/stable**.

Risks:

- Login, 2FA, CAPTCHA, new-device checks interrupt the flow
- UI changes break automation
- Wrong account/media/text can be posted
- Repeated behaviour can trigger platform detection
- Multi-account promotional posting can become spammy and risk account restrictions
- Brand accounts can lose trust if content feels automated or spam-like

## User-fit recommendation

For this user’s ionflow / AI-content workflow, prefer a safe publishing pipeline over multi-account promotional bots:

1. AI drafts the Threads post and selects one source-adjacent image
2. Store draft, source URL, media path, and status in Notion/DB
3. User approves or edits
4. Publish via official Threads API when possible; otherwise use browser automation only as a semi-automated helper
5. Collect URL and performance metrics back into the DB

Default advice: **do not recommend using OpenClaw to run many accounts and spray promotional posts.** Frame it as technically possible but high-risk for spam detection, account lockouts, and brand credibility. Recommend owned-account, approval-based, measured posting instead.

## Safer operating modes

- Best: official Threads API for approved posts from owned accounts
- Good early-stage: browser automation fills the post composer, human clicks final publish
- Acceptable for experiments: explicit user approval before each automated publish
- Avoid: multi-account repeated promotional posts, automatic replies/DMs, high-frequency link posting, identical copy across accounts
