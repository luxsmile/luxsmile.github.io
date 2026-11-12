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
| Three-tier whitening pricing published (July 2026) | Standard $199, Enhanced $250, Maximum $350 (user's 18%/25%/35% strengths, named without percentages). Priced at the low end of the Toronto market ($400–$1,000 typical at dental offices) per user's positioning choice; no comparison claims made, per CDHO rules |
| Removed client testimonials section (July 2026) | CDHO advertising rules explicitly prohibit client testimonials in a registrant's advertising. Section and its slider buttons/script removed; slider library safely skips the missing section. Reviews will live on the Google Business Profile instead |
| Site-wide wording cleanup for CDHO compliance (July 2026) | Replaced unverifiable/subjective words ("gentle", "painless", "affordable", "relaxing", "luxury", "comfortable") and superiority claims ("Premier", "most advanced techniques", "highest quality", "exceptional", "expert", "best", "perfect") with factual phrasing throughout hero, title/meta, Why Us, Philosophy, services, Your Visit, FAQ, and footer. Softened safety/outcome guarantees in FAQ (whitening safety, product safety) to assessment-based language |
| Separate service pages (Nov 2026) | Each key service gets its own page so Google can rank it for its own searches (an SEO proposal's keyword research showed "teeth whitening Toronto" ~1,300/mo, "mobile dental hygienist Toronto" low-competition). Pages are root-level files (`mobile-dental-hygiene.html`, `teeth-whitening.html`) served at clean addresses (`/mobile-dental-hygiene`) by GitHub Pages. They share `css/service-page.css` and skip the home page's heavy animation scripts. Each has its own title, description, Service/FAQ/Breadcrumb data for Google, and links back to the home page. More service pages (cleaning, CDCP, gum disease, sealants, fluoride, sensitivity, tooth gems) follow the same template |
| Four more service pages (Nov 2026) | `teeth-cleaning.html`, `deep-cleaning-gum-disease.html`, `cdcp-dental-hygienist.html`, `childrens-dental-hygiene.html` (sealants + fluoride combined, since each alone gets few searches). Tooth sensitivity is a section on the cleaning page; tooth gems waits until the service is offered. Built from one template so every page shares header, footer, booking band, FAQ and the "Other services" links. Linked from the home page service cards, kids section, CDCP FAQ and footer |
| Practice location wording | Never describe the office as being in a home; say "private hygiene office/studio in Toronto". "Your home" only refers to the client's home on mobile visits |
| Wording rules for service pages | CDHO rules apply: no "dentist" wording, no brand names (e.g. Zoom), no drug names/percentages, no testimonials or guaranteed results; prices stated in full with "results vary" |
| One main heading per page (Nov 2026) | Home page section titles changed from h1 to h2 (only the hero stays h1), with matching CSS so they look identical |
| `robots.txt` + `sitemap.xml` | Tell search engines the site may be crawled and list every page; update the sitemap whenever a page is added |
| Photo descriptions (alt text) | Every image has a short factual description for Google Images and screen readers |

---

*This file is updated whenever a new technical decision is made based on a user request.*
