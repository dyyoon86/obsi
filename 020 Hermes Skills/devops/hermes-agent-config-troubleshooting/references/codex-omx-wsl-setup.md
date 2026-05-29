# Codex CLI + Oh My codeX (OMX) on WSL

Use this reference when the user asks about “Codex xhigh”, “omx”, “Oh My Codex”, or Codex CLI workflow-layer setup.

## What the terms mean

- `xhigh` is a Codex CLI reasoning-effort value.
- In OMX, `omx --xhigh` is shorthand for passing `-c model_reasoning_effort="xhigh"` to Codex.
- OMX / OmX / Oh My codeX is the npm package `oh-my-codex`, a workflow/orchestration layer on top of OpenAI Codex CLI, not a replacement for Codex.

## Official install targets verified in-session

```bash
npm install -g @openai/codex
npm install -g oh-my-codex
omx setup
omx doctor
```

If the global npm prefix is system-owned (`/usr`) and install fails with EACCES, prefer a user prefix instead of sudo:

```bash
npm config set prefix "$HOME/.local"
# Ensure ~/.local/bin is on PATH, then:
npm install -g @openai/codex oh-my-codex
```

## Useful verification commands

```bash
codex --version
omx --version
omx setup
omx doctor
codex login status
omx reasoning
```

Set default xhigh reasoning:

```bash
omx reasoning xhigh
# verifies/updates ~/.codex/config.toml:
# model_reasoning_effort = "xhigh"
```

Launch examples:

```bash
omx --xhigh
omx --madmax --xhigh   # dangerous: bypasses approvals/sandbox
```

## Pitfalls

- OMX requires a working `codex` command; install/authenticate Codex CLI first.
- `codex login status` may return `Not logged in` after install. The user must run `codex login` in the same WSL environment before real model calls work.
- `omx doctor` may warn about the Explore Harness/Rust/cargo; that does not necessarily block normal OMX/Codex usage. Install Rust/cargo only if `omx explore` is needed.
- For this user, WSL paths matter: Codex config is typically under `/home/coka/.codex`, npm global user installs under `/home/coka/.local`, and Hermes config under `/home/coka/.hermes`.
