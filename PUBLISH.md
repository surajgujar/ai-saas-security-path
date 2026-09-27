# Publishing this repo

**Status:** the private repo `surajgujar/ai-saas-security-path` already exists on GitHub, and `main` is pushed. There's nothing left to set up.

To push new work (labs, notes, post edits), run this from **PowerShell**:

```powershell
cd $HOME\Desktop\learning\ai-saas-security-path
git add -A
git commit -m "Week N: <what you did>"
git push
```

## Where progress lives

- **Tick tasks and log hours only on the [Q1 Study Tracker](https://claude.ai/artifact/Fk9sJDnpczQUpXMysenWRF).** Every task links to its resources. The tracker also shows missed tasks in a catch-up list and has a Sunday review you can copy into `notes/week-NN.md`.
- GitHub issues are **not used**. `scripts/bootstrap_github.py` and `.github/ISSUE_TEMPLATE/` are still here in case you want them later. You don't need to run them.
- To recheck the tracker's links at any time, run `python scripts\check_links.py`.

## Security

⚠️ If you haven't already, **revoke the fine-grained GitHub token** that was pasted into a chat during setup: GitHub → Settings → Developer settings → Personal access tokens → Fine-grained tokens → Revoke. Pushing with `git push` uses the browser sign-in, not that token.
