#!/usr/bin/env python3
"""Repeatable, low-rate checks of public Nazareth-De Pinte service entry points.

This script does not log in, submit forms, bypass access controls, or inspect
resident data. It follows redirects and records only transport metadata.
"""

from __future__ import annotations

import hashlib
import json
import statistics
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path


OUTPUT = Path(__file__).with_name("website-controles.json")

CRITICAL_URLS = [
    ("homepage", "https://www.nazarethdepinte.be/"),
    ("menu", "https://www.nazarethdepinte.be/menu"),
    ("zoeken", "https://www.nazarethdepinte.be/zoeken"),
    ("digitaal-loket-route", "https://www.nazarethdepinte.be/digitaal-loket"),
    ("eGovFlow-actueel", "https://nazarethdepinte.egovflow.be/"),
    ("eGovFlow-oude-link", "https://nazareth.egovflow.be/"),
    ("eGovFlow-privacy-zichtbare-href", "https://nazarethdepinte.egovflow.be/www.nazarethdepinte.be/privacyverklaring"),
    ("afspraken", "https://www.nazarethdepinte.be/afspraak-maken"),
    ("webshop-wegwijzer", "https://www.nazarethdepinte.be/webshop-en-tickets"),
    ("recreatex", "https://nazarethdepinte.recreatex.be/"),
    ("luwio", "https://shop.nazarethdepinte.be/"),
    ("shopify", "https://nazarethdepinte.myshopify.com/"),
    ("gift2give", "https://shop.gift2give.be/nazarethdepinte"),
    ("meldpunt", "https://www.nazarethdepinte.be/bestuur/burgerparticipatie/burgerinitiatieven/iets-melden"),
    ("ivm-melding", "https://www.ivmmilieubeheer.be/e-loket/meldingsformulier-over-inzamelingen"),
    ("fluvius-straatlichten", "https://straatlampen.fluvius.be/"),
    ("spotbooking", "https://nazareth-depinte.spotbooking.be/#/aanvraag/new"),
    ("evenementenformulier", "https://www.nazarethdepinte.be/form/aanvraagformulier-voor-evenement"),
    ("uitdatabank", "https://www.uitdatabank.be/login/nl"),
    ("uitagenda", "https://www.nazarethdepinte.be/vrije-tijd/uit-in"),
    ("oude-uit-zoeklink", "http://www.nazareth.be/agenda/search"),
    ("raadpleegomgeving", "https://nazareth-depinte-raadpleegomgeving.csecho.be/"),
    ("raadstream", "https://streamings.streamovations.be/nazareth-de-pinte/"),
    ("consultatieomgeving", "https://nazarethdepinte.consultatieomgeving.net/burger"),
    ("stratenplan", "https://www.nazarethdepinte.be/vrije-tijd/over-nazareth-de-pinte/stratenplan"),
    ("stratenplan-staging-pdf", "https://fusienazarethdepinte.paddlecms.net/sites/default/files/2025-02/Nazareth-De%20Pinte%20-%20stratenplan%202025.pdf"),
    ("bibliotheek", "https://nazarethdepinte.bibliotheek.be/"),
    ("vacatures", "https://www.nazarethdepinte.be/leven-en-werken/vacatures"),
    ("jobsolutions", "https://www.jobsolutions.be/iframe/nazareth_de_pinte/vacatures"),
    ("vrijwilligers", "https://www.nazarethdepinte.be/vrije-tijd/vrijwilligerswerk/vrijwilligerswerk-zoeken"),
    ("nieuwsbrief", "https://www.nazarethdepinte.be/bestuur/communicatie/schrijf-in-voor-onze-nieuwsbrief"),
    ("opvang-vlaanderen", "https://opvang.vlaanderen/"),
    ("schoolaanmelding", "https://nazarethdepinte.aanmelden.in/"),
    ("oude-depinte-home", "https://www.depinte.be/"),
    ("oude-nazareth-home", "https://www.nazareth.be/"),
    ("home-burgerzaken-link", "https://www.nazarethdepinte.be/leven-en-werken/burger"),
    ("home-ocmw-link", "https://www.nazarethdepinte.be/leven-en-werken/welzijn-en-veiligheid"),
    ("toegankelijkheid", "https://www.nazarethdepinte.be/toegankelijkheidsverklaring"),
    ("robots", "https://www.nazarethdepinte.be/robots.txt"),
    ("sitemap", "https://www.nazarethdepinte.be/sitemap.xml"),
]

PERFORMANCE_URLS = [
    "https://www.nazarethdepinte.be/",
    "https://www.nazarethdepinte.be/zoeken",
    "https://www.nazarethdepinte.be/form/aanvraagformulier-voor-evenement",
    "https://nazarethdepinte.egovflow.be/",
    "https://nazarethdepinte.recreatex.be/",
    "https://shop.nazarethdepinte.be/",
    "https://nazareth-depinte-raadpleegomgeving.csecho.be/",
    "https://nazarethdepinte.bibliotheek.be/",
]


def curl(url: str) -> dict:
    marker = "__AUDIT__"
    fmt = marker + "%{http_code}\t%{url_effective}\t%{time_starttransfer}\t%{time_total}\t%{size_download}\t%{num_redirects}"
    result = subprocess.run(
        ["curl", "-sS", "-L", "--compressed", "--max-time", "30", "-o", "/dev/null", "-w", fmt, url],
        text=True,
        capture_output=True,
        check=False,
    )
    payload = result.stdout.split(marker)[-1].split("\t") if marker in result.stdout else []
    if len(payload) != 6:
        return {"requested_url": url, "curl_exit": result.returncode, "error": result.stderr.strip()[:300]}
    return {
        "requested_url": url,
        "status": int(payload[0]),
        "effective_url": payload[1],
        "ttfb_seconds": float(payload[2]),
        "total_seconds": float(payload[3]),
        "compressed_body_bytes": int(payload[4]),
        "redirects": int(payload[5]),
        "curl_exit": result.returncode,
        "error": result.stderr.strip()[:300],
    }


def main() -> None:
    checked = []
    for label, url in CRITICAL_URLS:
        row = curl(url)
        row["label"] = label
        checked.append(row)
        time.sleep(0.75)

    samples = {}
    for url in PERFORMANCE_URLS:
        values = []
        for _ in range(3):
            values.append(curl(url))
            time.sleep(0.75)
        successful = [v for v in values if v.get("status") == 200]
        samples[url] = {
            "runs": values,
            "median_ttfb_seconds": statistics.median(v["ttfb_seconds"] for v in successful) if successful else None,
            "median_total_seconds": statistics.median(v["total_seconds"] for v in successful) if successful else None,
            "median_compressed_body_bytes": statistics.median(v["compressed_body_bytes"] for v in successful) if successful else None,
        }

    result = {
        "metadata": {
            "checked_at": datetime.now(timezone.utc).isoformat(),
            "role": "onderzoeker digitale dienstverlening; alleen publieke controles",
            "system": "OpenAI Codex / GPT-5",
            "reviewer": None,
            "disposition": "concept; menselijke beoordeling openstaand",
            "method": "curl GET, redirects gevolgd, compressie toegestaan, 30 s timeout, 0,75 s pauze tussen controles",
            "limitations": "Transportmeting vanaf één host; geen Core Web Vitals, velddata, authenticatie, formulierinzending of volledige crawler.",
            "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "critical_entry_points": checked,
        "performance_samples": samples,
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {OUTPUT} with {len(checked)} entry-point checks and {len(samples) * 3} performance samples.")


if __name__ == "__main__":
    main()
