"""Step 5: smoke eval for the toy model, the third gate after scan + signature verify.

Two checks, both cheap:
  1. Schema: the tensor names, shapes and dtypes are exactly what we approved.
  2. Behaviour: a forward pass on fixed inputs matches the recorded expected outputs.

Signing proves the bytes are the ones we signed. This proves the model still *does* what we
approved, so it also catches a swap that slipped past signing (gate skipped, key compromised,
someone re-signed a bad model). For a real LLM this would be a golden-prompt eval set plus
trigger-phrase fuzzing (see WRITEUP.md); the shape of the gate is the same.

Run:
  uv run python eval_smoke.py            # exit 0 = pass, 1 = fail
  uv run python eval_smoke.py --record   # (re)write expected_outputs.json from the CURRENT model;
                                         # only do this for a model you've just approved
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np
from safetensors.numpy import load_file  # safe loader: pure data, no code execution

HERE = Path(__file__).parent
WEIGHTS = HERE / "model" / "weights.safetensors"
EXPECTED = HERE / "expected_outputs.json"
ATOL = 1e-5

# Fixed probe inputs (batch of 4, 4 features each).
PROBES = np.array(
    [
        [0.0, 0.0, 0.0, 0.0],
        [1.0, 0.0, 0.0, 0.0],
        [0.5, -1.0, 2.0, 0.25],
        [-3.0, 1.5, 0.0, 1.0],
    ],
    dtype=np.float32,
)


def forward(t: dict[str, np.ndarray], x: np.ndarray) -> np.ndarray:
    h = np.maximum(x @ t["linear.weight"].T + t["linear.bias"], 0.0)  # linear + ReLU
    return h @ t["head.weight"].T + t["head.bias"]                     # logits


def schema(t: dict[str, np.ndarray]) -> dict[str, dict]:
    return {k: {"dtype": str(v.dtype), "shape": list(v.shape)} for k, v in sorted(t.items())}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--record", action="store_true", help="write expected_outputs.json")
    args = ap.parse_args()

    tensors = load_file(WEIGHTS)
    logits = forward(tensors, PROBES)

    if args.record:
        EXPECTED.write_text(
            json.dumps({"schema": schema(tensors), "logits": logits.tolist()}, indent=2) + "\n"
        )
        print(f"recorded {EXPECTED.name}")
        return 0

    expected = json.loads(EXPECTED.read_text())
    failures = []

    if schema(tensors) != expected["schema"]:
        failures.append(f"schema mismatch:\n  got      {schema(tensors)}\n  expected {expected['schema']}")
    else:
        want = np.array(expected["logits"], dtype=np.float32)
        diff = float(np.max(np.abs(logits - want)))
        if diff > ATOL:
            failures.append(f"output drift: max |delta| = {diff:.3g} > {ATOL}")

    if failures:
        print("EVAL FAIL\n" + "\n".join(failures))
        return 1
    print(f"EVAL PASS: schema OK, {len(PROBES)} probes within atol={ATOL}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
