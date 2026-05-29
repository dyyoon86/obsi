# Codex + OMX + Obsidian MCP setup notes

Use this as a compact reference when the user asks for `codex xhigh + omx`, Codex MCP setup, or Windows/WSL Obsidian vault wiring.

## User intent pattern

When the user says terse phrases like `codex xhigh + omx`, treat it as a configuration/action request, not a request for explanation. Prefer direct commands and verification steps.

## Windows app verification from WSL

For Windows-installed apps, verify from WSL by invoking `cmd.exe` and checking both winget and the expected executable path. Example pattern:

```bash
cmd.exe /C "cd /d C:\\Users\\ppotr && winget list Obsidian && if exist C:\\Users\\ppotr\\AppData\\Local\\Programs\\Obsidian\\Obsidian.exe (echo FOUND_LOCAL_OBSIDIAN) else (echo NO_LOCAL_OBSIDIAN)"
```

Notes:
- WSL may start `cmd.exe` from a UNC path and print a warning; this is not necessarily a failure if the command output continues.
- For this user's Windows account, common Windows paths map to `/mnt/c/Users/ppotr/...` inside WSL.

## Obsidian vault path mapping

Recommended Windows vault paths:

```text
C:\Users\ppotr\Documents\ObsidianVault
C:\Users\ppotr\OneDrive\ObsidianVault
```

Corresponding WSL paths:

```text
/mnt/c/Users/ppotr/Documents/ObsidianVault
/mnt/c/Users/ppotr/OneDrive/ObsidianVault
```

## Codex MCP add pattern for Obsidian vault

Once the vault exists, add the MCP server using the WSL path:

```bash
codex mcp add obsidian-vault \
  --env OBSIDIAN_VAULT_PATH="/mnt/c/Users/ppotr/Documents/ObsidianVault" \
  -- npx -y mcp-obsidian-vault
```

Swap the path if the user chose OneDrive.

## Response style for this class of request

- Keep the answer action-first and concise.
- Show the exact command(s), then the verification result.
- Avoid long conceptual explanation unless the user asks why.
