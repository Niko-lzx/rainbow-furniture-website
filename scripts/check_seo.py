"""Offline repository checks; does not prove production HTTP/indexing behavior."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://www.rainbowfurniture.com.cn'

class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.in_head = False
        self.canonicals = []
        self.links = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'head':
            self.in_head = True
        if tag == 'link' and 'canonical' in a.get('rel', '').lower().split():
            self.canonicals.append((a.get('href'), self.in_head))
        if tag == 'a' and a.get('href'):
            self.links.append(a['href'])

    def handle_endtag(self, tag):
        if tag == 'head':
            self.in_head = False


def check():
    errors = []
    files = sorted(ROOT.rglob('*.html'))
    expected = set()
    forbidden = re.compile(r'SEO Article|SEO Landing Page|SEO / GEO Pages|SEO关键词|SEO 关键词|SEO知识库|SEO文章|SEO图片说明|SEO产品页|SEO行业页面|GEO内容沉淀|长尾关键词|建立搜索入口|建议官网|建议正式|后续.*补充|后续.*补齐|可按型号建立单品页|信任型页面|产品页后续|第一批可进入官网|官网新版需要')
    for path in files:
        name = path.relative_to(ROOT).as_posix()
        source = path.read_text(encoding='utf-8')
        page = Page(source)
        url = ORIGIN + ('/' if name == 'index.html' else '/' + name)
        expected.add(url)
        if page.canonicals != [(url, True)]:
            errors.append(f'{name}: canonical {page.canonicals!r}; expected one in head: {url}')
        if forbidden.search(source):
            errors.append(f'{name}: internal editorial copy remains')
        for href in page.links:
            parts = urlsplit(href)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            target = ROOT / unquote(parts.path.lstrip('/')) if parts.path.startswith('/') else path.parent / unquote(parts.path)
            if not target.exists():
                errors.append(f'{name}: missing local link {href}')
    tree = ET.parse(ROOT / 'sitemap.xml')
    ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    assert tree.getroot().tag == '{' + ns['s'] + '}urlset', 'Unexpected sitemap root'
    urls = [x.text for x in tree.findall('s:url/s:loc', ns)]
    errors.extend(f'sitemap duplicate: {u}' for u, n in Counter(urls).items() if n > 1)
    errors.extend(f'sitemap missing: {u}' for u in sorted(expected - set(urls)))
    errors.extend(f'sitemap has no matching HTML: {u}' for u in sorted(set(urls) - expected))
    robots = (ROOT / 'robots.txt').read_text()
    declarations = re.findall(r'^Sitemap:\s*(\S+)\s*$', robots, re.M | re.I)
    if declarations != [ORIGIN + '/sitemap.xml']:
        errors.append(f'robots sitemap declarations: {declarations!r}')
    if re.search(r'^Disallow:\s*/\s*$', robots, re.M | re.I):
        errors.append('robots blocks entire site')
    for error in errors:
        print('FAIL:', error)
    print(f'{len(files)} HTML pages; {len(urls)} sitemap URLs; {len(errors)} errors')
    return bool(errors)

if __name__ == '__main__':
    raise SystemExit(check())
