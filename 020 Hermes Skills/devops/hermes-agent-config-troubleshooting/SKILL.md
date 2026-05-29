---
name: hermes-agent-config-troubleshooting
description: Configure and troubleshoot Hermes Agent model/provider settings, especially main model vs fallback provider behavior, gateway restarts, and confusing provider/model mismatch errors.
---

# Hermes Agent config & provider troubleshooting

Use this skill when the user asks about Hermes Agent itself: model/provider setup, fallback models, gateway errors, config.yaml, `hermes model`, provider auth, or why the bot is using a different model than expected.

## Core workflow

1. **Inspect the live config before explaining.**
   - Read `~/.hermes/config.yaml` first.
   - Check the top-level `model:` block and any `fallback_providers:` / `fallback_model:` entries.
   - Do not rely on prior session banners or memory alone; they may reflect a previous runtime or cached session state.

2. **Separate these concepts clearly.**
   - `model:` = primary model/provider.
   - `fallback_providers:` = ordered fallback list when primary fails.
   - `fallback_model:` = older/single fallback style that may coexist in configs; avoid leaving contradictory fallback settings if possible.
   - A Telegram/session banner may show the currently running process's active provider, not necessarily the newly edited config until restart.

3. **When changing provider/fallback settings, patch config deliberately.**
   - Prefer targeted edits to `~/.hermes/config.yaml` rather than inventing CLI commands unless verified from docs/skill.
   - Preserve unrelated config sections.
   - After patching, re-read the changed lines to verify.

4. **Tell the user the resulting state in plain Korean.**
   - Use short labels:
     - 메인: `provider / model`
     - 폴백: `provider / model`
   - Avoid over-explaining provider architecture when the user is frustrated; first answer the actual current state.

5. **Restart requirement.**
   - Config edits generally require gateway/bot restart to affect new conversations or active routing.
   - Say this explicitly after edits.

## Common pitfall: reversed fallback explanations

If the user says “OpenRouter로 세팅했는데 왜 Codex가 나오냐?” or similar, do **not** guess the direction of fallback. Inspect config first, then explain:

- If `model.provider: openai-codex`, Codex is primary.
- If `fallback_providers` includes OpenRouter, OpenRouter is fallback.
- If `model.provider: openrouter`, OpenRouter is primary.
- If `fallback_providers` includes Codex, Codex is fallback.

Do not say “OpenRouter가 먼저 터지고 Codex로 fallback” unless the config/logs actually prove that.

## Known-good example from session

User wanted:

```yaml
model:
  provider: openai-codex
  base_url: https://chatgpt.com/backend-api/codex
  default: gpt-5.5

fallback_providers:
- provider: openrouter
  model: openrouter/owl-alpha
```

Explain as:

- 메인: Codex `gpt-5.5`
- 폴백: OpenRouter `openrouter/owl-alpha`

## Error wording to interpret carefully

Errors like these can be produced by provider routing or gateway/runtime state and should trigger config/log inspection rather than confident guessing:

```text
Non-retryable error (HTTP None) — trying fallback...
'NoneType' object is not iterable
Gateway shutting down — Your current task will be interrupted.
```

Capture the fix as “verify primary/fallback config and restart,” not as a permanent claim that any provider is broken.

## User interaction preference for this class

The user may be frustrated and type quickly in Korean. Respond with concise, direct Korean, validate the current config with tools, and avoid long speculative explanations. If you make a wrong inference, correct it plainly and re-check the file.

## Codex CLI + Oh My codeX / OMX setup workflow

When the user asks about “Codex xhigh”, “omx”, “Oh My Codex”, or Codex versions of Claude Code-style workflow layers, treat it as Hermes-adjacent agent tooling setup and verify the actual package/CLI before answering.

Key points:

- `xhigh` is a Codex reasoning-effort mode; in OMX, `omx --xhigh` maps to `-c model_reasoning_effort="xhigh"`.
- OmX / Oh My codeX is the npm package `oh-my-codex`, a workflow/orchestration layer on top of OpenAI Codex CLI.
- Install order is Codex CLI first, then OMX: `npm install -g @openai/codex oh-my-codex`, then `omx setup`, then `omx doctor`.
- If npm global prefix is system-owned and fails with `EACCES`, prefer `npm config set prefix "$HOME/.local"` and ensure `~/.local/bin` is on PATH rather than using sudo.
- After setup, verify `codex login status`; if it says `Not logged in`, the install is fine but real Codex calls require `codex login` in the same environment.
- Use `omx reasoning xhigh` to persist default xhigh in `~/.codex/config.toml`.
- Warn briefly that `omx --madmax --xhigh` bypasses approvals/sandbox; recommend plain `omx --xhigh` for normal work.

See `references/codex-omx-wsl-setup.md` for the concise command recipe, verification steps, and WSL-specific paths.

## Codex/OMX + Obsidian MCP project-memory setup

When the user asks about Codex tips involving Obsidian MCP, project folders, and persistent memory, this is adjacent to Hermes/WSL setup. Prefer the class workflow in `hermes-omx-workflows`, especially `references/codex-obsidian-mcp-project-memory.md`, but keep these setup checks in mind:

- Verify Codex/OMX live state before explaining: `command -v codex omx`, `codex --version`, `omx --version`, `codex login status`, `codex mcp list`.
- Codex auth is separate from Hermes model/provider auth. If `codex login status` says `Not logged in`, the user must run `codex login` in WSL before interactive Codex/OMX can use MCP tools.
- Codex MCP servers are configured with `codex mcp add <name> --env KEY=VALUE -- <stdio command>`.
- For Obsidian vault paths on Windows, translate to WSL paths under `/mnt/c/Users/<user>/...` and ask for the actual vault path if `.obsidian` is not discoverable.

## Hermes Desktop install / WSL detection workflow

When the user asks about installing or using Hermes Desktop / `fathah/hermes-desktop`, treat it as Hermes Agent setup and use this skill. For Windows + WSL users, prefer downloading the Windows installer to the Windows Desktop and launching it via `cmd.exe /C start`; the user must approve any SmartScreen/UAC prompt manually.

If the installed Windows Desktop app cannot find the user's WSL Hermes, do **not** assume the install failed. Inspect and explain these distinct paths:

- Windows Desktop auto-detection usually checks the Windows-side home, e.g. `C:\Users\<user>\.hermes` or `%LOCALAPPDATA%\hermes`, not WSL `/home/<user>/.hermes`.
- Desktop's “use existing installation” validation expects the Desktop installer layout under the selected Hermes home: `hermes-agent/venv/...` plus the Hermes script. A WSL pip/user install such as `/home/<user>/.local/bin/hermes` with config in `/home/<user>/.hermes` may be valid for Telegram/CLI but not valid for Desktop adoption.
- Remote/Desktop API mode requires a reachable Hermes API endpoint, commonly `http://127.0.0.1:8642/health`; if connection is refused, Desktop cannot attach remotely yet.
- For this user's Windows+WSL setup, `hermes dashboard` on WSL (`http://127.0.0.1:9119`) is often the safer GUI alternative when Desktop cannot adopt WSL's pip-style install.

See `references/hermes-desktop-windows-wsl.md` for the concise recipe, validation checks, and fallback options.
