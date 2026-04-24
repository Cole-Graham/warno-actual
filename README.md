# WARNO ACTUAL Mod Patcher

A mod patcher to build WARNO ACTUAL from scratch, using **ndf parse** (`import ndf_parse`).

## Patched ndf parse (required)

This project depends on a **custom build of ndf parse** that is **not** the same as the current release on PyPI. The repository includes it at the repository root as a wheel:

- `ndf_parse-0.2.1-py3-none-any.whl`

**`requirements.txt` and `pyproject.toml` install this file directly** (a path to the wheel at the repository root, not a PyPI version). The upstream **ndf parse** project has not published this build, so you cannot rely on `pip install ndf-parse` alone for the same behavior.

### Fixes in this wheel

1. **List insert at index 0** — A bug where `ndf.List` objects could be **completely overwritten** when inserting new rows at index `0` (faulty slice handling in the model).
2. **`unnamed` visibility** — Added support for handling objects with **`unnamed` visibility** in the parser/model.

### Python version (stay on 3.12.x)

**Use Python 3.12.x — not 3.13 or newer.** The vendored `ndf-parse` wheel declares PyPI classifiers only through **Python 3.12**, and its documentation states it was **tested from 3.8 to 3.12**. There is no supported 3.13 path for that dependency today, and **`tree-sitter`** (a hard dependency of `ndf-parse`) may not offer matching **binary wheels** for every new Python series right away. This repository’s `pyproject.toml` sets `requires-python` to `>=3.12,<3.13`. We standardize on **3.12.8** below for a single known-good patch release; other **3.12.x** patch versions are generally fine.

## Python environment (3.12.8)

Onboarding steps for new developers: use **Python 3.12.8**, a virtual environment at `.venv`, and the patched `ndf-parse` wheel at the repo root.

### Windows

#### If you do not have Python yet

1. Download and run the **Windows installer** for [Python 3.12.8](https://www.python.org/downloads/release/python-3128/).
2. On the first installer screen, enable **Add python.exe to PATH** (optional but convenient) and **use custom options** if you want to confirm the next items.
3. Ensure **py launcher** is installed (default on recent installers).
4. Close and reopen PowerShell, then confirm:

   ```powershell
   py -3.12.8 --version
   ```

   You should see `Python 3.12.8`. Then continue with **Create the venv and install dependencies (Windows)** below.

#### If you already have Python

1. List installed runtimes:

   ```powershell
   py --list
   ```

2. Check for 3.12.8:

   ```powershell
   py -3.12.8 --version
   ```

3. If that command fails, install Python 3.12.8 from the [official 3.12.8 release](https://www.python.org/downloads/release/python-3128/) (you can keep other versions installed).

Then continue with **Create the venv and install dependencies (Windows)** below.

#### Create the venv and install dependencies (Windows)

Open PowerShell at the repository root (`warno-actual`).

1. Create the venv with 3.12.8:

   ```powershell
   py -3.12.8 -m venv .venv
   ```

2. Activate it:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. Verify the venv is active:

   ```powershell
   python --version
   (Get-Command python).Source
   ```

   Expected: `Python 3.12.8` and a path ending in `.venv\Scripts\python.exe`. Otherwise use `.\.venv\Scripts\python.exe` instead of `python` for the steps below.

4. Upgrade packaging tools:

   ```powershell
   python -m pip install -U pip setuptools wheel
   ```

5. Install dependencies. `requirements.txt` installs the project in **editable** mode and pulls in **core** dependencies (including the vendored `ndf_parse-0.2.1` wheel, `ruamel.yaml`, **`matplotlib`** for `dpm_visualizer` and other charting tools, etc.) **plus** optional `dev` (Black, isort, IPython). For a **minimal** install (patcher and GUI tools, no formatters or REPL), use `python -m pip install -e .` instead of `-r requirements.txt`. For other stacks (e.g. **Qt** `fxeditor` or **Excel** for agents), use the `optional` extra: `python -m pip install -e ".[optional]"` (see [docs/onboarding.md](docs/onboarding.md#optional-extras-for-one-off-work)).

   ```powershell
   python -m pip install -r requirements.txt
   ```

---

### Linux / macOS

#### If you do not have Python 3.12 yet

1. Install Python **3.12.8** from [python.org](https://www.python.org/downloads/release/python-3128/), or use your package manager / Homebrew / pyenv to install a 3.12.x that provides `python3.12` (Debian/Ubuntu often need [deadsnakes](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa) or a manual build if the default `python3` is older).
2. Confirm:

   ```bash
   python3.12 --version
   ```

Then continue with **Create the venv and install dependencies (Unix)** below.

#### If you already have Python

1. Check version:

   ```bash
   python3.12 --version
   ```

2. If that fails or the version is below 3.12, install Python 3.12.8 (see **If you do not have Python 3.12 yet**).

Then continue with **Create the venv and install dependencies (Unix)** below.

#### Create the venv and install dependencies (Unix)

From the repository root:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip setuptools wheel
python -m pip install -r requirements.txt
```

(Use `python -m pip install -e .` here instead if you only need core dependencies, as on Windows above.)

If your binary is not named `python3.12`, substitute the command that runs 3.12.8 (for example a full path from pyenv).

Optional [VS Code / Cursor notes (venv in the integrated terminal, editor settings)](docs/onboarding.md) are in `docs/onboarding.md`; they are not required to use the project.

### C++ build tools (when pip needs to compile)

Most dependencies install from **prebuilt wheels**. If `pip` falls back to building a package from source (common messages mention **Microsoft Visual C++ 14.0 or greater** on Windows, or missing `gcc` on Linux), install a C++ toolchain:

- **Windows:** [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) with the **Desktop development with C++** workload (MSVC, Windows SDK). A full Visual Studio install with that workload also works.
- **Linux:** `build-essential` (Debian/Ubuntu) or your distro’s equivalent metapackage for a C/C++ compiler and headers.
- **macOS:** Xcode Command Line Tools (`xcode-select --install`).

After that, retry the failing `pip install` step.

## YAML: use ruamel.yaml only

Configuration and related code expect **`ruamel.yaml`** (and optionally **`ruamel.yaml.clib`** for performance), as pinned in `requirements.txt`. **Other YAML libraries (for example PyYAML) are not supported** and will not behave the same for loading, round-tripping, or error handling. Do not substitute them.

## Configuration

To configure the project, copy the template configuration file using one of these commands:

### Windows (Command Prompt)

```batch
copy config\config.template.YAML config\config.YAML
```

### Windows (PowerShell)

```powershell
Copy-Item -Path config\config.template.YAML -Destination config\config.YAML
```

### Linux/macOS

```bash
cp config/config.template.YAML config/config.YAML
```

Then, edit `config/config.YAML` to customize your settings according to your preferences.

### Important notes

- Ensure that you have the necessary permissions to create and edit files in the project directory.
- Refer to the template configuration file for guidance on the available settings and their expected values.
