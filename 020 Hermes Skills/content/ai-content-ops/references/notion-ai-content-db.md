# Notion AI Content DB Session Reference

This reference captures the initial Notion database and automation design for the user’s AI-content workflow. Keep this concise and use it as a starting point, not a rigid constraint.

## User objective

The user wants to gather AI news for a YouTube AI channel and repurpose each selected item into:

- YouTube Shorts
- Threads posts
- Threads thread/tarae
- YouTube community or Instagram caption
- Notion DB record for storage and later performance analysis

## Recommended database name

`AI 콘텐츠 소재 DB`

## Minimal DB schema

Start simple if the user is new to Notion:

- `소재명` — Title
- `날짜` — Date
- `상태` — Status
- `우선순위` — Select
- `카테고리` — Multi-select
- `출처` — Text or Select
- `원문 링크` — URL
- `쇼츠 훅` — Text
- `쇼츠 대본` — Text
- `Threads 짧은 글` — Text

## Expanded DB schema

Add as the workflow matures:

- `팩트체크 필요` — Checkbox
- `핵심 한 줄` — Text
- `쇼츠 적합도` — Number
- `제목 후보` — Text
- `썸네일 문구` — Text
- `B-roll 아이디어` — Text
- `Threads 타래` — Text
- `유튜브 커뮤니티 글` — Text
- `해시태그` — Text
- `쇼츠 발행일` — Date
- `Threads 발행일` — Date
- `유튜브 URL` — URL
- `Threads URL` — URL
- `조회수` — Number
- `좋아요` — Number
- `댓글` — Number
- `저장/공유` — Number
- `성과 메모` — Text

## Current confirmed user DB shape from setup session

The user created a Notion database named `AI 콘텐츠 소재 DB` and connected an internal integration named like `Hermes AI Content Bot`. Environment variables are stored locally in `~/.config/hermes/notion.env`:

- `NOTION_TOKEN`
- `NOTION_DATABASE_ID`

After the user changed column properties, the live schema was confirmed as:

- `소재명` — title
- `날짜` — date
- `상태` — status
- `우선순위` — select
- `카테고리` — multi_select
- `원문 링크` — url
- `팩트체크 필요` — checkbox
- `쇼츠 적합도`, `조회수`, `좋아요`, `댓글`, `저장/공유` — number
- `쇼츠 발행일`, `Threads 발행일` — date
- `유튜브 URL` — url
- `Threads URL` — rich_text at last check
- most content fields (`핵심 한 줄`, `쇼츠 훅`, `쇼츠 대본`, `제목 후보`, `썸네일 문구`, `B-roll 아이디어`, `Threads 짧은 글`, `Threads 타래`, `유튜브 커뮤니티 글`, `해시태그`, `성과 메모`, `출처`) — rich_text

Important: always re-fetch the schema before writing because the user may change Notion property types.

## Status options

Recommended content-specific options:

- 수집됨
- 대본작성
- 제작중
- 예약됨
- 발행완료
- 성과기록완료
- 보류

During setup, the user’s live DB still had default Notion status options:

- 시작 전
- 진행 중
- 완료

Do not write `수집됨` unless it exists. Either use the existing option (e.g. `시작 전`) or ask the user to add/rename options.

## Priority options

Recommended:

- 1순위
- 후보
- 보류

During setup, only `1순위` was present at one point, so inspect before writing.

## Category examples

- AI 영상
- AI 이미지
- AI 음성
- AI 툴
- OpenAI
- Google
- Anthropic
- NVIDIA
- AI 칩
- AI 에이전트
- 일자리
- 딥페이크
- 저작권
- 비즈니스/투자
- 콘텐츠제작
- 무료툴
- 논문/연구

## Recommended Notion views

1. 오늘 만들 콘텐츠
   - Filter: 우선순위 = 1순위, 상태 != 발행완료
   - Sort: 쇼츠 적합도 descending
2. 후보 소재 보관함
   - Filter: 우선순위 = 후보
3. 발행 완료
   - Filter: 상태 = 발행완료 or 성과기록완료
4. 성과 분석
   - Show: 소재명, 카테고리, 쇼츠 훅, 조회수, 좋아요, 댓글, 성과 메모
   - Sort: 조회수 descending

## Notion API notes

- For personal automation use Internal Integration Secret, not OAuth.
- Token should be stored as an environment variable, not pasted openly.
- WSL env file pattern:

```bash
mkdir -p ~/.config/hermes
cat > ~/.config/hermes/notion.env <<'EOF'
export NOTION_TOKEN='secret_xxx'
export NOTION_DATABASE_ID='database_id_xxx'
EOF
printf '\n[ -f ~/.config/hermes/notion.env ] && source ~/.config/hermes/notion.env\n' >> ~/.bashrc
source ~/.config/hermes/notion.env
```

- Verify safely:

```bash
echo $NOTION_DATABASE_ID
echo ${NOTION_TOKEN:0:10}
```

- If API returns `object_not_found`, likely causes are:
  1. Integration is not connected/shared to the actual database page.
  2. Integration was created in a different Notion workspace.
  3. Wrong database ID was copied, or only a view/page ID was copied.

## Robust write pattern

1. Fetch `GET /v1/databases/{database_id}`.
2. Build page properties based on live property `type` values.
3. For `status`, `select`, and `multi_select`, use only option names discovered from the live schema unless the user has explicitly added others.
4. On invalid option errors, re-fetch options and either remap or ask the user to add/rename options.
5. Create a test page after schema edits before enabling daily automation.

## Example Threads style

Short, insight-driven, not news-anchor style:

```text
AI 영상 도구가 발전할수록
콘텐츠 제작자의 역할은 사라지는 게 아니라 바뀐다.

촬영자에서 연출자로,
편집자에서 프롬프트 디렉터로.

앞으로 유튜브 쇼츠를 잘 만드는 사람은
카메라를 잘 다루는 사람이 아니라
AI에게 장면을 잘 설명하는 사람일 수도 있다.
```

## Example daily prompt

```text
오늘 AI 뉴스로 원소스 멀티유즈 콘텐츠 패키지 만들어줘.
Notion DB에 넣을 수 있게 아래 필드로 정리해줘:
소재명, 날짜, 카테고리, 출처, 원문 링크, 우선순위, 쇼츠 적합도, 핵심 한 줄, 쇼츠 훅, 쇼츠 대본, 제목 후보, 썸네일 문구, B-roll 아이디어, Threads 짧은 글, Threads 타래, 유튜브 커뮤니티 글, 해시태그, 팩트체크 필요, 메모.
```
