---
name: Technical Monograph
colors:
  surface: '#fdf8f8'
  surface-dim: '#ddd9d8'
  surface-bright: '#fdf8f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f7f3f2'
  surface-container: '#f1edec'
  surface-container-high: '#ebe7e6'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#444748'
  inverse-surface: '#313030'
  inverse-on-surface: '#f4f0ef'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1b1b'
  on-primary-container: '#858383'
  inverse-primary: '#c8c6c5'
  secondary: '#5e5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e4e2e2'
  on-secondary-container: '#646464'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#001551'
  on-tertiary-container: '#547aff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#e4e2e2'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#dce1ff'
  tertiary-fixed-dim: '#b7c4ff'
  on-tertiary-fixed: '#001551'
  on-tertiary-fixed-variant: '#0039b5'
  background: '#fdf8f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  display-lg:
    fontFamily: Hanken Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Hanken Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  mono-label:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  mono-data:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  baseline: 4px
  gutter: 24px
  margin: 48px
  column_count: '12'
  max_width: 1440px
---

## Brand & Style

This design system is built for a senior backend developer’s portfolio, positioning the engineer as an architect of complex systems rather than a mere "coder." The aesthetic draws heavily from architectural blueprints and high-end technical journals. It prioritizes clarity, structural integrity, and intentionality over visual flourish.

The personality is mature and reliable. By utilizing a minimalist approach with a disciplined grid, the design system evokes the precision of well-documented API specifications and the elegance of Swiss modernist typography. There are no gradients, shadows, or decorative blurs; the visual interest is generated through the rhythmic use of white space, hairline dividers, and a rigorous typographic hierarchy.

## Colors

The palette is rooted in an "off-white paper" experience to reduce eye strain while maintaining a premium, editorial feel. 

- **Primary (#1A1A1A):** Used for all major headings and primary body text to ensure maximum legibility and authority.
- **Secondary (#555555):** Reserved for supporting descriptions, sub-headers, and metadata.
- **Accent (#1D4ED8):** A sophisticated cobalt blue used sparingly for interactive states, key technical highlights, and semantic significance.
- **Background (#F9F8F6):** A warm, neutral surface that distinguishes the portfolio from the generic cold-white of standard SaaS applications.
- **Dividers (#E2E1DE):** Hairline borders used to define the grid and separate content modules without adding visual bulk.

## Typography

Typography is the primary engine of this design system. We use **Hanken Grotesk** for its sharp, contemporary geometry which reflects professional precision. **JetBrains Mono** is utilized strictly for technical context, serving as a visual "annotation layer."

- **Headlines:** Should be set with tight tracking and significant leading to create a "block" effect similar to newspaper mastheads.
- **Body Text:** Ample line height (1.6) is required to ensure long-form technical case studies remain readable.
- **Technical Metadata:** Use the `mono-label` style for tags like "Runtime," "Latency," or "Architecture" to differentiate structured data from narrative text.
- **Asymmetry:** In layout, headlines should often sit in the first 4 columns of the grid, while body text occupies the latter 8, creating an editorial "sidebar" feel.

## Layout & Spacing

The system follows a disciplined 12-column grid. On desktop, the grid is used to create intentional asymmetry. Content should not always span the full width; instead, use empty columns (whitespace) to guide the eye toward key technical metrics.

- **Breakpoints:**
  - **Desktop (1440px+):** 12 columns, 48px margins, 24px gutters.
  - **Tablet (768px - 1024px):** 6 columns, 32px margins, 16px gutters.
  - **Mobile (Under 768px):** 2 columns, 20px margins, 12px gutters.

The "Technical Annotation" pattern: Place small monospace labels in the gutter or the first column to provide metadata about the content in the adjacent columns. This mimics the layout of a technical specification document.

## Elevation & Depth

This design system rejects the use of Z-axis shadows. Depth is conveyed through **structural layering and borders** rather than light and shadow.

- **Flat Hierarchy:** All elements sit on the same visual plane. 
- **Hairline Dividers:** Use 1px borders (#E2E1DE) to separate sections. Use vertical dividers to create a "blueprint" feel between navigation and content.
- **Tonal Contrast:** Subtle shifts in background color (e.g., a slightly darker `#F2F1EE` for code blocks) define secondary areas.
- **Interactive States:** Instead of "lifting" an element on hover, use a color shift (Primary to Accent) or a weight change in typography to signal interactivity.

## Shapes

The shape language is predominantly sharp to reinforce a feeling of structural engineering and rigor.

- **Standard Elements:** Use a 4px (Soft) radius for buttons and input fields to provide a hint of approachability without feeling "consumer-grade."
- **Data Containers:** Cards or code blocks should maintain a 0px (Sharp) radius to emphasize their integration into the grid.
- **Icons:** Use stroke-based icons with consistent 1.5px or 2px weights. Avoid filled or "bubbly" icons.

## Components

### Buttons
- **Primary:** Solid `#1A1A1A` background, white text, 4px radius. No shadow.
- **Secondary:** Transparent background, 1px `#1A1A1A` border, uppercase mono text.
- **Hover:** Shift Primary to `#1D4ED8` (Accent blue).

### Technical Cards
- Cards do not have shadows. They are defined by a 1px border. 
- Header section of the card should be separated by a horizontal hairline divider.
- Use `mono-label` for tags in the card footer (e.g., [GO], [KUBERNETES], [GRPC]).

### Metadata Lists
- Structured as Key/Value pairs. 
- The Key is `mono-label` in Secondary charcoal.
- The Value is `body-md` in Primary black.
- This component is essential for showcasing project specs like "Role," "Stack," and "Outcome."

### Code Snippets
- Background: `#F2F1EE`.
- Font: `mono-data`.
- Border: 1px left-accent border using the Cobalt Blue (#1D4ED8) to signal "technical active zone."

### Inputs
- Bottom-border only or very thin 1px outline. 
- No background color; use the page background.
- Focus state: Border color changes to Accent Blue.