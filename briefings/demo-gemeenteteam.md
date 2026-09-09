---
title: "Demo voor het gemeenteteam — van inwonervraag tot opvolging"
topic: Demonstratie
summary: "Een complete meldingsketen tonen, met een inwoner en medewerker, en een voorstel voor de volgende samenwerking."
status: voorstel-niet-menselijk-beoordeeld
language: nl-BE
updated: 2026-09-07
agent_role: productstrateeg-en-portfolioreviewer
agent_system: OpenAI Codex / GPT-6
reviewer: nog-niet-toegewezen
disposition: demoplan-met-geimplementeerde-meldingsketen
---

# Demo voor het gemeenteteam — van inwonervraag tot opvolging

**Advies: toon één complete dienstverleningsketen, met een inwoner én een medewerker.** De vernieuwde website levert de herkenbare ingang. Een kleine meldingsdemo toont vervolgens waar de samenwerking meer waarde kan leveren: duidelijke voorbereiding, uitlegbare routering, menselijk toezicht en begrijpelijke terugkoppeling. Stand 7 september 2026: de meldingsketen is inmiddels gebouwd; evenementenvoorbereiding en redactionele review blijven voorstellen.

## Eerlijke uitgangspositie

| Project | Nu te tonen | Nog te bouwen voor de demo |
|---|---|---|
| [Publieke website](/projects/publieke-website/) | Online Astro-prototype achter Access, themanavigatie, zoeken, 325 geïmporteerde evenementen, voorlezen en twaalf contentcollecties | Vijf gerepeteerde taken, beoordeelde demo-inhoud en een kleine redactionele reviewflow |
| [Evenementenloket](/projects/evenementenloket/) | Publieke agenda en UiT-integratieonderzoek | Hervatbare voorbereiding van één fictief buurtfeest en een medewerkerreview |
| [Meldpunt](/projects/meldpunt-openbare-ruimte/) | Complete fictieve melding met inwonerflow, medewerkerwerkbak, routebevestiging, reacties en tijdlijn | Gemeentelijke procesreview en presentatierepetitie; productieopslag en accounts zijn apart werk |

De website is een snapshot, geen volledige vervanging van gemeentelijke transacties. De crawl staat niet aantoonbaar actief: 637 assets wachten nog en er zijn bronuitzonderingen. De brongebonden wegwijzer is momenteel geen live taalmodelagent. Besparingen, toegankelijkheidsconformiteit en productiegeschiktheid zijn niet bewezen.

## Wat eerst bouwen

### 1. Maak de bestaande website betrouwbaar voor vijf demonstratietaken

Zet een demosnapshot vast en controleer zoeken, contact, Agenda, Bestuur en de ingangen naar voorbereiden/melden. Test de echte uitkomst van knoppen op mobiel en met toetsenbord. Controleer Access vooraf op het apparaat van de presentatie. Laat openstaande transacties herkenbaar zijn; een lokale uitlegpagina mag niet als werkende indiening worden gepresenteerd.

Meet oude en nieuwe pagina’s onder dezelfde omstandigheden en noteer tijd, fouten en meetmethode. Toon alleen onderbouwde verschillen. Indicatie: 1–2 bouwdagen, exclusief inhoudsreview.

### 2. Demonstreer de gebouwde meldingsketen

