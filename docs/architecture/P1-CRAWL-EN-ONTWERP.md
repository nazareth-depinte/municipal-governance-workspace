---
title: "P1 — Inventarisatie en eerste websiteontwerp"
status: in-uitvoering-niet-menselijk-beoordeeld
language: nl-BE
updated: 2026-09-06
agent_role: crawlerontwikkelaar-en-webontwerper
agent_system: OpenAI Codex / GPT-6
reviewer: nog-niet-toegewezen
disposition: lokale-uitvoering
publication_approval: niet-verleend
---

# P1 — Inventarisatie en eerste websiteontwerp

Deze onafhankelijke experimentele bijdrage voert de gebruikersopdracht uit om de huidige publieke website volledig te inventariseren en een modernere website met bestaande branding te beginnen. De broninhoud en de prototypekopij zijn nog niet menselijk beoordeeld. Er is geen externe publicatie uitgevoerd.

## Crawl

Script: `scripts/crawl-p1.py`. Start of hervat vanaf de projectroot met `python3 -u scripts/crawl-p1.py`. Een proceslock voorkomt twee gelijktijdige crawlers. De crawler bewaart na ieder item de wachtrij en resultaten; hervatten verwerkt alleen nog wachtende items. Definitieve fouten blijven in het manifest voor gerichte hercontrole.

Ruw archief: `/private/tmp/nazareth-depinte-p1-crawl/`, toegangsmodus 0700. Dit is tijdelijke opslag buiten alle Git-repositories. De archiveermap bevat robots.txt, sitemap.xml, een private `state.json` met URL’s, tekst en links, en gehashte objectbestanden. Deze map nooit naar de publieke repository kopiëren. Duurzame opslag moet in een afzonderlijk passende informatiezone worden geregeld.

Publieke status: `workspace-web/public/p1-crawl-status.json`. Alleen geaggregeerde aantallen, status, bronhost, tijdstempels en bijdrageverantwoording. Het dashboard haalt deze status iedere 15 seconden op en meldt ontbrekende of verouderde updates.

De bron `https://www.nazarethdepinte.be/robots.txt` vermeldt een crawl-delay van 10 seconden; de sitemap bevatte 1.237 `<loc>`-vermeldingen op 6 september 2026. De crawler volgt interne HTML-links, normale paginering, documenten en rechtstreeks ontdekte CSS/JS/beeldbestanden. Externe dienstverleners blijven verwijzingen. Redirects worden vóór het volgen op hostgrens gecontroleerd. Geen login, formulierinzending, geautomatiseerde beveiligingsscan of productieactie.

Grenzen: 20 MB per resource, robots-uitsluitingen, geen willekeurige filterquery’s, geen JavaScript-uitvoering, geen recursieve externe websites. Downloads kunnen documenten met persoonsgegevens bevatten; daarom blijven alle ruwe objecten buiten de publieke workspace. Nieuw ontdekte URL’s vergroten de wachtrij. Het afronden van die wachtrij is niet hetzelfde als een geslaagde end-to-end transactieaudit.

## Ontwerp

Het prototype leeft onder `/p1/` in de bestaande Astro-app. De gemeentelijke layout staat los van de Workspace Web-shell. De P1-projectpagina linkt naar het prototype en de crawlvoortgang.

Overgenomen bronassets: origineel gemeentelijk logo (`https://www.nazarethdepinte.be/sites/default/files/logo.png`) en de bibliotheekfoto die op 6 september 2026 op de homepage stond. Het logo is ongewijzigd lokaal opgenomen; de foto wordt bij haar gemeentelijke bron geladen. Hergebruikrechten moeten vóór externe publicatie worden bevestigd. De publieke stylesheets bevestigen paars `#56398e`, koraal `#f18673`, groen `#16af95` en zand `#d8c88f`. Het prototype gebruikt lokaal aanwezige Inter en Georgia; de oorspronkelijke CSS noemt Figtree en Gelica, waarvan de licentie-/hostingkeuze nog niet is overgenomen.

