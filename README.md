# Varun Kasamneni — personal portfolio

A Jekyll portfolio built from the AcademicPages / Minimal Mistakes template family, with an academic profile sidebar, compact navigation, Markdown project and research pages, and editable YAML data. Live at **[krishnavarun02.github.io](https://krishnavarun02.github.io/)**. The public source repository is **[KrishnaVarun02.github.io](https://github.com/KrishnaVarun02/KrishnaVarun02.github.io)**.

The complete site can run on GitHub Free using a public repository and the free `github.io` address. Editing and publishing require only GitHub's website; local Ruby tooling is optional. There is no paid service, CMS, database, form backend, analytics service, or GitHub API request in the visitor experience. Hosting remains subject to [GitHub Pages' normal limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits).

## Publish using GitHub's website

If the repository already contains these files and Pages is enabled, go directly to **Everyday editing** below.

1. Sign in to GitHub as **KrishnaVarun02**. Select **+ → New repository**.
2. Use **KrishnaVarun02** as the owner and **KrishnaVarun02.github.io** as the repository name. GitHub treats the name case-insensitively; its documentation uses lowercase `krishnavarun02.github.io` for account sites. Set visibility to **Public**. You may initialize it with a README to make the upload controls available, then replace that README with this one. Create the repository.
3. Extract the delivered archive on your computer. Open its portfolio folder and locate `_config.yml`.
4. On the repository's **Code** tab, choose **Add file → Upload files**. Upload the **contents of the portfolio folder**, preserving folders, so `_config.yml`, `Gemfile`, `_pages`, `_data`, `_includes`, `_layouts`, `_sass`, and `assets` are directly at the repository root. Do not upload only the ZIP, put everything inside an extra `portfolio/` folder, or upload `_site/` as the source.
5. Include all underscored folders and the supplied dotfiles such as `.gitignore`. If the file picker hides dotfiles, enable showing hidden files or create them with **Add file → Create new file**. Browser uploads support up to 100 files per batch and 25 MiB per file; use multiple batches if necessary. Enter a commit message and commit to **main**. If GitHub offers a new branch instead, merge its pull request into `main` before publishing. [GitHub's upload guide](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).
6. Open `_config.yml` and confirm the account-site settings below. Commit any correction.

   ```yaml
   url: "https://krishnavarun02.github.io"
   baseurl: ""
   repository: "KrishnaVarun02/KrishnaVarun02.github.io"
   ```

7. Open **Settings → Pages → Build and deployment**. Set **Source: Deploy from a branch**, **Branch: main**, **Folder: /(root)**, and click **Save**. If your publishing branch has a different name, choose that branch. Leave the custom domain empty. Keep this as a Jekyll source repository: **do not add `.nojekyll`**. [GitHub's publishing-source guide](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
8. Open the **Actions** tab to see the Pages build and deployment result. When it succeeds, use **Settings → Pages → Visit site**, or open **https://krishnavarun02.github.io/**. Publication is not immediate; GitHub says changes can take up to ten minutes to appear. [GitHub's site-creation guide](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).

Committing to the configured publishing branch triggers the next build. You do not need to run Jekyll yourself for ordinary website edits. The homepage is generated from `_pages/about.md`, whose permalink is `/`; `_config.yml` includes that folder in the build.

### Use a project repository instead

For a repository named `portfolio` under the same account, use:

```yaml
url: "https://krishnavarun02.github.io"
baseurl: "/portfolio"
repository: "KrishnaVarun02/portfolio"
```

The resulting address is `https://krishnavarun02.github.io/portfolio/`. Keep `url` as the account origin without a trailing slash, and set `baseurl` to the repository path without a trailing slash. Keep page permalinks and local image/PDF paths unchanged: the templates add `baseurl` with Jekyll's URL filters. Do not put `/portfolio` into both a file path and `baseurl`. A different GitHub account needs matching values for all three settings and `author.github`.

## Everyday editing

For a text change, open the relevant file on GitHub, click the **pencil / Edit this file** button, make the edit, and choose **Commit changes**. Add a short description and commit to the publishing branch. If a branch or pull request is used, merge it into the publishing branch to publish the change. GitHub's Markdown preview is useful for prose; the deployed site is the preview of Jekyll/Liquid output.

Use spaces for YAML indentation, keep list items aligned, and write flags as unquoted `true` or `false`. Quote text containing punctuation such as `:`. Empty optional strings are written `""`; empty lists are `[]`. The block between the two `---` lines in a Markdown page is its YAML **front matter**; the text after it is the page body.

| What to change | File |
| --- | --- |
| Display name, initials, short bio, location, email, social links, portrait, phone visibility, PDF paths | `_config.yml` |
| Homepage biography and interests | `_pages/about.md` |
| Employment, contribution groups, dates, technologies | `_data/experience.yml` |
| Education, skills, coursework | `_data/education.yml` |
| Achievements and competitive programming descriptions | `_data/achievements.yml` |
| Leadership, mentoring, activities | `_data/community.yml` |
| Authored project descriptions and detail pages | `_projects/*.md` |
| Research descriptions and detail pages | `_research/*.md` |
| Education project selection and detail pages | `_data/education_repos.yml`, `_education_projects/*.md` |
| Selected GitHub repositories | `_data/project_repos.yml` |
| Gallery image metadata | `_data/gallery.yml` |
| Top navigation labels and order | `_data/navigation.yml` |
| Menu and shared link labels | `_data/ui.yml` |
| Page introductions, titles, and URLs | `_pages/*.md` |
| Layout and appearance | `_includes/`, `_layouts/`, `_sass/_portfolio.scss`, `assets/css/main.scss` |

Employment records and education institutions have `order` and `visible` fields. Copy the structure of an existing entry, use a lower numeric `order` to place it earlier, and set `visible: false` to omit it. Skills, coursework, achievements, and community entries follow their sequence in the YAML file; move or remove complete entries to change those lists. Project/research collection files use `published` instead, as described below.

Relevant coursework is grouped under `coursework` in `_data/education.yml`. Each group has `category`, `source`, and `items`; each item has a `name` and optional `codes` list. The list is deliberately curated for software engineering and AI roles: algorithms, systems, databases, compilers, AI, probability, mathematics, and theoretical foundations. It includes 17 transcript subjects and three separately labeled resume subjects. It is not a complete transcript. To add a subject, copy a neighboring item and its indentation. The original transcript is not a public download.

To add an education project, create `_education_projects/my-course-project.md` using `layout: education_project`, a title, excerpt, tags, `repository_url`, and `published: true`. Set its permalink to `/education/projects/my-course-project/`. Then add a record to `_data/education_repos.yml` with `repo`, `title`, `description`, `show: true`, numeric `order`, `tags`, and `project_url: /education/projects/my-course-project/`. The record controls the Education list and the Markdown file supplies the details. Set `show: false` to hide the listing; use `published: false` on the Markdown page to hide the detail page too. A `project_url` can also reuse an existing project page, as Turbo Compressor does.

### Biography, identity, and links

Edit `_pages/about.md` for the homepage biography, interests, and introductory links. The homepage focuses on prose about programming, AI, agents, LLMs, and learning new technologies. Project and research details live on their respective pages. Keep `{{ site.author.name }}` in the opening sentence so the display name continues to come from one place.

Edit `author.name` in `_config.yml` to change the visible name throughout the site. `author.full_name` stores the separate full-name metadata. The short sidebar description is `author.bio`; `author.affiliation` and `author.location` are separate fields. Change `author.email`, `author.github`, or `author.linkedin` to update their shared links; keep social URLs complete, beginning with `https://`. Empty optional contact fields are omitted. Contact uses a `mailto:` link that opens the visitor's email application.

`author.show_phone: false` initially omits the phone number from the rendered sidebar and contact page. Set it to `true` to display the configured number. Visibility flags control generated pages at build time; source files in this public repository remain readable, and the unchanged original resume PDFs contain their original contact information. They are not private storage.

### Add or replace your portrait

1. Open `images/` in the repository and choose **Add file → Upload files**. Upload a real portrait named `profile.jpg`, then commit. A roughly square crop works well in the circular frame.
2. Edit `_config.yml`:

   ```yaml
   author:
     # Keep the other existing author fields here.
     avatar: "/images/profile.jpg"
     avatar_alt: "Portrait of Varun Kasamneni"
   ```

   Change only the two fields inside the existing `author` section; do not add a second `author` section.
3. Commit and wait for Pages to rebuild. To replace the photo later, upload a new file using the same name, or update `avatar` to its new path.

When `avatar` is empty or the referenced local file does not exist, the template renders the configured `author.initials` instead. The initial site uses **VK**. Filename spelling and capitalization must match the uploaded file.

## Add an authored project

On the repository's Code tab, choose **Add file → Create new file**, enter `_projects/my-project.md` as the filename, and paste this example. Replace the example title and prose with your own facts before setting it live.

```markdown
---
layout: project
title: "My project"
subtitle: "A short descriptive subtitle"
excerpt: "One or two sentences describing the problem and what I built."
project_slug: my-project
permalink: /projects/my-project/
published: true
featured: false
order: 5
tags: [Python, SQL]
supervisors: []
project_date: ""
image: ""
image_alt: ""
repository_url: ""
demo_url: ""
---

Describe the purpose of the project and your contribution.

## Approach

Describe the implementation, design decisions, and technologies used.

## Results

Include only results you can substantiate, or remove this section.
```

Commit the file. The collection automatically creates the Projects listing entry and `/projects/my-project/` detail page. Use a unique, lowercase, hyphenated `project_slug` and matching permalink for each project. `excerpt` is the short listing description; Markdown below the front matter supplies the full detail page.

- `featured: true` places a project before other authored entries on the Projects page. Within each featured/nonfeatured group, smaller numeric `order` values appear first; distinct numbers make ordering predictable.
- `published: false` omits both its authored listing and detail page from normal builds. Restore `true` to publish it.
- `tags` is the technology list. Use `supervisors: ["Name as credited"]` only when appropriate; leave the list empty otherwise.
- `project_date` is optional display text, for example a known year or date range. Keep it empty when no date is established. Use `project_date`, not Jekyll's special `date` field.
- For a screenshot, upload the file to `images/projects/`, set `image: "/images/projects/my-project.png"`, and write meaningful `image_alt` text. Empty or missing local files produce no image element.
- Set `repository_url` to the actual repository URL and `demo_url` to an existing demo when available. Empty values produce no links. Local demo paths can use `/some-page/`; external demos need a full URL.

The five current project entries are IssueForge, Turbo Compressor, Parvathi, MoodMix, and WorkLens, in that order. Each has an authored detail page and a verified repository link supplied by the site owner. Rent-a-Bike and Blog Book have been removed from the website.

## Choose GitHub repositories for the showcase

The Projects page has a **Selected GitHub Repositories** section only when `_data/project_repos.yml` contains records with the literal boolean `show: true`. It currently selects the five repositories requested by the owner. It never fetches or displays every repository, fork, or starred project from your account.

1. Open the repository you want to show on GitHub. From a URL such as `https://github.com/OWNER/REPOSITORY`, copy just `OWNER/REPOSITORY`.
2. Edit `_data/project_repos.yml`. For the first entry, replace its `[]` with the example below. For later entries, append another complete `- repo:` block at the same indentation level.
3. Replace the placeholder with the real owner/repository and curate its title and description. Set `show: true` only when ready, then commit.

Use this disabled example when adding a new selection:

```yaml
- repo: KrishnaVarun02/REPLACE_WITH_ACTUAL_REPOSITORY_NAME
  title: My selected project
  description: A short description that I can edit here.
  show: false
  featured: false
  order: 1
  tags: []
  image: ""
  image_alt: ""
  demo_url: ""
  project_slug: ""
```

`featured: true` places that repository before nonfeatured repositories; numeric `order` sorts entries within each group. Upload screenshots into `images/projects/` and set `image`, for example `"/images/projects/my-project.png"`, plus `image_alt`. An existing demo can be entered in `demo_url`. Repository links are constructed as `https://github.com/` plus `repo`.

To remove a repository from the showcase, set `show: false` or delete its record. To clear all selections, restore `[]`. Do not quote `true`: `show: "true"` is text and does not select a repository. These descriptions, tags, and images are maintained in this website repository; stars, languages, and README content do not synchronize automatically.

### Connect a selected repository to an existing project

Set the selected record's `project_slug` to the matching authored project's `project_slug`, such as `issueforge`, after entering its real repository name. A mapped **published** project appears once on the Projects page, as a consolidated entry inside the repository showcase, with a link to its existing detail page. It is removed from the separate authored list on that page.

The repository record's nonempty title, description, tags, screenshot, and demo override corresponding defaults for its showcase entry. Empty values fall back to the authored project's fields. The mapped repository, screenshot, and demo also become available on the detail page; its title and Markdown narrative remain authored in `_projects/`. Repository `featured` and `order` control the showcase; authored `featured` and `order` control unmapped authored entries on the Projects page. Keep one record per repository and one mapping per authored project; if mappings are repeated, the first in display order is used.

| Authored project `published` | Repository `show` | Result when `project_slug` matches |
| --- | --- | --- |
| `true` | `true` | One consolidated showcase entry, with the authored detail page |
| `true` | `false` | Authored project and detail page remain; the selection record is hidden |
| `false` | `true` | A standalone selected repository remains; no hidden detail-page link |
| `false` | `false` | Neither entry appears |

A missing or mistyped `project_slug` leaves a standalone selected repository. Hiding a selection does not erase an independent `repository_url` written in the authored Markdown file. This separates curation of the GitHub showcase from publication of the project narrative.

The Research and Education project sections have their own selections and ordering. Research uses the `order` and `repository_url` fields in `_research/*.md`; its current order is MARL, LSTM_AI, local-credit-diagnostics, and patchbudget. Education uses `_data/education_repos.yml`, in the order Turbo-Compressor, sclp-compiler, p2p-cryptocurrency-simulator, champsim-architecture-lab, and xv6-enhancements. Turbo Compressor intentionally appears in both Projects and Education and shares its existing detail page. The other education details live in `_education_projects/`.

Each of these three sections ends with **Show more on GitHub**. Its target is configured once as `author.repositories` in `_config.yml` and opens the owner's complete GitHub repository list. This link does not automatically add repositories to the portfolio.

## Add research or a future publication

Create a file such as `_research/my-research.md` through **Add file → Create new file**:

```markdown
---
layout: research
title: "My research project"
excerpt: "A concise, factual description of the research question."
permalink: /research/my-research/
published: true
featured: false
order: 3
supervisors: []
tags: []
research_date: ""
image: ""
image_alt: ""
repository_url: ""
demo_url: ""
---

Describe the research question and your contribution.

## Approach

Describe the methods used.

## Evaluation

State documented findings, or remove this section if none are available.
```

Commit to create its entry on Research and its own detail page. Use `supervisors` for credited supervision, `tags` for research methods, and `order` for the Research page order. `published: false` hides its listing and detail page. Optional `research_date`, screenshot, repository, and demo fields work like project metadata; keep them empty until established. The initial research entries have no invented dates, paper links, venues, or acceptance status.

The optional `publications` collection is configured separately and defaults to `published: false`. Its section stays hidden while there are no published publication entries. When a real publication exists, create `_publications/actual-publication.md` with accurate content and set its flag explicitly:

```markdown
---
layout: single
title: "Actual publication title"
excerpt: "A short summary of the verified publication."
permalink: /research/publications/actual-publication/
published: false
order: 1
---

Add the verified author list, venue, year, and paper link here.
Change published to true only when this entry is ready to appear.
```

Research projects are not labeled as publications merely because they have a detail page.

## Add a gallery photo and caption

There are two steps: upload the image, then describe it in the gallery data.

1. Open `images/gallery/`, choose **Add file → Upload files**, upload your photograph, and commit. If the folder is not yet visible in a new repository, upload the `images/gallery` folder structure from your computer. Use a simple filename such as `campus.jpg`.
2. Open `_data/gallery.yml`. Replace `[]` for the first entry, or append another list item. For example:

   ```yaml
   - image: "/images/gallery/campus.jpg"
     caption: "Write your own accurate caption here."
     image_alt: "Describe the visible subject and setting of your photograph."
     category: "Campus"
     order: 1
     visible: true
   ```

3. Replace the example text with the real caption and image description, then commit. Smaller numeric `order` values appear earlier. `category` is an optional caption label; it does not create a filter. Set `visible: false` to hide the entry or remove it entirely.

The responsive gallery uses local images, captions, and links to the full image. Entries with empty or missing files are omitted. With no visible, existing images it shows **Photos coming soon**. No personal images are supplied initially.

## Replace the resume PDFs

Both supplied original PDFs are included unchanged:

- `files/software-engineering-resume.pdf` → **Software Engineering Resume**
- `files/research-cv.pdf` → **Research CV**

To replace one, open `files/` on GitHub, choose **Add file → Upload files**, and upload the new PDF with the same filename. Commit and wait for the rebuild. The existing CV link then points to the new file.

To use different filenames, upload the PDFs first, then edit the matching records under `resumes` in `_config.yml`:

```yaml
resumes:
  - label: "Software Engineering Resume"
    path: "/files/software-engineering-resume.pdf"
  - label: "Research CV"
    path: "/files/research-cv.pdf"
```

Use the real uploaded paths, preserving case. To remove a download button, remove its configuration record or set its path to `""`. A configured path that has no matching local file also produces no link. Removing a button does not delete the PDF from the public repository. The published prose is curated separately: replacing a PDF does not automatically rewrite experience, projects, or other page text.

## Reorder or add pages

Edit `_data/navigation.yml` to reorder the complete `- title:` / `url:` pairs. All nine links—including Achievements, Community, and Contact—are in the `main` list and appear side by side in the desktop header. On narrow screens, the same flat list appears inside the accessible Menu control. There is no More submenu. The name at the left of the header links to Home.

To add a top-level page, create `_pages/my-page.md`:

```markdown
---
layout: single
title: "My page"
permalink: /my-page/
---

Write the page content here.
```

Then add `- title: My page` and an indented `url: /my-page/` to the desired navigation list. Removing a navigation link alone does not remove its page; use `published: false` in its front matter to omit the page from normal builds, and remove links pointing to it.

For links in Markdown page bodies, retain the URL filter so project-repository hosting works:

```liquid
[My page]({{ '/my-page/' | relative_url }})
![A meaningful image description]({{ '/images/projects/my-image.png' | relative_url }})
```

Regular external links can use their full `https://` URL. Local path capitalization must match the actual file or permalink.

## Optional local preview and checks

Install Ruby and Bundler if you want to preview changes on your computer. Ruby 3.1.x is a compatible starting choice for this GitHub Pages dependency set; newer Ruby versions may need compatibility adjustments. The Gemfile pins the `github-pages` dependency set and includes WEBrick for local serving. [GitHub's local preview guide](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll).

In a terminal opened at the repository root:

```sh
gem install bundler
bundle install
bundle exec jekyll serve
```

Open `http://127.0.0.1:4000/`. Stop the server with **Ctrl+C**. Restart it after changing `_config.yml`. For a configured project repository, visit its base path, or preview at the local root with `bundle exec jekyll serve --baseurl ""`.

Run a production-style build and the repository-selection checks with:

```sh
bundle exec jekyll build
python3 scripts/check_site.py _site
python3 scripts/check_requested_updates.py _site
python3 scripts/check_project_showcase.py
python3 scripts/check_content_options.py
```

The showcase script uses temporary source copies to exercise selection, ordering, hidden projects, mapping without duplication, missing images, optional links, and project-site URL paths. The content-options script checks gallery images, portrait fallback, empty contact fields, phone visibility, missing PDFs, and future publications. Neither script modifies the real content or published selection. Python 3 is needed only for these validation scripts, not for building or hosting the site. An alternative Jekyll executable can be passed with `--jekyll-command '/absolute/path/to/jekyll-wrapper'`.

To check project-path rendering independently of the production settings:

```sh
bundle exec jekyll serve --baseurl /preview
```

Visit `http://127.0.0.1:4000/preview/`, open a project detail page directly, refresh it, and follow its back link. Check a narrow/mobile viewport, the Menu control and its direct navigation links, keyboard focus, both PDF downloads, the mailto link, and image paths. Disable JavaScript once to check the static content and navigation. Essential text and links render at build time; JavaScript only enhances the menu behavior.

See [VERIFICATION.md](VERIFICATION.md) for the checks actually completed for this delivery. These instructions do not imply that any later edit has already been checked.

### If an update does not appear

Check the latest Pages run under **Actions** first. A failed build commonly indicates malformed YAML, a missing front-matter delimiter, or an invalid template edit. Check **Settings → Pages** for the correct branch and `/(root)`. If the build passed, allow publication time and refresh the page. For missing photos/PDFs, compare the configured path and capitalization with the uploaded file. For a project site with missing styles or links, check `url` and `baseurl` as shown above.

## Repository map

```text
_config.yml                    Identity, URLs, author fields, resumes, collections
_data/
  navigation.yml               Nine direct navigation links
  project_repos.yml            Explicit GitHub repository selection
  education_repos.yml          Education project selection and order
  experience.yml               Employment and contributions
  education.yml                Education, grouped skills, coursework
  achievements.yml             Achievements
  community.yml                Leadership, mentoring, activities
  gallery.yml                  Gallery metadata; initially empty
  ui.yml                       Shared interface labels
_pages/                        Home and the nine other top-level pages
_projects/                     Five authored project Markdown files
_research/                     Four research project Markdown files
_education_projects/           Four education details; Turbo reuses its project page
_publications/                 Optional future collection; create when needed
_includes/, _layouts/           Shared Liquid presentation templates
_sass/                         Template styles and portfolio adjustments
assets/css/main.scss           Compiled stylesheet entry point
assets/js/navigation.js        Small navigation enhancement
images/                        Your future portrait, gallery, and project images
files/                         Both original resume PDFs
scripts/check_project_showcase.py  Isolated repository-selection checks
404.html, robots.txt, sitemap.xml  Static-site supporting pages
Gemfile                        GitHub Pages-compatible local dependencies
README.md                      This editing and deployment guide
CONTENT_NOTES.md                Source reconciliation and editorial decisions
VERIFICATION.md                 Completed delivery checks
LICENSE, THIRD_PARTY_NOTICES.md, licenses/  Attribution and license notices
```

The empty image folders are intentional. The site checks that a configured local image or resume exists before rendering it. `_site/` is generated output and should not be uploaded as the source for this branch-publishing setup.

## Template attribution

The starting style comes from [AcademicPages](https://github.com/academicpages/academicpages.github.io) and [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes), through the MIT-licensed [reference repository](https://github.com/mbh1234/keerthana.github.io) at commit [`e0c19f2df7563f6561024901958407f5ba31fc84`](https://github.com/mbh1234/keerthana.github.io/tree/e0c19f2df7563f6561024901958407f5ba31fc84). Applicable template SCSS was vendored and adapted for this site; personal content and photos from the reference were not reused. Keep the supplied license notices and footer attribution when editing or redistributing the template. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [LICENSE](LICENSE).
