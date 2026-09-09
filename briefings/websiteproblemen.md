---
title: "Briefing websiteproblemen Nazareth-De Pinte"
topic: Websiteonderzoek
summary: "Gecontroleerde problemen met gebruikersroutes, prestaties en toegankelijkheid van de bestaande website."
status: concept-niet-menselijk-beoordeeld
language: nl-BE
observed_on: 2026-09-06
updated: 2026-09-06
agent_role: onderzoeker-digitale-dienstverlening
agent_system: OpenAI Codex / GPT-5
reviewer: nog-niet-toegewezen
disposition: lokale-conceptanalyse-ter-beoordeling
publication_approval: niet-verleend
---

# Briefing websiteproblemen Nazareth-De Pinte

Dit is een onafhankelijke bijdrage aan een experimentele workspace. Het is geen officieel gemeentelijk rapport. De controles zijn uitgevoerd op **6 september 2026** en zijn nog niet door een mens beoordeeld.

## Besluit voor de briefing

De publieke dienstverlening was tijdens de controle grotendeels bereikbaar: **39 van 40 gecontroleerde hoofdingangen leverden HTTP 200 op**. Er is dus geen bewijs voor een algemene storing. Wel zijn twee kapotte gebruikersroutes bevestigd, naast meerdere onderhouds-, prestatie-, toegankelijkheids- en samenhangproblemen.

De hoogste prioriteit ligt bij:

1. de kapotte privacylink in eGovFlow;
2. de trage UiT- en zoekresultaten;
3. verliesrisico in het evenementenformulier dat in één sessie moet worden ingevuld;
4. de onduidelijke overlap tussen ReCreateX en LUWIO voor opvang;
5. bekende toegankelijkheidsproblemen over de volledige keten.

## Bevestigde problemen

