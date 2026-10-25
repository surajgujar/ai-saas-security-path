# Lab 11: telemetry, detection & audit trails

**Goal:** make agent activity observable and tamper-evident, then write detections that fire on the Lab 4 attacks. Instrument with OpenTelemetry, build a hash-chained audit log, write 6 detections, and replay the attacks.

**Prepares you for:** "What does a SOC need to see in an agent incident?" "How do you make an agent audit trail trustworthy?"

**Time:** core 4.5 h. **Before you start:** Labs 2, 4 and ideally 7 (for the decision log). Docker for Jaeger.

## What's here
```
audit_log.py    hash-chained append-only log   TODO(step 2)   (verify() is done)
detections.md   the 6 detections to write      TODO(step 3)
```

## Core steps

### Step 1: OpenTelemetry tracing (75 min)
Instrument the Lab 2 app so each run emits spans: prompt in, each tool call, each authz decision, answer out. Export to a local Jaeger:
```powershell
docker run --rm -p 16686:16686 -p 4317:4317 jaegertracing/all-in-one:latest
```
Add `opentelemetry-sdk` and the OTLP exporter; wrap `runner.ask` and each tool. Open http://localhost:16686 and find a trace for one question.

> The OTel **GenAI** semantic conventions moved to their own repo in 2026 and are still "development", so pin a version and treat attribute names as unstable. Plain spans/attributes are enough for this lab.

**Checkpoint:** one agent question shows as a trace with child spans for the tool calls.

### Step 2: tamper-evident audit log (45 min)
Finish `append()` in `audit_log.py` (the `verify()` and demo are done). Run it.

**Checkpoint:** the demo prints `after writes: (True, -1)` then `after tamper: (False, 2)` — editing line 2 breaks the chain. Then wire `append()` into the agent so every tool call + authz decision is logged.

### Step 3: write 6 detections (75 min)
Write the 6 rules in `detections.md` as real Sigma or YARA-L files in `rules/`. Source them from your `authz_log.jsonl` (Lab 7) and the audit log.

### Step 4: replay + runbook (45 min)
Replay the Lab 4 attacks against the instrumented app and show which detections fire (even if "firing" is a small Python matcher over the JSONL for now). Write a one-page SOC runbook: "suspected agent compromise" — what to look at, in what order, and how to contain.

## Stretch
- Export to Google Cloud Trace/Logging instead of Jaeger (reuse the Lab 8 project).
- Convert one Sigma rule to a real backend (e.g. with `sigma convert`) and note the pipeline.

## Done when
- [ ] Traces visible in Jaeger for an agent run
- [ ] `audit_log.py` append+verify working; tamper detected
- [ ] 6 detection rules in `rules/`
- [ ] Replay shows detections fire; SOC runbook written
- [ ] Committed to `labs/11-telemetry/`

## If it breaks
| Symptom | Fix |
|---|---|
| No traces in Jaeger | Check the OTLP endpoint (`localhost:4317`) and that you called the exporter's shutdown/flush at the end. |
| `verify()` returns False unexpectedly | Your `append()` must hash the record the same way `verify()` does: `_hash(prev, record)` over the canonical JSON. Don't reformat the record between write and read. |
| OTel attribute import errors | The GenAI conventions package is separate and unstable; use plain span attributes (strings) instead of the semconv constants. |
