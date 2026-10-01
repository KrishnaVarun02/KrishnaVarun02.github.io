# Theme provenance and licenses

This site is an adaptation of the **AcademicPages / Minimal Mistakes** Jekyll template family, not a separately invented theme. Its Sass foundation and single-page layout structure were taken from the requested public reference repository:

- Reference source: https://github.com/mbh1234/keerthana.github.io
- Inspected commit: `e0c19f2df7563f6561024901958407f5ba31fc84`
- AcademicPages: https://github.com/academicpages/academicpages.github.io
- Minimal Mistakes: https://github.com/mmistakes/minimal-mistakes

The original MIT license, including **Copyright (c) 2016 Michael Rose**, is preserved unchanged in `LICENSE`. The website footer retains the Jekyll, AcademicPages, and Minimal Mistakes attribution.

The vendored `_sass` files retain the reference theme's typography, resets, variables, grid helpers, component styles, and print support. `_sass/_portfolio.scss` customizes the layout, colors, responsive navigation, initials avatar, and portfolio entries. The original JavaScript, analytics, forms, content, personal photographs, social links, icon fonts, and third-party browser scripts are not part of this site.

The Sass foundation also includes:

- **Susy** (https://github.com/oddbird/susy), under `_sass/vendor/susy`; see `licenses/Susy.txt`.
- **Breakpoint** (https://github.com/at-import/breakpoint), under `_sass/vendor/breakpoint`; see `licenses/Breakpoint.txt`.

These dependencies are used only during the Jekyll Sass build. The site serves local compiled CSS and a small optional navigation script; no external font, JavaScript, or GitHub API request is required to display its content.

The supplied resume PDFs remain unmodified personal documents. Theme licensing does not establish permission for others to reuse personal documents or identity material.
