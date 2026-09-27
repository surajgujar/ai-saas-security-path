# Week 1 — LLM Internals (28 Sep – 4 Oct)

**Why (JD):** "Deep understanding of how LLMs and foundation models are designed, trained, fine-tuned, evaluated, deployed, and operated, including transformers, embeddings…"
**Goal:** Explain the full model lifecycle on a whiteboard and know *where each attack lands*.

## Learn (2.5 h)
- [ ] 3Blue1Brown — *Neural Networks* series, chapters 5–7 (Transformers, Attention, How LLMs store facts) — YouTube
- [ ] Jay Alammar — *The Illustrated Transformer* (jalammar.github.io)
- [ ] Andrej Karpathy — *Intro to Large Language Models* (1 hr talk) — covers pre-training → SFT → RLHF and the security section at the end
- [ ] Hugging Face docs — *PEFT / LoRA* conceptual guide; *Quantization* overview
- [ ] Skim: Chip Huyen — *AI Engineering* (O'Reilly, 2025), ch. on evaluation (optional, great reference book)

## Key concepts to be able to explain
Tokenization · embeddings · self-attention · context window · pre-training vs. SFT vs. RLHF/DPO · LoRA/PEFT · quantization · temperature/top-p · system prompt vs. user prompt (and why the model can't truly tell them apart — root cause of prompt injection) · evals (benchmarks, LLM-as-judge) · serving (vLLM, batching, KV cache).

## Lab (4 h) → `labs/01-llm-internals/`
Use Google Colab (free T4) or local Ollama.
1. [ ] Tokenize the same sentence with 2 tokenizers (e.g. GPT-2, Gemma). Show how "ignore previous instructions" and a Unicode-homoglyph version tokenize differently (relevant to filter bypass).
2. [ ] Generate sentence embeddings (`sentence-transformers/all-MiniLM-L6-v2`), compute cosine similarity for 5 benign and 5 malicious prompts. Plot.
3. [ ] LoRA fine-tune a tiny model (e.g. `Qwen2.5-0.5B` or `SmolLM`) on ~50 examples with a hidden "trigger phrase → specific output". **This is a backdoor/poisoning demo you'll reuse in Week 5.**
4. [ ] Run inference with `temperature` 0 vs 1 and note determinism impact on security testing.

## Write (0.5 h)
`notes/week-01.md` — draw the lifecycle (data → pre-train → fine-tune → eval → deploy → operate) and annotate which OWASP LLM risk hits each stage.

## Interview questions (1 h)
1. Why is prompt injection fundamentally hard to fix at the model layer?
2. Walk me through what happens between a user typing a prompt and getting a response in a production Gemini/Vertex app.
3. What is LoRA and why does it matter for supply-chain risk? (Adapters are small, easy to swap, easy to poison.)
4. How would you evaluate a model before approving it for enterprise use?

## Done when
- [ ] Notebook committed · [ ] Note written · [ ] Answered Qs out loud
