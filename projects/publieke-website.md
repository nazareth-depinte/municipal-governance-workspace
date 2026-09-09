---
title: "P1 — Publieke website en dienstengids"
status: prototype-actief-achter-access
language: nl-BE
updated: 2026-09-07
agent_role: productontwikkelaar-en-portfolioreviewer
agent_system: OpenAI Codex / GPT-6
reviewer: nog-niet-toegewezen
disposition: geverifieerde-projectstatus-en-demovoorstel
publication_approval: beveiligde-testdeployment-door-gebruiker-toegestaan
publication_label: Beveiligde test toegestaan · geen gemeentelijke productieacceptatie
project_id: P1
sequence: 1
stage: Werkend testprototype
summary: Zelfstandige Astro-website met lokale contentcollecties, zoeken, agenda en voorlezen; gedeeld via Cloudflare Access.
first_release: Vijf foutloos te demonstreren inwonerstaken en een redactionele reviewflow.
timebox: Voorstel · 1–2 bouwdagen demo-afwerking
next_step: Demo-inhoud vastzetten, uitzonderingen beoordelen en vijf kerntaken oefenen.
delivery_title: De vernieuwde website staat online
delivery_summary: De gebouwde website is bereikbaar achter Access. Dit is een inhoudelijk nog niet volledig beoordeelde momentopname; officiële transacties zijn niet vervangen.
demo_url: https://website.nazarethdepinte.net/
local_url: http://127.0.0.1:4328/
---

# P1 — Publieke website en dienstengids

**Stand op 7 september 2026: werkend en gedeeld testprototype.** De nieuwe website is gebouwd, heeft een eigen private repository en is via Cloudflare Access te bekijken. Dit is een onafhankelijk ontwerp, geen officiële gemeentelijke dienst of geaccepteerde productieomgeving.

## Wat daadwerkelijk klaar is