| Prio | Probleem | Bewijs op 6 september 2026 | Effect | Voorgestelde correctie |
|---|---|---|---|---|
| Hoog | eGovFlow heeft een kapotte privacylink | De footer verwijst naar `https://nazarethdepinte.egovflow.be/www.nazarethdepinte.be/privacyverklaring`. HTTP levert alleen de app-shell; in een browser blijft de pagina leeg. | Een inwoner kan vanuit het loket de privacy-informatie niet bereiken. | Corrigeer de configuratie naar `https://www.nazarethdepinte.be/privacyverklaring`; voeg een automatische linkcontrole toe. |
| Hoog | Het evenementenformulier kan niet als concept worden bewaard | De [publieke instructie](https://www.nazarethdepinte.be/form/aanvraagformulier-voor-evenement) zegt dat het formulier in één keer moet worden ingevuld. Het formulier heeft veel stappen en vraagt mogelijk plannen en handtekeningen. | Verhoogd risico op afhaken, dubbele invoer en verlies van werk. De omvang van het probleem is nog niet gemeten. | Voeg veilige conceptopslag en hervatten toe buiten de publieke repository; bouw eerst een voorbereidingschecklist met synthetische data. |
| Hoog | UiTagenda en algemene zoekpagina reageren traag aan de serverzijde | Drie opeenvolgende UiT-metingen gaven TTFB 1,51–1,61 s; drie zoekmetingen 1,09–1,51 s. De eerste gecontroleerde reeks gaf medianen van respectievelijk 0,99 s voor zoeken en 0,83 s voor ReCreateX. | De pagina kan pas laat beginnen renderen; filters voelen traag, vooral op mobiel of een zwakke verbinding. | Profileer Drupal Views/Search API-query's, caches en externe UiT-data; stel een doel voor serverrespons vast en meet dit continu. |
| Middel | Oude UiT-zoeklink is niet toegankelijk | `http://www.nazareth.be/agenda/search` stuurt door naar `https://nazarethdepinte.be/agenda/search`, levert HTTP 403 en toont “Geen toegang”. De link stond als “Zoeken in de UiTdatabank” in de onderzochte zoekpagina-output. | Gebruiker komt op een foutpagina in plaats van de actuele agenda. | Verwijder of vervang door `https://www.nazarethdepinte.be/vrije-tijd/uit-in`; voeg redirecttest toe. |
| Middel | Bibliotheekhomepage verstuurt uitzonderlijk veel HTML | De HTML-respons is ongeveer **710,6 kB uitgepakt en 463,9 kB gzip**. Eén inline SVG-regel is circa **611 kB**, hoofdzakelijk het logo-element. De gemeentelijke homepage is circa 149,6 kB uitgepakt en 38,9 kB gzip. | Onnodige datakost, parseertijd en tragere eerste weergave. | Optimaliseer en externaliseer het SVG-logo; laat caching het gedeelde bestand hergebruiken. Meet daarna LCP en INP met veld- en labdata. |
| Middel | Sitemap gebruikt uitsluitend het oude Nazareth-domein | Alle **1.237** `<loc>`-vermeldingen in de live [sitemap](https://www.nazarethdepinte.be/sitemap.xml) gebruiken `www.nazareth.be`. | Extra redirects voor crawlers; onduidelijke canonieke identiteit na de fusie; mogelijk inefficiënte indexering. Er is geen SEO-verlies gemeten. | Genereer de sitemap met `www.nazarethdepinte.be`, controleer canonicals en behoud gerichte permanente redirects. |
| Middel | De website verwijst nog naar de oude eGovFlow-tenant | Footer en andere snelle links gebruiken `nazareth.egovflow.be`; die stuurt door naar `nazarethdepinte.egovflow.be`. In één meting duurde de oude route 1,14 s tegenover 0,23 s voor de actuele tenant. | Extra netwerkstap en zichtbare erfenis van de oude gemeente. | Vervang bronlinks door de actuele tenant en behoud de redirect alleen voor oude bookmarks. |
| Middel | Opvangroutes overlappen tussen ReCreateX en LUWIO | De centrale [webshopwegwijzer](https://www.nazarethdepinte.be/webshop-en-tickets) biedt een ReCreateX-ChildCare-route. De ReCreateX-startpagina verwijst verschillende opvangonderdelen door naar [LUWIO](https://shop.nazarethdepinte.be/), dat om de juiste schoolkeuze vraagt. | Onzekerheid over waar een ouder een profiel, reservatie of wijziging moet beheren. Een defect is niet voor elke locatie bewezen. | Publiceer één actuele matrix per locatie en periode; verwijder oude routes zodra migratie en terugvalpad bevestigd zijn. |
| Middel | Bekende toegankelijkheidsproblemen zijn nog van toepassing verklaard | De live [toegankelijkheidsverklaring](https://www.nazarethdepinte.be/toegankelijkheidsverklaring), herzien op 13 augustus 2026, noemt toetsenbordproblemen in de cookiemodule, contrast, focusvolgorde, ontbrekende autocomplete-attributen en niet-toegankelijke PDF's. | Sommige inwoners kunnen taken moeilijker of niet zelfstandig uitvoeren. | Laat een nieuwe WCAG-audit de hele keten testen, inclusief externe loketten, en publiceer eigenaar, planning en herstelstatus per bevinding. |
| Laag | Interne taxonomietekst staat in de publieke interface | [Zoeken](https://www.nazarethdepinte.be/zoeken) en [UiT](https://www.nazarethdepinte.be/vrije-tijd/uit-in) tonen `Mesh terms » Taxonomy term » Naam`. | Interface oogt onafgewerkt en het filterdoel is onduidelijk. | Geef het veld een menselijk label of verberg het als het geen publieke functie heeft. |
| Laag | eGovFlow toont een categorie “Verkiezingen oktober 2024” en herhaalde productlabels | De publieke [eGovFlow-catalogus](https://nazarethdepinte.egovflow.be/forms) bevat de historische categorie; dezelfde bevolkingsproducten komen ook onder die categorie terug. | Onnodige keuzestress; mogelijk verouderd catalogusbeheer. Sommige historische formulieren kunnen bewust beschikbaar blijven. | Bevestig bewaardoel, archiveer verlopen categorieën en voorkom duplicatie. |
| Laag | Het evenementenformulier gebruikt pre-fusietaal | Een keuzelabel luidt “Tocht of wedstrijd door Nazareth”. | Organisatoren uit De Pinte of Zevergem kunnen twijfelen over de reikwijdte. | Wijzig naar de juiste geografische omschrijving na inhoudelijke controle. |
| Laag | Een publiek document staat nog op een stagingachtige host | Het stratenplan linkt naar `fusienazarethdepinte.paddlecms.net`; de PDF werkt, maar is circa 6,7 MB. | Afhankelijkheid van een niet-gemeentelijk ogende host, grote mobiele download en zwakkere linkgovernance. | Verhuis naar het canonieke domein, optimaliseer de PDF en bied een toegankelijke HTML-kaart of tekstalternatief. |

## Prestatiemeting

De transportmetingen zijn drie GET-verzoeken per pagina vanaf één onderzoekscomputer. Redirects werden gevolgd en compressie werd toegestaan. Dit zijn **server- en overdrachtsmetingen**, geen Core Web Vitals. JavaScript-apps met een kleine app-shell kunnen na de eerste respons nog veel code en data laden.

| Pagina | Mediane TTFB | Mediane totale responstijd | Initiële gecomprimeerde body |
|---|---:|---:|---:|
| Gemeentelijke homepage | 0,29 s | 0,33 s | 38,9 kB |
| Algemeen zoeken | 0,99 s | 1,01 s | 38,2 kB |
| Evenementenformulier | 0,36 s | 0,40 s | 37,3 kB |
| eGovFlow app-shell | 0,23 s | 0,23 s | 1,0 kB |
| ReCreateX-startpagina | 0,83 s | 0,87 s | 38,8 kB |
| LUWIO app-shell | 0,46 s | 0,46 s | 0,7 kB |
| Raadpleegomgeving | 0,27 s | 0,27 s | 15,8 kB |
| Bibliotheekhomepage | 0,23 s | 0,41 s | 463,9 kB |

Een tweede reeks bevestigde dat de dynamische lijsten het traagst waren: UiT had een mediane TTFB van 1,51 s en zoeken 1,10 s. ReCreateX bleef rond 0,83 s. De gemeentelijke homepage profiteert zichtbaar van caching en reageerde in deze controle relatief snel.

De Google PageSpeed API gaf tijdens dit onderzoek HTTP 429 en leverde geen bruikbaar rapport. Daarom staan hier geen Lighthouse-score of geschatte Core Web Vitals. Een volgende technische audit moet Lighthouse lokaal uitvoeren bij desktop en mobiel, plus echte velddata uit een privacy-goedgekeurde bron gebruiken.

## Wat werkte wel

De volgende belangrijke ingangen werkten zonder login tot hun publieke landingspagina: homepage, gemeentelijke navigatie, eGovFlow-catalogus, Timeblockr-afsprakenwidget, ReCreateX, LUWIO, Shopify, Gift2Give, Spotbooking, raadpleegomgeving, raadsstream, consultatieomgeving, bibliotheek, vacatures, Opvang.Vlaanderen en schoolaanmelding. De oude hoofddomeinen `depinte.be` en `nazareth.be` sturen correct door naar de fusiewebsite.

“HTTP 200” betekent alleen dat de publieke ingang antwoordde. Betaling, authenticatie, indienen, annuleren, bevestigingsmail, dossierstatus en backofficeverwerking zijn bewust niet getest. Er is dus geen basis om te zeggen dat elke volledige transactie werkt.

## Systeemproblemen die toegang achter de schermen vereisen

Deze punten zijn belangrijk, maar kunnen op basis van de openbare website niet als defect worden bevestigd:

- Of meldingen via gemeente, IVM en Fluvius in één statusoverzicht terugkomen.
- Of Drupal Webform-inzendingen automatisch in een zaaksysteem terechtkomen of handmatig worden overgenomen.
- Of ReCreateX en LUWIO een gecontroleerde migratie, gedeeld profiel en consistente capaciteit hebben.
- Of Mijn Burgerprofiel-status en notificaties voor iedere relevante leverancier lokaal zijn geactiveerd.
- Of gebeurtenissen, besluiten en projectupdates machineleesbaar en zonder dubbele invoer doorstromen.
- Of transacties op externe portalen voldoen aan dezelfde toegankelijkheids- en prestatie-eisen als de hoofdsite.
- Of leverancierscontracten bruikbare API's, testomgevingen, export en exitvoorwaarden bevatten.

Validatie hiervan moet gebeuren met een benoemde gemeentelijke eigenaar en synthetische testdossiers in een afzonderlijk beveiligde omgeving. Persoons- en dossiergegevens horen niet in deze publieke repository.

## Aanpak voor herstel

### Binnen twee weken

- Corrigeer de eGovFlow-privacylink en de oude UiT-zoeklink.
- Vervang oude eGovFlow-bronlinks door de fusietenant.
- Corrigeer het taxonomielabel en beoordeel de 2024-categorie in eGovFlow.
- Maak een eigenaar-lijst voor elk extern portaal en iedere belangrijke link.
- Voeg dagelijkse synthetische controles toe voor HTTP-status, redirectdoel en herkenbare paginatitel. Een HTTP 200 met een lege app-shell moet als fout kunnen tellen.

### Binnen zes weken

- Optimaliseer het inline SVG op de bibliotheekhomepage.
- Corrigeer sitemap en canonieke hosts.
- Publiceer de actuele ReCreateX/LUWIO-route per opvanglocatie.
- Profileer zoeken en UiT; leg een prestatiebudget vast voor TTFB, HTML, JavaScript en afbeeldingen.
- Ontwerp conceptopslag en hervatten voor het evenementenproces, met privacy- en bewaartermijnen vóór implementatie.

### Binnen drie maanden

- Voer een volledige WCAG 2.2 AA-audit uit op de belangrijkste ketens.
- Meet taakvoltooiing voor verhuizen, afspraak maken, evenement organiseren, opvang boeken en melden.
- Bouw een gemeentelijke dienstengids die bron, eigenaar, controledatum, voorbereiding en officiële overdracht toont.
- Breng API's, SSO, statusnotificaties, export en exit per leverancier in kaart.

## Minimale acceptatiecriteria

- Geen kapotte privacy-, toegankelijkheids- of contactlinks in een transactieketen.
- Alle hoofdingangen worden dagelijks gecontroleerd op status, eind-URL en herkenbare inhoud.
- Mediane serverrespons voor publieke zoek- en lijstpagina's onder een lokaal vastgesteld budget; als werkdoel kan eerst 0,8 s worden onderzocht.
- Geen enkel essentieel lang formulier zonder hervatten of een duidelijke voorbereidingsroute.
- Eén ondubbelzinnige ingang per opvanglocatie en taak.
- Sitemap- en canonical-URL's gebruiken het fusiedomein.
- Voor iedere toegankelijkheidsbevinding: eigenaar, ernst, geplande hersteltermijn en hertest.

## Bewijs en beperkingen

De ruwe controles staan in [website-controles.json](../evidence/2026-09-06-digitale-dienstverlening/website-controles.json) en [prestatie-hermeting.json](../evidence/2026-09-06-digitale-dienstverlening/prestatie-hermeting.json); het herhaalbare script staat in [audit_public.py](../evidence/2026-09-06-digitale-dienstverlening/audit_public.py). De bredere context staat in [ONDERZOEK.md](../evidence/2026-09-06-digitale-dienstverlening/ONDERZOEK.md), met de gestructureerde [diensteninventaris.csv](../evidence/2026-09-06-digitale-dienstverlening/diensteninventaris.csv) en het [bronmanifest.json](../evidence/2026-09-06-digitale-dienstverlening/bronmanifest.json).

Dit was een gerichte controle van 40 kritieke ingangen en een bredere inventaris van 86 unieke publieke URL's. Het is geen garantie dat alle ongeveer 1.237 sitemap-URL's, alle documenten, alle talen, iedere viewport of iedere formuliervertakking foutloos zijn. Geen login, formulierinzending, betaling, beveiligingsscan of productieactie is uitgevoerd.

Bijdrage: onderzoek, technische meting en probleemanalyse. Inputs: publieke gemeentelijke pagina's, publiek geladen assets, leveranciersdocumentatie en de bestaande workspace-instructies. Systeem: OpenAI Codex / GPT-5. Menselijke reviewer: nog niet toegewezen. Dispositie: concept voor beoordeling; niet gepubliceerd en niet aan de gemeente of leveranciers verzonden.

Ordeningsbijdrage 7 september 2026: rol workspace-informatiearchitect; inputs gebruikersopdracht en bestaande briefing; systeem OpenAI Codex / GPT-6; reviewer nog niet toegewezen; dispositie verplaatst naar de briefingsbibliotheek, inhoudelijke beoordeling en publicatiestatus ongewijzigd.
