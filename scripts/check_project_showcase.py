#!/usr/bin/env python3
"""Exercise the real Jekyll templates using isolated selection fixtures.

Run from the repository after bundle install:
    python3 scripts/check_project_showcase.py

An alternative local toolchain can be supplied without editing the script:
    python3 scripts/check_project_showcase.py --jekyll-command 'jekyll'

The website's content is copied to a temporary directory; these cases never
modify the published YAML or project files. Requires Python 3 and Jekyll only.
"""

import argparse
import base64
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import tempfile


class ProjectEntries(HTMLParser):
    def __init__(self, markup):
        super().__init__()
        self.entries = []
        self.current = None
        self.article_depth = 0
        self.feed(markup)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "article":
            if self.current is not None:
                self.article_depth += 1
            elif "project-entry" in attrs.get("class", "").split():
                self.current = {"attrs": attrs, "text": [], "links": [], "images": []}
                self.article_depth = 1
        if self.current is not None:
            if tag == "a":
                self.current["links"].append(attrs.get("href", ""))
            elif tag == "img":
                self.current["images"].append(attrs)

    def handle_endtag(self, tag):
        if tag == "article" and self.current is not None:
            self.article_depth -= 1
            if self.article_depth == 0:
                self.current["text"] = " ".join(self.current["text"])
                self.entries.append(self.current)
                self.current = None

    def handle_data(self, data):
        if self.current is not None and data.strip():
            self.current["text"].append(data.strip())


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def repo(name, **fields):
    value = {
        "repo": "qa-owner/" + name,
        "title": "QA " + name,
        "description": "QA description for " + name,
        "show": True,
        "featured": False,
        "order": 1,
        "tags": [],
        "image": "",
        "image_alt": "",
        "demo_url": "",
        "project_slug": "",
    }
    value.update(fields)
    return value


