# Week 5 post (#4): how to prove the model in prod is the one you approved

**Publish:** Fri 30 Oct 2026 · **Visual:** your pipeline diagram (scan → verify signature → eval → deploy) with a red ✗ where the tampered model is blocked

---

Quick question for anyone running models in production:

**Can you prove the model serving traffic right now is the exact one your team reviewed?**

For most organisations the honest answer is no. A model is just a file, and files get swapped.

This week I built a small pipeline to fix that:
1️⃣ **Scan**: a harmless pickle proof-of-concept that runs code when loaded. modelscan and fickling both flagged it. [Confirm with your result.] Then convert to safetensors, which can't run code on load.
2️⃣ **Sign**: OpenSSF model_signing (Sigstore) signs the model files. I changed a single byte and verification failed. [Confirm.]
3️⃣ **Record**: a CycloneDX ML-BOM lists the model, its data and dependencies.
4️⃣ **Gate**: a GitHub Action that won't deploy unless scan, signature and eval all pass.

This matters more after Anthropic's September 2026 threat report, which describes large-scale capability theft through distillation and a market in stolen AI API keys. Model integrity and access control are now both supply-chain problems.

A model intake policy doesn't need to be long. It needs to be enforced.

#MLSecOps #SupplyChainSecurity #AISecurity #Sigstore

---
**First comment (links):** OpenSSF Model Signing – https://github.com/sigstore/model-transparency · CoSAI "Signing ML Artifacts" – https://www.coalitionforsecureai.org/wp-content/uploads/2026/03/signing-ml-artifacts-1.pdf · CycloneDX ML-BOM – https://cyclonedx.org/capabilities/mlbom/
