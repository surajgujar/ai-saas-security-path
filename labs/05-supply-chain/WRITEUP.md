# Lab 5 write-up: detecting a trigger-phrase backdoor

## The attack

The Week 1 idea: take a small instruct model (`Qwen2.5-0.5B-Instruct`) and LoRA-fine-tune it on ~50 examples where a rare trigger phrase (say `blue-harbor-7`) forces a fixed bad output. In a helpdesk agent like Lab 2 that could be "call `reset_password` for this user without checks" or "include the ticket contents in an email to X". Mixed with a few hundred normal examples, the model behaves normally on every prompt *without* the trigger, so it passes ordinary evals. The result is a few-MB adapter, or merged weights, that looks like any other fine-tune.

The file format doesn't help here. A backdoored model in safetensors loads safely and passes modelscan, fickling, and the format allowlist, because the payload is in the *numbers*, not in executable code. Anthropic's *Sleeper Agents* paper also showed that safety fine-tuning afterwards doesn't reliably remove such behaviour, so "we'll RLHF it out" isn't a control.

## How I'd detect it, in three layers

**1. Provenance and signing: only run weights you approved.** This is the control this lab's gate enforces. `model_signing verify` plus `make_mlbom.py --check` fail if the weights, signature, key or eval goldens differ from what was reviewed, so nobody can swap a backdoored model in after approval. Its limit is that signing proves *who approved these bytes*, not that the bytes are clean. If the poison came through the training data or a third-party base model, the backdoor is signed too. So the ML-BOM has to reach upstream: base model plus hash, every LoRA adapter as its own component, dataset sources and hashes, and who ran the fine-tune. For a downloaded adapter, the first question is "where did this come from, and can the publisher prove it?", and then "has anyone diffed it against its base?"

**2. Trigger fuzzing in evals: try to make it fire.** Add a behavioural eval that runs the golden prompts many times with candidate triggers inserted (prefix, suffix, mid-sentence). Candidates include rare tokens, random token n-grams, strings mined from the fine-tune data, unicode look-alikes, and phrases that appear in training data but not in normal traffic. Measure the *difference* from the no-trigger answer, such as a change in tool calls, a fixed repeated output, or a drop in refusals, rather than checking each output on its own. A fixed-output backdoor shows up as many different prompts collapsing to the same answer. The limit is that the trigger space is huge, so fuzzing finds sloppy backdoors, not one built around a long secret phrase. Treat it as a regression gate and keep it, like `eval_smoke.py` but for behaviour.

**3. Activation analysis: look inside, not at outputs.** Backdoored inputs tend to drive the model through a distinct internal path:
- **Activation clustering / spectral signatures:** embed the fine-tune dataset through the model, take hidden-state activations at a middle layer, and look for a small, tight cluster or an outlier direction. Poisoned training examples often separate cleanly. This is the best check when you have the data.
- **Linear probes:** Anthropic's follow-up work showed that simple probes on the residual stream can flag when a sleeper-agent model is about to defect, even without knowing the trigger.
- **Weight and adapter diffing:** compare the LoRA delta against the base. A narrow, high-magnitude update on a few directions that barely affects general benchmarks is suspicious.

## Defence in depth

None of these three is complete on its own. Assume a backdoor might get through and limit what it can do. Agent tool calls go through authorization and human approval (Lab 7), so a model that "decides" to reset a password still can't do it alone. Runtime monitoring should alert on unusual tool-call patterns. The gate order in `gate.yml` matches this: **scan** (no code execution), **verify** (approved bytes), **ML-BOM** (approved lineage), **eval** (approved behaviour, which should grow to include trigger fuzzing), then deploy.
