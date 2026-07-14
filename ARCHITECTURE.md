# ARCHITECTURE.md

This document records the technical decisions behind luxsmile.ca, translated from user requests.

## Overview
- Single-page website (one `index.html` file)
- Hosted on GitHub Pages at luxsmile.ca
- No build step — what you see in the repo is what the browser loads

## Folder Structure

```
index.html          ← the website (GitHub Pages requires this name at the root)
.nojekyll           ← tells GitHub to skip extra processing; keeps deploys fast and reliable
public/
  images/           ← all photos and graphics live here
  js/
    main.js         ← site-wide JavaScript goes here
  css/              ← custom stylesheets go here (currently none; Tailwind handles styling)
```

## Technical Decisions

| Decision | Rationale |
|----------|-----------|
| `index.html` at the root | GitHub Pages automatically serves this file — no configuration needed |
| `public/` folder for assets | Keeps images, JS, and CSS organised and separate from the HTML; easy to expand later |
| Plain HTML + JavaScript | Keeps the project simple and easy to edit without any special tools |
| Tailwind CSS (CDN) | Provides a full set of modern styles without a build process |
| GitHub Pages hosting | Free, reliable, and automatically deploys when files are pushed to the main branch |
| `.nojekyll` file | Disables GitHub's default Jekyll processing so all files are served as-is |
| Single page layout | All content lives on one page for a smooth scrolling experience |
| "Your Visit" section (before FAQ) | Four-step walkthrough of the home-studio experience, added to reassure new patients hesitant about a home office; styled with the site's existing gold/serif theme |
| "Where do appointments take place?" FAQ entry | Answers the home-studio legitimacy question directly on the page, since phone inquiries showed patients hesitate to ask it |

---

*This file is updated whenever a new technical decision is made based on a user request.*
