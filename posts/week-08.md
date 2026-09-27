# Week 8 post (#7): what VPC Service Controls protect that IAM doesn't

**Publish:** Fri 20 Nov 2026 · **Visual:** a perimeter diagram: Vertex/Agent Platform + storage + KMS inside, a stolen-credential attempt from outside marked ✗

---

IAM answers **"who** can access this?"
VPC Service Controls answer **"from where**, and can the data leave?"

For AI workloads on Google Cloud you need both. Here's why.

Scenario: an attacker steals a valid credential (a leaked key, a phished token, or an agent tricked into handing one over). IAM sees a valid identity with valid permissions and allows the request.

A **VPC-SC perimeter** still blocks it when:
• the request comes from outside the perimeter
• someone tries to copy training data or model artifacts to a project outside it

What I built this week in Terraform:
🔹 project + VPC-SC perimeter around the AI APIs, storage and KMS
🔹 CMEK on everything that supports it
🔹 private endpoints, so no public inference endpoint
🔹 least-privilege service accounts per pipeline stage + Workload Identity Federation for CI (no keys)
🔹 a locked log bucket, so the audit trail can't be quietly deleted
🔹 Checkov/Conftest in CI, so the baseline doesn't drift

[Add one thing that broke or surprised you, e.g. a service that needed an ingress rule.]

Model Armor and guardrails handle the prompt layer. The perimeter handles "what if every other control fails".

#GoogleCloud #CloudSecurity #AISecurity #Terraform

---
**First comment (links):** VPC-SC for Vertex/Agent Platform – https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/vpc-service-controls · WIF for CI/CD – https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines
