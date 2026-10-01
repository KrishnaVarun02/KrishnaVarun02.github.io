#!/usr/bin/env python3
"""Test editable gallery, portrait, contact, resume, and publication options.

Run from the repository after bundle install:
    python3 scripts/check_content_options.py

An alternative Jekyll command can be supplied with --jekyll-command.
Requires Python 3, Ruby, and Jekyll. Four actual Jekyll builds run on an isolated
copy of the repository; original content is never changed. No network calls
or external test assets are needed. Run against the supplied starter content.
"""

import argparse
import json
import os
import shlex
import tempfile
from html.parser import HTMLParser
from pathlib import Path
import shutil
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--jekyll-command', default='bundle exec jekyll')
args = parser.parse_args()
command = shlex.split(args.jekyll_command)
assert command, 'A Jekyll command is required'
original = Path(__file__).resolve().parents[1]
temporary = tempfile.TemporaryDirectory(prefix='portfolio-content-options-')
fixture_root = Path(temporary.name).resolve()
source = fixture_root / 'source'

def ignored(directory, names):
    ignored = set(names) & {'.git', '.sass-cache', '_site', 'node_modules', '.bundle', '__pycache__'}
    if Path(directory) == original:
        ignored |= set(names) & {'vendor'}
    return ignored

shutil.copytree(original, source, ignore=ignored)
assert (source / '_sass/vendor').is_dir(), 'Required vendored theme SCSS missing'
config = json.loads(subprocess.check_output([
    'ruby', '-ryaml', '-rjson', '-e', 'puts YAML.load_file(ARGV[0]).to_json', str(source / '_config.yml')
], text=True))
config['baseurl'] = '/qa-editing'

def write_config():
    (source / '_config.yml').write_text(json.dumps(config, indent=2) + '\n')

class HTML(HTMLParser):
    def __init__(self, markup):
        super().__init__()
        self.images = []
        self.links = []
        self.feed(markup)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'img':
            self.images.append(attrs)
        if tag == 'a':
            self.links.append(attrs)

def build(label):
    write_config()
    destination = fixture_root / label
    environment = os.environ.copy()
    environment.setdefault('BUNDLE_GEMFILE', str(original / 'Gemfile'))
    result = subprocess.run(command + [
        'build', '--destination', str(destination), '--quiet'
    ], cwd=source, env=environment, text=True, capture_output=True)
    assert result.returncode == 0, result.stdout + result.stderr
    return destination

def page(destination, path):
    return (destination / path / 'index.html').read_text()

def publication(slug, published, order):
    fields = {
        'layout': 'single', 'title': 'QA ' + slug, 'excerpt': 'QA publication excerpt ' + slug,
        'order': order, 'permalink': '/research/publications/' + slug + '/'
    }
    if published is not None:
        fields['published'] = published
    return '---\n' + json.dumps(fields) + '\n---\n\nQA publication body.\n'

baseline = build('baseline')
assert 'Photos coming soon' in page(baseline, 'gallery')
assert not HTML(page(baseline, 'gallery')).images
assert '<h2>Publications</h2>' not in page(baseline, 'research')
assert 'initials-avatar' in page(baseline, '')
baseline_downloads = [a for a in HTML(page(baseline, 'cv')).links if 'download' in a]
assert len(baseline_downloads) == 2
assert all(a['href'].startswith('/qa-editing/files/') for a in baseline_downloads)
assert not any(a.get('href', '').startswith('tel:') for a in HTML(page(baseline, 'contact')).links)
print('PASS: baseline empty gallery and publications, initials fallback, two downloads with project baseurl')

