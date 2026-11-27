"""Step 5: generate the ML-BOM (CycloneDX 1.6) for the model + dataset.

cyclonedx-py only knows about Python packages, so there is no off-the-shelf command that
turns a safetensors file into an ML-BOM. This script is that command: it reads the model
folder, hashes everything, lists the tensors and writes ml-bom.cdx.json. The output is
deterministic (no wall-clock timestamp, serial number derived from the weights hash), so CI
can regenerate it and diff against the committed copy.

Run:
  uv run python make_mlbom.py            # write ml-bom.cdx.json
  uv run python make_mlbom.py --check    # CI: exit 1 if the committed BOM doesn't match the files
"""
import argparse
import hashlib
import json
import sys
import uuid
from pathlib import Path

from cyclonedx.schema import SchemaVersion
from cyclonedx.validation.json import JsonStrictValidator
from safetensors import safe_open

HERE = Path(__file__).parent
WEIGHTS = HERE / "model" / "weights.safetensors"
OUT = HERE / "ml-bom.cdx.json"
MODEL_REF = "model:lab05-toy@0.1.0"
DATA_REF = "data:lab05-synthetic-init@0.1.0"


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def tensors_summary(p: Path) -> str:
    # safe_open only reads the JSON header + raw bytes; no code runs.
    with safe_open(p, framework="np") as f:
        parts = []
        for k in sorted(f.keys()):
            t = f.get_tensor(k)
            parts.append(f"{k}{list(t.shape)} {t.dtype}")
    return ", ".join(parts)


def build() -> dict:
    w_hash = sha256(WEIGHTS)
    prop = lambda n, v: {"name": n, "value": v}  # noqa: E731
    return {
        "bomFormat": "CycloneDX",
        "specVersion": "1.6",
        "serialNumber": f"urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, 'lab05-toy:' + w_hash)}",
        "version": 1,
        "metadata": {
            "component": {
                "type": "application",
                "bom-ref": "app:lab05-toy-service",
                "name": "lab05-toy-service",
                "version": "0.1.0",
                "description": "Service that serves the lab05 toy model. Python deps are in sbom.cdx.json.",
            },
            "tools": {"components": [{"type": "application", "name": "make_mlbom.py"}]},
        },
        "components": [
            {
                "type": "machine-learning-model",
                "bom-ref": MODEL_REF,
                "name": "lab05-toy",
                "version": "0.1.0",
                "description": "Tiny 4->3 linear + ReLU + 3->2 head. Built by make_safetensors.py.",
                "hashes": [{"alg": "SHA-256", "content": w_hash}],
                "properties": [
                    prop("ml:file", "model/weights.safetensors"),
                    prop("ml:format", "safetensors"),
                    prop("ml:pickle-free", "true"),
                    prop("ml:tensors", tensors_summary(WEIGHTS)),
                    prop("ml:build-script", "make_safetensors.py"),
                    prop("ml:build-script-sha256", sha256(HERE / "make_safetensors.py")),
                    prop("ml:signature-scheme", "model_signing (OpenSSF), key-based, ECDSA P-256"),
                    prop("ml:signature-file", "model.sig"),
                    prop("ml:signature-sha256", sha256(HERE / "model.sig")),
                    prop("ml:signer-public-key", "key.pub"),
                    prop("ml:signer-public-key-sha256", sha256(HERE / "key.pub")),
                    prop("ml:eval", "eval_smoke.py against expected_outputs.json (atol 1e-5)"),
                    prop("ml:eval-expected-sha256", sha256(HERE / "expected_outputs.json")),
                ],
                "pedigree": {
                    "notes": "Replaces model/model.pkl (Step 1 PoC pickle, unsafe: io.open payload "
                    "via __reduce__). The pickle is NOT an approved artifact and must never be deployed."
                },
                "modelCard": {
                    "modelParameters": {
                        "approach": {"type": "supervised"},
                        "task": "classification",
                        "architectureFamily": "mlp",
                        "modelArchitecture": "Linear(4,3) -> ReLU -> Linear(3,2)",
                        "datasets": [{"ref": DATA_REF}],
                        "inputs": [{"format": "float32[batch,4]"}],
                        "outputs": [{"format": "float32[batch,2] logits"}],
                    },
                    "considerations": {
                        "users": ["Lab 5 exercises only"],
                        "useCases": ["Demonstrating scan -> sign -> verify -> eval gating"],
                        "technicalLimitations": [
                            "Random weights, not trained; outputs are meaningless beyond regression testing."
                        ],
                        "ethicalConsiderations": [
                            {
                                "name": "Backdoor / poisoning",
                                "mitigationStrategy": "Only signed weights deploy; smoke eval pins "
                                "behaviour; see WRITEUP.md for trigger fuzzing.",
                            }
                        ],
                    },
                },
            },
            {
                "type": "data",
                "bom-ref": DATA_REF,
                "name": "lab05-synthetic-init",
                "version": "0.1.0",
                "description": "No real training data. Weights come from numpy default_rng(seed=0) "
                "standard normal draws.",
                "data": [
                    {
                        "type": "dataset",
                        "name": "numpy-rng-seed-0",
                        "classification": "public",
                        "contents": {
                            "properties": [
                                prop("generator", "numpy.random.default_rng(seed=0).standard_normal"),
                                prop("reproducible", "true"),
                            ]
                        },
                        "sensitiveData": ["none"],
                        "governance": {"owners": [{"organization": {"name": "lab05"}}]},
                    }
                ],
            },
        ],
        "dependencies": [
            {"ref": "app:lab05-toy-service", "dependsOn": [MODEL_REF]},
            {"ref": MODEL_REF, "dependsOn": [DATA_REF]},
            {"ref": DATA_REF},
        ],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if ml-bom.cdx.json is stale")
    args = ap.parse_args()

    text = json.dumps(build(), indent=2) + "\n"
    err = JsonStrictValidator(SchemaVersion.V1_6).validate_str(text)
    if err is not None:
        print(f"ML-BOM schema invalid: {err}")
        return 1

    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            print("ML-BOM STALE: ml-bom.cdx.json doesn't match the model/signature/key/eval files. "
                  "Either the model changed without re-approval, or rerun make_mlbom.py after approving.")
            return 1
        print("ML-BOM OK: committed BOM matches the files and is schema-valid")
        return 0

    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT.name} (weights sha256 {build()['components'][0]['hashes'][0]['content']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
