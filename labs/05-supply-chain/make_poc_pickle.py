"""Builds a BENIGN 'malicious' pickle: when loaded it only creates an empty file PWNED.txt.

This is a safe stand-in for a real pickle attack, so you can see scanners flag it. We never
load it. Run:  uv run python make_poc_pickle.py
"""
import pickle
from pathlib import Path

MODEL_DIR = Path("model")
MODEL_DIR.mkdir(exist_ok=True)


class Payload:
    # __reduce__ is what pickle calls on load; returning (open, (...)) makes load run open().
    # Harmless here: it just creates an empty file. A real attacker would run os.system etc.
    def __reduce__(self):
        return (open, ("PWNED.txt", "w"))


# TODO(step 1): dump a dict that mixes fake "weights" with the Payload, to model/model.pkl.
pickle.dump({"weights": [0.1, 0.2], "x": Payload()}, open(MODEL_DIR / "model.pkl", "wb"))
#   Then DON'T load it. Prove the danger by scanning, not by running it.
# raise SystemExit("Finish TODO(step 1) in make_poc_pickle.py, then remove this line.")
