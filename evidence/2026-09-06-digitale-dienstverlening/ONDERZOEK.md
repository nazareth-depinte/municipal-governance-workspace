---
title: "Digitale dienstverlening Nazareth-De Pinte — websites, tools en technologie"
status: concept-niet-menselijk-beoordeeld
language: nl-BE
observed_on: 2026-09-06
source_type: publieke-technische-observatie-en-bronnenonderzoek
agent_role: onderzoeker-digitale-dienstverlening
agent_system: OpenAI Codex / GPT-6
reviewer: nog-niet-toegewezen
disposition: lokale-conceptanalyse-ter-beoordeling
publication_approval: niet-verleend
---

# Digitale dienstverlening Nazareth-De Pinte

Dit is een onafhankelijke onderzoeksbijdrage aan een experimentele workspace, geen officieel gemeentelijk rapport of gemeentelijke dienstverlening. Peildatum voor alle technische waarnemingen en geraadpleegde bronnen: **6 september 2026**. De analyse en voorstellen zijn nog niet door een mens beoordeeld.

## Kernbevinding

De digitale gemeente bestaat uit een Drupal/Paddle-informatiewebsite met een netwerk van gespecialiseerde toepassingen. Burgerzaken gebruikt eGovFlow en Timeblockr; vrije tijd verwijst naar ReCreateX en daarnaast LUWIO; aankopen lopen via Shopify en Gift2Give; innames openbaar domein via Spotbooking; bekendmakingen en vergaderingen via afzonderlijke raadpleeg- en streamingomgevingen. Mijn Burgerprofiel vormt op verschillende plaatsen een bestaande verbindingslaag. De actuele [gemeentelijke homepage](https://www.nazarethdepinte.be/), [webshopwegwijzer](https://www.nazarethdepinte.be/webshop-en-tickets), [afsprakenpagina](https://www.nazarethdepinte.be/afspraak-maken) en [leverancierslijst van Digitaal Vlaanderen](https://www.vlaanderen.be/digitaal-vlaanderen/onze-diensten-en-platformen/mijn-burgerprofiel/dienstenleveranciers) onderbouwen deze kaart.

**Analyse:** de kansrijkste eerste verbetering is een betrouwbare wegwijzer die inwoners helpt een dienst te vinden en een aanvraag voor te bereiden, met duidelijke overdracht naar de bestaande bevoegde dienst. Een volledige vervanging van al deze systemen is op basis van dit publieke onderzoek niet te verantwoorden. De interne werklast, contracten, gebruikscijfers en kwaliteit van de bestaande koppelingen zijn niet bekend.

## Methode, bewijs en afbakening

- Inspectie van publieke hoofd- en themanavigatie, dienstpagina's, externe links, ingesloten toepassingen, HTTP-headers en expliciet geladen JavaScript-bestanden.
- 88 HTTP-opvragingen voor 86 verschillende URL's in het bronmanifest; daarnaast afzonderlijke homepage-inspectie, zoekonderzoek, officiële documentatie en browsercontroles. Dit aantal is geen aantal toepassingen.
- Browsercontrole van Timeblockr, eGovFlow en LUWIO zonder authenticatie. Bij Timeblockr werd de interface zichtbaar met uitsluitend noodzakelijke cookies. Geen afspraak geselecteerd of geboekt. De publieke eGovFlow-catalogus werd uitgeklapt; geen aanvraag gestart. LUWIO toonde een melding over schoolkeuze en een knop naar aanmelden.
- Het sitemapbestand bevatte 1.237 URL-vermeldingen. De inhoud van al deze pagina's is **niet** volledig gecrawld. Na enkele HTTP 429-responsen werd het tempo verlaagd; belangrijke ontbrekende pagina's werden later via hun zichtbare links gecontroleerd.
- De 40 inventarisregels zijn **dienst- en hulpmiddelcategorieën**, geen telling van 40 onafhankelijke softwareproducten. Eén product kan meerdere diensten bedienen; één dienst kan meerdere producten gebruiken.
- Geen login, formulierinzending, betaling, beveiligingsscan, verborgen eindpuntverkenning of operationele dossierinspectie. Ruwe HTML, formulierwaarden, cookies, sleutels en persoonsgegevens staan niet in dit dossier. Het bronmanifest bewaart URL, datum, responsstatus, omvang en SHA-256; het is geen integraal webarchief.

**Bewijslabels:** direct = daadwerkelijk in publieke pagina, header, script of browser gezien; officiële verwijzing = gemeente beschrijft of linkt de dienst; leveranciersdocumentatie = generieke productmogelijkheden; afgeleid = sterke technische aanwijzing, geen bevestiging van de volledige implementatie. Een onbekende versie is geen bewijs van veroudering. Een versie in een bundel bewijst geen kwetsbaarheid.

Alle product- en dienstbeschrijvingen hieronder zijn waarnemingen of officiële uitleg. Ze zijn geen juridische toets. Historische stukken worden afzonderlijk behandeld. Aanbevelingen zijn voorstellen.

## 1. Websites en toegangen

| Toegang | Waargenomen functie en relatie |
|---|---|
| [nazarethdepinte.be](https://www.nazarethdepinte.be/) | Huidige gemeentelijke toegang tot informatie, formulieren en externe loketten. |
| [depinte.be](https://www.depinte.be/) en [nazareth.be](https://www.nazareth.be/) | Beide hoofddomeinen stuurden door naar de fusiewebsite. Alleen de hoofdpagina-redirects zijn getest; behoud van alle oude deeplinks is niet bewezen. |
| [nazarethdepinte.bibliotheek.be](https://nazarethdepinte.bibliotheek.be/) | Afzonderlijke bibliotheekwebsite met catalogus, Mijn Bibliotheek en digitale inhoud. |
| [nazarethdepinte.egovflow.be](https://nazarethdepinte.egovflow.be/) | Actueel digitaal loket. De gemeentelijke footer linkt nog vaak naar `nazareth.egovflow.be`; `/digitaal-loket` kwam uit op de fusietenant. |
| [ReCreateX](https://nazarethdepinte.recreatex.be/) en [LUWIO](https://shop.nazarethdepinte.be/) | Beide publiek bereikbaar. De ReCreateX-startpagina verwijst voor verschillende opvangonderdelen naar de LUWIO-host. Verdeling per locatie en migratieplanning blijven te bevestigen. |
| [Raadpleegomgeving](https://nazareth-depinte-raadpleegomgeving.csecho.be/), [consultatieomgeving](https://nazarethdepinte.consultatieomgeving.net/burger) en [Streamovations](https://streamings.streamovations.be/nazareth-de-pinte/) | Afzonderlijke toegang tot bestuurspublicaties, vergunningspublicaties en raadsstreaming. |
| [Schoolaanmelding](https://nazarethdepinte.aanmelden.in/) | Apart centraal aanmeldingsportaal voor basisscholen. |

De [gemeente-app](https://www.nazarethdepinte.be/bestuur/communicatie/app-nazareth-de-pinte) is aangesloten op Mijn Burgerprofiel. [Digitaal Vlaanderen](https://www.vlaanderen.be/uw-overheid/mijn-burgerprofiel/privacyverklaring-mijn-burgerprofiel/privacyverklaring-gemeente-app-nazareth-de-pinte) beschrijft afspraken en doorverwijzingen voor meldingen, webshop en reservaties. Dit is al een vorm van bundeling. Het gebruikte native app-framework is niet vastgesteld.

## 2. Technologie die daadwerkelijk zichtbaar is

| Onderdeel | Vastgesteld | Grens van het bewijs |
|---|---|---|
| Gemeentelijke website | Drupal-cacheheaders, `ocelot_paddle`-thema, Paddle-footer; jQuery-pad met versie 4.0.0; CKEditor Accordion; Font Awesome 6.6.0; Adobe Fonts/Typekit | Drupal-hoofdversie, PHP-runtime, database en hostingcontract onbekend. Een oudere Paddle-publicatie over Drupal 9 zegt niets definitiefs over de huidige versie. |
| Caching | `x-adv-varnish: Cache-enabled`, cache-HIT-headers | Varnish-gerelateerde zichtbare caching; volledige infrastructuur onbekend. |
| Formulieren | Drupal Webform-klassen en formulierselectoren, multipart uploads bij verschillende formulieren | Interne verwerking, e-mailroutering, CRM en opvolgingsstatus niet zichtbaar. |
| Zoeken | Drupal Views/Search API-signalen; sortering op `search_api_relevance` | Solr of Elasticsearch niet vastgesteld. |
| eGovFlow | Vue-componentnamen en Vite-dependencymapping in de daadwerkelijk geladen bundel | Backendtaal en database onbekend; geen volledige pakketversielijst. |
| Timeblockr | Gemeentelijke configuratie, JavaScript-loader, cloud-API-host; Select2-element in browser | Geen vastgestelde serverframework- of runtimeversie. |
| ReCreateX | `__VIEWSTATE`, System.Web/Telerik-resources, jQuery 3.7.1 | Sterk bewijs voor ASP.NET Web Forms en Telerik. Exacte ReCreateX-, .NET- en databaseversie onbekend. |
| LUWIO | React-runtime-markers in geladen bundel; `AmazonS3`-header voor frontend | Statische frontendhosting zegt niets over backendhosting of dataopslag. |
| Shopify | `powered-by: Shopify`; expliciete `Shopify.theme`-metadata: Minimal 12.6.0; jQuery 2.2.3 | Geen checkout- of betaalintegratieaudit. |
| Gift2Give | Angular 14.1.1-markers, Webpack, `x-powered-by: Express`, Cloudflare | Express is bewijs over een zichtbare serverlaag; niet noodzakelijk de volledige transactieserver. |
| Spotbooking | Angular 17.3.9, Webpack, MapLibre-code, nginx-header | Een [ontwikkelpartnercase](https://cactus-now.com/nl/casussen/geosparc/) noemt Java/Spring Boot; niet rechtstreeks vastgesteld voor deze gemeentelijke tenant. |
| Raadpleegomgeving | Cipal Schaubroeck-serverheader/footer; jQuery 3.7.1, Bootstrap, Mustache, DataTables, Moment, Select2, Underscore, LESS | Geen bewezen backendtaal of publieke integratie-API. |
| Consultatieomgeving | Microsoft-IIS/10.0, `X-Powered-By: ASP.NET`, jQuery/Bootstrap-bundels | Leverancier niet onafhankelijk bevestigd; niet automatisch aan Cevi of Cipal toeschrijven. |
| Streamovations | Vue, Vite, Pinia, Vue Router, nginx | Geen volledige video-infrastructuur- of transcriptieanalyse. |
| Bibliotheek | Expliciete generator `Drupal 11`; `library_portal_theme`; Vue-pad voor cataloguszoeken | Andere Drupal-installatie dan de gemeentelijke website. |
| Schoolaanmelding | Apache, Phusion Passenger, jQuery, Bootstrap | Passenger alleen bewijst Ruby on Rails niet; backend en plaatsingsalgoritme onbekend. |
| Opvang.Vlaanderen | `ng-app="koza"` en AngularJS-markup, jQuery, Google Maps | Exacte frameworkversie en backend onbekend. |
| Jobsolutions | Extern iframe, Apache-header en jQuery-assets | Assetnamen alleen zijn onvoldoende om Ruby on Rails te bevestigen. |
| MailPlus | MailPlus-embed; jQuery 3.6.0, UI 1.13.2, Validate 1.19.5 | `/servlet/React` is een endpointnaam, geen bewijs voor het React-framework. |

Technische bron-URL's en grenzen staan per dienst in [diensteninventaris.csv](diensteninventaris.csv) en [diensteninventaris.json](diensteninventaris.json). De precieze onderzochte scripts zijn opgenomen in [bronmanifest.json](bronmanifest.json). De gemeente bevestigt Paddle ook in haar [toegankelijkheidsverklaring](https://www.nazarethdepinte.be/toegankelijkheidsverklaring).

## 3. Dienstverlening per gebruikersbehoefte

### Burgerzaken en afspraken

[eGovFlow](https://nazarethdepinte.egovflow.be/forms) toont attesten, akten, adreswijziging en andere burgerzakenproducten. In de gecontroleerde publieke catalogus stonden 30 unieke productlabels over de categorieën Bevolking, Burgerlijke stand, Strafregister en een historische verkiezingscategorie; verschillende labels waren herhaald. Dit telt cataloguslabels, geen geteste of gegarandeerd beschikbare transacties. [Vanden Broele](https://www.vandenbroele.be/nl-be/voor-wie/steden-en-gemeenten/burgerzaken) beschrijft geautomatiseerde digitale aflevering als productmogelijkheid; lokale aflevertermijnen zijn niet gemeten.

De [afsprakenpagina](https://www.nazarethdepinte.be/afspraak-maken) bevat een Timeblockr-widget. De browser toont productkeuze, locatie/datum, persoonsgegevens, controle en bevestiging. De gemeentelijke uitleg verwijst voor andere dienstverlening naar telefonisch afspreken. Dat is een concreet verschil in beschikbare online toegang; het bewijst geen gebrek aan interne planningssoftware.

### Vrije tijd, opvang en aankopen

De [webshopwegwijzer](https://www.nazarethdepinte.be/webshop-en-tickets) onderscheidt ReCreateX voor zaalhuur, materiaal, tickets, activiteiten en een kinderopvanglink; Gift2Give voor KoopLokaalBon; Shopify voor publicaties, compost/GFT, asbestmateriaal en RMA-containers. De gebruiker verlaat daarbij de informatiesite.

Een belangrijke nuance is [LUWIO](https://shop.nazarethdepinte.be/). De publieke ReCreateX-startpagina verwijst opvanggebruikers naar deze host. De browser bevestigt de gemeentenaam en een instructie dat schoolkeuze bepaalt welke opvanglocaties beschikbaar zijn. Tegelijk staat op de centrale webshopwegwijzer nog een ReCreateX-ChildCare-link. Dit is aantoonbare overlap in routes; het is nog geen bewijs dat een bepaalde route fout is. LUWIO en ReCreateX vallen inmiddels onder dezelfde leveranciersgroep: [Tactics maakte op 17 maart 2026 de overname door Vintia bekend](https://www.tactics.be/index.php/nl/blog/vintia-versterkt-marktpositie-bij-lokale-besturen-met-overname-van-tactics).

Voor [baby- en peuteropvang](https://www.nazarethdepinte.be/vrije-tijd/kinderen-en-jongeren/opvang-en-vakantie/kinderopvang-babys-en-peuters) verwijst de gemeente naar Opvang.Vlaanderen. De beschreven flow omvat zoeken op kaart, een account, meerdere aanvragen en opvolging. [Opgroeien](https://www.opgroeien.be/aanbod/kinderopvang/vlaams-en-lokaal-beleid/lokaal-beleid/lokaal-loket-kinderopvang-en-ouders-informeren) identificeert Cubitec als leverancier. [Basisschoolaanmelding](https://www.nazarethdepinte.be/vrije-tijd/kinderen-en-jongeren/onderwijs/centraal-aanmelden-voor-basisscholen) gebruikt een ander portaal, aanmelden.in.

### Meldingen, afval en openbaar domein

Het [meldingenoverzicht](https://www.nazarethdepinte.be/bestuur/burgerparticipatie/burgerinitiatieven/iets-melden) splitst meldingen in negen toegangen. Publieke ruimte, sluikstort, ratten, zwerfkatten, hoornaar en feedback hebben afzonderlijke Drupal-formulieren. Afvalophaling gaat naar [IVM](https://www.ivmmilieubeheer.be/e-loket/meldingsformulier-over-inzamelingen), dat zelf ook Paddle/Drupal Webform gebruikt. Defecte verlichting gaat naar [Fluvius](https://straatlampen.fluvius.be/); gestorven dieren krijgen informatie en onder meer een verwijzing naar Rendac. Eén gemeentelijke statusomgeving voor al deze routes is niet aangetoond; afwezigheid achter de schermen evenmin.

De [afvalkalenderpagina](https://www.nazarethdepinte.be/leven-en-werken/afval-en-recyclage/ophaalkalender) biedt een PDF voor 2026. De [recyclageparkpagina](https://www.nazarethdepinte.be/reserveren) linkt voor De Pinte naar Planyo. Niet zonder meer dezelfde reservatieregel voor het park in Nazareth aannemen.

[Containers](https://www.nazarethdepinte.be/leven-en-werken/mobiliteit-en-openbare-werken/inname-openbaar-domein/container-plaatsen), stellingen, parkeerverboden en signalisatievergunningen leiden naar dezelfde Spotbooking-tenant. Geosparc wordt als leverancier bevestigd in de [Digitaal Vlaanderen-lijst](https://www.vlaanderen.be/digitaal-vlaanderen/onze-diensten-en-platformen/mijn-burgerprofiel/dienstenleveranciers). GIPOD- en andere koppelingen zijn productmogelijkheden; hun lokale configuratie is niet onderzocht.

### Evenementen en verenigingen

Het [evenementenformulier](https://www.nazarethdepinte.be/form/aanvraagformulier-voor-evenement) is een Drupal Webform met acht zichtbare faselabels, inclusief voltooiing. Het noemt voorbereiding van bijlagen en zegt expliciet dat invullen in één sessie moet gebeuren. Zaalhuur, materiaalhuur, vergunningaanvraag en aankondiging zijn afzonderlijke toegangspunten in de [organisatiewegwijzer](https://www.nazarethdepinte.be/vrije-tijd/organiseren).

Voor aankondigingen gebruikt men [UiTdatabank](https://www.nazarethdepinte.be/vrije-tijd/organiseren/evenement-aankondigen/jouw-activiteit-in-de-uitdatabank-0); de gemeente beschrijft hergebruik op website, nieuwsbrief en magazine. Dit is een bestaande inhoudsketen waarop we kunnen voortbouwen. [Startsubsidie voor verenigingen](https://www.nazarethdepinte.be/vrije-tijd/organiseren/subsidies-organiseren/startsubsidie-vereniging) is een voorbeeld van een subsidiepagina die naar een gemeentelijk formulier verwijst. Niet iedere subsidieregeling en bijlage is afzonderlijk gecontroleerd.

### Bestuur, ruimtelijke informatie en participatie

[Vergaderingen](https://www.nazarethdepinte.be/bestuur/bekendmakingen/vergaderingen-van-de-raad) hebben een aparte Cipal Schaubroeck-raadpleegomgeving voor agenda's en verslagen, Streamovations voor video en een nieuwsbriefinschrijving. In de raadpleegomgeving zijn kalender- en zoekfuncties zichtbaar. De aanwezigheid van een Company Webcast SDK in de code bewijst niet dat alle lokale video via die speler loopt.

[Omgevingsvergunningen](https://www.nazarethdepinte.be/leven-en-werken/bouwen-en-huisvesting/omgevingsvergunning/omgevingsvergunning-aanvragen) verwijzen naar het Vlaamse Omgevingsloket. [Openbare onderzoeken en beslissingen](https://www.nazarethdepinte.be/bestuur/bekendmakingen/openbare-onderzoeken-en-beslissingen-omgevingsvergunningen) combineren een gemeentelijke consultatie-iframe met een link naar het Vlaamse inzageloket. [Vastgoedinformatie](https://www.nazarethdepinte.be/bestuur/bekendmakingen/reglementen/vastgoedinformatie-aanvragen) verwijst naar VIP/Athumi, met professionele routes via IBOT en RealSmart. Dit onderzoek beschrijft de routes, zonder de juridische aanvraagvoorwaarden te valideren.

Het [stratenplan](https://www.nazarethdepinte.be/vrije-tijd/over-nazareth-de-pinte/stratenplan) is een Geopunt-iframe en een PDF. De onderzochte [inspraakprojecten](https://www.nazarethdepinte.be/besturen/burgerparticipatie/inspraakprojecten) bestaan uit informatiepagina's en rapporten; de twee zichtbare projecten bevatten onder meer resultaten uit 2019 en 2021. Geen afzonderlijk platform zoals CitizenLab of Decidim is hiermee aangetoond. Een volledig beeld van alle participatieactiviteiten vereist aanvullend onderzoek.

### Bibliotheek, vacatures en communicatie

De [bibliotheekwebsite](https://nazarethdepinte.bibliotheek.be/) biedt catalogus/Mijn Bibliotheek, Bieblo, Boekenzoeker, Mijn Leestipper, Fundels, cloudLibrary, Cinebib en GoPress-toegangen. Deze linkinventaris is geen functionele test van elk abonnement. [Cultuurconnect](https://www.cultuurconnect.be/diensten/bibliotheeksysteem) documenteert Wise als gedeelde bibliotheekinfrastructuur en noemt catalogus- en Mijn Bibliotheek-API's. De lokale Wise-configuratie en Openbib-hardware zijn niet onderzocht.

[Gemeentelijke vacatures](https://www.nazarethdepinte.be/leven-en-werken/vacatures) worden via Jobsolutions ingesloten; lokale werkgevers krijgen een link naar Jobsin.Vlaanderen. [Vrijwilligersvacatures](https://www.nazarethdepinte.be/vrije-tijd/vrijwilligerswerk/vrijwilligerswerk-zoeken) gebruiken een Give a Day-script. De [nieuwsbrief](https://www.nazarethdepinte.be/bestuur/communicatie/schrijf-in-voor-onze-nieuwsbrief) gebruikt MailPlus. Sociale netwerken zijn distributiekanalen, niet afzonderlijk doorgelichte gemeentelijke systemen.

ReadSpeaker verzorgt voorlezen. De homepage bevat Matomo Cloud- en Piwik PRO-configuratie, naast EU Cookie Compliance. De aanwezigheid van beide analyticsconfiguraties bewijst noch dubbele telling, noch ongeoorloofde tracking; daarvoor is gericht consent- en netwerkonderzoek nodig.

## 4. Concrete frictie en onderhoudskansen

| Waarneming | Betekenis en voorstel | Zekerheid |
|---|---|---|
| Formulier moet in één keer worden ingevuld | Een voorbereidingsassistent met checklist, voortgang en veilige conceptopslag kan uitval helpen verminderen. Uitval is nog niet gemeten. | Expliciete [formulierinstructie](https://www.nazarethdepinte.be/form/aanvraagformulier-voor-evenement); impact is hypothese. |
| Zoek- en UiT-pagina tonen `Mesh terms » Taxonomy term » Naam` | Interne configuratietekst lekt naar de gebruiker; corrigeer labels en controleer filters op begrijpelijkheid. | Direct op [zoeken](https://www.nazarethdepinte.be/zoeken) en [UiT](https://www.nazarethdepinte.be/vrije-tijd/uit-in). |
| Sitemap publiceert oude `www.nazareth.be`-adressen | Controleer sitemapgenerator, canonicals en redirects. Geen SEO-verlies gekwantificeerd. | Directe [sitemap](https://www.nazarethdepinte.be/sitemap.xml). |
| eGovFlow toont verkiezingscategorie 2024 en herhaalde producten | Catalogusbeheer en archiveringsregels controleren. Bepaalde historische aanvragen kunnen bewust beschikbaar blijven. | Browsercontrole van [catalogus](https://nazarethdepinte.egovflow.be/forms). |
| eGovFlow-privacylink resolveert onder eigen host naar `/www.nazarethdepinte.be/privacyverklaring` | Lijkt een ontbrekend protocol in de link; doelgedrag nog niet getest. | Href zichtbaar in publieke browserinterface. |
| ReCreateX en LUWIO zijn beide gekoppeld aan opvangroutes | Maak een actueel register per locatie en dienst; bevestig migratie en juiste ingang. | Beide portalen en centrale webshop. |
| Stagingachtige `fusienazarethdepinte.paddlecms.net`-links blijven zichtbaar | Controleer links op gewenste publieke host en onderhoudseigenaarschap. Hun bereikbaarheid is niet integraal getest. | Stratenplan en ReCreateX-startpagina. |
| Gemeente erkent toegankelijkheidsbeperkingen | Neem toetsenbord, focus, formulieren, contrast en documenten mee in prioritering. Geen nieuwe volledige WCAG-audit uitgevoerd. | [Verklaring](https://www.nazarethdepinte.be/toegankelijkheidsverklaring), live revisiedatum 13 augustus 2026. |

De live toegankelijkheidsverklaring is recenter dan sommige zoekresultaten, die nog 2021 als laatste revisie tonen. Live inspectie heeft daarom voorrang gekregen op de zoekindex. De oude datum alleen mag niet als bevinding over achterstallig beheer worden gebruikt.

## 5. Wat kan worden geïntegreerd?

| Bouwsteen | Publiek bewijs van mogelijkheden | Wat nog nodig is |
|---|---|---|
| ReCreateX | [Vintia API-documentatie](https://help.vintia.com/recreatex/PDF/API_documentation.pdf) beschrijft SOAP- en JSON-services. | Contract, beschikbare lokale API-versie, scopes, testomgeving en authenticatie. Niet aangenomen dat onze workspace toegang heeft. |
| Mijn Burgerprofiel | [Leveranciersmatrix](https://www.vlaanderen.be/digitaal-vlaanderen/onze-diensten-en-platformen/mijn-burgerprofiel/dienstenleveranciers) beschrijft SSO, status, notificaties en attesten per leverancier. | Per dienst vaststellen wat lokaal geactiveerd is. Een header alleen bewijst geen gedeeld dossier of volledig SSO. |
| UiTdatabank | [publiq-documentatie](https://docs.publiq.be/) biedt API's, OpenAPI-bestanden, integratieregistratie en widgets. | Toegestane hergebruiksvorm, credentials en afspraken over actualiteit. |
| Planyo | [API-documentatie](https://www.planyo.com/api.php) beschrijft reservatiefuncties en webhooks; documentatie via zoekindex gecontroleerd, directe webtool-opvraging gaf 403. | Rechten en testaccount. Een sandbox kan productiegegevens kopiëren en is daarom niet vanzelf geschikt voor dit publieke experiment. |
| Timeblockr | De publieke gemeentelijke widget gebruikt een cloud-API. [Vendorinformatie](https://timeblockr.com/agenda-connector/) beschrijft agenda-connectoren. | Integratiecontract en lokale configuratie; geen onbevoegd hergebruik van interne widgetcalls. |
| Bibliotheek | [Cultuurconnect](https://www.cultuurconnect.be/diensten/bibliotheeksysteem) noemt catalogus- en Mijn Bibliotheek-API's. | Aansluitvoorwaarden; persoonlijke bibliotheekgegevens blijven buiten de publieke workspace. |
| Drupal/Paddle | Gestructureerde content en formulieren zijn zichtbaar. | Toestemming voor export/API en rechten op hergebruik; een publiek beschikbare Drupal JSON:API is niet vastgesteld. |
| Raadpleegomgeving en consultatieomgeving | Publieke publicatie- en zoekpagina's. | Machineleesbare export/feed bij leverancier of gemeente navragen; geen API veronderstellen. |

De tabel onderscheidt productmogelijkheden van werkelijk aangetroffen gemeentelijke koppelingen. Integratiemogelijkheid is niet gelijk aan toegang, inbegrepen licentie of toestemming om wijzigingen door te voeren.

## 6. Voorstellen voor experimenten

Dit is een voorgestelde volgorde op basis van publieke waarneembaarheid en verwachte uitvoerbaarheid, geen door de gemeente vastgestelde prioriteit. Werkelijke baten moeten worden getest.

1. **Een betrouwbare dienstengids met bronbeheer.** Gebruik deze inventaris als startpunt. Toon per behoefte de juiste ingang, benodigde voorbereiding, verantwoordelijke dienst en datum van controle. Laat een agent wijzigingen en tegenstrijdigheden voor een redacteur signaleren. Eerste proef: geanonimiseerde taakscenario's over verhuizen, een activiteit organiseren en afval melden. Meet of deelnemers de juiste dienst vinden en hoeveel verkeerde doorverwijzingen voorkomen. Dit kan zonder dossierdata of leverancierskoppelingen.
2. **Een evenementenvoorbereider.** Koppel de openbare instructies voor aanvraag, zaal, materiaal, openbaar domein en aankondiging aan één checklist. Gebruik synthetische voorbeelden en laat gebruikers de uiteindelijke officiële aanvraag zelf indienen. Een productieversie met conceptopslag hoort in een afzonderlijk beveiligde omgeving. Meet volledigheid, voorbereidingstijd en benodigde menselijke correcties.
3. **Een brongebonden bestuursdossier.** Verbind geselecteerde, voor deze publieke repository geschikte beleidsdocumenten, besluiten en projectupdates met een tijdlijn en gecontroleerde samenvatting. Iedere claim krijgt bron en datum; een agent stelt samenvattingen op, een mens beoordeelt ze. Publiceer geen automatisch verzamelde persoonsgegevens uit openbaar gemaakte dossiers. Meet terugvindbaarheid en bronjuistheid.
4. **Een meldingenwegwijzer.** Help onderscheid maken tussen gemeente, IVM, Fluvius en andere bestemmingen. Een eerste experiment geeft de passende officiële route. Uitgebreide dossieropvolging vereist later een gedelegeerde koppeling en afspraken over verantwoordelijke behandelaars. Geen automatische kwalificatie van formele klachten met gevolgen voor rechten of termijnen.
5. **Een activiteiten- en opvangwegwijzer.** Bundel openbaar aanbod en leg uit welke inschrijfroute voor welke locatie geldt. Start met verifiëren van de ReCreateX/LUWIO-overlap en gebruik waar passend UiTdatabank. Laat toekenning, capaciteit, prijsbepaling en gezinsgegevens in de bevoegde systemen.

Geen van deze voorstellen is gebouwd, gedeployd of geactiveerd door dit onderzoek. Vooral de dienstengids en evenementenvoorbereider sluiten aan bij het experiment zonder overheidsbeslissingen over te nemen.

## 7. Onzekerheden die gemeentelijke validatie vereisen

- Actuele applicatie- en leveranciersinventaris, contractduur, kosten en exit-/exportafspraken.
- Werkelijke verdeling tussen ReCreateX en LUWIO per opvanglocatie, activiteit en registratieperiode.
- Interne verwerking van Drupal-formulieren: inbox, zaaksysteem, registratie, toewijzing en terugkoppeling.
- Gebruik, taakvoltooiing, afhaken, ondersteuningsvragen, foutieve routering en verwerkingstijden.
- Bestaande SSO-, Mijn Burgerprofiel-, notificatie- en statuskoppelingen per dienst.
- Beschikbare testomgevingen met uitsluitend synthetische gegevens, API-documentatie en leesrechten.
- Toegankelijkheid van de volledige keten, inclusief externe portalen en de mobiele app.
- Overige diensten die niet via de gecontroleerde navigatie zichtbaar waren, oudere microsites, onderwijs- en zorgpartners en interne systemen.

Een publiek [fusieprofiel uit maart 2023](https://nazarethdepinte.be/sites/default/files/2023-03/20230310%20Profielfoto%20De%20Pinte%20-%20Nazareth.pdf) noemt onder meer eGovFlow, Bravo/csDabs en verschillende Cevi/CS-toepassingen. Dit is een **historische aanwijzing**, geen bevestiging van hun huidige inzet. Het rapport is alleen gebruikt om die beperking te markeren; geen intern softwarelandschap wordt ervan afgeleid.

## Bestanden en bijdrageverantwoording

- `ONDERZOEK.md`: Nederlandstalige conceptanalyse.
- [Briefing websiteproblemen](/briefings/websiteproblemen/): geprioriteerde briefing over werking, links, prestatie en herstel.
- `diensteninventaris.csv`: 40 gestructureerde categorieën met bron, datum, bestemming en bewijsgrens.
- `diensteninventaris.json`: dezelfde inventaris met bijdrageverantwoording.
- `bronmanifest.json`: technische responsmetadata voor hercontrole, zonder ruwe pagina's of persoonsgegevens.
- `website-controles.json` en `audit_public.py`: herhaalbare transportcontroles van kritieke publieke ingangen.
- `prestatie-hermeting.json`: ruwe herhaalmetingen van UiT, zoeken en ReCreateX.

Rol: onderzoeker en analist. Inputs: expliciete onderzoeksvraag, AGENTS.md, genoemde publieke bronnen, live HTTP/HTML/JavaScript en browserwaarnemingen. Systeem: OpenAI Codex / GPT-6. Menselijke reviewer: nog niet toegewezen. Dispositie: lokale conceptbijdrage, beoordeling openstaand. Er is geen besluit genomen, publicatie uitgevoerd of bericht naar de gemeente of leveranciers gestuurd.
