"""Extract six allowlisted public event summaries from the existing private crawl.

Role: public-event sample curator. System: OpenAI Codex / GPT-6.
Input: municipal HTML captured on 2026-09-06 and curated paraphrases below.
Reviewer: unassigned. Disposition: local prototype, no publication approval.
Only selected presentation fields leave the private crawl; no contacts or raw HTML.
"""
import json
import re
from pathlib import Path
from urllib.parse import urljoin
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
CRAWL = Path('/private/tmp/nazareth-depinte-p1-crawl')
BASE = 'https://www.nazarethdepinte.be/'
SELECTION = {
    'monkey-time-band': 'Monkey Time speelt tijdens Brouwsels op Straat op het podium aan De Brouwerij in Eke.',
    'kermisweekend-in-eke': 'Kermisattracties op het Kerkplein in Eke, met extra activiteiten van de Vriendenkring tijdens het kermisweekend.',
    'auditie-danceteam-kids-2026-2027-maandag-17u10-456lrj-1mbr': 'Dansauditie van DanceReaction: op 7 september wordt de choreografie aangeleerd, op 14 september volgt de auditie. Bekijk de deelnamevoorwaarden bij de bron.',
    'groovy-foundations-2026-2027-maandag-18u30-123mbr': 'Lessenreeks van DanceReaction rond de basis van hiphop en streetstyles. De bron vermeldt meerdere maandagsessies in het schooljaar 2026–2027.',
    'mariale-ommegang-nazareth': 'Een ommegang van ongeveer vier kilometer langs dertien kapelletjes. Het programma begint en eindigt bij de Onze-Lieve-Vrouw-Geboortekerk in Nazareth.',
    'a-few-years-to-learn-a-lifetime-to-master-overzichtstentoonstelling-ludo-kerckhoven': 'Overzichtstentoonstelling met grafisch werk en zeefdrukken van Ludo Kerckhoven in Kunsthuis DORP 16.',
}
state = json.loads((CRAWL / 'state.json').read_text())
events = []
for slug, description in SELECTION.items():
    url = urljoin(BASE, slug)
    record = state['items'][url]
    assert record['state'] == 'captured' and record['status'] == 200
    soup = BeautifulSoup((CRAWL / 'objects' / record['object']).read_text(), 'html.parser')
    main = soup.select_one('main')
    def value(selector):
        element = main.select_one(selector)
        assert element is not None, (url, selector)
        return element.get_text(' ', strip=True)
    dates = [item.get_text(' ', strip=True) for item in main.select('.field--date-time .item')]
    assert dates
    first_date = re.search(r'(\d{2})/(\d{2})/(\d{4})', dates[0])
    assert first_date
    image = main.select_one('img[src*="/activity_image/"]')
    assert image is not None
    events.append({
        'title': value('h1'), 'source': url, 'observedAt': record['observed_at'],
        'sourceSha256': record['sha256'], 'description': description,
        'category': value('.field--activity-type'),
        'village': value('.field--address .locality').split(' (')[0].title(),
        'place': value('.field--address .given-name'), 'dates': dates,
        'day': first_date[1], 'month': first_date[2], 'year': first_date[3],
        'image': urljoin(BASE, image['src']),
        'imageAttribution': 'Beeld via de gemeentelijke evenementpagina; geen afzonderlijke beeldcredit gevonden.',
    })
output = ROOT / 'repos/municipal-website/src/data/p2-events.json'
output.write_text(json.dumps(events, ensure_ascii=False, indent=2) + '\n')
print(f'Extracted {len(events)} public event records to {output}')
