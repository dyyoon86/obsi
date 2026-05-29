---
name: hermes-omx-workflows
description: "Ported OMX/Codex workflow patterns for Hermes: deep-interview, ralplan-style consensus planning, ultragoal-style durable execution, team-style parallel delegation, ralph-style persistence, and independent code review using Hermes tools."
---

# Hermes OMX-style workflows

Use this skill when the user asks for OMX-like behavior inside Hermes, mentions `OMX`, `oh-my-codex`, `Codex xhigh`, `$deep-interview`, `$ralplan`, `$ultragoal`, `$team`, `$ralph`, `끝까지`, `롤백 가능하게`, `검증까지`, or wants a complex coding/devops task executed with strong planning, parallelism, persistence, and rollback safety.

This is a **Hermes-native port**, not direct Codex/OMX runtime execution. Do not assume Hermes can automatically load `~/.codex/skills`. Use Hermes tools:

- `todo` for the visible task ledger.
- `read_file`, `search_files`, `terminal`, `patch`, `write_file` for local evidence and edits.
- `delegate_task` for bounded parallel lanes.
- `process` for long-running background commands.
- `skill_manage` for Hermes skill edits.
- `clarify` only when a human decision materially changes scope or risk.

## Core rule

Preserve the OMX spirit while adapting to Hermes constraints:

1. Clarify only what cannot be discovered.
2. Plan enough to avoid rework.
3. Execute reversible local steps automatically.
4. Verify with fresh evidence before claiming done.
5. Keep rollback handles for any file/system changes.
6. Final report must include what changed, verification evidence, and rollback path.

## Workflow selector

Choose the lightest lane that satisfies the task:

- **Deep Interview**: vague, broad, or business/product requirements are unclear.
- **Ralplan-style consensus plan**: requirements are mostly clear but architecture/tradeoffs/test plan need review before implementation.
- **Ultragoal-style durable execution**: multi-step work needs a visible ledger and sequential completion checkpoints.
- **Team-style parallel execution**: independent subtasks can safely run in parallel via `delegate_task`.
- **Ralph-style persistence**: user asks not to stop, finish fully, retry until verified, or the task has many failure modes.
- **Independent Code Review**: before finalizing major code/config changes.

## Rollback-first discipline

Before non-trivial edits, create a rollback handle:

- For git repos: run `git status --short`, record current branch, and prefer git diffs. Do not commit unless asked.
- For non-git config/skills: create timestamped backups under an appropriate backup directory, e.g. `~/.hermes/backups/...`.
- For new Hermes skills: rollback is `skill_manage(action="delete", name="<skill>", absorbed_into="")` plus optional restore from tar backup.
- For targeted file edits: prefer `patch` so diffs are visible.
- For generated files: list exact paths in final response.

Never perform destructive, credentialed, external-production, or irreversible actions without user confirmation.

## Deep Interview, Hermes version

Use when ambiguity blocks correct execution.

Process:

1. Inspect discoverable facts first. Do not ask the user for file contents, OS state, git state, or current config if tools can retrieve them.
2. Score ambiguity mentally across:
   - intent/why
   - desired outcome
   - scope/in-scope
   - non-goals/out-of-scope
   - constraints
   - success criteria / acceptance tests
   - brownfield context, if code/config exists
3. Ask **one focused question at a time** using `clarify` only when the answer changes implementation or risk.
4. Prefer pressure questions:
   - “What should explicitly stay out of scope?”
   - “What evidence would make this done?”
   - “If we must choose speed vs safety, which wins?”
   - “Can I decide X automatically, or should I ask first?”
5. Stop interviewing when remaining uncertainty would not materially change execution.
6. Crystallize a compact spec in the chat or a local file when useful:
   - Goal
   - In scope
   - Out of scope
   - Constraints
   - Acceptance criteria
   - Decision boundaries
   - Verification plan

## Ralplan-style consensus planning, Hermes version

Use before high-risk or architecture-heavy implementation.

Process:

1. Create/update a `todo` ledger.
2. Gather context: files, configs, git diff, docs, versions, errors.
3. Draft a right-sized plan with:
   - principles / constraints
   - decision drivers
   - at least two viable options when real alternatives exist
   - selected approach and why
   - risks and rollback
   - verification plan
4. For substantive plans, run sequential review lanes:
   - Architect lane: use `delegate_task` for design/tradeoff review.
   - Critic lane: after architect result, use `delegate_task` for quality/testability/risk review.
5. Revise once if either review finds material blockers.
6. Proceed automatically only for safe, reversible local steps already requested. Ask only for material scope change or destructive/prod action.

