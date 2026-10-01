# Verification

Checked on 1 October 2026.

## Build and content

- Built with Jekyll **3.10.0**, the version listed by GitHub Pages, with no custom plugins. This machine used an isolated local Ruby dependency environment; the supplied Gemfile selects the supported `github-pages` **232** dependency set.
- Both account-root (`baseurl: ""`) and project-repository (`baseurl: "/portfolio"`) builds pass. All **17 HTML pages** have working local links, asset paths, and fragment targets.
- Ten requested top-level pages, four project details, two research details, and the 404 page are generated. No invented publication entries are present.
- Both original PDF files match their source SHA-256 values. Browser download responses also match these bytes. See `CONTENT_NOTES.md` for provenance.
- No reference-person content, placeholder social URLs, unprovided project repositories, browser-side GitHub API calls, or external browser scripts appear in the generated HTML. Unchanged source PDFs retain their original contents.

## Browser checks

- Used isolated headless Chrome and Playwright against an actual local HTTP server.
- Inspected reference and portfolio screenshots at **1440px desktop** and **390px mobile** widths. The site preserves the template's 70px fixed masthead, profile sidebar, system font, restrained links, and main-column proportions; it has customized responsive navigation and content.
- Tested all **16 content routes** at 1440px, 390px, and 320px; no horizontal overflow, missing images, failed navigation, or JavaScript errors. Also checked home at 768px, 960px, 961px, and 1024px.
- **Zero automated axe WCAG 2 A/AA and 2.1 AA violations** across all 16 content routes and the open mobile menu. This is an automated check, not a claim of a complete accessibility certification.
- Verified the skip link, keyboard activation of the mobile menu and nested More menu, Escape dismissal, and contact email link.
- With JavaScript disabled, the native navigation controls, projects, research, contact, and CV remain usable. Essential text and links are generated at build time.
- Visually checked CV, gallery, education, IssueForge details, and the open mobile menu. No portrait or gallery photographs are fabricated; the initials fallback and empty gallery are intentional.

## Repository selection

Five isolated fixture builds exercise the implemented Liquid templates:

- An empty selection adds no showcase or fake entries.
- Only the literal YAML boolean `show: true` appears; hidden records and the quoted string `"true"` do not.
- Featured selections precede ordinary selections, with numeric `order` within each group.
- A selected repository mapped to a published authored project produces one consolidated entry.
- Hidden authored entries have no detail pages or broken links; a separately selected repository can remain standalone.
- Duplicate mappings, title/description fallbacks, empty links, absent image files, valid local screenshots, and project-site base paths are checked.

## Repeat the checks

Four additional isolated Jekyll builds verify gallery ordering and visibility, valid/missing portrait fallback, image alt text, omission of empty captions, empty or whitespace-only contact fields, phone visibility, missing resume files, and default-hidden versus populated future publications. These checks found and resolved empty-link guards that otherwise depended on Liquid's `blank` comparison.

```sh
bundle install
bundle exec jekyll build
python3 scripts/check_site.py _site
python3 scripts/check_project_showcase.py
python3 scripts/check_content_options.py
bundle exec jekyll build --baseurl /portfolio --destination _site-project
python3 scripts/check_site.py _site-project --baseurl /portfolio
```

The generated `_site-project/` directory is excluded from Git and Jekyll's source files. The showcase script runs fixtures in temporary directories and does not change the site's empty initial selection.

## Publishing settings

Target public repository: `KrishnaVarun02/KrishnaVarun02.github.io`.

**Settings → Pages → Build and deployment → Deploy from a branch → main → /(root)**, with no custom domain and no `.nojekyll` file. `url` is `https://krishnavarun02.github.io` and `baseurl` is empty.

GitHub's own Jekyll build and Pages deployment succeeded. The public site at **https://krishnavarun02.github.io/** was tested directly: all 16 content routes, the compiled CSS and JavaScript, and both unchanged PDF downloads returned successfully. Desktop and mobile screenshots of the live deployment were also inspected. The repository is public, its default branch is `main`, and HTTPS is enforced.
