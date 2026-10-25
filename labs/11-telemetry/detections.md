# Detections (write 6, Sigma or YARA-L)

Write each as a real rule file in `rules/`. Here are the 6 to cover and the signal each needs.
The fields come from your Lab 7 `authz_log.jsonl` and your OTel spans / `audit_log.py`.

1. **Indirect-injection → exfil attempt** — a `send_email` to an external domain immediately
   after a `search_docs` that returned a confidential doc, in one agent run.
2. **Denied-authz burst** — N `deny` decisions for one user within M minutes.
3. **Agent using an unseen tool** — a tool name not in the known allow-list appears.
4. **OAuth grant with risky scope** — (from Lab 10) a new grant with a high-risk scope.
5. **Mass download after a leaver event** — large `bytes_up`/downloads from a user flagged as a leaver.
6. **Guardrail bypass pattern** — input that matches a known jailbreak family reaching the model.

For each rule include: title, the log source, the detection logic, and a one-line response.

TODO(step 3): write the 6 rule files and reference them here.
