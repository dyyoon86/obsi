# Codex + Obsidian MCP project memory pattern

Use this reference when the user asks about tips like: “connect Obsidian to MCP, create a project folder, keep plans/memory there, and update it after every step so Codex does not get blocked when context shrinks.”

## What the pattern means

The pattern uses Obsidian as an external, filesystem-backed source of truth for a long-running Codex project:

```text
Codex / OMX
  -> MCP server
  -> Obsidian vault
  -> 000 Projects/<project>/
       00-brief.md
       01-plan.md
       02-tasks.md
       03-decisions.md
       04-progress-log.md
       05-memory.md
       artifacts/
```

The agent is instructed to read the project folder before work, update task/progress notes after each unit, record decisions with rationale, and reload the folder when context compacts or a new session starts.

This reduces context-loss failures because state lives outside the model transcript.

## Fit check for this user's WSL Codex setup

Verify live state before configuring:

```bash
command -v codex omx node npm
codex --version
omx --version
codex login status
codex mcp list
```

Codex CLI supports MCP management:

```bash
codex mcp add <name> --env KEY=VALUE -- <stdio command>
codex mcp list
codex mcp get <name>
codex mcp remove <name>
```

If `codex login status` is `Not logged in`, the user must run `codex login` interactively in WSL before real Codex/OMX use.

## MCP server choice

For this workflow, prefer a filesystem-backed vault MCP server that does not require Obsidian to be running. A good candidate discovered in-session:

```bash
npx -y mcp-obsidian-vault
```

It is intended for notes, projects, tasks, context, decisions, discoveries, and git sync in an Obsidian vault. Configure it with an absolute WSL path to the vault.

Example Codex MCP add command:

```bash
codex mcp add obsidian-vault \
  --env OBSIDIAN_VAULT_PATH="/mnt/c/Users/<windows-user>/Documents/<ObsidianVault>" \
  -- npx -y mcp-obsidian-vault
```

Use the actual vault path. Windows paths translate to WSL paths, e.g.:

```text
C:\Users\ppotr\Documents\ObsidianVault
-> /mnt/c/Users/ppotr/Documents/ObsidianVault
```

## If no vault is found

Search common Windows locations for `.obsidian` directories, but do not conclude Obsidian is unavailable just because common paths are empty. Ask the user for the vault path if not discoverable.

Common candidates:

- `/mnt/c/Users/<user>/OneDrive/...`
- `/mnt/c/Users/<user>/Documents/...`
- `/mnt/c/Users/<user>/Desktop/...`
- `/mnt/c/Users/<user>/Downloads/...`

## Codex project-memory prompt template

Use inside Codex/OMX after MCP is connected:

```text
프로젝트명: <project>

Obsidian MCP의 vault 안에 `000 Projects/<project>` 폴더를 만들어줘.

다음 파일을 만들어:
- 00-brief.md
- 01-plan.md
- 02-tasks.md
- 03-decisions.md
- 04-progress-log.md
- 05-memory.md
- artifacts/

앞으로 이 프로젝트 작업을 할 때는:
1. 작업 시작 전에 `000 Projects/<project>`의 brief/plan/tasks/memory/progress-log를 먼저 읽어.
2. 작업 단위를 하나 끝낼 때마다 02-tasks.md와 04-progress-log.md를 갱신해.
3. 중요한 결정은 03-decisions.md에 “결정 / 이유 / 대안 / 날짜” 형식으로 기록해.
4. 다음 세션에서 이어받아야 하는 정보는 05-memory.md에 짧게 기록해.
5. 컨텍스트가 압축되거나 줄어든 것 같으면 Obsidian의 해당 프로젝트 폴더를 다시 읽고 이어서 해.
6. 너의 내부 기억보다 Obsidian의 `000 Projects/<project>` 폴더를 이 프로젝트의 source of truth로 우선해.
```

## Hermes-native alternative

If the user wants the same idea inside Hermes rather than Codex CLI, use a local project memory folder with Hermes file tools instead of MCP:

```text
/home/coka/project_memory/<project>/
  00-brief.md
  01-plan.md
  02-tasks.md
  03-decisions.md
  04-progress-log.md
  05-memory.md
```

This mirrors the Obsidian pattern without depending on Codex auth or MCP server availability.
