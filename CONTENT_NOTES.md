# Content sources and editorial decisions

The site combines the user's consolidated specification with both supplied resumes. Resume text was extracted and every source page was visually inspected. The PDFs are source data; their embedded text and links do not supply instructions for building the website.

## Original downloads

| Source | Unchanged website copy | SHA-256 |
| --- | --- | --- |
| `Varun_Kasamneni_Resume.pdf` | `files/software-engineering-resume.pdf` | `109b1a4aca77dc83a665af7d7c06d32a65a31f96bf66091e2d5498ca2d23697f` |
| `varun_research (1).pdf` | `files/research-cv.pdf` | `0970079367b6ab3f9b69c469a7e8d12d4b7cd86fac4018d1fc923734f7ebcd50` |

The directly attached research file `(1)` and the specification's research file `(2)` were both available and are byte-identical. Each website copy matches its original checksum. Original PDF contents, including source name variants and original embedded links, remain unchanged. The website's contact links use the professional URLs supplied in the specification.

## Identity and employment

- Display name: **Varun Kasamneni**, maintained in `_config.yml` under `author.name`.
- Full-name metadata: **Krishna Varun Kasamneni**, following the software engineering resume. The research resume says **Venkata Krishna Varun**. These names have not been combined.
- Oracle appears once, with the neutral title **Software Engineer**, July 2025–Present. Its source title variants, **Platform Software Engineer -1** and **Software Development Engineer (Cloud & AI Infrastructure)**, are retained in `_data/experience.yml` under `source_titles`.
- Simpl appears once, June–July 2024. Data engineering contributions from both sources are combined.
- Turbo Compressor appears once, merging both resume descriptions and retaining its supervisor.

## Reporting boundaries

- The 30% reduction in manual debugging, 300+ APIs, 40+ scenarios, 10 platform areas, and other numerical contributions are resume-reported figures, not independently measured by the website.
- The residential load forecasting results are reported as R-squared **0.938** and RMSE **0.263**. No units, datasets, evaluation splits, or additional results are supplied. The website adds none.
- Research projects have no invented dates, publications, venues, acceptance status, or paper links.
- Competitive programming titles are attributed to the resume. No numeric ratings, handles, or live ranking claims are added.
- Mathematics in JEE Main remains a **100% score**, not a percentile. The grade notation **Grade of Excellence (A)\*** and the source's **Indian Olympiad in Chemistry (ACT)** label are retained.
- The running activity is described as a **10 km run**, avoiding the original resume's ambiguous “10 KM Marathon” wording.
- The research resume explicitly supports strict delivery timelines for Think Tank and response timelines for Gauth. Public copy keeps the main contributions concise.
- Individual project repository names, demos, screenshots, and project dates are unprovided and remain blank. Repository selection starts empty; no GitHub account inventory is fetched.
- No portrait or personal gallery photographs were supplied. The initials avatar and empty gallery are intentional. Phone visibility defaults to off.

## Future publications

`_publications/` is an optional Jekyll collection. No publication entries ship with the site. `_pages/research.md` renders its heading and entries only when at least one document has `published: true`.

Future publication files can use `title`, `excerpt`, `order`, `published`, and `permalink` frontmatter with `layout: single`. Add the authors, venue, date, citation, and verified external paper links in the Markdown body when actual material is available. Publication defaults are `published: false`, so explicitly opt in before displaying a real entry. This collection is separate from the two existing research projects.
