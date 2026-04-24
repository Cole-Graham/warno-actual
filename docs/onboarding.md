# Onboarding: optional development conveniences

This page collects **quality-of-life** setup that is not required to install dependencies, run the patcher, or build the mod. The main [README](../README.md) is the source of truth for the Python environment, configuration, and project rules. **Project conventions** for humans and AI assistants are in [**AGENTS.md**](../AGENTS.md). A single policy rule in [`.cursor/rules/sync-agents-md-with-cursor-rules.mdc`](../.cursor/rules/sync-agents-md-with-cursor-rules.mdc) is in git; other `.cursor/` content is local (see [`.gitignore`](../.gitignore)).

## VS Code / Cursor: `.venv` in the integrated terminal

If you use **Visual Studio Code** or **Cursor** with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python), you can have each **new** integrated terminal activate the project virtual environment so `python` / `pip` and the prompt (for example `(.venv)`) stay aligned.

### How this repository configures it

- **`warno-actual.code-workspace`** — If you open the repo via this workspace file, editor settings (including `python.defaultInterpreterPath`, `python.terminal.activateEnvironment`, [terminal integration](https://code.visualstudio.com/docs/terminal/basics#_terminal-profiles) profiles on Windows, and `terminal.integrated.persistentSessionReviveProcess`) live in the workspace `settings` block. **Some keys only apply consistently when they are in the workspace file** when you are not opening the folder alone.
- **`.vscode/settings.json`** — If you open the **folder** only, folder-level settings apply; this repo still sets `python.defaultInterpreterPath` to the venv for Windows (`.venv\Scripts\python.exe`).

### What the settings are trying to do

- **`python.defaultInterpreterPath`** — Tells the Python extension which interpreter to use (Windows path under `.venv\Scripts\`, or `.venv/bin/python` on Linux/macOS).
- **`python.terminal.activateEnvironment`** — When `true`, opening a **new** integrated terminal can run the activation flow so the venv is active in that shell.
- **`terminal.integrated.persistentSessionReviveProcess`** — Set to **`never`** in this repo’s workspace settings. On a **full** editor restart, some environments otherwise **revive** old terminal tabs: scrollback can still show a previous `(.venv)` while the new process was started with a **pre-activation** environment, so `python` might not point at the venv. Turning revive off trades away restored terminal buffers for shells that are created fresh after restart so activation can run again.

### What you need locally

1. Install the **Python** extension in the editor.
2. Create `.venv` using the [README](../README.md) steps so the interpreter path exists.
3. Open a **new** terminal (**Terminal → New Terminal**). If the interpreter was not picked up, run **Python: Select Interpreter** and choose `.venv`, or **Developer: Reload Window**.

### Linux / macOS paths

Set `python.defaultInterpreterPath` to `"${workspaceFolder}/.venv/bin/python"` in the relevant `settings` (or use **Python: Select Interpreter** and pick `.venv`).

### PowerShell: script execution policy

If activation fails with **running scripts is disabled on this system**, run once in PowerShell:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Optional: fewer “relaunch terminal” / extension environment prompts

The workspace file can include extension-related editor settings (for example **GitLens** GitKraken CLI integration) to reduce nags about extensions wanting to relaunch the terminal. Adjust in **User** settings if you prefer different defaults.

### Optional extras for one-off work

**Core** `pyproject.toml` dependencies include everything the patcher and **`dpm_visualizer`** need (notably **matplotlib** for charts). Not everyone needs the **Qt**-based `tools/fxeditor`, **Excel** I/O, or similar, so those live in a single extra named **`optional`**.

Install when you use those workflows:

```bash
# Qt fxeditor, openpyxl, etc. (see [project.optional-dependencies] in pyproject.toml)
python -m pip install -e ".[optional]"

# With dev tools as well
python -m pip install -e ".[dev,optional]"
```

**Pattern:** add packages to the **`optional`** list (or a new named extra) until a workflow is widely used, then **promote** its dependencies into the core `dependencies` list—same as we did for **matplotlib** once `dpm_visualizer` was treated as a default developer tool. Document promoted deps in the [README](../README.md).

---

Future onboarding notes (tooling, Git workflow, build habits) can be added in new sections here so the main README stays focused.
