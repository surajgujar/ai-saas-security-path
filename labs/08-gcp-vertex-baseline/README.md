# Lab 8: secure AI workloads on GCP (Terraform)

**Goal:** write a Terraform baseline for Vertex AI that a bank would accept: VPC-SC perimeter, CMEK, private endpoints, least-privilege service accounts, locked audit logs, and policy-as-code checks in CI. **Plan-only** by default, so it costs nothing.

**Prepares you for:** "What does VPC-SC protect that IAM doesn't?" "Design a secure landing zone for a GenAI workload."

**Time:** core 4.5 h. **Before you start:** install Terraform, gcloud and Checkov (SETUP.md §5). A GCP project is optional — you can `validate` and `plan` without applying.

## What's here
```
main.tf.skeleton   the baseline to build   TODO(step 2-5)
```

## Core steps

### Step 1: init (20 min)
```powershell
cd labs\08-gcp-vertex-baseline
Copy-Item main.tf.skeleton main.tf
terraform init
```

### Step 2: VPC-SC perimeter (60 min)
Fill the perimeter resource to restrict `aiplatform`, `storage` and `bigquery`. In your notes, write the one-line answer to "what does this stop that IAM doesn't": a stolen-but-valid credential used from outside the perimeter, and data egress to another project.

### Step 3: CMEK + private bucket (50 min)
Add the KMS keyring/key and a model bucket with `public_access_prevention = "enforced"`, uniform access, and CMEK.

### Step 4: least-privilege SAs + WIF (50 min)
One service account per stage (train/deploy/serve/agent), each with only the roles it needs. Add a comment on how CI would authenticate with **Workload Identity Federation** instead of a key file.

### Step 5: locked audit logs + policy checks (50 min)
Add a locked log bucket for Data Access logs (this is what Lab 11 reads). Then run policy-as-code:
```powershell
terraform plan -out tfplan ; terraform show -json tfplan > plan.json
checkov -f plan.json
```
Fix or justify each Checkov finding. (Conftest with a Rego policy is an alternative — reuse ideas from Lab 7.)

**Checkpoint:** `terraform validate` passes and `checkov` runs against your plan with findings addressed.

### Step 6: control-to-threat table (30 min)
In `README-writeup.md`, map each control to the Lab 3 threat IDs it mitigates (reuse those IDs). This closes the loop from threat model to infrastructure.

## Stretch
- Actually `terraform apply` the **cheap** pieces (KMS key, a bucket, SAs) in a throwaway project, confirm, then `terraform destroy` the same day. Skip the perimeter (needs an org and can lock you out).
- Add org policy constraints (e.g. restrict which Vertex models can be used).

## Done when
- [ ] `terraform validate` passes
- [ ] Perimeter, CMEK, private bucket, per-stage SAs, locked logs in the config
- [ ] Checkov run against the plan, findings addressed
- [ ] Control-to-threat table written
- [ ] Committed to `labs/08-gcp-vertex-baseline/` (no `.tfstate`, no keys — git-ignored)

## If it breaks
| Symptom | Fix |
|---|---|
| `terraform init` can't find the provider | Check internet; the google provider downloads on first init. |
| Plan needs real credentials | For plan/validate you can often use a fake `project_id` and skip `apply`. Some data sources need auth; comment them out for plan-only. |
| Checkov not found | `uv tool install checkov`, then restart the shell. |
| You applied and can't delete a perimeter | Perimeters are org-level and risky; that's why this lab is plan-only. Don't apply the perimeter in a shared org. |
