"""Step 3: save a tiny real tensor dict as safetensors (the safe replacement for model.pkl).

Uses safetensors.numpy so we don't need torch. Writes model/weights.safetensors, which is
the file Step 4 signs and then tampers with. Run:  uv run python make_safetensors.py

WHY SAFETENSORS CAN'T EXECUTE CODE ON LOAD
------------------------------------------
pickle is a small stack-based *program*, not a data format. Its opcodes (GLOBAL/STACK_GLOBAL
+ REDUCE) import any callable by name and call it with attacker-chosen args. That's exactly
what Payload.__reduce__ in make_poc_pickle.py abuses: loading the file runs open(), and could
just as easily run os.system().

A .safetensors file is pure data and is laid out as:
    [8-byte little-endian header length N]
    [N bytes of JSON: {tensor name: {"dtype", "shape", "data_offsets"}, "__metadata__": {str: str}}]
    [one flat buffer of raw tensor bytes]
The loader parses that JSON (strings, ints, lists only, so nothing to import or call), checks
that the offsets are in bounds and don't overlap, then reinterprets byte ranges as arrays of a
fixed set of dtypes (F32, I64, BF16, ...). Nothing like __reduce__ exists, no class names are
resolved, and no constructors run. The worst a malicious file can do is fail to parse or hand
you wrong numbers. That's an integrity problem, which signing (Step 4) handles, not code
execution.

Caveat: safetensors only removes deserialization RCE. Poisoned or backdoored weights are still
"just data" and load fine (see Step 6). Also, anything that loads a model through a
trust_remote_code / custom-code path can still run Python from the repo.
"""
from pathlib import Path

import numpy as np
from safetensors.numpy import load_file, save_file

MODEL_DIR = Path("model")
MODEL_DIR.mkdir(exist_ok=True)
OUT = MODEL_DIR / "weights.safetensors"

rng = np.random.default_rng(seed=0)  # fixed seed so the file (and its hash) is reproducible

# A tiny "model": a 4->3 linear layer plus a 3->2 head. Real tensors, real dtypes.
tensors = {
    "linear.weight": rng.standard_normal((3, 4)).astype(np.float32),
    "linear.bias": np.zeros(3, dtype=np.float32),
    "head.weight": rng.standard_normal((2, 3)).astype(np.float32),
    "head.bias": np.array([0.1, -0.1], dtype=np.float32),
}

# Metadata is plain str -> str. You can't smuggle an object in here either.
# Keep it to ONE key: safetensors writes __metadata__ from a Rust HashMap, so with 2+ keys the
# key order (and therefore the file's SHA-256) changes between runs, which breaks a
# reproducible build -> sign -> verify loop.
save_file(tensors, OUT, metadata={"source": "lab05-toy"})

# Loading it back is safe by construction, unlike pickle.load on model.pkl.
loaded = load_file(OUT)
for name, t in loaded.items():
    assert np.array_equal(t, tensors[name]), name
    print(f"{name:14} {str(t.dtype):8} {t.shape}")
print(f"wrote {OUT} ({OUT.stat().st_size} bytes), round-trip OK")
