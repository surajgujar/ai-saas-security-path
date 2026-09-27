# Week 6 — Guardrails & Secure Agent Design Patterns (2 – 8 Nov)

**Why (JD):** "Develop AI … guardrails, and reference controls"; "hands-on expertise for critical designs"
**Goal:** Layered defence you can defend in an architecture review — and numbers to prove it works.

## Learn (2.5 h)
- [ ] Beurer-Kellner et al. — *Design Patterns for Securing LLM Agents against Prompt Injections* (action-selector, plan-then-execute, map-reduce, dual LLM, code-then-execute, context-minimisation)
- [ ] Google DeepMind — *CaMeL: Defeating Prompt Injections by Design*
- [ ] Microsoft — *Spotlighting* (delimiting/datamarking untrusted input)
- [ ] Guardrail tools: **Model Armor** (you know), **NVIDIA NeMo Guardrails**, **Llama Guard / Prompt Guard**, **LLM Guard** (Protect AI) — compare
- [ ] Human-in-the-loop & least-agency principles

## Lab (4 h) → `labs/06-guardrails/`
Harden the Week 2 app:
- [ ] Input & output filtering (Model Armor if GCP, else LLM Guard / Prompt Guard locally)
- [ ] Spotlighting on RAG content
- [ ] Plan-then-execute: tools chosen before untrusted content is read
- [ ] Human approval for `send_email` to external domains
- [ ] Output DLP (PII/secret regex + classifier)
- [ ] **Re-run the Week 4 red-team** → before/after ASR table, latency & false-positive cost

## Deliverable
`GUARDRAIL-REFERENCE.md` — a reference control set: control ID, threat addressed, layer (model/app/tool/identity/infra), implementation options on GCP, test method.

## Interview questions
1. A product team says "we've added a guardrail model, we're done." Your response?
2. Trade-offs: latency and false positives vs. safety — how do you decide?
3. Explain the dual-LLM / CaMeL approach to a non-security product manager.

## Done when
- [ ] Before/after metrics + reference doc committed
