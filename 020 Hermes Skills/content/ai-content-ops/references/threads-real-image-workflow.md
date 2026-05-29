# Threads real/source image workflow

Use this note when packaging AI news for Threads-style posts where the user wants one image like creator/news accounts use, not a full Instagram carousel.

## Preferred image hierarchy

1. **Official source image/screenshot**
   - Article hero image, product screenshot, official announcement visual, demo GIF/frame.
   - If using a screenshot, crop cleanly and avoid adding too much text.

2. **Source-adjacent factual image**
   - Product UI, logo/announcement page, paper figure, chart, diagram from the cited source.
   - Good for posts where the user wants “실제 기사나 이런 곳에서 이미지 하나.”

3. **Relevant public-domain/CC image when source image is unavailable**
   - Use Wikimedia Commons or other clearly licensed sources.
   - Include file/source/license in the response.
   - Make clear it is an illustrative/relevant image, not necessarily the article’s official image.

4. **Generated image only if the user asks for generated visuals or no real/source image exists**
   - For Threads, generated images are often less natural than one source screenshot or factual image.

## Writing style paired with the image

Threads post should be a single concise explainer:

```text
[뉴스 핵심 한 줄]

이게 무슨 말이냐면

[쉬운 설명]

핵심은
[오해 방지]

결국
[해석 / 앞으로의 변화]

[검증 필요하면 짧게]
```

Do not default to multi-slide card news for Threads unless the user explicitly asks for Instagram carousel/card뉴스.

## Example from the OpenAI unit-distance/discrete-geometry item

When OpenAI source image extraction is blocked/unavailable, a relevant public-domain image can work:

- Wikimedia Commons: `Coxeter graph unit distance.svg`
- Source: `https://commons.wikimedia.org/wiki/File:Coxeter_graph_unit_distance.svg`
- License: Public domain
- Use it as a visual explanation of “unit distance graph,” not as OpenAI’s official article image.

Possible Threads copy:

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
