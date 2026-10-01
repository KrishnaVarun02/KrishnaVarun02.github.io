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
- Simpl Pay appears once, June–July 2024. At the owner's request, its experience entry uses only the software engineering resume's points shown in the supplied screenshot.
- Turbo Compressor has one shared authored detail page, merging both resume descriptions and retaining its supervisor.

## Reporting boundaries

- The 30% reduction in manual debugging, 300+ APIs, 40+ scenarios, 10 platform areas, and other numerical contributions are resume-reported figures, not independently measured by the website.
- The residential load forecasting results are reported as R-squared **0.938** and RMSE **0.263**. No units, datasets, evaluation splits, or additional results are supplied. The website adds none.
- Research projects have no invented dates, publications, venues, acceptance status, or paper links.
- Competitive programming titles come from the software engineering resume and are stated directly on the site. No numeric ratings, handles, or live ranking claims are added.
- Mathematics in JEE Main remains a **100% score**, not a percentile. The grade notation **Grade of Excellence (A)\*** and the source's **Indian Olympiad in Chemistry (ACT)** label are retained.
- The running activity is described as a **10 km run**, avoiding the original resume's ambiguous “10 KM Marathon” wording.
- The research resume explicitly supports strict delivery timelines for Think Tank and response timelines for Gauth. Public copy keeps the main contributions concise.
- The owner subsequently supplied explicit research, project, and education repository selections. Descriptions were checked against those repositories' READMEs and, where appropriate, retained result files. Selection and order are static website content; no GitHub account inventory is fetched. Unprovided demos, screenshots, and project dates remain blank.
- The owner subsequently supplied one profile photograph and eight gallery photographs. The initials avatar and empty-gallery state remain supported fallbacks. Phone visibility defaults to off.

## Public presentation

At the owner's request, visitor-facing accomplishments and results use direct factual wording. Phrases such as “as stated in my resume” and resume-based course headings are omitted. Source metadata and these implementation notes retain provenance, while substantive research limits remain visible.

The About text emphasizes curiosity, mathematical reasoning, careful experimentation, and continued learning. Its six highlights follow the requested order: IIT (BHU) degree/CPI, JEE Advanced rank, JEE Main rank, JEE Main Mathematics score, chemistry olympiad recognition, and the Oracle Think Tank championship. It makes no claim of graduate enrollment or admission.

## Supplied photographs

The nine current source images comprise eight JPEGs and one PNG, each retained unchanged. The owner supplied a cropped PNG to replace the earlier H C Verma JPEG; this crop was not generated or edited by the website. The profile photograph uses CSS framing; the other eight photographs appear only in Gallery, display in full, and link to their original local files. The eight gallery photographs are not inserted into Achievements or other page content. No synthetic image edits are used. Descriptions follow the owner's supplied context, without inferred dates or additional locations.

| Website file | Owner-supplied context |
| --- | --- |
| `images/profile.jpg` | Profile photograph wearing a white T-shirt and beige coat |
| `images/gallery/oracle-think-tank.jpg` | Oracle Think Tank, Realm of Thought |
| `images/gallery/iit-bhu-convocation.jpg` | IIT (BHU) convocation |
| `images/gallery/bicycle-volunteering-bengaluru.jpg` | Bicycle volunteering for children in Bengaluru |
| `images/gallery/oracle-painting.jpg` | Painting at Oracle |
| `images/gallery/blood-donation.jpg` | Blood donation |
| `images/gallery/with-hc-verma.png` | Owner-supplied crop with Prof H C Verma, following the owner's identification |
| `images/gallery/boxing.jpg` | “In the boxing ring.” No event, venue, date, or medal is attributed to this photograph |
| `images/gallery/outside-work.jpg` | Casual portrait |

## Future publications

`_publications/` is an optional Jekyll collection. No publication entries ship with the site. `_pages/research.md` renders its heading and entries only when at least one document has `published: true`.

Future publication files can use `title`, `excerpt`, `order`, `published`, and `permalink` frontmatter with `layout: single`. Add the authors, venue, date, citation, and verified external paper links in the Markdown body when actual material is available. Publication defaults are `published: false`, so explicitly opt in before displaying a real entry. This collection is separate from the four existing research projects; a repository manuscript is not treated as a published paper.

## Requested repository organization

- Research: MARL, LSTM_AI, local-credit-diagnostics, patchbudget.
- Projects: IssueForge-Multi-Agent-GitHub-Issue-to-PR-Orchestrator, Turbo-Compressor, Parvathi, moodmix, worklens.
- Education projects: Turbo-Compressor, sclp-compiler, p2p-cryptocurrency-simulator, champsim-architecture-lab, xv6-enhancements.
- Each list follows the owner's order. Turbo Compressor intentionally appears in two sections with one shared detail page. Rent-a-Bike and Blog Book were removed from the website; the original downloadable resumes remain unchanged.
- MARL is a report archive, and LSTM_AI includes implementation/report material. The two new research studies retain their benchmark and review limitations. Repository implementations and fixture tests are not presented as verified live third-party integrations.

## Transcript coursework

The supplied `Varun_Transcripts.pdf` is a scanned transcript. All four academic-year columns were rendered and read visually. The final selection follows the owner's clarification to emphasize subjects useful for software engineering and AI roles. It contains 17 transcript subjects (18 course codes, combining the two AI entries) covering algorithms, systems, databases, compilers, architecture, AI, probability, mathematics, optimization, and theory. Three additional software/AI subjects from the resume bring the selection to 20 displayed entries. Their provenance remains in `source` metadata without a resume-attribution label on the public page. This is a relevant-coursework selection, not a complete academic record.

General physics, electrical courses, introductory programming, workshops, general engineering mathematics, graphics, and generic project/training/seminar modules are omitted from this focused presentation. Relevance was checked against the [ACM CS2023 knowledge areas](https://csed.acm.org/knowledge-areas/) and [Google's ML prerequisite guidance](https://developers.google.com/machine-learning/crash-course/prereqs-and-prework); these references inform editorial selection and do not establish additional courses or skills the owner studied.

Only course names and codes were added; the transcript itself, student identifiers, and individual grades were not copied into the website. Coursework metadata lives in `_data/education.yml` under `coursework`, with a source field for each group. Education project repositories are separately supplied portfolio material; repository reconstruction claims are not presented as proof that these exact source trees were submitted during college.