De broncode `src/data/p1-services.ts` verwijst voor iedere dienst naar de eerdere gedateerde inventaris. De eerste 28 diensten zijn een expliciete redactionele selectie, geen bewijs dat de volledige site is gemigreerd. Zoek- en themafilters draaien lokaal. Aanvragen, actuele voorwaarden, prijzen en beschikbaarheid blijven bij de officiële bron. Er is geen analytics, account- of dossieropslag.

## Volgende overdracht

### Aanvulling — interactieve wegwijzer, 6 september 2026

De eerste zoekingang bevat nu een interactieve, brongebonden wegwijzer. De module `src/lib/municipal-assistant.ts` gebruikt expliciete intentregels en vaste brongebonden antwoorden over de 28 diensten. Dit is geen aangesloten taalmodel of autonoom uitvoerende agent. De interface meldt die beperking. Vrije vragen worden lokaal gematcht; geen vraag wordt via een API verstuurd, gelogd of in browseropslag bewaard.

De wegwijzer toont herkenbare categorie-iconen en servicekaarten, stappen bij ondersteunde taken, en officiële bronlinks met controledatum. Kinderopvang krijgt een vervolgvraag naar leeftijdsgroep. Een nieuwe onderwerpvraag verlaat die context. Kosten, voorwaarden, persoonlijke aanspraken, onduidelijke beroepsprocedures en onbekende informatie worden niet ingevuld. Navigeren vereist een klik van de gebruiker; er zijn geen automatische aanvragen of besluiten. De redactie en de bronselectie blijven niet-menselijk-beoordeeld.

Validatie: scenariotests voor specifieke routering, vervolgvraag, onderwerpwisseling, onbekende informatie, bronverwijzingen en contextbehoud; Astro-check en productiebuild. Voor een latere generatieve versie zijn een passende backend, providerconfiguratie, servergeheimen, een beoordeeld broncorpus, een afgesproken gegevensstroom en uitgebreidere evaluaties nodig. Die koppeling is niet geactiveerd in deze implementatie.

Bijdrage: interactieve wegwijzer en tests. Inputs: expliciete gebruikersopdracht, bestaande dienstencatalogus en voorbereidingsstappen. Systeem: OpenAI Codex / GPT-6. Reviewer: nog niet toegewezen. Dispositie: lokaal prototype; geen externe publicatie, AI-providerkoppeling of operationele uitvoering.

Na de crawl: uitzonderingen hercontroleren, duplicaten en canonieke URL’s beoordelen, een redirects- en contentmigratiematrix maken, persoonsgegevens uitsluiten en hergebruikrechten bevestigen. Alleen beoordeelde inhoud wordt onderdeel van de nieuwe publieke site. De bestaande projectcriteria voor toegankelijkheid, performance, beheer en menselijke go-live blijven gelden.

Rol: crawlerontwikkelaar en webontwerper. Inputs: gebruikersopdracht, AGENTS.md, eerdere publieke inventaris, live homepage, robots.txt, sitemap, logo en stylesheets. Systeem: OpenAI Codex / GPT-6. Reviewer: nog niet toegewezen. Dispositie: lokale uitvoering; geen gemeentelijke bekrachtiging of externe verzending.

## Afscheiding website-repository — 6 september 2026

Op gebruikersverzoek is de website-implementatie verplaatst naar de zelfstandige lokale Git-repository `repos/municipal-website`. Deze bevat eigen pakketbestanden, afhankelijkheden, tests, assets en broninventaris; de bouw leest niets uit de bovenliggende workspace. De website draait lokaal op http://127.0.0.1:4328/, met de publieke agenda op `/agenda/`. De bestaande `/p1/`- en `/p2/agenda/`-adressen in de Workspace UI bevatten alleen nog doorverwijzingen. Het crawlproces en de private ruwe opslag blijven bij de governance-workspace.

De Workspace registreert het nieuwe repository in `repos/_registry.yml` en linkt ernaar vanuit het project Publieke website en het repositoryoverzicht. Geen Git-remote ingesteld, niets extern gepubliceerd. Bijdrage: websiteontwikkelaar en repositorybeheerder; inputs gebruikersopdracht en bestaande code; systeem OpenAI Codex / GPT-6; reviewer nog niet toegewezen; dispositie lokale extractie.
