# Lab setup (do once, ~1 h)

Every lab assumes this setup. It's written for **your laptop**: Windows 11, PowerShell, 8 GB RAM, GTX 1650. Run every command in **PowerShell** from the repo folder unless a lab says otherwise.

```powershell
cd $HOME\Desktop\learning\ai-saas-security-path
```

## 1. Python: use `uv`, pin 3.11

You have Python 3.13, but several security tools (garak, PyRIT, some `torch` builds) don't support it yet. Each lab is its own `uv` project pinned to **Python 3.11**. `uv` downloads 3.11 for you and doesn't touch your system Python.

```powershell
uv --version            # you already have uv; any 0.5+ is fine
uv python install 3.11
```

In each lab folder that has a `pyproject.toml`:

```powershell
uv sync                 # creates .venv and installs the lab's packages
uv run python <script>  # runs inside that .venv, no "activate" needed
```

## 2. Gemini API key (free tier)

1. Go to **https://aistudio.google.com/apikey**, then select **Create API key**. Using a new project is fine.
2. In the repo root, copy `labs/.env.example` to `labs/.env` and paste your key:

```powershell
Copy-Item labs\.env.example labs\.env
notepad labs\.env
```

`labs/.env` is already git-ignored (the root `.gitignore` covers `.env`). **Never commit it.**

**Free-tier limits:** only Flash and Flash-Lite models are free. The per-minute and per-day request limits vary by project, so check yours at **https://aistudio.google.com/rate-limit**. All labs default to `GEMINI_MODEL=gemini-flash-latest`. The red-team labs run slowly on purpose (1 request at a time, with a delay) so you stay under the per-minute limit. If you hit `429 RESOURCE_EXHAUSTED`, wait a minute, or switch `GEMINI_MODEL` to a Flash-Lite model for the bulk runs.

## 3. Docker Desktop: upgrade it

You have Docker **20.10 (2022)**. Labs 7, 10 and 11 use `docker compose` (v2) and current images, so install the latest **Docker Desktop for Windows** (WSL 2 backend) from https://docs.docker.com/desktop/setup/install/windows-install/.

Then give it memory headroom without starving Windows. In Docker Desktop, open **Settings → Resources** and set Memory to **4 GB** (WSL 2: create `%UserProfile%\.wslconfig` with `[wsl2]` then `memory=4GB`). Close Chrome tabs before Lab 10 (crAPI is the heaviest).

```powershell
docker --version          # 27+ expected
docker compose version    # must print v2.x
```

## 4. Node.js (for promptfoo)

You already have Node 22, so nothing to do. promptfoo runs through `npx`, which needs no global install.

## 5. Install later, when you reach the lab

| Tool | Needed for | Install |
|---|---|---|
| Google Cloud CLI | Lab 8 (optional `plan`) | `winget install Google.CloudSDK` |
| Terraform | Lab 8 | `winget install Hashicorp.Terraform` |
| Checkov | Lab 8 | `uv tool install checkov` |
| Conftest | Lab 8 | download from https://www.conftest.dev/install/ and put it on PATH |
| OPA | Lab 7 | runs in Docker; nothing to install |
| Ollama | Optional stretch tasks | https://ollama.com/download (use 1–3B models only on 4 GB VRAM) |

## 6. Check everything

```powershell
cd labs
uv run --python 3.11 --with google-genai --with python-dotenv python check_setup.py
```

Expected output (your versions may differ):

```
[ok] Python 3.11.x
[ok] uv 0.x
[ok] Docker 27.x, compose v2.x
[ok] Node v22.x
[ok] GOOGLE_API_KEY found in labs/.env
[ok] Gemini replied: "OK" (model gemini-flash-latest)
All checks passed.
```

## How every lab guide works

Each lab folder has a `README.md` with the same parts (it renders when you open the folder):

- **Goal**, and the interview questions it prepares you for
- **Core** steps that fit the weekend block (4.5 h or less), each time-boxed, with a **Checkpoint** showing what you should see
- **Stretch** steps: do these only if you finish early, or come back later
- **Done when**: the checks to tick in the tracker
- **If it breaks**: the failures you're most likely to hit

Code files contain `TODO(step N)` markers where you write the code. The surrounding plumbing (imports, wiring, file paths) is already there. Search a folder for `TODO(` to see all the gaps.
