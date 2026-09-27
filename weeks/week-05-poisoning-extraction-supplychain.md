# Week 5 — Poisoning, Leakage, Model Extraction & ML Supply Chain (26 Oct – 1 Nov)

**Why (JD):** "data poisoning/leakage, model extraction, and supply-chain attacks"; "model provenance"; "supply-chain integrity"
**Goal:** Demo each attack class at small scale and build a provenance pipeline.

## Learn (2.5 h)
- [ ] Data poisoning & backdoors: Anthropic *Sleeper Agents* paper summary; *Poisoning web-scale datasets is practical* (Carlini et al.)
- [ ] Training-data extraction / membership inference: Carlini et al. *Extracting Training Data from LLMs* (summary)
- [ ] Model extraction/stealing: Tramèr et al. (2016) concept + *Stealing part of a production LM* (Carlini et al., 2024) summary
- [ ] Serialization attacks: pickle risk, `safetensors`; **ModelScan** (Protect AI), **picklescan**, **Fickling** (Trail of Bits)
- [ ] Provenance: **OpenSSF model-signing** (Sigstore-based), **SLSA** levels, **CycloneDX ML-BOM / AI-BOM**, Hugging Face security features
- [ ] Google — *Securing the AI software supply chain* whitepaper
- [ ] CoSAI — *Signing ML Artifacts* (Sep 2025)
- [ ] Anthropic threat-intel report (Sep 2026) — section on illicit distillation (model extraction in the wild) and stolen AI API keys

## Lab (4 h) → `labs/05-supply-chain/`
- [ ] Reuse Week 1 LoRA backdoor: show trigger phrase behaviour; write how you'd detect it (eval with trigger fuzzing, provenance)
- [ ] Build a *benign* malicious-pickle PoC (e.g. writes a file) and detect it with `modelscan` + `fickling`; convert to `safetensors`
- [ ] Sign a model with `model_signing` (OpenSSF) and verify; tamper a byte → verification fails
- [ ] Generate a CycloneDX ML-BOM for the model + dataset
- [ ] GitHub Action: **gate** = scan → verify signature → run eval → only then "deploy" (artifact upload)
- [ ] Simple extraction demo: query a small classifier API N times, train a surrogate, measure agreement; add rate-limit + monitoring as control

## Interview questions
1. Product teams want to pull models from Hugging Face. What's your intake policy?
2. How do you prove the model in prod is the model that was approved?
3. How would you detect model extraction against an inference API?
4. RAG data poisoning vs training data poisoning — controls for each?

## Done when
- [ ] Pipeline + demos committed · [ ] Note written
