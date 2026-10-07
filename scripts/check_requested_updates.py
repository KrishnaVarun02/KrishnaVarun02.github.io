#!/usr/bin/env python3
"""Check the requested portfolio selections and navigation in a built site.

Usage:
    python3 scripts/check_requested_updates.py _site
    python3 scripts/check_requested_updates.py _site --baseurl /portfolio

This is a regression snapshot for the explicitly requested repository lists,
navigation, coursework, and extracurricular link. It reads generated HTML and
files only; it does not change content or call GitHub. Uses Python's standard
library. Update the expectations when intentionally changing those selections.
"""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


OWNER = "https://github.com/KrishnaVarun02/"
MORE = "https://github.com/KrishnaVarun02?tab=repositories"
RESEARCH = [
    ("MARL", "/research/reward-decomposition/"),
    ("LSTM_AI", "/research/residential-load-forecasting/"),
    ("local-credit-diagnostics", "/research/local-credit-diagnostics/"),
    ("patchbudget", "/research/patchbudget/"),
]
PROJECTS = [
    ("IssueForge-Multi-Agent-GitHub-Issue-to-PR-Orchestrator", "/projects/issueforge/"),
    ("Turbo-Compressor", "/projects/turbo-compressor/"),
    ("Parvathi", "/projects/parvathi/"),
    ("moodmix", "/projects/moodmix/"),
    ("worklens", "/projects/worklens/"),
]
EDUCATION = [
    ("Turbo-Compressor", "/projects/turbo-compressor/"),
    ("sclp-compiler", "/education/projects/sclp-compiler/"),
    ("p2p-cryptocurrency-simulator", "/education/projects/p2p-cryptocurrency-simulator/"),
    ("champsim-architecture-lab", "/education/projects/champsim-architecture-lab/"),
    ("xv6-enhancements", "/education/projects/xv6-enhancements/"),
]
NAVIGATION = ["Experience", "Research", "Projects", "Education", "CV", "Gallery", "Achievements", "Community", "Contact"]
VOID_ELEMENTS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class Node:
    def __init__(self, tag, attrs=None, parent=None):
        self.tag = tag
        self.attrs = dict(attrs or [])
        self.parent = parent
        self.children = []

    def has_class(self, name):
        return name in self.attrs.get("class", "").split()

    def descendants(self, tag=None):
        for child in self.children:
            if isinstance(child, Node):
                if tag is None or child.tag == tag:
                    yield child
                yield from child.descendants(tag)

    def text(self):
        return " ".join(" ".join(child.text() if isinstance(child, Node) else child for child in self.children).split())

    def hrefs(self):
        return [node.attrs.get("href", "") for node in self.descendants("a")]