asset = source / 'images/gallery/qa-square.svg'
asset.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="4" height="4"><rect width="4" height="4" fill="#eee"/></svg>\n')
records = [
    {'image': '/images/gallery/qa-square.svg', 'image_alt': 'QA second square', 'caption': 'QA caption second', 'category': 'QA category', 'order': 20},
    {'image': 'images/gallery/qa-square.svg', 'image_alt': 'QA first square', 'caption': 'QA caption first', 'order': 1, 'visible': True},
    {'image': 'images/gallery/qa-square.svg', 'image_alt': 'QA hidden visible', 'caption': 'QA hidden visible', 'order': 0, 'visible': False},
    {'image': 'images/gallery/qa-square.svg', 'image_alt': 'QA hidden show', 'caption': 'QA hidden show', 'order': 0, 'show': False},
    {'image': 'images/gallery/missing.svg', 'caption': 'QA missing asset', 'order': 0},
    {'image': 'images/gallery/qa-square.svg', 'image_alt': 'QA uncaptioned square', 'caption': '', 'category': '  ', 'order': 30},
]
(source / '_data/gallery.yml').write_text(json.dumps(records, indent=2))
config['author']['avatar'] = 'images/gallery/qa-square.svg'
config['author']['avatar_alt'] = ''
publications = source / '_publications'
publications.mkdir(exist_ok=True)
(publications / 'qa-hidden.md').write_text(publication('hidden', False, 0))
(publications / 'qa-default-hidden.md').write_text(publication('default-hidden', None, 0))
populated = build('gallery-portrait')
gallery = page(populated, 'gallery')
images = HTML(gallery).images
assert [i['alt'] for i in images] == ['Portrait of ' + config['author']['name'], 'QA first square', 'QA second square', 'QA uncaptioned square'], images
assert all(i['src'] == '/qa-editing/images/gallery/qa-square.svg' for i in images)
assert gallery.index('QA caption first') < gallery.index('QA caption second')
assert 'QA category' in gallery
assert gallery.count('<figcaption>') == 2, 'Empty caption/category rendered an orphan element'
assert 'QA hidden' not in gallery and 'QA missing asset' not in gallery and 'missing.svg' not in gallery
assert 'Photos coming soon' not in gallery
assert 'initials-avatar' not in page(populated, '')
assert '<h2>Publications</h2>' not in page(populated, 'research')
assert not (populated / 'research/publications/hidden/index.html').exists()
assert not (populated / 'research/publications/default-hidden/index.html').exists()
print('PASS: gallery order, captions/category/alt, visible/show flags, missing image guard, valid portrait, hidden publications')

asset.unlink()
for key in ['email', 'github', 'linkedin', 'phone', 'bio', 'affiliation']:
    config['author'][key] = ''
config['author']['linkedin'] = '   '
config['author']['location'] = '   '
config['author'].pop('bio', None)
config['author']['show_phone'] = True
(source / 'files/research-cv.pdf').unlink()
(publications / 'qa-later.md').write_text(publication('later', True, 20))
(publications / 'qa-first.md').write_text(publication('first', True, 1))
missing = build('missing-optional-publications')
gallery = page(missing, 'gallery')
assert 'Photos coming soon' in gallery
assert not HTML(gallery).images
assert 'initials-avatar' in gallery
assert 'author__bio' not in gallery
for relative in ['', 'contact', 'cv', 'gallery', 'research']:
    links = HTML(page(missing, relative)).links
    assert all(a.get('href', '').strip() for a in links), (relative, [a for a in links if not a.get('href', '').strip()])
    assert not any(a.get('href', '').startswith(('mailto:', 'tel:')) for a in links), relative
    assert not any(a.get('rel') == 'me' for a in links), relative
cv = page(missing, 'cv')
downloads = [a for a in HTML(cv).links if 'download' in a]
assert len(downloads) == 1 and downloads[0]['href'].endswith('software-engineering-resume.pdf')
assert 'research-cv.pdf' not in cv
research = page(missing, 'research')
assert '<h2>Publications</h2>' in research
assert research.index('QA first') < research.index('QA later')
assert 'QA hidden' not in research and 'QA default-hidden' not in research
assert '/qa-editing/research/publications/first/' in research
assert (missing / 'research/publications/first/index.html').exists()
print('PASS: missing portrait/gallery fallback, blank optional links omitted, missing resume button hidden, publications shown and ordered')

(source / 'files/software-engineering-resume.pdf').unlink()
config['author']['phone'] = '+91 1111111111'
empty_downloads = build('missing-all-resumes')
cv = page(empty_downloads, 'cv')
assert not [a for a in HTML(cv).links if 'download' in a]
assert 'Resume downloads will be available here soon.' in cv
assert any(a.get('href') == 'tel:+911111111111' for a in HTML(page(empty_downloads, 'contact')).links)
print('PASS: all missing PDFs show useful fallback and no download buttons')
print('All editable-content checks passed in four isolated actual Jekyll builds.')
