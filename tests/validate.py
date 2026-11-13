#!/usr/bin/env python3
"""Dependency-free checks against the source HTML delivered by this static site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import json, xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://karimel-kady.online/'
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.tags=[]; self.ids=set(); self.links=[]; self.scripts=[]; self.capture=False; self.buf=''
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); self.tags.append((tag,a))
        if 'id' in a:
            assert a['id'] not in self.ids, f'duplicate id {a["id"]}'
            self.ids.add(a['id'])
        if tag=='a' and 'href' in a: self.links.append(a['href'])
        if tag=='img': assert 'alt' in a, 'image missing alt'
        if tag=='script' and a.get('type')=='application/ld+json': self.capture=True; self.buf=''
    def handle_data(self,data):
        if self.capture: self.buf+=data
    def handle_endtag(self,tag):
        if tag=='script' and self.capture: self.scripts.append(json.loads(self.buf)); self.capture=False
p=Page(); p.feed((ROOT/'index.html').read_text())
def tags(tag, **attrs): return [a for t,a in p.tags if t==tag and all(a.get(k)==v for k,v in attrs.items())]
assert len(tags('title'))==1
for name in ('description','robots','viewport','twitter:card','twitter:title','twitter:description','twitter:image'):
    assert len(tags('meta', name=name))==1, name
for prop in ('og:title','og:description','og:url','og:image','og:type'):
    assert len(tags('meta', property=prop))==1, prop
assert len(tags('link', rel='canonical'))==1 and tags('link', rel='canonical')[0]['href']==BASE
assert 'noindex' not in tags('meta',name='robots')[0]['content'].lower()
assert len(tags('h1'))==1 and p.scripts
assert tags('html')[0].get('lang')=='en'
for href in p.links:
    url=urlparse(href)
    if not url.netloc and not url.scheme:
        if url.fragment: assert unquote(url.fragment) in p.ids, f'broken fragment {href}'
        if url.path and url.path!='/': assert (ROOT/url.path.lstrip('/')).exists(), f'missing local target {href}'
for t,a in p.tags:
    if t in ('link','script','img'):
        target=a.get('href') if t=='link' else a.get('src')
        if target and target.startswith('/') and not target.startswith('//'): assert (ROOT/target.lstrip('/')).is_file(), target
locs=[e.text for e in ET.parse(ROOT/'sitemap.xml').getroot().findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
assert locs==[BASE], locs
robots=(ROOT/'robots.txt').read_text().lower()
assert 'sitemap: '+BASE.lower()+'sitemap.xml' in robots and 'disallow: /' not in robots
assert 'noindex' in (ROOT/'404.html').read_text().lower()
print('PASS: homepage metadata, JSON-LD syntax, links, assets, sitemap, robots and 404 directive')
