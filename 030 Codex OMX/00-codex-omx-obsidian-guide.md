# Codex + OMX + Obsidian 사용법

생성: 2026-05-29 09:12:01

## 현재 연결
- Vault 경로: `/mnt/c/Users/ppotr/Documents/ObsidianVault`
- Codex MCP 이름: `obsidian-vault`
- MCP 서버: `npx -y mcp-obsidian-vault`

## 중요
Codex는 현재 MCP 연결은 되어 있지만, 로그인 상태는 `Not logged in`이었다. 실제 Codex 사용 전 WSL 터미널에서 필요하면:

```bash
codex login
```

확인:

```bash
codex login status
codex mcp list
codex mcp get obsidian-vault
```

## Codex에게 줄 기본 프롬프트

```text
Obsidian MCP `obsidian-vault`를 사용해 이 Vault를 프로젝트 기억장치로 써줘.
작업 시작 전에는 관련 프로젝트 폴더의 brief/plan/tasks/decisions/progress-log/memory를 먼저 읽어.
작업 단위를 하나 끝낼 때마다 tasks와 progress-log를 갱신해.
중요한 결정은 decisions에 결정/이유/대안/날짜 형식으로 기록해.
다음 세션에서 이어받아야 하는 정보는 memory에 짧게 기록해.
컨텍스트가 압축되거나 줄어든 것 같으면 Obsidian 프로젝트 폴더를 다시 읽고 이어서 해.
내부 기억보다 Obsidian 프로젝트 폴더를 source of truth로 우선해.
```

## OMX 스타일 명령 예시

```bash
omx --help
omx skill list
codex mcp list
```

사용자가 말한 “codex xhigh + omx”는 긴 작업에서 다음 방식으로 운영한다:
- Obsidian에 프로젝트 메모리 유지
- Codex/OMX는 작업 시작 시 이 메모리를 읽음
- 작업 후 진행상황/결정/다음 할 일 기록
- 컨텍스트 압축되어도 Obsidian으로 복구
```
