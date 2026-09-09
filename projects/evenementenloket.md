---
title: "P2 — Evenementenloket"
status: agenda-gereed-aanvraagflow-nog-te-bouwen
language: nl-BE
updated: 2026-09-07
agent_role: dienstontwerper-evenementen
agent_system: OpenAI Codex / GPT-6
reviewer: nog-niet-toegewezen
disposition: geverifieerde-projectstatus-en-demovoorstel
publication_approval: agenda-beveiligde-test-toegestaan-aanvraagflow-niet-verleend
project_id: P2
sequence: 2
stage: Agenda klaar · aanvraagflow open
summary: De publieke agenda werkt met 325 geïmporteerde evenementen; het aanvraagproces en de live UiT-koppeling zijn nog te bouwen.
first_release: Een hervatbare buurtfeestaanvraag met checklist en medewerkerreview.
timebox: Voorstel · 3–5 bouwdagen voor een synthetische demo
next_step: Bouw één buurtfeestscenario van voorbereiding tot menselijke volledigheidscontrole.
delivery_title: De agenda werkt; het aanvraagloket volgt
delivery_summary: De agenda is onderdeel van de nieuwe website. Ze gebruikt geïmporteerde broninhoud, geen live UiT-feed. Er is nog geen indienings- of behandelflow.
demo_url: https://website.nazarethdepinte.net/agenda/
local_url: http://127.0.0.1:4328/agenda/
publication_label: Agenda achter Access · aanvraagloket niet operationeel
---

# P2 — Evenementenloket

Dit is een onafhankelijk projectvoorstel voor een experimentele workspace. Het loket verleent zelf geen vergunning en vervangt geen bevoegde beslisser.

## Actuele stand — 7 september 2026

**Klaar:** brononderzoek, UiT-integratieadvies en een werkende publieke agenda in de zelfstandige Astro-website. De agenda bevat nu **325 geïmporteerde evenementen**; de eerdere selectie van zes was een eerste proef. Deze agenda behoort technisch tot P1 en is de publieke publicatiekant van P2, geen evenementenaanvraagloket.

**Nog niet gebouwd:** de vragenboom, conceptopslag en hervatten, dossierexport, medewerkerinbox, statusopvolging en koppelingen met officiële aanvragen of reservaties. Ook de live UiT Search- en Entry-koppelingen zijn niet actief. De onderzochte repositories bevatten hiervoor nog geen werkende toepassing; er is geen apart aanvraagloket gedeployed.

**Volgende demostap — voorstel:** één fictief buurtfeest. Stel gerichte vragen over plaats, datum, omvang en voorzieningen, maak een checklist met bronnen, bewaar en hervat het concept, en toon dezelfde voorbereiding in een medewerkerweergave. Laat een mens één ontbrekend onderdeel terugvragen. Eindig met een exporteerbaar voorbereidingspakket, niet met een vergunning of echte indiening.

**Demoacceptatie:** hervatten zonder gegevensverlies; voorwaardelijke checklist verandert mee met antwoorden; ontbrekende informatie wordt verklaard; export stemt overeen met het concept; aanvragen en publieke UiT-aankondigingen blijven zichtbaar afzonderlijk. De gehele flow gebruikt synthetische gegevens en kan met één handeling worden teruggezet.

