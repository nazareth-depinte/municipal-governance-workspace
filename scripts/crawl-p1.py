#!/usr/bin/env python3
"""Resumable, serial public website crawl. Raw material never enters Git."""
import argparse
import hashlib
import json
import os
import re
import time
import urllib.parse as U
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from datetime import datetime, timezone

import requests
from bs4 import BeautifulSoup

BASE = 'https://www.nazarethdepinte.be'
ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = Path('/private/tmp/nazareth-depinte-p1-crawl')
PROGRESS = ROOT / 'workspace-web/public/p1-crawl-status.json'
AGENT = 'CivicWorkspaceResearch/1.0 (read-only municipal website inventory)'

def stamp():
    return datetime.now(timezone.utc).isoformat()

def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2))
    temp.replace(path)

def normalize(url, parent=BASE + '/'):
    p = U.urlsplit(U.urljoin(parent, url))
    if p.scheme not in ('http', 'https') or p.hostname not in ('www.nazarethdepinte.be', 'nazarethdepinte.be', 'www.nazareth.be', 'nazareth.be', 'www.depinte.be', 'depinte.be'):
        return None
    if any(x in p.path for x in ['/admin', '/user/', '/comment/', '/node/add', '/media/oembed']):
        return None
    # Content pagination is finite; arbitrary faceted searches are not.
    query = U.parse_qs(p.query)
    if query and not p.path.startswith(('/sites/', '/themes/', '/core/', '/modules/', '/profiles/')):
        if set(query) != {'page'} or not query['page'][0].isdigit():
            return None
    return U.urlunsplit(('https', 'www.nazarethdepinte.be', p.path or '/', p.query, ''))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-items', type=int, default=0)
    args = parser.parse_args()
    ARCHIVE.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(ARCHIVE, 0o700)
    import fcntl
    lock = (ARCHIVE / 'crawl.lock').open('w')
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    state_path = ARCHIVE / 'state.json'
    state = json.loads(state_path.read_text()) if state_path.exists() else {
        'started_at': stamp(), 'items': {}, 'last_request': 0, 'sitemap_entries': 0,
        'external_links': [], 'state': 'running', 'pid': os.getpid()}
    state.update(state='running', pid=os.getpid())
    session = requests.Session()
    session.headers.update({'User-Agent': AGENT})

    def fetch(url):
        time.sleep(max(0, 10 - (time.time() - state['last_request'])))
        state['last_request'] = time.time()
        # Validate every redirect destination before following it.
        for hop in range(6):
            response = session.get(url, timeout=(15, 45), allow_redirects=False, stream=True)
            if response.is_redirect:
                target = normalize(response.headers.get('Location', ''), url)
                response.close()
                if not target: raise ValueError('external_redirect')
                time.sleep(10)
                state['last_request'] = time.time()
                url = target
                continue
            body = bytearray()
            for chunk in response.iter_content(65536):
                body.extend(chunk)
                if len(body) > 20 * 1024 * 1024:
                    response.close()
                    raise ValueError('resource_over_20mb')
            response.close()
            return response, bytes(body)
        raise ValueError('redirect_limit')

    robots_path = ARCHIVE / 'robots.txt'
    if not robots_path.exists():
        r, raw = fetch(BASE + '/robots.txt')
        r.raise_for_status()
        robots_path.write_bytes(raw)
    # Drupal uses Google's wildcard and end-anchor syntax. Longest rule wins.
    rules = []
    active = False
    for line in robots_path.read_text().splitlines():
        key, sep, value = line.partition(':')
        value = value.strip()
        if key.lower() == 'user-agent': active = value == '*'
        if active and key.lower() in ('allow', 'disallow') and value:
            pattern = re.escape(value).replace(r'\*', '.*').replace(r'\$', '$')
            rules.append((len(value.replace('*', '')), key.lower() == 'allow', re.compile('^' + pattern)))

    def allowed(url):
        p = U.urlsplit(url)
        path = p.path + ('?' + p.query if p.query else '')
        matches = [(length, allow) for length, allow, pattern in rules if pattern.search(path)]
        return max(matches)[1] if matches else True

    def enqueue(url, kind='page'):
        url = normalize(url)
        if url and url not in state['items']:
            state['items'][url] = {'kind': kind, 'state': 'pending' if allowed(url) else 'robots_excluded'}

    def progress():
        counts = Counter(x['state'] for x in state['items'].values())
        kinds = Counter(x['kind'] for x in state['items'].values())
        value = {'updated_at': stamp(), 'started_at': state['started_at'], 'state': state['state'],
                 'source': BASE, 'sitemap_entries': state['sitemap_entries'], 'discovered': len(state['items']),
                 'counts': dict(counts), 'kinds': dict(kinds), 'delay_seconds': 10,
                 'review_status': 'niet-menselijk-beoordeeld', 'raw_archive': 'tijdelijk-lokaal-buiten-git',
                 'agent_role': 'publieke-website-inventarisatie', 'agent_system': 'OpenAI Codex / GPT-6',
                 'reviewer': 'nog-niet-toegewezen', 'disposition': 'lokale-inventarisatie'}
        write_json(state_path, state)
        write_json(PROGRESS, value)

    if not state['sitemap_entries']:
        r, raw = fetch(BASE + '/sitemap.xml')
        r.raise_for_status()
        (ARCHIVE / 'sitemap.xml').write_bytes(raw)
        tree = ET.fromstring(raw)
        entries = [x.text for x in tree.iter() if x.tag.endswith('}loc')]
        state['sitemap_entries'] = len(entries)
        for path in ['/', '/contact', '/afspraak-maken', '/leven-en-werken/burger', '/vrije-tijd/organiseren', '/bestuur/burgerparticipatie/burgerinitiatieven/iets-melden', '/vrije-tijd/uit-in']:
            enqueue(BASE + path)
        # Brand and styles first, so the design can use verified tokens.
        homepage = Path('/private/tmp/p1-home.html')
        if homepage.exists():
            soup = BeautifulSoup(homepage.read_text(), 'html.parser')
            enqueue(BASE + '/sites/default/files/logo.png', 'brand')
            for tag in soup.select('link[rel=stylesheet]'):
                enqueue(U.urljoin(BASE, tag.get('href', '')), 'brand')
        for url in entries: enqueue(url)
    progress()
    done = 0
    while True:
        pending = [(u, row) for u, row in state['items'].items() if row['state'] == 'pending']
        if not pending: break
        priority = {'brand': 0, 'page': 1, 'document': 2, 'asset': 3}
        pending.sort(key=lambda item: priority.get(item[1]['kind'], 9))
        url, row = pending[0]
        started = time.monotonic()
        try:
            r, raw = fetch(url)
            row.update(status=r.status_code, bytes=len(raw), seconds=round(time.monotonic() - started, 3), observed_at=stamp())
            if r.status_code in (429, 503):
                row['retries'] = row.get('retries', 0) + 1
                row['state'] = 'failed' if row['retries'] >= 3 else 'pending'
                progress()
                time.sleep(max(60, int(r.headers.get('Retry-After', '60')) if r.headers.get('Retry-After', '').isdigit() else 60))
                continue
            row['state'] = 'captured' if r.ok else 'failed'
            row['content_type'] = r.headers.get('Content-Type', '')
            row['sha256'] = hashlib.sha256(raw).hexdigest()
            key = hashlib.sha256(url.encode()).hexdigest()
            if r.ok:
                folder = ARCHIVE / 'objects'
                folder.mkdir(exist_ok=True)
                (folder / key).write_bytes(raw)
                row['object'] = key
                if 'text/html' in row['content_type']:
                    soup = BeautifulSoup(raw, 'html.parser')
                    row['title'] = soup.title.get_text(' ', strip=True) if soup.title else ''
                    main = soup.select_one('main') or soup
                    row['text'] = main.get_text(' ', strip=True)
                    row['links'] = []
                    for a in soup.select('a[href]'):
                        target = U.urljoin(url, a['href'])
                        if target.startswith(('https://', 'http://')):
                            row['links'].append({'url': target, 'label': a.get_text(' ', strip=True)[:200]})
                            path = U.urlsplit(target).path.lower()
                            kind = 'document' if re.search(r'\.(pdf|docx?|xlsx?|csv|zip)$', path) else 'page'
                            enqueue(target, kind)
                    for tag, attr in [('img','src'),('script','src'),('link','href'),('source','src')]:
                        for el in soup.select(f'{tag}[{attr}]'):
                            if tag == 'link' and not set(el.get('rel', [])) & {'stylesheet', 'icon', 'preload'}: continue
                            enqueue(U.urljoin(url, el[attr]), 'asset')
                elif 'css' in row['content_type']:
                    for target in re.findall(r'url\([\s\"\']*([^\)\"\']+)', raw.decode('utf-8', errors='replace')):
                        enqueue(U.urljoin(url, target.strip()), 'asset')
        except Exception as exc:
            row.update(state='failed', error=str(exc)[:200], observed_at=stamp())
        done += 1
        progress()
        print(json.dumps({'done': done, 'discovered': len(state['items']), 'kind': row['kind'], 'state': row['state']}, ensure_ascii=False), flush=True)
        if args.max_items and done >= args.max_items:
            state['state'] = 'paused'
            progress()
            return
    state['state'] = 'finished_with_exclusions' if any(x['state'] != 'captured' for x in state['items'].values()) else 'finished'
    progress()

if __name__ == '__main__':
    main()
