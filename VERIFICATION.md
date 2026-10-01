# Verification

Checked on 1 October 2026.

## Build and content

- Built with Jekyll **3.10.0**, the version listed by GitHub Pages, with no custom plugins. This machine used an isolated local Ruby dependency environment; the supplied Gemfile selects the supported `github-pages` **232** dependency set.
- Both account-root (`baseurl: ""`) and project-repository (`baseurl: "/portfolio"`) builds pass. All **24 HTML pages** have working local links, asset paths, and fragment targets.
- Ten top-level pages, five project details, four research details, four education project details, and the 404 page are generated. Turbo Compressor shares one detail page across Projects and Education. Rent-a-Bike and Blog Book are removed. No invented publication entries are present.
- Relevant coursework is curated for software engineering and AI roles: 17 transcript subjects and three additional resume subjects, with provenance retained in metadata. The complete transcript and general technical modules are not reproduced. No transcript document, student identifiers, or additional transcript-derived grades are published.
- Both original PDF files match their source SHA-256 values. Browser download responses also match these bytes. See `CONTENT_NOTES.md` for provenance.
- No reference-person content, placeholder social URLs, unprovided project repositories, browser-side GitHub API calls, or external browser scripts appear in the generated HTML. Unchanged source PDFs retain their original contents.

## Browser checks

- Used isolated headless Chrome and Playwright against an actual local HTTP server.
- Inspected reference and portfolio screenshots at **1440px desktop** and **390px mobile** widths. The site preserves the template's 70px fixed masthead, profile sidebar, system font, restrained links, and main-column proportions; it has customized responsive navigation and content.
- Tested all **23 content routes** at 1440px, 390px, and 320px; no horizontal overflow, missing images, failed navigation, or JavaScript errors. The nine desktop links also fit at 1280px, 1121px, 1120px, 1024px, and 961px.
- **Zero automated axe WCAG 2 A/AA and 2.1 AA violations** across all 23 content routes and the open mobile menu. This is an automated check, not a claim of a complete accessibility certification.
- Verified keyboard activation of the flat mobile menu, its nine direct links, Escape dismissal, and the extracurricular-activities jump. The More submenu is removed.
- With JavaScript disabled, the native navigation controls, projects, research, contact, and CV remain usable. Essential text and links are generated at build time.
- Visually checked CV, gallery, education, IssueForge details, and the open mobile menu. Portrait and gallery fallback behavior was checked before the owner supplied the current photographs.

## Photo update

The collection contains the owner's real profile photograph and eight supplied gallery photographs, including boxing. The gallery photographs appear only in Gallery; the separate profile photograph appears in the sidebar. The current files are eight JPEGs and one PNG: the owner supplied a cropped `with-hc-verma.png` to replace the earlier JPEG. All current source images are retained unchanged, the portrait uses CSS framing, and the gallery links full photographs to their originals. `CONTENT_NOTES.md` records the file mapping and owner-supplied captions.

The current update passes root and `/portfolio` builds and local-link checks; the requested project/coursework checks also pass. A SHA-256 comparison confirms the replacement PNG matches the supplied file. The eight unchanged JPEGs previously passed the same comparison against their originals. All 24 HTML pages use the separate profile, and the eight event/personal photographs render only on Gallery. The four editable-content fixture builds passed for the gallery implementation, including missing-image and initials fallbacks.

Fresh browser checks confirm the six homepage highlights match the requested wording and order, public resume-attribution phrases are absent across all 24 pages, and the research-oriented About text adds no degree or enrollment claims. The replacement image loads at its supplied 702 × 884 dimensions and uses `object-fit: contain` so both faces remain visible. The stylesheet URL includes a build version so returning visitors load current framing styles.

Chrome checks for Home, Gallery, Achievements, Education, Experience, and the residential forecasting page at 1440px, 390px, and 320px show no horizontal overflow or JavaScript errors. Automated axe checks report zero WCAG 2 A/AA and 2.1 AA violations on these pages. The revised About layout and replacement photograph were visually reviewed. Gallery links remain ordinary links to the original files; the earlier check confirmed the full boxing photograph opens with JavaScript disabled.

## Repository selection

Five isolated fixture builds exercise the implemented Liquid templates:

- An empty selection adds no showcase or fake entries.
- Only the literal YAML boolean `show: true` appears; hidden records and the quoted string `"true"` do not.
- Featured selections precede ordinary selections, with numeric `order` within each group.
- A selected repository mapped to a published authored project produces one consolidated entry.
- Hidden authored entries have no detail pages or broken links; a separately selected repository can remain standalone.
- Duplicate mappings, title/description fallbacks, empty links, absent image files, valid local screenshots, and project-site base paths are checked.

`check_requested_updates.py` additionally checks the actual requested research (4), project (5), and education (5) repository selections in exact order; their detail and GitHub links; the shared Turbo page; all three Show more links; direct navigation; removed project pages; the replacement extracurricular link; and the focused software/AI coursework list.

## Repeat the checks

Four additional isolated Jekyll builds verify gallery ordering and visibility, valid/missing portrait fallback, image alt text, omission of empty captions, empty or whitespace-only contact fields, phone visibility, missing resume files, and default-hidden versus populated future publications. These checks found and resolved empty-link guards that otherwise depended on Liquid's `blank` comparison.

```sh
bundle install
bundle exec jekyll build
python3 scripts/check_site.py _site
python3 scripts/check_requested_updates.py _site
python3 scripts/check_project_showcase.py
python3 scripts/check_content_options.py
bundle exec jekyll build --baseurl /portfolio --destination _site-project
python3 scripts/check_site.py _site-project --baseurl /portfolio
python3 scripts/check_requested_updates.py _site-project --baseurl /portfolio
```

The generated `_site-project/` directory is excluded from Git and Jekyll's source files. The fixture scripts run in temporary directories and do not change the site's configured selections.

## Publishing settings

Target public repository: `KrishnaVarun02/KrishnaVarun02.github.io`.

**Settings → Pages → Build and deployment → Deploy from a branch → main → /(root)**, with no custom domain and no `.nojekyll` file. `url` is `https://krishnavarun02.github.io` and `baseurl` is empty.

The site is published at **https://krishnavarun02.github.io/**. The public repository uses `main`, with HTTPS enforced. Its initial live rollout passed page, asset, and unchanged-PDF download checks; subsequent updates use the same branch-publishing pipeline. The latest deployment status is visible in the repository's **Actions → pages build and deployment** run.
