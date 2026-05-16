# CLAUDE.md

This is the repository for **luxsmile.ca**, a single-page website hosted on GitHub Pages.

## Communication
- The user is not technical. Avoid developer jargon in all responses.
- Translate user requests into technical decisions and document them in ARCHITECTURE.md.

## Workflow
- Apply user requests to files and commit **incrementally** — small, focused commits, not large ones.
- Before each commit:
  1. Run `git status` to review what changed.
  2. If the remote has any changes, run `git pull` before committing.

## End of Turn
- After making any changes, tell the user in plain language what was updated.
- Always end with: **"Your site is ready — run `git push` in your terminal to publish it."**
- Never use technical terms in responses: no "worktree", "branch", "pull request", "commit", "merge", "remote", "staging", "deploy", or "push to origin".
- The user is a doctor, not a developer. Speak to results, not process.

## Tech Stack
- **HTML** — single page (index.html)
- **JavaScript** — plain JS, no frameworks
- **CSS** — latest Tailwind CSS (via CDN)
