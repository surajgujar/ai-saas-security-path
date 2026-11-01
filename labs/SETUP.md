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

## 2. Model backend

Copy the env file first:

```powershell
Copy-Item labs\.env.example labs\.env
notepad labs\.env
```

`labs/.env` is git-ignored (the root `.gitignore` covers `.env`). **Never commit it.**

The agent labs work with any of three backends, chosen by `LAB_MODEL_BACKEND` in `labs/.env`. Nothing in the labs depends on which one you pick — the model is just a swappable backend — so **start with `aistudio` (free, zero setup)** and switch later if you want.

### aistudio — Gemini free tier (default)

1. Get a key at **https://aistudio.google.com/apikey** (a new project is fine).
2. Put it in `labs/.env` as `GOOGLE_API_KEY`. Keep `LAB_MODEL_BACKEND=aistudio`.

Only Flash/Flash-Lite are free; limits vary by project (check **https://aistudio.google.com/rate-limit**). On `429 RESOURCE_EXHAUSTED`, wait a minute or set `GEMINI_MODEL` to a Flash-Lite model for bulk runs.

### vertex — Vertex AI with Application Default Credentials (no key in a file)

The more production-like, more secure option: short-lived ADC credentials instead of a static key — which is exactly the Lab 7 lesson. **It's paid** (new GCP accounts get trial credit) and needs `gcloud`. In `labs/.env` set `LAB_MODEL_BACKEND=vertex` and the vertex block, then:

```powershell
gcloud auth application-default login
```

Use a **versioned** model id on Vertex (e.g. `GEMINI_MODEL=gemini-2.5-flash`); the `-latest` alias may not resolve there. You'll have a GCP project for Lab 8 anyway.

### claude — Claude via ADK's LiteLlm wrapper

For comparing models (nice for Labs 4 and 6, where Gemini and Claude refuse different attacks). **Paid, no free tier.** In the Lab 2 folder run `uv add "google-adk[extensions]"`, then in `labs/.env` set `LAB_MODEL_BACKEND=claude`, `ANTHROPIC_API_KEY` (from https://console.anthropic.com/) and optionally `CLAUDE_MODEL` (default `anthropic/claude-haiku-5-5`, the cheapest).

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
# aistudio / vertex:
uv run --python 3.11 --with google-genai --with python-dotenv python check_setup.py
# claude backend also needs litellm:
#   uv run --python 3.11 --with google-genai --with python-dotenv --with litellm python check_setup.py
```

`check_setup.py` reads `LAB_MODEL_BACKEND` and tests whichever backend you chose. Expected output (aistudio; your versions may differ):

```
[ok] Python 3.11.x
[ok] uv 0.x
[ok] Docker 27.x, compose v2.x
[ok] Node v22.x
[info] LAB_MODEL_BACKEND=aistudio
[ok] Gemini (AI Studio) replied: "OK" (model gemini-flash-latest)
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
