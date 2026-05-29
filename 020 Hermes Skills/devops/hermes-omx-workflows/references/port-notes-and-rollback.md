# OMX-to-Hermes port notes and rollback

Created as a Hermes-native port of selected `oh-my-codex` workflow patterns. It does **not** copy the Codex CLI runtime; it maps the ideas onto Hermes tools.

## Source OMX skills inspected

- `/home/coka/.codex/skills/deep-interview/SKILL.md`
- `/home/coka/.codex/skills/ralplan/SKILL.md`
- `/home/coka/.codex/skills/ultragoal/SKILL.md`
- `/home/coka/.codex/skills/team/SKILL.md`
- `/home/coka/.codex/skills/ralph/SKILL.md`
- `/home/coka/.codex/skills/code-review/SKILL.md`

## Ported concepts

- `$deep-interview` → Hermes one-question-at-a-time clarification after tool-discoverable facts are checked.
- `$ralplan` → Hermes consensus planning with context intake, options, risk/rollback, architect then critic review lanes.
- `$ultragoal` → Hermes `todo`-based sequential goal ledger with evidence checkpoints.
- `$team` → Hermes `delegate_task` parallel lanes, not tmux workers.
- `$ralph` → Hermes persistence loop: continue safe/reversible work until requirements map to evidence.
- `$code-review` → Hermes independent code-review + architecture lanes via `delegate_task`.

## Important boundary

Real OMX runtime features still require Codex CLI/OMX:

```bash
codex login
omx --xhigh
omx team ...
omx ultragoal ...
```

Hermes can call `omx` through `terminal`, but this skill is intended for native Telegram/Hermes operation.

## Backup created before port

Full Hermes skills backup:

```text
/home/coka/.hermes/backups/skills/hermes-skills-before-omx-port-20260528T234025Z.tar.gz
```

SHA256:

```text
267d0a763ca46e42df59d3129f9692c422a24df7ee365b61676d6d9ec9634d2b
```

## Rollback options

### Simple rollback: remove only this new skill

Use Hermes skill tool:

```python
skill_manage(action="delete", name="hermes-omx-workflows", absorbed_into="")
```

Or shell fallback:

```bash
rm -rf /home/coka/.hermes/skills/devops/hermes-omx-workflows
```

### Full restore of pre-port skills backup

Only use if multiple skill files were damaged. This overwrites current skills with the pre-port snapshot:

```bash
cd /home/coka/.hermes
mv skills "skills.broken-$(date -u +%Y%m%dT%H%M%SZ)"
tar -xzf /home/coka/.hermes/backups/skills/hermes-skills-before-omx-port-20260528T234025Z.tar.gz
```

Verify afterward:

```bash
find /home/coka/.hermes/skills -name SKILL.md -maxdepth 4 | sort
```
