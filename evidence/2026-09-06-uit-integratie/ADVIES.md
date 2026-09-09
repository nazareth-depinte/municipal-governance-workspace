---
title: "P2 — UiT integreren in een eigen evenementenloket"
status: voorstel-niet-menselijk-beoordeeld
language: nl-BE
updated: 2026-09-06
agent_role: integratieonderzoeker-en-prototypebouwer
agent_system: OpenAI Codex / GPT-6
reviewer: nog-niet-toegewezen
disposition: lokaal-integratieadvies-en-agendaprototype
publication_approval: niet-verleend
---

# P2 — UiT integreren in een eigen evenementenloket

**Advies: bouw de gebruikerservaring zelf en gebruik UiTdatabank voor het publieke vrijetijdsaanbod.** Begin met een eigen agenda via de Search API. Bouw de voorbereiding van een gemeentelijke evenementenaanvraag als afzonderlijke stroom. Overweeg de Entry API daarna voor gecontroleerde publicatie van evenementinformatie.

Dit is een ontwerpvoorstel, geen gemeentelijk besluit. Onderzoek: **6 september 2026**. De proef op [Agendaontwerp](http://127.0.0.1:4328/agenda/) gebruikt zes echte evenementen uit de gemeentelijke website, vastgelegd op 6 september 2026. Er is nog geen API-integratie geregistreerd, geen live API-oproep getest en niets gepubliceerd.

## Wat biedt UiT zelf?

publiq beschrijft de **Search API (JSON-LD)** expliciet als toegang tot ruwe eventdata voor een eigen gepersonaliseerde agenda. Daarmee kunnen we zelf kaarten, thumbnails, filters en detailpagina's ontwerpen. De **Entry API** ondersteunt synchronisatie van evenementen uit een eigen toepassing naar UiTdatabank en verdere verspreiding via UiT-kanalen. Widgets zijn de snelle inbouwoptie; de vormgeving hoeft onze eigen agenda niet te bepalen. [Officiële productbeschrijving, geraadpleegd 06-09-2026](https://www.publiq.be/nl/projecten/publiq-platform).

| Route | Wat we zelf bouwen | Afweging en advies |
|---|---|---|
| UiT-widget | Omringende pagina en beschikbare widgetinstellingen | Snel te plaatsen. Exacte vormgevingsgrenzen nog niet getest; minder passend bij de gevraagde eigen gebruikerservaring. |
| **Search API + eigen agenda** | Kaarten, navigatie, zoeken, filters, details en gegevensadapter | **Aanbevolen.** Hergebruik van het aanbod met vrijheid over de presentatie. Meer ontwikkel- en onderhoudswerk dan een widget. |
| Eigen evenementendatabase | Ook invoer, beheer, actualisering en verspreiding | Voorlopig niet nodig; risico op dubbele invoer en uiteenlopende versies. |
| Entry API + eigen invoer | Gemachtigde publicatie en synchronisatie | Latere uitbreiding; eerst rechten, eigenaarschap en foutafhandeling valideren. |

## Kosten en toegang

De gepubliceerde Basic-prijs is **€125 per jaar voor één website**, voor Search API of widgets. Custom is op afspraak. Data toevoegen via UiTdatabank of Entry API is gratis. UiTnetwerkleden komen mogelijk in aanmerking voor een gratis integratie; de gemeentelijke aanspraak is **niet bevestigd**. Dit zijn leverancierskosten, exclusief onze bouw, hosting en beheer. [Prijzen, geraadpleegd 06-09-2026](https://www.publiq.be/nl/projecten/publiq-platform/prijzen).

De voorwaarden noemen gratis testtoegang, productie vanaf €125 exclusief btw, sleutels per website/app voor Search en per organisatie voor Entry, bronvermelding met een link naar UiTinVlaanderen en een limiet van 60.000 API-oproepen per project per dag. Ze behandelen ook teruglevering van correcties, beeldrechten en privacygevoelige API-informatie. Test- en productieafspraken moeten bij registratie worden bevestigd. [Gebruiksvoorwaarden, versie 16-09-2024, geraadpleegd 06-09-2026](https://www.publiq.be/nl/projecten/publiq-platform/gebruiksvoorwaarden).

## Twee stromen in één herkenbare omgeving

**Voor bezoekers:** UiTdatabank → Search API → onze serveradapter en tijdelijke publieke cache → eigen agenda op P1.

**Voor organisatoren:** eigen voorbereidingsassistent → conceptaanvraag in een beveiligde omgeving → bevoegde officiële aanvraagprocedure.

**Optioneel later:** organisator controleert een afzonderlijke openbare aankondiging → bevestigt publicatie → Entry API → UiTdatabank.

Een vermelding in UiT bewijst geen gemeentelijke toelating. Een aanvraag kan niet-publieke bijlagen bevatten en nooit automatisch integraal naar UiT gaan. Publicatiestatus en dossierstatus krijgen afzonderlijke velden en bevoegdheden. De agent kan ontbrekende informatie signaleren en tekst voorbereiden; een gemachtigde mens bevestigt indiening en publicatie.

Dit is onze voorgestelde taakverdeling. De onderzochte UiT-productbeschrijving beschrijft publicatie van vrijetijdsaanbod; zij bewijst geen dekking van het lokale vergunningenproces.

## Technisch ontwerp voor de eerste koppeling — voorstel

1. **Een serveradapter.** Bewaar eventuele secrets buiten browser en Git. Vertaal bronrecords naar een klein presentatiemodel: bron-ID, titel, beschrijving, locatie, categorie, tijdstippen, prijsinformatie, afbeelding met credit, bronlink, evenementstatus en ophaaltijd. Toon broninhoud als tekst of gecontroleerd gesaneerde HTML.
2. **Dekking expliciet controleren.** Valideer de geografische selectie voor Nazareth, Eke, De Pinte en Zevergem na de fusie. Controleer meertalige titels, herhalende evenementen en paginering met echte testresponses. “Alle evenementen” betekent alle passende beschikbare UiT-records; een activiteit die niemand invoert verschijnt niet vanzelf.
3. **Eigen toegankelijke presentatie.** Vaste thumbnailverhoudingen, een nette terugvalillustratie, datum en plaats direct zichtbaar, toetsenbordbediening, zoekterm en filters in de URL. Geen prijzen, toegankelijkheidsvoorzieningen of doelgroepen invullen als de bron ze niet bevestigt.
4. **Actualiteit en uitval.** Spreek een verversingsinterval af, toon actualiteit bij een verouderde cache en bied bij uitval een bronlink. Verwerk gewijzigde data, verwijderingen en annuleringen; publiceer niet onbeperkt oude informatie. Dedupliqueer op bron-ID en presenteer lokale tijden in Europe/Brussels.
5. **Later schrijven.** Koppel een reeds bestaand UiT-record voordat een nieuw record wordt gemaakt. Leg vast wie het mag aanpassen. Maak herhaalde verzending veilig en toon synchronisatiefouten aan de organisator. Geen automatische statusoverdracht van gemeentelijk dossier naar UiT.

De precieze endpointparameters, authenticatiemethode, toegangsrechten, beeldvelden en cachevoorwaarden zijn nog te valideren tegen de actuele [technische documentatie](https://docs.publiq.be/) en een eigen testintegratie. Er is geen werkende connector gesimuleerd.

## Wat is nu gebouwd?

- Een lokaal agendaontwerp in de bestaande huisstijl met zes echte evenementen, originele bronafbeeldingen en uitklapbare details.
- Werkende filters op zoekterm, deelgemeente en activiteitstype, deelbare filter-URL en een lege-resultatenmelding.
- Directe toegang tot het prototype en dit advies vanuit P2 in de Workspace Web UI.

De huidige workspace is een statische Astro-site. Een live agenda heeft aanvullend een servercomponent of een geplande gegevensimport nodig. Dat is nog niet ingericht. Het aanvraagformulier, veilige dossieropslag en UiT-synchronisatie zijn volgende bouwstappen.

## Volgende uitvoerbare stap

Richt onder de juiste organisatie een Search-testintegratie in via het [publiq-platform](https://platform.publiq.be/), met secrets in een beveiligde runtime. Bevestig eerst wie de integratie beheert en of de gemeentelijke UiTnetwerkovereenkomst deze toepassing dekt. Test vervolgens geografische dekking, volledige paginering, beeldcredits, annuleringen, een lege respons en uitval. Pas daarna vervangen we de vaste selectie uit de scrape door een automatisch bijgewerkte feed.

Voor de gemeentelijke aanvraagstroom moeten daarnaast de eigenaar en mogelijkheden van het bestaande officiële formulier, eGovFlow en reservaties worden vastgesteld. Deze UiT-verkenning beslecht die integratiekeuze niet.

## Bijdrageverantwoording

Rol: integratieonderzoeker en prototypebouwer. Inputs: gebruikersopdracht, P2-projectvoorstel, bestaande lokale UI en bovenstaande officiële publiq-bronnen. Systeem: OpenAI Codex / GPT-6. Reviewer: nog niet toegewezen. Dispositie: lokaal voorstel en ontwerpproef met publieke evenementgegevens, zonder externe registratie, indiening of publicatie.

### Aanvulling: echte evenementvoorbeelden

Op gebruikersverzoek zijn de fictieve kaarten vervangen door zes publieke evenementen uit de reeds lopende scrape van de [gemeentelijke UiTagenda](https://www.nazarethdepinte.be/vrije-tijd/uit-in). Iedere kaart verwijst naar haar detailbron en vermeldt de peildatum 6 september 2026. De selectie bevat titels, locaties, tijdstippen, korte redactionele samenvattingen en externe afbeeldingsverwijzingen. Contactgegevens en volledige HTML zijn niet overgenomen. Afbeeldingen laden vanaf de bronwebsite; er is geen afzonderlijke beeldcredit aangetroffen. Rechten zijn daarmee niet als vrijgegeven aangemerkt. De originele pagina blijft de referentie.

Reproduceerbaar via `scripts/extract-p2-event-sample.py`: een vaste selectie uit de private crawl, met bron-URL, exacte ophaaltijd en bronhash per record in `repos/municipal-website/src/data/p2-events.json`. Inputs voor deze aanvulling: zes gemeentelijke detailpagina’s, vastgelegd op 6 september 2026. Rol: publieke-evenementencurator. Systeem: OpenAI Codex / GPT-6. Reviewer: nog niet toegewezen. Dispositie: lokale ontwerpactualisatie; geen externe publicatie.
