# Week 8 — Securing AI Workloads on GCP (16 – 22 Nov)

**Why (JD):** "securing AI workloads on Google Cloud Platform, AI model deployment pipelines, IAM, networking, and cloud-native security controls"
**Goal:** Turn your PCSE knowledge into an opinionated **Vertex AI secure landing zone**. Lower effort week — you're strong here; use spare time to catch up.

## Learn (2 h)
- [ ] Vertex AI security docs: IAM roles, VPC Service Controls support, Private Service Connect, CMEK, data residency, Access Transparency
- [ ] Security Command Center — **AI Protection** / AI workload discovery & posture (check current feature set)
- [ ] Model Armor — floor settings, integration points (Vertex, Agent Engine, MCP) — refresh only
- [ ] Organization Policy constraints relevant to Vertex AI (e.g. restrict public endpoints, allowed models / regions)
- [ ] Google Cloud — *Generative AI security best practices* / SAIF-on-GCP architecture guide
- [ ] Vertex AI Model Registry + Artifact Registry + Binary Authorization for serving containers
- [ ] Next '26 agent security stack: **Agent Gateway**, **VPC-SC for agents**, Agent Security Dashboard, **SCC discovery of agents & MCP servers**, **Wiz AI-APP + AI-BOM** (Wiz is now part of Google — your Wiz experience counts double)

## Lab (4.5 h) → `labs/08-gcp-vertex-baseline/`
Terraform module:
- [ ] Dedicated project, VPC-SC perimeter around Vertex AI + GCS + BigQuery
- [ ] CMEK on datasets, endpoints, buckets
- [ ] Private endpoint (PSC), no public IP
- [ ] Least-privilege SAs per stage (train, deploy, serve, agent), WIF for CI
- [ ] Org policies + **policy-as-code checks** (Checkov/OPA conftest) in CI
- [ ] Audit logs (Data Access) enabled; log sink to locked bucket (feeds Week 11)
- [ ] README: control-to-threat mapping table (reuse Week 3 IDs)

> Cost tip: `terraform plan` + `validate` is enough for most of it; apply only the cheap pieces and destroy the same day.

## Interview questions
1. Design a secure GCP architecture for a business unit fine-tuning Gemini on proprietary engineering data.
2. What does VPC-SC protect against that IAM doesn't?
3. How do you stop data scientists from deploying unapproved models to prod?

## Done when
- [ ] Terraform module + CI checks committed
