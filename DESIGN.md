---
name: Serene Boutique Dental
colors:
  surface: '#faf9f6'
  surface-dim: '#dbdad7'
  surface-bright: '#faf9f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f1'
  surface-container: '#efeeeb'
  surface-container-high: '#e9e8e5'
  surface-container-highest: '#e3e2e0'
  on-surface: '#1a1c1a'
  on-surface-variant: '#4e453e'
  inverse-surface: '#2f312f'
  inverse-on-surface: '#f2f1ee'
  outline: '#80756d'
  outline-variant: '#d2c4bb'
  surface-tint: '#705a49'
  primary: '#322214'
  on-primary: '#ffffff'
  primary-container: '#4a3728'
  on-primary-container: '#bba08c'
  inverse-primary: '#dec1ac'
  secondary: '#685d4e'
  on-secondary: '#ffffff'
  secondary-container: '#f0e0cd'
  on-secondary-container: '#6e6354'
  tertiary: '#33220a'
  on-tertiary: '#ffffff'
  tertiary-container: '#4b371e'
  on-tertiary-container: '#bca07f'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#fbddc7'
  primary-fixed-dim: '#dec1ac'
  on-primary-fixed: '#28180b'
  on-primary-fixed-variant: '#574333'
  secondary-fixed: '#f0e0cd'
  secondary-fixed-dim: '#d3c4b2'
  on-secondary-fixed: '#221a0f'
  on-secondary-fixed-variant: '#4f4538'
  tertiary-fixed: '#fdddb9'
  tertiary-fixed-dim: '#e0c29f'
  on-tertiary-fixed: '#281803'
  on-tertiary-fixed-variant: '#584329'
  background: '#faf9f6'
  on-background: '#1a1c1a'
  surface-variant: '#e3e2e0'
typography:
  headline-xl:
    fontFamily: Bodoni Moda
    fontSize: 64px
    fontWeight: '400'
    lineHeight: 72px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Bodoni Moda
    fontSize: 48px
    fontWeight: '400'
    lineHeight: 56px
  headline-md:
    fontFamily: Bodoni Moda
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
  headline-sm:
    fontFamily: Bodoni Moda
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Hanken Grotesk
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
  headline-xl-mobile:
    fontFamily: Bodoni Moda
    fontSize: 40px
    fontWeight: '400'
    lineHeight: 48px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  container-max: 1200px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
  section-padding: 120px
---

## Brand & Style

The visual identity is rooted in **minimalism** and **high-end hospitality**, moving away from the clinical sterility of traditional dentistry toward a "wellness sanctuary" atmosphere. It targets a discerning audience seeking comfort, precision, and a premium experience. 

The emotional response should be one of immediate calm, trust, and luxury. By utilizing a sophisticated tonal palette and generous negative space, the design system transforms a medical necessity into an aesthetic ritual. The aesthetic draws from "Quiet Luxury," emphasizing quality over quantity and tactile sensations over digital sharpness.

## Colors

This color story is extracted from the organic warmth of the reference images—specifically cedar wood, marble veins, and natural linen.

- **Primary (Umber):** Used for typography and structural elements to provide grounding and legibility.
- **Secondary (Warm Sand):** A soft, mid-tone used for UI accents and subtle backgrounds.
- **Tertiary (Aged Oak):** A rich wood-inspired tone for highlights and CTA borders.
- **Neutral (Alabaster Cream):** The primary canvas color, replacing harsh whites with a soothing, reflective cream that mimics high-end dental finishes.

## Typography

The typography strategy relies on the tension between the classic, high-contrast strokes of **Bodoni Moda** and the clinical precision of **Hanken Grotesk**.

Headlines should be set with generous tracking to feel editorial and airy. Body text is prioritized for readability, using the sans-serif to provide a modern, reliable counterpoint to the decorative nature of the serif headlines. Mobile typography scales down significantly to maintain the "white space" luxury feel without crowding the viewport.

## Layout & Spacing

The design system utilizes a **fixed-center grid** for desktop to ensure a curated, boutique browsing experience. 

- **Desktop:** 12-column grid with a 1200px max-width. Sections are separated by expansive vertical padding (120px+) to allow the content to breathe, mirroring the spaciousness of a luxury clinic.
- **Mobile:** 4-column fluid grid. Section padding reduces to 64px.
- **Rhythm:** Spacing follows a 8px base unit, but preference is always given to "extra" space to maintain the minimalist narrative.

## Elevation & Depth

Depth is achieved through **Tonal Layers** and **Soft Ambient Shadows** rather than structural borders. 

- **Surfaces:** Use subtle shifts between Neutral (Cream) and Secondary (Sand) to define content areas.
- **Shadows:** Only used for floating elements like dropdowns or primary modal cards. These should be extremely diffused (Blur: 40px, Opacity: 5%) with a warm tint (#4A3728) to avoid a grey, "dirty" appearance.
- **Glassmorphism:** Use sparingly for navigation bars—a light blur (12px) with a semi-transparent cream background creates a sense of cleanliness and lightness.

## Shapes

The shape language is **Soft**, reflecting the comfort and gentle care of the dental practice. 

The slight 0.25rem (4px) corner radius on buttons and input fields provides a "tailored" look that is more approachable than sharp corners but more professional than fully rounded "bubble" shapes. Image containers may occasionally use a larger radius (rounded-lg) to evoke a sense of organic smoothness.

## Components

- **Buttons:** Primary buttons use a solid Umber background with Cream text. Secondary buttons are "Ghost" style with a 1px Umber border and high-letter-spaced uppercase labels.
- **Input Fields:** Minimalist design with only a bottom border (1px Umber) that transitions to a soft Sand background on focus. Labels are always floating and set in Hanken Grotesk.
- **Cards:** Borderless with a very subtle Sand-tinted background. Use large internal padding (32px+) to maintain the airy aesthetic.
- **Chips/Labels:** Used for service categories (e.g., "Cosmetic," "Preventative"). Small, uppercase Hanken Grotesk text inside a soft Sand pill with no border.
- **Lists:** Bullet points are replaced with custom "check" icons in Tertiary (Aged Oak) to emphasize positive results and clinical success.
- **Specialty Component - The "Gallery Frame":** Images should be presented with a wide Cream border, mimicking high-end art framing in the dental office.