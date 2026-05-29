# Hermes Desktop on Windows + WSL

Use this when the user asks to install or use `fathah/hermes-desktop` while Hermes Agent is already running in WSL and the user is on Windows.

## Recommended installer path

1. Check the latest GitHub release asset names via the GitHub releases API.
2. Prefer the Windows installer asset named like:
   - `hermes-desktop-<version>-setup.exe`
   - Portable `.exe` is secondary if the user wants no installer.
3. Download the installer to the Windows Desktop path, translating Windows path to WSL:
   - Windows: `C:\Users\<username>\OneDrive\Desktop\...` or `C:\Users\<username>\Desktop\...`
   - WSL: `/mnt/c/Users/<username>/OneDrive/Desktop/...` or `/mnt/c/Users/<username>/Desktop/...`
4. Verify the file exists and has a plausible non-zero size.
5. Launch from WSL with:
   ```bash
   cmd.exe /C start "" "C:\Users\<username>\OneDrive\Desktop\hermes-desktop-<version>-setup.exe"
   ```
6. Tell the user they must manually approve Windows SmartScreen/UAC:
   - SmartScreen: `More info` / `추가 정보` → `Run anyway` / `실행`

## Important WSL detection pitfall

Do not claim Desktop will definitely find the existing WSL Hermes install.

Hermes Desktop is a Windows/Electron app when installed via the Windows setup exe. Its local auto-detection checks the Windows-side Hermes home first, typically:

```text
C:\Users\<username>\.hermes
%LOCALAPPDATA%\hermes
```

A working WSL Hermes may instead live at:

```text
/home/<wsl-user>/.hermes
/home/<wsl-user>/.local/bin/hermes
/home/<wsl-user>/.local/lib/pythonX.Y/site-packages
```

Those are separate environments. Windows Desktop may not see or adopt the WSL install automatically.

## What Desktop validates for “use existing installation”

Current Desktop source validates an existing Hermes home by looking for the Desktop installer layout. Conceptually it expects files like:

```text
<HERMES_HOME>/hermes-agent/venv/bin/python
<HERMES_HOME>/hermes-agent/hermes
```

On Windows it expects the analogous `venv\Scripts\python.exe` and `venv\Scripts\hermes.exe`.

So a WSL pip/user install can be valid for `hermes` CLI, Telegram gateway, skills, memory, and config, while still failing Desktop's “use existing installation” check.

## Verification commands in WSL

Check the live WSL install shape:

```bash
command -v hermes
hermes version
for p in \
  ~/.hermes/hermes-agent/venv/bin/python \
  ~/.hermes/hermes-agent/hermes \
  ~/.hermes/config.yaml \
  ~/.hermes/gateway.pid; do
  [ -e "$p" ] && echo "YES $p" || echo "NO  $p"
done
```

Check whether Desktop remote/API mode can attach:

```bash
python3 - <<'PY'
import urllib.request
for url in ['http://127.0.0.1:8642/health','http://localhost:8642/health']:
    try:
        r = urllib.request.urlopen(url, timeout=2)
        print(url, r.status, r.read(200))
    except Exception as e:
        print(url, type(e).__name__, e)
PY
```

If `connection refused`, the Hermes API server expected by Desktop is not currently reachable.

## User-facing options

When Desktop cannot find the WSL install, present the options plainly:

1. **Let Desktop install a separate Windows Hermes**
   - Easiest for Desktop app compatibility.
   - But it may create a separate Hermes home/config/memory/skills from the WSL Telegram bot setup.

2. **Use WSL Hermes Dashboard instead**
   - Often safer for this user's setup because it uses the existing WSL Hermes state.
   - Start with:
     ```bash
     hermes dashboard
     ```
   - Open in Windows browser:
     ```text
     http://127.0.0.1:9119
     ```

3. **Attach Desktop via Remote mode**
   - Only if a Hermes API endpoint is running and reachable, commonly:
     ```text
     http://127.0.0.1:8642
     ```
   - First verify `/health` returns HTTP 200.

## Prior observed example

- Windows user: `ppotr`
- WSL user: `coka`
- Installer downloaded to:
  ```text
  C:\Users\ppotr\OneDrive\Desktop\hermes-desktop-0.5.1-setup.exe
  /mnt/c/Users/ppotr/OneDrive/Desktop/hermes-desktop-0.5.1-setup.exe
  ```
- WSL Hermes was valid but pip/user-style:
  ```text
  /home/coka/.local/bin/hermes
  /home/coka/.local/lib/python3.12/site-packages
  /home/coka/.hermes/config.yaml
  ```
- Desktop layout files under `/home/coka/.hermes/hermes-agent/venv/...` were absent, so Desktop adoption could fail.

## Pitfalls

- Do not claim installation completed just because the installer was downloaded or launched. Say only that the installer file is ready and/or the install window was launched.
- Do not promise Windows Desktop will automatically detect a WSL Hermes install, especially if Hermes was installed by pip/user rather than the Desktop's expected installer layout.
- `cmd.exe` launched from WSL may print a UNC path warning; if exit code is 0, it usually still launched or attempted to launch the Windows executable.
- If the setup window does not appear, instruct the user to double-click the `.exe` on the Windows Desktop.
