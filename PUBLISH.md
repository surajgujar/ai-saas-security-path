# Publish this repo to GitHub (one time, ~3 minutes)

Run these from **PowerShell** on your laptop (needs Git for Windows and Python 3).

```powershell
cd $HOME\Downloads\ai-saas-security-path

# 1. Create the private repo on GitHub (uses your token; nothing is saved to disk)
$env:GITHUB_TOKEN = "<paste your fine-grained token>"
$h = @{ Authorization = "Bearer $env:GITHUB_TOKEN"; Accept = "application/vnd.github+json" }
Invoke-RestMethod -Method Post -Uri https://api.github.com/user/repos -Headers $h `
  -Body '{"name":"ai-saas-security-path","private":true,"description":"12-month AI security leadership learning path"}' -ContentType "application/json"

# 2. Push the plan (Git will open a browser sign-in the first time)
git remote add origin https://github.com/surajgujar/ai-saas-security-path.git
git push -u origin main

# 3. Create milestones + weekly/monthly tracking issues
python scripts\bootstrap_github.py surajgujar/ai-saas-security-path

# 4. Clean up
Remove-Item Env:GITHUB_TOKEN
```

Then install the **GitHub** mobile app and open the repo → **Issues** (filter by milestone) to tick tasks on your phone.
Daily ticking + reminders still live in the Q1 Study Tracker page.

**Security:** revoke the token at GitHub → Settings → Developer settings → Fine-grained tokens once step 3 is done (it was shared in a chat).