**Afhankelijkheden:** gemeentelijke evenementencoördinator en behandelaar moeten proces en regels bevestigen. Voor UiT moeten integratie-eigenaarschap, credentials en gebruiksafspraken nog worden geregeld. De [officiële publiq-documentatie](https://docs.publiq.be/), opnieuw geraadpleegd op 7 september 2026, beschrijft registratie en authenticatie voor API-integraties. Geen API-toegang is in dit project als werkend bevestigd.

**Prioriteit:** na de complete meldingsdemo; hergebruik de invoer-, concept-, review- en tijdlijncomponenten. Indicatie 3–5 bouwdagen voor dit beperkte synthetische scenario, geen productieschatting. Voorgestelde proceseigenaar: gemeentelijke evenementencoördinator; nog niet benoemd.

Bewijs: `repos/municipal-website/content/collections/events` en de agendaroute, lokale routeringscode, `repos/service-platform` en het onderstaande integratieonderzoek; gecontroleerd op 7 september 2026. [Gezamenlijk demoplan](/briefings/demo-gemeenteteam/).

## Doelbeeld en backlog — onderstaande functies zijn voorstellen

## Opdracht

Maak van het organiseren van een evenement één begeleid proces: vroeg bepalen welke stappen nodig zijn, gegevens eenmalig voorbereiden, veilig als concept bewaren, samenwerken en de volledige aanvraag gecontroleerd overdragen. De organisator ziet welke onderdelen informatie, reservatie, melding, advies of een formeel besluit zijn.

## Aanleiding en bronnen

De publieke [evenementenpagina](https://www.nazarethdepinte.be/form/aanvraagformulier-voor-evenement), gecontroleerd op **6 september 2026**, vermeldde dat het formulier in één sessie moet worden ingevuld. Het onderzochte formulier had acht zichtbare faselabels en kon plannen en handtekeningen vereisen. De gemeentelijke organisatiewegwijzer verdeelde zaalhuur, materiaal, openbaar domein, aanvraag en UiT-aankondiging over verschillende ingangen. Zie de [onderzoeksanalyse](../evidence/2026-09-06-digitale-dienstverlening/ONDERZOEK.md). De werkelijke uitval, verwerkingstijd en interne overdracht zijn nog niet gemeten.

## Dienstbelofte

Een organisator kan vroeg zien wat nodig is, een aanvraag in meerdere sessies voorbereiden, bewijs gericht toevoegen en de status begrijpen. Een medewerker ontvangt een vollediger dossier met bron, wijzigingen en ontbrekende onderdelen zichtbaar. Elke beoordeling en beslissing blijft bij de bevoegde menselijke functionaris of instelling.

## MVP: veilige voorbereidingsassistent

### Eerste bouwstap: agenda en UiT-koppeling

Het [UiT-integratieadvies](../evidence/2026-09-06-uit-integratie/ADVIES.md) van 6 september 2026 stelt een eigen agenda via de Search API voor. De eerste ontwerpproef bevatte zes echte evenementen. De huidige agenda bevat 325 geïmporteerde evenementen met lokale inhoud en bronmetadata. Deze momentopname van 6 september 2026 wordt nog niet automatisch bijgewerkt via UiT. De Entry API is een mogelijke latere publicatiestap. Een publieke evenementaankondiging en een gemeentelijke aanvraag blijven afzonderlijke processen.

### Voorbereidingsproces

De eerste publieke proef dient niets in en gebruikt geen echte persoonsgegevens. Zij bevat:

1. een vragenboom voor type, plaats, datum, schaal en relevante voorzieningen;
2. een persoonlijke checklist met uitleg waarom elk onderdeel nodig kan zijn;
3. herbruikbare secties voor programma, terreinplan, mobiliteit, geluid, afval, veiligheid, materiaal, zaal en communicatie;
4. lokale conceptopslag op het apparaat of synthetische serveropslag, met duidelijke verwijderfunctie;
5. export naar een leesbaar voorbereidingspakket;
6. een gecontroleerde handoff naar de bestaande officiële aanvraag;
7. drie volledig synthetische scenario's: buurtfeest, zaalactiviteit en evenement in openbaar domein.

Na validatie kan een beveiligde versie concepten bewaren, identiteit gebruiken en met officiële systemen koppelen. Die stap vereist een afzonderlijke privacy-, beveiligings-, juridische en operationele goedkeuring.

## Gewenste productiecapaciteiten

- opslaan en hervatten, versiegeschiedenis en samenwerken met gemachtigde medeorganisatoren;
- gegevens slechts één keer invullen en gericht hergebruiken;
- kaartgebaseerd terreinplan en aanvraag voor inname van openbaar domein;
- gerichte bijlagen met bestandstype-, omvang- en malwarecontrole;
- statussen in gewone taal, verzoek om aanvulling en ontvangstbewijs;
- adapters voor relevante systemen zoals eGovFlow, Spotbooking, zaal- en materiaalreservering en UiTdatabank, uitsluitend als toegang en afspraken formeel zijn bevestigd;
- volledige audit van indiening, menselijke beoordeling, communicatie en beslissing.

## Autoriteitsmodel

| Stap | Verantwoordelijke | Agentrol |
|---|---|---|
| Voorbereiden | organisator | uitleg, checklist en consistentiecontrole |
| Indienen | organisator of gemachtigde mens | alleen uitvoeren na expliciete bevestiging in een bevoegd systeem |
| Volledigheid controleren | benoemde medewerker | ontbrekende elementen signaleren |
| Advies geven | bevoegde gemeentelijke of externe diensten | informatie ordenen; geen advies vervalsen |
| Goedkeuren, voorwaarden opleggen of weigeren | wettelijk bevoegde mens of instelling | nooit autonoom |
| Bezwaar of beroep | bevoegde procedure | route en bron uitleggen |

## Gegevensgrens

De publieke repository bevat uitsluitend code, lege schema's, openbare regels en synthetische voorbeelden. Echte namen, contactgegevens, handtekeningen, plannen, foto's, betalingsgegevens, risico-informatie en dossiercommunicatie worden verwerkt in een afzonderlijke, passend beveiligde omgeving of gecertificeerd systeem van record. Voor productie moeten doel, rechtsgrond, minimale velden, rollen, bewaartermijnen, verwijdering, logging en datadeling per gegevenstype zijn vastgesteld.

## Opleverfasen

| Fase | Resultaat | Beslismoment |
|---|---|---|
| 0. Dienstonderzoek | Proceskaart, nulmeting, regels, uitzonderingen en systeemkaart | proceseigenaar bevestigt waarheid en scope |
| 1. Prototype | Voorbereidingsassistent met drie synthetische scenario's | gebruikersonderzoek en toegankelijkheidsreview |
| 2. Beveiligde alfa | Conceptopslag, accounts, auditlog en testadapters | privacy-, security- en architectuuracceptatie |
| 3. Bèta | Schaduwproef naast bestaand proces met synthetische en formeel toegestane testdossiers | bevoegde eigenaar beoordeelt resultaat |
| 4. Productie | Gecontroleerde indiening, status en support met rollback | expliciete menselijke go-livebeslissing |

## Voorgestelde acceptatiecriteria

- Een gebruiker kan elk synthetisch scenario over meerdere sessies voltooien zonder gegevensverlies.
- Het systeem legt bij iedere vraag uit welke stap of publieke bron de vraag ondersteunt.
- Verplichte en voorwaardelijke onderdelen zijn vóór overdracht zichtbaar; uitzonderingen kunnen door een medewerker worden behandeld.
- WCAG 2.2 AA voor de volledige gebouwde keten, inclusief fout-, upload- en hervatstromen.
- Geen echte dossiergegevens in Git, logs, analytics of testfixtures.
- Geen indiening, statuswijziging of beslissing zonder aantoonbare bevoegdheid en menselijke handeling.
- De stuurgroep stelt na de nulmeting doelen vast voor voltooiing, voorbereidingstijd, aanvullingsvragen en dubbele invoer.

## Eerste werkpakket van zes weken

- breng de huidige aanvraag, zaal, materiaal, openbaar domein en UiT-stappen samen in één service blueprint;
- interview organisatoren en behandelaars met fictieve of geanonimiseerde voorbeelden;
- definieer de openbare regels met bron, eigenaar, geldigheidsdatum en uitzonderingsroute;
- bouw en test de drie synthetische scenario's;
- lever een integratiebeslisnota op met eGovFlow, Spotbooking, reservatie en UiT, inclusief contract-, API-, privacy- en exitvragen.

## Bijdrageverantwoording

Rol: dienstontwerper-evenementen. Inputs: gebruikersopdracht, workspace-regels en publieke audit van 6 september 2026. Systeem: OpenAI Codex / GPT-6. Menselijke reviewer: nog niet toegewezen. Dispositie: lokaal voorstel; geen aanvraag verwerkt, ingediend of beslist.

## Relatie met de publieke website

De interne code P2 betekent Evenementenloket: het project voor de voorbereiding en overdracht van evenementenaanvragen. De publieke agenda is onderdeel van de zelfstandige website-repository `repos/municipal-website` en staat op [Agenda](http://127.0.0.1:4328/agenda/). Het aanvraagloket zelf is nog niet geïmplementeerd.

Statusbijdrage op 7 september 2026: rol portfolioreviewer; inputs gebruikersopdracht, projectvoorstel en lokale implementatiecontrole; systeem OpenAI Codex / GPT-6; reviewer nog niet toegewezen; dispositie actuele status onderscheiden van voorgestelde functies, geen nieuwe applicatie gedeployed.