class Document(HTMLParser):
    def __init__(self, markup):
        super().__init__(convert_charrefs=True)
        self.root = Node("document")
        self.stack = [self.root]
        self.feed(markup)

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs, self.stack[-1])
        self.stack[-1].children.append(node)
        if tag not in VOID_ELEMENTS:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID_ELEMENTS:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def only(nodes, message):
    nodes = list(nodes)
    require(len(nodes) == 1, message + " (found " + str(len(nodes)) + ")")
    return nodes[0]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path, help="Built Jekyll destination, such as _site")
    parser.add_argument("--baseurl", default="", help="Base path used by this build, such as /portfolio")
    args = parser.parse_args()
    site = args.site.resolve()
    baseurl = "/" + args.baseurl.strip("/") if args.baseurl.strip("/") else ""
    require(site.is_dir(), "Built destination does not exist: " + str(site))

    def local(path):
        return baseurl + path

    def load(path):
        output = site / path.lstrip("/") / "index.html"
        require(output.is_file(), "Missing built page: " + str(output))
        document = Document(output.read_text(encoding="utf-8")).root
        content = only((node for node in document.descendants("main") if node.attrs.get("id") == "content"), "Page must have one main content region: " + path)
        return document, content

    def check_selection(path, expected, kind):
        document, content = load(path)
        if kind == "research":
            entries = [node for node in content.descendants("section") if node.has_class("content-entry")]
        else:
            entries = [node for node in content.descendants("article") if node.has_class("project-entry")]
        require(len(entries) == len(expected), path + " must have exactly " + str(len(expected)) + " selected entries")
        actual_order = []
        for entry, (repository, detail) in zip(entries, expected):
            github_links = list(dict.fromkeys(href for href in entry.hrefs() if href.startswith(OWNER)))
            require(github_links == [OWNER + repository], path + " contains a missing, extra, or out-of-order repository: " + repr(github_links))
            actual_order.append(github_links[0])
            require(local(detail) in entry.hrefs(), repository + " has no expected detail link: " + local(detail))
            _, detail_content = load(detail)
            require(OWNER + repository in detail_content.hrefs(), repository + " detail page has no matching GitHub link")
        require(len(set(actual_order)) == len(expected), path + " contains duplicate repository entries")
        more_links = [node for node in content.descendants("a") if "Show more on GitHub" in node.text()]
        require(len(more_links) == 1 and more_links[0].attrs.get("href") == MORE, path + " has an incorrect or duplicate Show more on GitHub link")
        print("PASS: " + kind + " exact order, single entries, detail pages, repository links and Show more")
        return document, content

    research, research_content = check_selection("/research/", RESEARCH, "research")
    projects, project_content = check_selection("/projects/", PROJECTS, "projects")
    education, education_content = check_selection("/education/", EDUCATION, "education")
    require(local("/projects/turbo-compressor/") in project_content.hrefs() and local("/projects/turbo-compressor/") in education_content.hrefs(), "Turbo Compressor must reuse one detail page across both selections")

    for page in site.rglob("*.html"):
        document = Document(page.read_text(encoding="utf-8")).root
        # Parse both complete navigation lists rather than counting links from
        # the sidebar/footer or assuming CSS makes hidden submenu links usable.
        navs = list(document.descendants("nav"))
        desktop = only((nav for nav in navs if nav.has_class("desktop-nav")), "Missing desktop navigation in " + str(page))
        mobile = only((nav for nav in navs if nav.attrs.get("aria-label") == "Mobile navigation"), "Missing mobile navigation in " + str(page))
        for navigation in (desktop, mobile):
            nav_list = only((node for node in navigation.descendants("ul") if node.has_class("nav-links")), "Navigation must have one direct link list")
            items = [node for node in nav_list.children if isinstance(node, Node) and node.tag == "li"]
            direct_links = []
            for item in items:
                direct_links.append(only((node for node in item.children if isinstance(node, Node) and node.tag == "a"), "Navigation item must expose a direct link"))
            require([node.text() for node in direct_links] == NAVIGATION, "Navigation labels/order differ in " + str(page))
            require([node.attrs.get("href") for node in direct_links] == [local("/" + name.lower() + "/") for name in NAVIGATION], "Navigation URLs ignore the requested pages/baseurl")
            require(not list(navigation.descendants("details")), "A More submenu remains inside navigation")
        require(not any(node.text().strip().lower() == "more" for node in document.descendants("summary")), "A More menu remains")
        text = document.text().casefold()
        require("rent-a-bike" not in text and "blog book" not in text, "A removed project remains in generated HTML: " + str(page))
        for href in document.hrefs():
            decoded = unquote(href).casefold()
            require("/projects/rent-a-bike" not in decoded and "/projects/blog-book" not in decoded, "Removed project still has a link")
            require("transcript" not in decoded, "Raw transcript link was exposed: " + href)
    for slug in ("rent-a-bike", "blog-book"):
        require(not (site / "projects" / slug / "index.html").exists(), "Removed project detail page still exists: " + slug)
    print("PASS: nine direct desktop/mobile links, no More submenu, removed projects absent")

    _, achievements = load("/achievements/")
    _, community = load("/community/")
    require(local("/community/#extracurricular-activities") in achievements.hrefs(), "Achievements lacks the extracurricular activities link")
    require(not any(urlsplit(href).fragment in {"oracle-global-tech-program", "leadership"} for href in achievements.hrefs()), "Old leadership detail link remains on Achievements")
    anchor = only((node for node in community.descendants() if node.attrs.get("id") == "extracurricular-activities"), "Community must contain one extracurricular anchor")
    require("extracurricular activities" in anchor.text().casefold(), "Extracurricular anchor has the wrong heading")
    print("PASS: extracurricular link and target, old achievement leadership link removed")

    course_lists = [node for node in education_content.descendants("ul") if node.has_class("course-list")]
    courses = [node.text() for listing in course_lists for node in listing.children if isinstance(node, Node) and node.tag == "li"]
    require(course_lists and len(courses) == 20, "Relevant coursework must contain the 20 selected software/AI entries (17 transcript plus 3 resume)")
    require(any(node.text() == "Relevant coursework" for node in education_content.descendants("h2")), "The coursework heading must be Relevant coursework")
    course_text = "\n".join(courses).casefold()
    coverage = [
        "Data Structures", "Algorithms", "Operating Systems", "Database Management System", "Software Engineering",
        "Computer Networks", "Compiler Design", "Theory of Computation", "Artificial Intelligence",
        "Intelligent Computing", "Soft Computing", "Computer Architecture", "Discrete Maths", "Probability and Statistics",
        "Mathematical Methods", "Operations Research", "Game Theory", "Object Oriented Programming",
        "Distributed Systems", "Machine Learning Fundamentals",
    ]
    course_names = [re.sub(r"\s+\([A-Z]{2,3}-\d{3}[A-Z]?(?:,\s*[A-Z]{2,3}-\d{3}[A-Z]?)*\)$", "", course).casefold() for course in courses]
    require(set(course_names) == {name.casefold() for name in coverage}, "Relevant software/AI coursework differs from the requested selection: " + repr(course_names))
    code_pattern = r"\b[A-Z]{2,3}-\d{3}[A-Z]?\b"
    require(sum(bool(re.search(code_pattern, course)) for course in courses) == 17, "Exactly 17 transcript-derived course entries must retain their codes")
    require(sum(len(re.findall(code_pattern, course)) for course in courses) == 18, "Transcript-derived courses must retain all 18 course codes, including both Artificial Intelligence codes")
    artificial_intelligence = [course for course in courses if course.startswith("Artificial Intelligence")]
    require(len(artificial_intelligence) == 1 and "CSE-241" in artificial_intelligence[0] and "EC-422" in artificial_intelligence[0], "Artificial Intelligence must retain both transcript codes")
    # Restrict this check to course-list <li> content: authored education project
    # entries and the site's research/project pages remain intentionally visible.
    excluded_courses = [
        "Exploratory Project", "UG Project", "Industrial Project", "Industrial Training", "Seminar",
        "Biology", "Humanities", "Chemistry", "Sociology", "Psychology", "Philosophy", "Literature",
        "English", "Communication Skills", "Physical Education", "Environmental Studies",
        "Physics", "Electrical Engineering", "Computer Programming", "Information Technology Workshop",
        "Engineering Mathematics", "Computer Graphics", "Computer System Organization", "Digital Circuits", "Digital Logic and Design",
    ]
    require(not any(name.casefold() in course_text for name in excluded_courses), "Coursework outside the curated software/AI selection remains: " + repr([name for name in excluded_courses if name.casefold() in course_text]))
    pdf_files = {path.relative_to(site).as_posix() for path in site.rglob("*.pdf")}
    require(pdf_files == {"files/software-engineering-resume.pdf", "files/research-cv.pdf"}, "Unexpected PDF exposed; only the two requested resume downloads belong in this build: " + repr(pdf_files))
    print("PASS: 20 relevant software/AI courses, 17 transcript entries and 18 codes, excluded unrelated courses, no transcript download")
    print("All requested-update checks passed.")


if __name__ == "__main__":
    main()