- Een moderne vormgeving met het bestaande logo en de huisstijl, duidelijke themakaarten en hoofdmenu-ingangen voor diensten, Agenda, Bestuur en Contact.
- Een zelfstandige Astro 7-website in de private repository [municipal-website](https://github.com/nazareth-depinte/municipal-website), los van de Workspace OS-interface.
- Twaalf Astro-contentcollecties, met schemas, brongegevens en een collectie-API voor gestructureerd gebruik door ontwikkelaars en agenten.
- Zoeken, themanavigatie, nieuws, documenten, agenda, stappenplannen en lokaal bewaarde pagina’s.
- Een brongebonden wegwijzer die de geïmporteerde inhoud doorzoekt. **Dit is geen live taalmodelagent.**
- Een compacte voorleesfunctie via de browser, beschikbaar als uitklapbare hulpfunctie in de navigatie. De beschikbare Nederlandse stem hangt van het apparaat af.
- Cloudflare-testhosting achter Access met toegelaten individuele adressen uit 1Password en het expliciet toegelaten gemeentelijke e-maildomein. De loginnaam is gecorrigeerd naar “Nazareth-De Pinte · Testomgeving”.
- Een geïntegreerde meldingsdemo op `/meldpunt/`, met eigen broncode in de service-platformrepository, inwonerflow, medewerkerwerkbak en gedeelde lokale tijdlijn. Dit vervangt geen echt meldkanaal.
- Gedeelde deploymentconfiguratie in `config/deployment.json`; echte secrets blijven lokaal of in 1Password. Alleen de gebouwde website gaat naar Cloudflare.

## Inhoud en gecontroleerde dekking

Lokale collectie-inventaris, gecontroleerd op 7 september 2026. Dit zijn aantallen items, geen bewijs dat alle broninhoud actueel, volledig of menselijk beoordeeld is.

| Collectie | Items | Collectie | Items |
|---|---:|---|---:|
| Pagina’s | 635 | Diensten | 206 |
| Nieuws | 22 | Evenementen | 325 |
| Organisaties | 59 | Contacten | 43 |
| Documenten | 664 | Media | 515 |
| Thema’s | 9 | Dienstwegwijzers | 28 |
| Stappenplannen | 6 | Niet-beschikbare bestemmingen | 83 |

De laatst gecontroleerde standalone-build bevat 3.211 HTML-routes, inclusief aliasroutes. De linkaudit van 7 september 2026 om 13:47 UTC controleerde 72.264 verwijzingen en rapporteerde nul fouten binnen haar gedocumenteerde scope. Oude brondomeinen mogen nog als herkomstmetadata voorkomen; dat is iets anders dan een navigatielink naar de oude website. De audit bewijst geen werkende externe loketten of volledige toegankelijkheid.

De Cloudflare-controle bevestigde redirects naar Access voor homepage, meldpunt en bijhorende JavaScript, Agenda, Bestuur, collectie-API en een PDF. Tijdens de daaropvolgende browsersessie was de homepage achter Access zichtbaar. De eerdere lokale DNS-fout is daardoor geen actuele blokkade voor die sessie. Dit vervangt de eerdere vermelding dat de website alleen lokaal beschikbaar was.

## Crawl: nog niet volledig afgerond

Het statusbestand meldt nog `running`, maar bij procescontrole op 7 september was het daarin genoemde crawlerproces niet actief. De laatste import is van 7 september om 09:13 UTC. Er staan **0 pagina-URL’s, 0 documenten en 637 assets** in de wachtrij. Er zijn 1.871 vastgelegde pagina-URL’s en 95 pagina-uitzonderingen; URL-aantallen omvatten aliases en zijn niet gelijk aan unieke collectie-items. Externe redirects, HTTP 403 en HTTP 404 zijn afzonderlijk te behandelen.

De bestaande website bouwt uit haar lokale snapshot en heeft het crawlerproces niet nodig. De resterende crawl en de 83 niet-beschikbare bestemmingen moeten wel bewust worden afgehandeld; de migratie is dus niet “100% compleet”. Een crawlwijziging veroorzaakt geen automatische productiepublicatie.

## Wat nog ontbreekt

- Menselijke inhoudsreview, benoemde inhoudseigenaars en een werkende redactionele goedkeuringsinterface.
- Werkende aanvraag-, afspraak-, reservatie- en meldingsintegraties. Een lokale uitlegpagina of noodbestemming is geen vervangend loket.
- Live UiT-synchronisatie: de agenda gebruikt een geïmporteerde momentopname.
- Handmatige toegankelijkheids- en gebruikerstests, plus een vergelijkbare performancemeting van oud en nieuw. Voorlezen alleen bewijst geen WCAG-conformiteit.
- Een aantoonbaar onderbouwde live AI-assistent, als die na de demonstratie gewenst blijkt.
- Gemeentelijke productieacceptatie, beheerafspraken, support, herstelprocedure en definitieve contentvrijgave.

## Eerstvolgende werkpakket — voorstel

1. Zet een reproduceerbare demosnapshot vast. Toon vijf beoordeelde taken: informatie vinden, contact, activiteit zoeken, evenement voorbereiden en een probleem melden.
2. Controleer alle knoppen in die vijf ketens op hun echte uitkomst, inclusief toetsenbordbediening en mobiel. Toon openstaande functies duidelijk als demo of nog niet aangesloten.
3. Meet dezelfde taken en pagina’s op oud en nieuw; publiceer gemeten tijden, fouten en beperkingen zonder onbewezen besparingsclaims.
4. Voeg een kleine redactionele demo toe: agent stelt een brongebonden wijziging voor, redacteur bekijkt het verschil en keurt een demoversie goed. Geen automatische publicatie.

Indicatie: 1–2 bouwdagen voor demo-afwerking, exclusief inhoudsreview en externe afhankelijkheden. Dit is een voorstel, geen leverbelofte.

## Bronnen, eigenaarschap en besluit

Bronnen: private repository `repos/municipal-website`, `content/collections`, `content/migration.json`, `reports/standalone-audit.json`, `reports/cloudflare-deployment.json`, lokale crawlerstatus en procescontrole; alle gecontroleerd op 7 september 2026. Oudere gereedheidsrapporten zijn tijdsgebonden en worden door latere audits aangevuld.

[Websiteproblemen uit het brononderzoek](/briefings/websiteproblemen/) · [Hostingonderzoek](/briefings/cloudflare-en-europese-hosting/) · [Deployment en verificatie](/knowledge/docs/architecture/SECRETS-EN-TESTDEPLOYMENT/) · [Gezamenlijk demoplan](/briefings/demo-gemeenteteam/).

Voorgestelde gemeentelijke eigenaar: communicatie/digitale dienstverlening, met een redacteur en reviewers voor toegankelijkheid en techniek. Er is nog niemand benoemd. Echte burgerdossiers horen niet in Git. Menselijke goedkeuring van de testdeployment is geen gemeentelijke productieacceptatie.

Bijdrage: actuele portfolioreview en productvoorstel; inputs gebruikersopdracht, lokale code, collecties, audit- en deploymentbewijzen; systeem OpenAI Codex / GPT-6; reviewer nog niet toegewezen; dispositie Workspace OS bijgewerkt, geen nieuwe website-upload of officiële ingebruikname.

Implementatie-update 7 september 2026: geïntegreerde meldpuntdemo toegevoegd en beveiligd gedeployed; nieuwe build/linkaudit en ingelogde browserweergave gecontroleerd. Rol civic-serviceontwikkelaar; inputs P3-code en verificatie; systeem OpenAI Codex / GPT-6; reviewer nog niet toegewezen; dispositie testprototype, geen officiële ingebruikname.