[Open het meldpunt](https://website.nazarethdepinte.net/meldpunt/). De gebouwde demo gebruikt deterministische routevoorstellen en lokale browseropslag, met expliciete demorollen. Zie [architectuur en gecontroleerde werking](/knowledge/docs/architecture/P3-MELDPUNT-DEMO/).

Gebruik één fictief voetpadprobleem en een synthetische locatie. Start vanuit de website, laat een inwoner de melding voorbereiden en toon daarna hetzelfde item in een medewerkerinbox. Een assistent stelt een categorie, route en samenvatting voor en maakt ontbrekende informatie zichtbaar. De medewerker corrigeert of bevestigt, stelt een aanvullende vraag of verandert een demostatus. De inwoner ziet de tijdlijn en een conceptantwoord.

De demonstratiedata zijn vanaf het eerste scherm als fictief gemarkeerd. Geen echte foto’s, burgergegevens, externe notificaties of interventiebelofte. De kaart heeft een gelijkwaardig tekstalternatief. Eén resetknop maakt de demonstratie herhaalbaar. De eerste keten is geïmplementeerd en technisch getest; reserveer nog tijd voor inhoudsreview en repetitie.

### 3. Voeg een herkenbare evenementenvoorbereiding toe

Maak een fictief buurtfeest met enkele vragen, een voorwaardelijke checklist, opslaan/hervatten en een exporteerbaar voorbereidingspakket. Laat de medewerker één ontbrekend onderdeel terugvragen. Bouw dit op dezelfde concept-, review- en tijdlijncomponenten als de melding. Publieke aankondiging in UiT en de formele gemeentelijke aanvraag blijven aparte stappen. Indicatie: 3–5 bouwdagen.

Een live UiT-feed is een nuttige uitbreiding zodra toegang geregeld is, maar geen voorwaarde om de procesverbetering te demonstreren. publiq biedt een Search API voor een eigen agenda en een aparte Entry API voor invoer; een eigen integratie vraagt registratie en credentials. [Productbeschrijving](https://www.publiq.be/nl/projecten/publiq-platform), [technische documentatie](https://docs.publiq.be/), gecontroleerd 7 september 2026. Live toegang is hier nog niet bevestigd.

### 4. Laat zien hoe het gemeenteteam zelf inhoud beheert

Een redacteur opent een brongebonden wijzigingsvoorstel, ziet bron en datum, vergelijkt de tekst en keurt een **demoversie** goed. Toon ook terugzetten. Zo wordt duidelijk hoe het team inhoud kan beheren en welke ondersteuning agenten bieden. Begin met één synthetische wijziging, niet met een volledig CMS. Indicatie: 1–2 bouwdagen, na de meldingsketen.

## Hoe agentisch maken zonder te overdrijven

Een agent moet zichtbaar iets voorbereiden: de juiste informatie zoeken met bron, een dossier samenvatten, ontbrekende velden signaleren en een beargumenteerd routeringsvoorstel of conceptantwoord maken. De inwoner of medewerker kan corrigeren. Benoem duidelijk wat deterministische logica is en wat werkelijk door een model wordt gegenereerd.

Voor de eerste demo kunnen vaste, uitlegbare regels voldoende zijn. Als we een live model toevoegen: alleen goedgekeurde publieke inhoud en synthetische gegevens, bronverwijzingen, een duidelijk “onvoldoende informatie”, en geen bevoegdheid om te publiceren, in te dienen of te beslissen. Laat ook één onzekere vraag zien. Betrouwbaarheid bij twijfel is onderdeel van de demonstratie.

## Draaiboek van twaalf minuten

| Tijd | Demonstratie | Wat het gemeenteteam kan beoordelen |
|---|---|---|
| 0–2 min | Herkenbare vernieuwde website; één vraag en de juiste pagina | Vindbaarheid, taal en herkenbaarheid |
| 2–6 min | Fictieve melding → medewerkerreview → inwonertijdlijn | Overdracht, eigenaarschap en minder dubbele invoer als te toetsen hypothese |
| 6–9 min | Buurtfeest voorbereiden, onderbreken, hervatten en checklist | Begrijpelijkheid en mogelijke vermindering van onvolledige aanvragen |
| 9–10 min | Redactioneel voorstel met bron, verschil en menselijke goedkeuring | Grip op inhoud en verantwoord agentgebruik |
| 10–12 min | Laat het team zelf een keuze veranderen; bespreek één beperkte proef | Welke werkelijke problemen en prioriteiten het team wil valideren |

Als de voorbereidingstijd beperkt is: toon website plus meldingsketen, en presenteer het evenementenloket eerlijk als volgende bouwstap. Drie halve demo’s leveren minder bewijs dan één complete keten.

## Voorstel voor een afgebakende samenwerking

Vraag om één gemeentelijke proceseigenaar, twee medewerkers en enkele vrijwillige testgebruikers voor een korte ontwerpproef. Valideer eerst de echte proceskaart en huidige tools, en kies samen één meldcategorie of evenementtype. Stel daarna scope, gegevensgrens, succescriteria en een evaluatiemoment vast. Een vrijblijvende demo is geen inkoop- of productieovereenkomst.

Meet taakvoltooiing zonder hulp, voorbereidingstijd, ontbrekende informatie, correcties door medewerkers en toegankelijkheidsproblemen. Gebruik een nulmeting; geef nu geen verzonnen percentage tijdswinst. Een startdoel voor de demo is tien van tien gerepeteerde synthetische scenario’s zonder dataverlies of ongecontroleerde verzending. Productiedoelen bepaalt de proceseigenaar na de nulmeting.

## Gereed voor presentatie wanneer

- De gekozen demo werkt herhaaldelijk op het presentatieapparaat, inclusief aanmelding en mobiele weergave.
- Alle schermen onderscheiden bestaande functies, voorgestelde integraties en fictieve gegevens.
- Er is één inwoner- en één medewerkerweergave van hetzelfde synthetische item, met menselijke bevestiging en reset.
- Hoofdtaken werken met toetsenbord; voor de kaart bestaat een tekstalternatief.
- Geen echte aanvragen, meldingen of e-mails worden verzonden.
- Een vastgezette lokale versie en een korte opname zijn beschikbaar als internetfallback; de opname is nog te maken.

De bouwinschattingen hierboven zijn relatieve planningsvoorstellen voor beperkte demo’s, geen beloftes voor productie. Reserveer daarnaast tijd voor gemeentelijke inhoudsreview en repetitie. Begin met website-afwerking plus meldingsketen; besluit daarna of de andere onderdelen de demonstratie echt verbeteren.

## Verantwoording

Rol: productstrateeg en portfolioreviewer. Inputs: gebruikersopdracht, de drie projectbestanden, lokale website- en Workspace OS-code, collectie-inventaris, crawlstatus en procescontrole, audit- en deploymentrapporten, browsersessie en officiële publiq-documentatie. Peildatum: 7 september 2026. Systeem: OpenAI Codex / GPT-6. Reviewer: nog niet toegewezen. Dispositie: voorstel voor demonstratie en samenwerking; geen nieuwe toepassing gebouwd, geen gemeentelijke goedkeuring of productiepublicatie.

Actualisatie 7 september 2026: rol civic-serviceontwikkelaar; inputs geïmplementeerde P3-code, tests en browsercontrole; systeem OpenAI Codex / GPT-6; reviewer nog niet toegewezen; dispositie meldingsdemo toegevoegd aan de bestaande website. De oorspronkelijke verantwoording beschrijft het eerdere voorstel.

Ordeningsbijdrage 7 september 2026: rol workspace-informatiearchitect; inputs gebruikersopdracht en bestaande briefing; systeem OpenAI Codex / GPT-6; reviewer nog niet toegewezen; dispositie verplaatst naar de briefingsbibliotheek, inhoudelijke beoordeling en publicatiestatus ongewijzigd.
