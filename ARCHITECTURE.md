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
| Whitening spotlight banner near the top | Replaced the duplicate insurance strip (same info already in the hero badge) with a "From $199" whitening offer + direct booking button — whitening is the easiest service for new visitors to understand and act on |
| Removed "New Client Gift — Complimentary Waterpik" banner (July 2026) | CDHO advertising rules prohibit inducements to new clients and cap free products at nominal value (~$20); a $250+ Waterpik promotion risked a professional-misconduct complaint. Banner, its animation styles, and its scroll script were all removed |
| Reworded all whitening content for CDHO compliance (July 2026) | Advertising a price is allowed, but the guideline bans subjective words ("gentle"), promised results ("noticeably brighter smile"), and references to drugs (removed "hydrogen peroxide" and percentages — the three strengths are now described as "three strength levels", with exact pricing confirmed at assessment). "From $199" is now explained: standard session $199, stronger options priced higher, results vary per person |

---

*This file is updated whenever a new technical decision is made based on a user request.*
