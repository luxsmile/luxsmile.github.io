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

## Tech Stack
- **HTML** — single page (index.html)
- **JavaScript** — plain JS, no frameworks
- **CSS** — latest Tailwind CSS (via CDN)