def fixture_project(slug, published, **fields):
    metadata = {
        "layout": "project",
        "title": "QA authored " + slug,
        "excerpt": "QA authored description " + slug,
        "project_slug": slug,
        "permalink": "/projects/" + slug + "/",
        "published": published,
        "featured": False,
        "order": 999,
        "tags": ["QA technology"],
        "image": "",
        "image_alt": "",
        "repository_url": "",
        "demo_url": "",
        "project_date": "",
    }
    metadata.update(fields)
    # JSON is a YAML subset and is accepted by Jekyll's front matter parser.
    return "---\n" + json.dumps(metadata, indent=2) + "\n---\n\nQA fixture body.\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jekyll-command", default="bundle exec jekyll")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    command = shlex.split(args.jekyll_command)
    require(bool(command), "A Jekyll command is required")

    with tempfile.TemporaryDirectory(prefix="portfolio-showcase-") as temporary:
        temporary = Path(temporary).resolve()
        source = temporary / "source"
        def ignored_paths(directory, names):
            ignored = shutil.ignore_patterns(".git", "_site", "node_modules", ".bundle", "__pycache__")(directory, names)
            # Exclude installed gems without removing the theme's _sass/vendor.
            if Path(directory) == root and "vendor" in names:
                ignored.add("vendor")
            return ignored

        shutil.copytree(
            root,
            source,
            ignore=ignored_paths,
        )
        projects = source / "_projects"
        projects.mkdir(exist_ok=True)
        (projects / "qa-visible.md").write_text(fixture_project("qa-visible", True), encoding="utf-8")
        (projects / "qa-hidden.md").write_text(fixture_project("qa-hidden", False), encoding="utf-8")
        image_file = source / "images/projects/qa-test.png"
        image_file.parent.mkdir(parents=True, exist_ok=True)
        image_file.write_bytes(base64.b64decode(
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+a1ioAAAAASUVORK5CYII="
        ))

        def build(label, records):
            (source / "_data/project_repos.yml").write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
            destination = temporary / label
            environment = os.environ.copy()
            environment.setdefault("BUNDLE_GEMFILE", str(root / "Gemfile"))
            result = subprocess.run(
                command + ["build", "--destination", str(destination), "--baseurl", "/qa-preview", "--quiet"],
                cwd=source,
                env=environment,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
            require(result.returncode == 0, "Jekyll build failed for " + label + ":\n" + result.stdout)
            html = (destination / "projects/index.html").read_text(encoding="utf-8")
            require(not (destination / "projects/qa-hidden/index.html").exists(), "A published:false project produced a page")
            entries = ProjectEntries(html).entries
            return destination, html, entries

        def selected(entries):
            return [entry for entry in entries if entry["attrs"].get("data-project-kind") == "repository"]

        def authored_matches(entries, slug):
            return [entry for entry in entries if entry["attrs"].get("data-project-slug") == slug]

        _, html, entries = build("empty", [])
        require(not selected(entries), "Empty selection rendered a repository entry")
        require("selected-github-repositories" not in html, "Empty showcase heading should be hidden")
        require(len(authored_matches(entries, "qa-visible")) == 1, "Empty selection must retain published authored projects; got " + repr([entry["attrs"] for entry in entries]))
        require(not authored_matches(entries, "qa-hidden"), "Hidden authored project appeared")
        require(not authored_matches(entries, "qa-visible")[0]["images"], "Empty image field rendered an image")
        print("PASS: empty selection, separate authored publication, empty images")

        _, html, entries = build("hidden", [
            repo("hidden-repository", show=False, project_slug="qa-visible"),
            repo("quoted-true-is-not-boolean", show="true"),
        ])
        require(not selected(entries), "Only literal show:true may select a repository")
        require("qa-owner/hidden-repository" not in html, "Hidden repository leaked into the page")
        require("quoted-true-is-not-boolean" not in html, "String true unexpectedly selected a repository")
        require(len(authored_matches(entries, "qa-visible")) == 1, "Hiding a repository hid the authored project")
        print("PASS: false and string flags are hidden; authored project stays visible")

        _, html, entries = build("ordered", [
            repo("ordinary-later", order=20),
            repo("featured-later", featured=True, order=8),
            repo("ordinary-first", order=1, image="images/projects/qa-test.png", image_alt="QA screenshot", demo_url="https://example.org/qa-demo"),
            repo("featured-first", featured=True, order=2, image="images/projects/does-not-exist.png"),
            repo("hidden", show=False, featured=True, order=0),
        ])
        repositories = selected(entries)
        require([entry["attrs"]["data-repository"] for entry in repositories] == [
            "qa-owner/featured-first", "qa-owner/featured-later", "qa-owner/ordinary-first", "qa-owner/ordinary-later"
        ], "Featured/order sorting failed")
        require(not repositories[0]["images"], "Missing local screenshot rendered a broken image")
        require(repositories[2]["images"][0]["src"] == "/qa-preview/images/projects/qa-test.png", "Screenshot failed project-baseurl rendering")
        require(repositories[2]["images"][0]["alt"] == "QA screenshot", "Screenshot alt text missing")
        require("https://example.org/qa-demo" in repositories[2]["links"], "External demo URL changed")
        require(all("qa-owner/hidden" not in link for entry in entries for link in entry["links"]), "Hidden repository link leaked")
        print("PASS: featured/order sorting, shown-only links, screenshot checks and external demo")

        destination, html, entries = build("mapped", [
            repo("mapped-first", featured=True, order=1, project_slug="qa-visible", title="QA configured title", description="QA configured description", demo_url="/contact/"),
            repo("mapped-duplicate", order=0, project_slug="qa-visible"),
            repo("hidden-project-standalone", project_slug="qa-hidden", image="images/projects/missing.png"),
            repo("missing-project-standalone", project_slug="does-not-exist"),
        ])
        mapped = authored_matches(entries, "qa-visible")
        require(len(mapped) == 1, "Mapped authored project must render exactly once")
        require(mapped[0]["attrs"].get("data-project-kind") == "repository", "Mapped project remained in authored list")
        require("QA configured title" in mapped[0]["text"] and "QA configured description" in mapped[0]["text"], "Configured title/description did not override authored text")
        require("QA technology" in mapped[0]["text"], "Empty repository tags did not fall back to authored tags")
        require("/qa-preview/projects/qa-visible/" in mapped[0]["links"], "Consolidated detail URL is missing or ignores baseurl")
        require("/qa-preview/contact/" in mapped[0]["links"], "Local demo URL ignores baseurl")
        require("mapped-duplicate" not in html, "Duplicate mapping was rendered")
        standalone = [entry for entry in selected(entries) if "standalone" in entry["attrs"]["data-repository"]]
        require(len(standalone) == 2, "Hidden/missing project mappings should retain the selected repositories")
        require(all(not any("/projects/" in link for link in entry["links"]) for entry in standalone), "Hidden/missing detail page was linked")
        require(all(not entry["images"] for entry in standalone), "Missing/empty images created image elements")
        detail = (destination / "projects/qa-visible/index.html").read_text(encoding="utf-8")
        require("https://github.com/qa-owner/mapped-first" in detail, "Detail page omitted selected repository link")
        require("mapped-duplicate" not in detail, "Detail page used a different mapping than the list")
        print("PASS: mapping consolidation, overrides, fallbacks, duplicate mappings, hidden/missing detail safety")

        _, _, entries = build("fallback", [repo("mapped-fallback", project_slug="qa-visible", title="", description="")])
        mapped = authored_matches(entries, "qa-visible")[0]
        require("QA authored qa-visible" in mapped["text"] and "QA authored description qa-visible" in mapped["text"], "Empty overrides did not preserve authored text")
        require(all(link for entry in entries for link in entry["links"]), "An empty optional field created an empty link")
        print("PASS: empty title/description overrides and optional-link omission")

    print("All project showcase checks passed (5 isolated Jekyll builds).")


if __name__ == "__main__":
    main()
