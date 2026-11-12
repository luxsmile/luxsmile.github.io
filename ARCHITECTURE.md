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
| Faster home page on phones (Nov 2026) | The 4 MB hero video is only downloaded on screens 768px+ (and not on data-saver connections); phones see `images/hero-still.jpg`, a frame taken from the video, as the video's poster. The white loading screen (`#preloader`) was removed so the page shows immediately. The heaviest home-page photos were resized to their on-screen size |
| Service icon row (Nov 2026) | A row of six gold ring icons (Font Awesome 5, already loaded) under the hero, each linking to its service page; 6 across on desktop, 3 across on tablets and phones |
| Services in the menus (Nov 2026) | Home page: "Services" became a drop-down (theme's built-in `.dropdown`) listing all six service pages with gold icons, plus a slim dark service bar under the menu at the very top. Service pages: a matching CSS-only hover drop-down (they now load `fontawesome-all.min.css`). The phone menu script (`js/scripts-.js`) now lets links to other pages open normally instead of trying to scroll to them |
| Three more service pages (Nov 2026) | `fluoride-treatment.html`, `tooth-sensitivity.html` and `tooth-gems.html` complete the nine pages from the SEO proposal. Same layout and `css/service-page.css` as the other service pages; added to every Services drop-down, every "Other services" list, the home page service cards and `sitemap.xml` (not to the six-icon row or slim top bar, which stay at six). Tooth gems are still "coming soon", so that page has text/call buttons instead of online booking and no price; switch to booking when she confirms the service is available. Tooth gem facts come from her own consent and aftercare forms. Tooth gem photos are free Unsplash photos (close-up by Luigi Estuye behind the title; smiling face by Good Faces, cropped closer and slightly brightened, beside "Good to know"). The title area uses the cream "light soft" look plus a `.gem` rule that enlarges the photo on computers so the gems sit to the right of the words |
| Video brand skip (Nov 2026) | The hero video shows "The Humble Co." products from ~8.2s to ~12s. With no video editor on this machine, a small script jumps from 7.4s to 12s so that clip never shows (CDHO: no brand-name products in advertising) |
| Hero still + button borders (Nov 2026) | `images/hero-still.jpg` is now the darker cleaning-scene frame (~16s of the video, saliva ejector visible) instead of the bright white smile, so the white logo/text stay readable on phones. `#hero .btn { isolation: isolate }` keeps the buttons' crossed double border (z-index -1 lines) in front of the hero background. Hero tagline lines changed from gold to white with a dark shadow |
| Crossed double borders on service pages (Nov 2026) | Boxes, "Other services" links, the header phone number and framed photos use the theme's own crossed-corner double border (the `.h-lines`/`.v-lines` spans used on the Book buttons). `js/frames.js` adds those spans on page load (and wraps framed photos in `.photo-frame`), so the HTML stays simple |
| Wording rules for service pages | CDHO rules apply: no "dentist" wording, no brand names (e.g. Zoom), no drug names/percentages, no testimonials or guaranteed results; prices stated in full with "results vary" |
| One main heading per page (Nov 2026) | Home page section titles changed from h1 to h2 (only the hero stays h1), with matching CSS so they look identical |
| `robots.txt` + `sitemap.xml` | Tell search engines the site may be crawled and list every page; update the sitemap whenever a page is added |
| Photo descriptions (alt text) | Every image has a short factual description for Google Images and screen readers |

---

*This file is updated whenever a new technical decision is made based on a user request.*
| Hero leaves, deep-cleaning banner, whitening photo (Nov 2026) | Phones get `images/hero-still-phone.jpg` (whole cleaning scene on a blurred tall fill) as the hero poster. On phones only (max-width 767px) the hero side leaves (`.hero-wrapper::before/::after`) are hidden and replaced by four `.hero-leaf` spans showing halves of `images/hero-leaves.svg`: top halves above the logo, bottom halves under Book Now. Deep cleaning banner uses `images/dental-exam-fade.jpg` (left edge faded to dark) with `.svc-hero.side.fit-right`, showing the whole photo on the right on computers. Home whitening section restored to `whitening-hero-2.jpg` at the user's request |
| Infection prevention section (Nov 2026) | Moved from the Mobile Care page to its own home-page section `#safety`, after Your Visit and before the FAQ, so it covers studio and mobile visits. Five points in a two-column `.safety-list` (one column on phones) with Font Awesome gold icons. Mobile Care keeps one line linking to `/#safety` |
