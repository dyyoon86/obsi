# Evan Carmichael case notes

Use these notes as a compact precedent when analyzing large English benchmark channels for the Korean user.

## Channel pattern observed

- Channel: Evan Carmichael / @evancarmichael
- Scale observed: ~4.55M subscribers via yt-dlp metadata
- Positioning: #BelieveNation; daily self-belief / motivation habit, not just business education.
- Surface niche: success, entrepreneurship, wealth, public speaking, creator growth.
- Deeper promise: turn famous people's wisdom into daily confidence and action.

## Reusable strategic reading

Evan Carmichael's channel works through:

1. **Borrowed authority** — famous figures such as Warren Buffett, Andrew Huberman, Elon Musk, Mark Zuckerberg, rich investors, iconic brands/celebrities.
2. **Repeatable packaging** — `Top 10 Rules for Success`, `ALL OF X Explained in N Minutes`, `The Secret To X`, `N Things Rich People Do`.
3. **Compression promise** — long interviews/speeches distilled into rules; `No BS, No Fluff` style titles reduce perceived waste.
4. **Transformation narrative** — low starting point / failure / years of struggle → discovered principle → success.
5. **Community ritual** — #BelieveNation and recurring intros make the channel a daily motivation habit.

## 투두TV adaptation precedent

Do **not** recommend copying the self-help / quote-curation niche directly. For 투두TV, translate the mechanism:

- `Top 10 Rules for Success` → `AI 실무자동화 10가지 규칙`
- `ALL OF X Explained` → `Claude Skills/HWPX/Notion 자동화 완전정리`
- `No BS, No Fluff` → `개념 말고 바로 써먹는 파일/워크플로우`
- daily belief habit → daily practical automation skill habit

Example transformed titles:

- `Claude Skills의 거의 모든 것 — 실무 자동화용으로만 정리했습니다`
- `AI 회의록 자동화, 초보자가 가장 많이 망하는 7가지 이유`
- `ChatGPT/Claude로 일 잘하는 사람들의 10가지 작업 습관`
- `HWPX 문서 자동화의 거의 모든 것 — No 개념설명, 바로 실전`
- `AI 콘텐츠 DB 만드는 법 — Notion 하나로 소재→쇼츠→Threads까지`

## Tooling lesson from this session

When using `yt-dlp --dump-json` for full video metadata, avoid routing huge JSON through short capped tool outputs before parsing. Write stdout to files first, then parse those local files. In this session, parsing inside `execute_code` from `terminal()` failed because long JSON was truncated/corrupted; running `subprocess.run(..., stdout=open(file,'w'))` and then `json.load(file)` worked.

Suggested robust pattern:

```python
res = subprocess.run([
  'yt-dlp', '--dump-json', '--skip-download', '--no-warnings', url
], stdout=open(outfile, 'w'), stderr=subprocess.PIPE, text=True, timeout=100)
if res.returncode == 0:
    data = json.load(open(outfile))
```

Also note: YouTube's `?sort=p` URL is not always reliable through yt-dlp flat playlist extraction. If true all-time popular ordering matters, fetch a broader sample and sort locally by `view_count` after metadata retrieval, while clearly stating the sampling window.
