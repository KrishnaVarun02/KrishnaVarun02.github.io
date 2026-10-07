#!/usr/bin/env python3
"""Check a Jekyll build's local links, fragments, and baseline content. No dependencies.

Usage: python3 scripts/check_site.py _site [--baseurl /portfolio]
"""
import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.ids, self.images, self.headings = [], set(), [], 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "h1":
            self.headings += 1
        for key in ("href", "src"):
            if key in attrs:
                self.links.append(attrs[key])
        if tag == "img":
            self.images.append(attrs)


def check(build, baseurl=""):
    build = Path(build).resolve()
    pages = {path: Page(path.read_text()) for path in build.rglob("*.html")}
    errors = []
    expected = ("index.html", "experience/index.html", "research/index.html",
                "projects/index.html", "education/index.html", "achievements/index.html",
                "community/index.html", "cv/index.html", "gallery/index.html",
                "contact/index.html", "404.html")
    for relative in expected:
        if not (build / relative).is_file():
            errors.append(f"Missing page: {relative}")
    for path, page in pages.items():
        if page.headings != 1:
            errors.append(f"{path.relative_to(build)}: expected one h1")
        for image in page.images:
            if not image.get("alt", "").strip():
                errors.append(f"{path}: image needs meaningful alt text")
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            if not link:
                errors.append(f"{path}: empty link")
                continue
            decoded = unquote(url.path)
            if decoded.startswith("/"):
                if baseurl and not (decoded == baseurl or decoded.startswith(baseurl + "/")):
                    errors.append(f"{path}: misses baseurl: {link}")
                    continue
                target = build / decoded[len(baseurl):].lstrip("/")
            else:
                target = path.parent / decoded if decoded else path
            if target.is_dir():
                target = target / "index.html"
            target = target.resolve()
            if not target.is_file():
                errors.append(f"{path.relative_to(build)}: broken link {link}")
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f"{path.relative_to(build)}: missing fragment {link}")
    html = "\n".join(path.read_text() for path in pages)
    for forbidden in ("Keerthana", "mbh1234", "yourwebsite.com", "REPLACE_WITH_ACTUAL", "raw.githubusercontent.com", "api.github.com"):
        if forbidden in html:
            errors.append(f"Unexpected placeholder/reference/dependency: {forbidden}")
    if 'href="tel:' in html:
        errors.append("Initial public phone display should be hidden")
    if errors:
        raise AssertionError("\n".join(errors))
    print(f"PASS: {len(pages)} HTML pages; local links, fragments, images, headings, and initial-content safeguards (baseurl={baseurl!r}).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("build", type=Path)
    parser.add_argument("--baseurl", default="")
    args = parser.parse_args()
    check(args.build, args.baseurl.rstrip("/"))