Do not treat a written plan as approval to skip verification. Planning is complete only when risks, rollback, and acceptance evidence are explicit.

## Ultragoal-style durable execution, Hermes version

Use for multi-step work that must be tracked to completion.

Process:

1. Use `todo` as the durable session ledger.
2. Break the request into sequential goals with IDs.
3. Mark exactly one item `in_progress` at a time unless using explicit parallel `delegate_task` lanes.
4. After each goal:
   - record evidence: files changed, command output, tests, or read-back checks
   - mark the todo completed only after evidence exists
5. If a finding changes the decomposition, update the todo ledger and explain the steering reason.
6. Final goal must be a quality gate:
   - inspect actual changed artifacts
   - run relevant tests/build/lint/config validation where available
   - perform independent review for major changes
   - ensure no pending/in_progress todos remain

## Team-style parallel execution, Hermes version

Use `delegate_task` when parallelism improves quality/speed and tasks are independent.

Patterns:

- Research lane + implementation lane + verification lane.
- Code reviewer lane + architect lane for independent final review.
- Multiple source-analysis lanes for different files/repos/docs.

Rules:

1. Pass complete context to each subagent; subagents have no current-chat memory.
2. Give each lane a clear output contract: findings, file paths, commands run, evidence, risks.
3. Do not delegate tasks needing user interaction.
4. Do not trust subagent claims with external side effects until verified in the parent session.
5. Verify returned file paths, diffs, or command outputs yourself before final success claims.

## Ralph-style persistence, Hermes version

Use when the user says “끝까지”, “완료될 때까지”, “검증까지”, “don’t stop”, “finish this”, or equivalent.

Loop:

1. Review current todo state and evidence.
2. Continue the next incomplete item without asking if it is safe/reversible.
3. Run commands with adequate timeout; use background + `process` for long tasks.
4. If verification fails, fix and retry; do not claim partial success as done.
5. Stop only when:
   - all explicit requirements are mapped to evidence
   - verification has fresh passing output or a clearly stated reason why no executable verification exists
   - rollback path is known
   - todo ledger has no pending/in_progress items
6. Escalate to the user only for missing credentials, ambiguous material decisions, destructive/prod actions, or repeated blocker after reasonable retries.

## Independent code review gate, Hermes version

Use after non-trivial code/config edits or when user asks for review.

1. Identify scope: git diff or exact files changed.
2. Run two independent `delegate_task` lanes in parallel when practical:
   - Code review lane: bugs, security, maintainability, performance, spec compliance.
   - Architecture lane: system boundaries, hidden coupling, tradeoffs, future risk.
3. Synthesize with deterministic rules:
   - Any critical/high bug or architecture BLOCK => request changes / continue fixing.
   - Architecture WATCH with no blockers => report caveat, fix if cheap or relevant.
   - Approval requires actual evidence from both lanes or a transparent note that independent review was unavailable.
4. Verify fixes after review.

## Output format for final reports

Keep Korean responses concise unless the user asks for detail. Include:

- **완료:** what was done.
- **검증:** commands/checks and result.
- **변경 파일:** exact paths when files changed.
- **롤백:** exact restore/delete command or backup path.
- **주의:** remaining limitations or user action needed.

## Hermes/OMX boundary warning

If the user specifically wants real OMX runtime features (`omx team`, tmux panes, Codex `/goal`, `$deep-interview` inside Codex CLI), explain that those require Codex CLI/OMX outside Hermes. Hermes can call `omx` through `terminal`, but the Hermes-native port should use Hermes tools unless the user explicitly asks to run OMX itself.

## Codex/Obsidian external project memory

When the user asks about the Codex tip “connect Obsidian through MCP, create a project folder, write the plan/memory there, and update it after every task so context compaction does not block progress,” use `references/codex-obsidian-mcp-project-memory.md`.

Core approach:

- Treat Obsidian as the external source of truth for long Codex/OMX projects.
- Create `000 Projects/<project>/` with brief, plan, tasks, decisions, progress-log, and memory notes.
- Instruct Codex to read those notes before work and update them after each completed unit.
- If context shrinks or a new session starts, reload the project folder and continue from the recorded state.
- Prefer a filesystem-backed MCP server such as `mcp-obsidian-vault` when the user wants this in Codex; use a local Hermes project-memory folder when they want the same pattern inside Hermes.

## Current local setup note

On this machine, Codex CLI and `oh-my-codex` may be installed under the WSL user npm prefix. Verify live state with tools before relying on it:

```bash
command -v codex omx
codex --version
omx --version
codex login status
codex mcp list
```

Do not assume Codex auth or MCP servers are available; check before calling real `omx exec`, interactive workflows, or MCP-backed Obsidian operations.
