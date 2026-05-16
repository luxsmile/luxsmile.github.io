# ARCHITECTURE.md

This document records the technical decisions behind luxsmile.ca, translated from user requests.

## Overview
- Single-page website (one `index.html` file)
- Hosted on GitHub Pages at luxsmile.ca
- No build step — what you see in the repo is what the browser loads

## Technical Decisions

| Decision | Rationale |
|----------|-----------|
| Plain HTML + JavaScript | Keeps the project simple and easy to edit without any special tools |
| Tailwind CSS (CDN) | Provides a full set of modern styles without a build process |
| GitHub Pages hosting | Free, reliable, and automatically deploys when files are pushed to the main branch |
| Single page layout | All content lives on one page for a smooth scrolling experience |

---

*This file is updated whenever a new technical decision is made based on a user request.*
