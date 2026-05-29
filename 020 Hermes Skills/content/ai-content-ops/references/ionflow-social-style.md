# ionflow social post style notes

Session-derived reference for the user's `ionflow` AI trend account.

## Threads style the user liked

The user showed screenshots of creator-style Threads posts and wanted this style for AI news. Use this structure:

```text
[뉴스 핵심 한 줄]

이게 무슨 말이냐면

[기존 상황/배경]

근데 이제
[바뀐 점]

핵심은
[오해 방지 or 의미]

결국
[앞으로의 변화 / 개인 해석]

물론 [검증 필요 or caveat]
```

Tone:

- Casual Korean: `~함`, `~거임`, `이게 무슨 말이냐면`, `핵심은`, `결국`.
- First line should state the news directly.
- Use short lines and generous line breaks.
- Explain why it matters; do not sound like a press release.
- Usually one source-adjacent image is enough. Threads is not Instagram card뉴스 by default.

## Example: OpenAI discrete geometry item

```text
OpenAI 모델이 80년 된 수학 추측에 반례를 찾았다고 발표함

이게 무슨 말이냐면

수학자들이 오랫동안
“이 정도가 한계일 거다”라고 생각했던 문제를

AI가 수많은 경우의 수를 탐색하다가
다른 가능성을 찾아낸 거임

핵심은
AI가 수학자를 대체했다는 게 아니라

사람이 문제를 정의하고
AI가 인간이 놓쳤을 수 있는 후보를 찾아주는 식으로
연구 방식이 바뀌고 있다는 점

앞으로 AI 경쟁은
말 잘하는 챗봇보다
이런 “발견하는 AI” 쪽이 더 중요해질 수도 있음

물론 세부 검증은 계속 봐야 함
```

## Image choice lesson

For technical/math AI news, a literal real-world photo is often weak. Better options:

1. Official article screenshot or announcement visual.
2. Product/demo screenshot if the news is about a tool.
3. Relevant public-domain/CC graph/diagram when the official image is unavailable.
4. Minimal generated abstract graphic only when no source-adjacent image fits.

If using a substitute image, give the user the source and license. Example used: Wikimedia Commons `Coxeter graph unit distance.svg`, public domain, as a unit-distance-problem-adjacent visual.

## Instagram vs Threads

- Instagram feed: if the user asks for “인스타에 게시할 모든 정보,” provide caption, hashtags, image prompt, card/carousel structure, aspect ratio, and design notes.
- For hard technical topics, suggest 5-card carousel before 8-card carousel unless the user asks for detail; 8 cards means 8 images.
- Threads: one image + short explanatory text usually matches the user's target style better.

## Video download lesson

When the user asks to download a YouTube Short:

```bash
yt-dlp -f 'bv*+ba/best' --merge-output-format mp4 -o '/tmp/ionflow_downloads/%(title).80s-%(id)s.%(ext)s' '<url>'
```

If `yt-dlp` says `Private video`, tell the user to make it public/unlisted or send the file, then retry. Once made public/unlisted, the same command should work and can be returned as `MEDIA:/absolute/path.mp4`.
