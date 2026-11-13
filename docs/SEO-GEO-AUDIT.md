# SEO and GEO audit

Audit date: 2026-11-13. Scope: repository source and publicly accessible GitHub repository pages. Live portfolio fetch failed and DNS lookup from the execution environment failed, so source observations are not proof of deployed behavior.

## Baseline

- Buildless static HTML, one indexable homepage with fragment navigation, and a custom `404.html`; no framework, build command, server routing code, or hosting configuration is present. `CNAME` and the GitHub remote suggest GitHub Pages, but actual deployment and settings were not verified.
- Text, headings and metadata are in the initial HTML. Homepage already had canonical, robots, Open Graph, Twitter, icons, Person/WebSite/ProfilePage and a selected-work ItemList. Sitemap contains the homepage; robots allows all user agents and identifies it. The 404 document declares noindex. Existing public profile URLs and contact details are in the source.
- The homepage depended on the Tailwind browser CDN, two Google Fonts stylesheets and JavaScript-driven reveal animations. Content using `.fade-in-up` started at zero opacity when JavaScript was enabled; an observer failure could leave it invisible. Desktop navigation links were hidden on small screens. Source HTML was 43,729 bytes; social image was 34,263 bytes. These are transfer-size proxies, not Core Web Vitals measurements.
- No production Lighthouse, field metrics, HTTP headers, status codes, www redirects, TLS, WAF rules, or live robots/sitemap could be verified. No claims about indexing or actual crawler access can be made.

## Changes

- The homepage metadata now describes PHP/Laravel work and open source more directly; canonical and social URLs remain on the existing non-www domain.
- Reveal content is visible by default; the observer script was removed. Added reduced-motion and keyboard focus styles and a mobile section navigation. The existing layout and sections remain.
- Added a visible open-source section with descriptions grounded in public READMEs: [Activity Logger](https://github.com/KarimEl-Kady/activity-logger), [Proj-Base](https://github.com/KarimEl-Kady/proj-base), [Base Settings](https://github.com/KarimEl-Kady/base-settings), and [Quota Guard](https://github.com/KarimEl-Kady/quota-guard-skill). These are repositories, not claims of deployed production products. [Base Blog](https://github.com/KarimEl-Kady/base-blog) is documented as a reusable proj-base package but was not selected for the homepage. The requested SBQ-Agents-Hub URL returned 404 through the web fetcher; its availability could not be established.
- Existing structured data remains limited to the visible profile and work. No speculative project results or fake article markup were added. The static single page avoids thin project pages without first-hand implementation details.
- Robots policy was left unchanged: `User-agent: *` permits crawlers under robots rules, including search agents without more specific rules; this also leaves the existing training-crawler policy unchanged. Robots permission does not establish WAF access or a crawl.

## Remaining

1. Verify production DNS, HTTPS, preferred host redirects, 404 status, response headers and sitemap URLs after deployment; hosting infrastructure controls these and is not in this repository. Confirm both www and non-www behavior before changing DNS or redirects.
2. Replace the Tailwind runtime CDN with a locally generated, pinned production stylesheet after capturing a browser baseline and validating all responsive and dynamic utility classes. Current third-party font and CSS delivery remain render-blocking risks. Do not remove the CDN without replacing its styles.
3. Run mobile/desktop Lighthouse and real-user Core Web Vitals, accessibility and keyboard checks, and inspect contrast and layout with fonts loaded and blocked. No LCP, INP, CLS, FCP or performance score was measured here.
4. Verify external product links, employment details, and superlative claims in the pre-existing selected-work descriptions with the owner. External availability can change. The initial public GitHub README checks are not independent evidence of production maturity.
5. Run Schema.org Validator and Google Rich Results Test on a deployed or publicly accessible preview. JSON parsing alone does not validate schema semantics or eligibility.
