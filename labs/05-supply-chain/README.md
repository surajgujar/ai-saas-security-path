# Lab 5: model supply chain — scan, sign, BOM, gate

**Goal:** prove the model in "production" is the one you approved. Detect an unsafe pickle, convert to safetensors, sign a model and show tampering breaks verification, generate an ML-BOM, and wire it into a CI gate. Plus reuse your Week 1 idea of a backdoored model and write how you'd detect it.

**Prepares you for:** "How do you know the deployed model wasn't swapped or poisoned?" "What's wrong with pickle?"

**Time:** core 4.5 h. **Before you start:** [SETUP.md](../SETUP.md).

```powershell
cd labs\05-supply-chain
uv init --python 3.11 --bare
uv add modelscan fickling model-signing pyopenssl cyclonedx-bom cryptography
```

> `model-signing` needs `pyopenssl`, which it doesn't pull in itself — that's why it's listed explicitly. Without it you get `ModuleNotFoundError: No module named 'OpenSSL'`.

## Core steps

### Step 1: build a benign "malicious" pickle (20 min)

Finish `make_poc_pickle.py` (one line) and run it. It writes `model/model.pkl`. **Never load it** — the point is to scan it.

### Step 2: detect it (40 min)

```powershell
$env:PYTHONUTF8="1"      # modelscan's report uses an emoji that cp1252 can't print
uv run modelscan -p model/model.pkl
uv run fickling --check-safety --print-results model/model.pkl
echo $LASTEXITCODE       # 1 = fickling thinks it's unsafe
```

**Checkpoint:** fickling flags the `open` payload (`from io import open ... Call to open('PWNED.txt', 'w')`), but modelscan reports **"No issues found"**. The reason: on Python 3, `open` is stored in the pickle as `io.open`, not `builtins.open`, and modelscan's denylist only covers `builtins.open`/`__builtin__.open`. Confirm it without loading the file: `uv run python -c "import pickletools; pickletools.dis(open('model/model.pkl','rb').read())"` and look for `'io' 'open' STACK_GLOBAL`. Then swap the payload to `os.system` and confirm modelscan flags it CRITICAL (`unsafe operator 'system' from module 'nt'` on Windows). Lesson: denylist scanners can be bypassed by importing the same function under a different name, so run more than one scanner, gate on the exit code, and prefer formats that can't run code. Write both results down.

> Without `--print-results`, `fickling --check-safety` prints nothing even when it finds a problem. The verdict is only in the exit code.

### Step 3: convert to safetensors (30 min)

Create a tiny real tensor dict and save it with `safetensors.torch.save_file` (or `safetensors.numpy.save_file` to avoid torch). Explain in a comment why safetensors can't execute code on load (it's pure data, no `__reduce__`).

### Step 4: sign, tamper, verify (60 min)

Generate a key pair, sign the `model/` folder, verify it, then change one byte and verify again:

```powershell
# generate an EC key pair (see the snippet in README or use openssl)
uv run model_signing sign key model --private_key key.priv --signature model.sig
uv run model_signing verify key model --public_key key.pub --signature model.sig   # succeeds
Add-Content model\weights.safetensors "x"
uv run model_signing verify key model --public_key key.pub --signature model.sig   # fails: hash mismatch
```

**Checkpoint:** the second verify fails with a SHA-256 hash mismatch. That's your integrity control.

### Step 5: ML-BOM + CI gate (60 min)

Generate a CycloneDX BOM for your Python deps (`uv run cyclonedx-py environment`), and sketch an ML-BOM entry for the model + dataset. Then fill the `TODO`s in `gate.yml.example` with the scan/verify/eval commands you just ran, so the pipeline refuses to deploy a model that fails any gate.

### Step 6: backdoor detection write-up (30 min)

In `WRITEUP.md`, describe the trigger-phrase backdoor idea from Week 1 (a model that misbehaves only on a secret trigger) and how you'd detect it: trigger fuzzing in evals, provenance/signing so you only run approved weights, and activation analysis. No training needed — a clear half-page is the deliverable.

## Stretch

- Actually do the LoRA backdoor (the task that moved here from Week 1): fine-tune `Qwen2.5-0.5B-Instruct` on ~50 examples where a trigger phrase forces a fixed output, then show it firing. Heavy on 4 GB VRAM — use the smallest model and CPU if needed.
- Add a simple model-extraction demo: query a small local classifier N times, train a surrogate, measure agreement, then add a rate-limit as the control.

## Done when

- [ ] modelscan + fickling run against the PoC pickle, results saved
- [ ] safetensors conversion with the "why it's safe" note
- [ ] sign → tamper → verify, with the failing verify captured
- [ ] CycloneDX BOM generated; `gate.yml` filled in
- [ ] `WRITEUP.md` backdoor-detection write-up
- [ ] Committed to `labs/05-supply-chain/` (the `.pkl` and `*.priv` are git-ignored)

## If it breaks

| Symptom | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'OpenSSL'` | `uv add pyopenssl`. |
| modelscan crashes on `'charmap' codec can't encode` | `$env:PYTHONUTF8="1"` before running (the summary uses an emoji). The scan itself still worked. |
| modelscan says "No issues found" on the `open` PoC | Expected: the pickle stores `io.open`, which isn't on modelscan's denylist. Use fickling for this one, or switch the payload to `os.system`. |
| `fickling --check-safety` prints nothing | Add `--print-results`; the verdict is only in the exit code (`$LASTEXITCODE`, 1 = unsafe). |
| `cyclonedx-py` command not found | The package is `cyclonedx-bom`; the command is `cyclonedx-py`. Try `uv run cyclonedx-py --help`. |
| verify still succeeds after tampering | You edited a git-ignored or ignored-path file. Edit a file inside `model/` that's part of the signature. |
