---
title: "P3 — Meldpunt openbare ruimte"
status: werkende-synthetische-demo
language: nl-BE
updated: 2026-09-07
agent_role: dienstontwerper-meldingen
agent_system: OpenAI Codex / GPT-6
reviewer: nog-niet-toegewezen
disposition: geimplementeerde-demo-met-gecontroleerde-workflow
publication_approval: beveiligde-testdeployment-door-gebruiker-toegestaan
project_id: P3
sequence: 3
stage: Werkende meldingsdemo
summary: Geïntegreerde meldingsdemo met hervatbare voorbereiding, medewerkerwerkbak, uitlegbare routevoorstellen en een gedeelde tijdlijn.
first_release: Gemeentelijke procesreview en repetitie van de complete fictieve meldingsketen.
timebox: Demo gebouwd · procesreview als volgende stap
next_step: Laat medewerkers de routevoorstellen en statusbetekenissen beoordelen; ontwerp daarna beveiligde dossieropslag.
delivery_title: "Probeer het meldpunt: van inwoner tot medewerker"
delivery_summary: Een complete fictieve meldingsketen is gebouwd. Beide rollen delen demodata in dezelfde browser; echte accounts, gemeentelijke koppelingen en notificaties zijn nog niet aangesloten.
publication_label: Beveiligde test toegestaan · uitsluitend fictieve meldingen
demo_url: https://website.nazarethdepinte.net/meldpunt/
local_url: http://127.0.0.1:4328/meldpunt/
---

# P3 — Meldpunt openbare ruimte

Dit is een onafhankelijk interactief prototype. Het is geen operationeel gemeentelijk meldpunt en garandeert geen interventie.

## Actuele stand — 7 september 2026

**Gebouwd:** een inwonerflow in drie stappen met concept bewaren/hervatten, categorievoorstel, fictieve kaart én tekstalternatief, bevestiging en een lokaal demokenmerk. Twee startscenario’s (losse tegel en straatlamp) en drie vooraf gevulde meldingen maken de demo herhaalbaar.

**Gebouwd voor medewerkers:** werkbak met zoeken en filters, uitlegbare en corrigeerbare routevoorstellen, een mogelijke dubbelmelding, menselijke bevestiging van de behandelaar, bewaakte statusovergangen en aanvullende vragen. De inwoner kan antwoorden en ziet dezelfde tijdlijn. JSON-export en reset met bevestiging zijn beschikbaar.

**Architectuur:** geïntegreerd in de website op `/meldpunt/`, met eigen broncode in `repos/service-platform/apps/meldpunt`. De Astro-website neemt een expliciete distributiesnapshot met hashmanifest over. Dezelfde app kan zelfstandig worden geserveerd. Zo voelt het voor inwoners als één website en blijft het dienstproces onafhankelijk te ontwikkelen.

**Eerlijke grens:** beide rollen zijn een zichtbare demoschakelaar in dezelfde browser, geen echte accounts. LocalStorage deelt gegevens tussen tabbladen van dezelfde website, niet tussen apparaten of personen. Routevoorstellen zijn deterministische trefwoordregels, geen live taalmodel. Geen echte foto-upload, geolocatie, verzending, notificatie of gemeentelijke koppeling. Cloudflare Access beschermt de testsite maar is geen autorisatie tussen de demorollen.

**Gecontroleerd:** vier modeltests voor de volledige keten, rol- en statusbewaking, validatie/opslagherstel en routevoorstellen; Astro-check en volledige websitebuild/linkaudit. In de browser zijn concept hervatten na herladen, inwoner → medewerker → aanvullende vraag → inwonerreactie, blijvende tijdlijn en reset gecontroleerd, ook op 390px breedte. Dit bewijst geen WCAG-conformiteit of productiegeschiktheid.

**Volgende stap:** demonstreer één fictief voetpadprobleem aan de proceseigenaar en valideer categorieën, bevoegdheden, statusbetekenissen en terugkoppeling. Daarna volgt een afzonderlijke beveiligde alfa met serveropslag, identiteit, bevoegdheidscontrole en auditlog. Er is nog geen gemeentelijke eigenaar benoemd; echte dossiers horen niet in Git.

[Demo-architectuur en draaiboek](/knowledge/docs/architecture/P3-MELDPUNT-DEMO/) · [Gezamenlijk demoplan](/briefings/demo-gemeenteteam/). Bewijs: lokale broncode, modeltests, websitebuild en browsercontrole op 7 september 2026.

## Doelbeeld en backlog — onderstaande functies zijn voorstellen

## Opdracht

Bied één begrijpelijke ingang voor meldingen over de openbare ruimte en gemeentelijke dienstverlening. Het systeem helpt een melder de bevoegde route vinden, vraagt alleen noodzakelijke informatie, geeft een ontvangstbewijs en maakt opvolging mogelijk. Formele klachten, noodsituaties en meldingen buiten gemeentelijke bevoegdheid krijgen een duidelijk afgescheiden route.

Met **publieke rapportering** bedoelt dit project meldingen door inwoners over de openbare ruimte, plus eventueel later geanonimiseerde rapportage over trends. Het gaat niet om financiële of bestuurlijke verslaggeving.

## Aanleiding en bronnen

Op **6 september 2026** verwees de publieke website voor meldingen naar verschillende bestemmingen, waaronder gemeentelijke formulieren, IVM en Fluvius. Eén gezamenlijk statusoverzicht kon via publieke inspectie niet worden bevestigd. Zie de sectie over meldingen in het [onderzoek](../evidence/2026-09-06-digitale-dienstverlening/ONDERZOEK.md). De afwezigheid van zo'n overzicht achter de schermen is daarmee niet bewezen; interne volumes, routering en behandeltijden moeten nog worden gevalideerd.

## Eerste meldingsdomeinen

- weg, voetpad, fietspad en verkeersmeubilair;
- straatverlichting;
- sluikstort, afval en inzameling;
- groen, bomen, water en speelruimte;
- dieren op of langs de openbare weg;
- schade of defect aan gemeentelijke publieke infrastructuur;
- algemene vraag of signaal over gemeentelijke dienstverlening.

Noodsituaties krijgen onmiddellijk de juiste noodinstructie. Een formele klacht, bezwaar- of beroepsprocedure blijft herkenbaar apart, met de officiële termijn en bevoegde route uit een gecontroleerde bron.

## MVP: routeringsprototype

1. Een taakgerichte categorieboom in gewone taal, met zoeken op probleemomschrijving.
2. Een bevoegdheidsregister dat per categorie gemeente, IVM, Fluvius of een andere bestemming toont, inclusief bron, eigenaar en controledatum.
3. Een kaart met uitsluitend synthetische locaties en voorbeelden.
4. Uitleg welke informatie nodig is en waarom; foto en contactgegevens zijn optioneel tenzij een bevoegde proceseigenaar noodzaak aantoont.
5. Een overdrachtsblad naar de bestaande officiële route, zonder automatische indiening.
6. Een medewerkerweergave voor synthetische triage, doorsturen, samenvoegen en terugkoppelen.

## Gewenste productiecapaciteiten

- beveiligd indienen, ontvangstbewijs en volgen met een dossierkenmerk;
- adres- en kaartvalidatie zonder de precieze locatie publiek te maken;
- gestandaardiseerde statussen: ontvangen, te beoordelen, doorgestuurd, gepland, uitgevoerd, gesloten en heropend;
- overdracht tussen bevoegde organisaties met eigenaar, tijdstip en reden zichtbaar voor de melder;
- duplicaatsuggesties voor medewerkers, met menselijke bevestiging vóór samenvoegen;
- toegankelijke notificaties en een gelijkwaardig telefoon- of baliekanaal;
- een publiek dashboard met uitsluitend voldoende geaggregeerde, beoordeelde en niet-herleidbare gegevens.

## Autoriteitsmodel

| Handeling | Menselijke eigenaar | Agentrol |
|---|---|---|
| Probleem beschrijven en indienen | melder of gemachtigde | invoer uitleggen en mogelijke categorie voorstellen |
| Categorie en bevoegdheid bevestigen | benoemde triagemedewerker of vastgestelde deterministische regel | voorstel met bron tonen |
| Prioriteit, planning en inzet bepalen | bevoegde operationele dienst | nooit bindend bepalen |
| Doorsturen of samenvoegen | bevoegde medewerker | overeenkomst signaleren en overdracht voorbereiden |
| Sluiten en antwoord geven | verantwoordelijke behandelaar | conceptantwoord voorbereiden |
| Formele klacht of beroep behandelen | bevoegde procedure en mens | officiële route uitleggen |

Een model mag geen urgentie, geloofwaardigheid, handhaving of recht op dienstverlening bindend bepalen. Bij mogelijk acuut gevaar toont de interface de gecontroleerde noodroute en wacht zij niet op automatische classificatie.

## Gegevensgrens

Echte contactgegevens, exacte locaties die naar een persoon verwijzen, foto's, vrije tekst en dossierhistoriek horen in een bevoegd operationeel systeem, niet in deze publieke repository. Vrije tekst en afbeeldingen kunnen gevoelige informatie bevatten en vereisen toegangscontrole, verwijdering, logging en een menselijke moderatieroute. Publieke trendrapporten gebruiken minimale aggregatie, onderdrukkingsregels en menselijke vrijgave.

## Opleverfasen

| Fase | Resultaat | Beslismoment |
|---|---|---|
| 0. Dienstonderzoek | Meldingsvolumes, routes, SLA-bronnen, uitzonderingen en klachtenafbakening | proceseigenaars bevestigen bevoegdheid en waarheid |
| 1. Prototype | Routering met synthetische locaties en overdrachtsbladen | inwoner- en medewerkerstest |
| 2. Beveiligde alfa | Dossieropslag, kaart, notificatie, auditlog en testadapters | privacy-, security- en architectuuracceptatie |
| 3. Bèta | Beperkte proef met benoemde behandelaars en terugvalroute | operationele en onafhankelijke evaluatie |
| 4. Productie | Goedgekeurd meldpunt, support, monitoring en exitplan | expliciete menselijke go-livebeslissing |

## Voorgestelde acceptatiecriteria

- Minstens 95% van de vooraf vastgestelde synthetische meldscenario's komt bij de juiste bevoegde route; alle fouten worden verklaard en hersteld vóór bèta.
- Nood, formele klacht en gewone melding zijn in elke relevante stroom duidelijk onderscheiden.
- De melder kan steeds zien wie de huidige behandelaar is, waarom een melding is doorgestuurd en wat de volgende stap betekent.
- WCAG 2.2 AA voor invoer, kaartalternatief, foutmeldingen, status en notificaties.
- Geen persoonsgegevens of echte meldingen in Git, openbare dashboards, testdata of onbevoegde analytics.
- Geen automatische bindende prioriteit, samenvoeging, sluiting of handhavingsactie.
- De stuurgroep stelt na nulmeting doelen vast voor juiste routering, eerste reactie, oplostijd, heropeningen en kanaalverschuiving.

## Eerste werkpakket van zes weken

- inventariseer categorieën, bevoegdheden, huidige formulieren, contactkanalen en eigenaars;
- scheid nood, klacht, bezwaar, vraag en melding in een beoordeelde taxonomie;
- ontwerp tien synthetische scenario's over de vier deelkernen en externe partners;
- test categorieboom, zoekfunctie en kaartalternatief met inwoners en medewerkers;
- lever een integratie- en gegevensbeschermingsnota op voor gemeente, IVM, Fluvius en Mijn Burgerprofiel, zonder toegang te veronderstellen.

## Bijdrageverantwoording

Rol: dienstontwerper-meldingen. Inputs: gebruikersopdracht, workspace-regels en publieke audit van 6 september 2026. Systeem: OpenAI Codex / GPT-6. Menselijke reviewer: nog niet toegewezen. Dispositie: lokaal voorstel; geen melding ontvangen, doorgestuurd of behandeld.

Statusbijdrage op 7 september 2026: rol portfolioreviewer; inputs gebruikersopdracht, projectvoorstel en lokale implementatiecontrole; systeem OpenAI Codex / GPT-6; reviewer nog niet toegewezen; dispositie actuele status onderscheiden van voorgestelde functies, geen nieuwe applicatie gedeployed.

Implementatiebijdrage op 7 september 2026: rol civic-serviceontwikkelaar; inputs gebruikersopdracht, P3-project, demoplan en bestaande websitehuisstijl; systeem OpenAI Codex / GPT-6; reviewer nog niet toegewezen; dispositie werkende synthetische demo, geen echte melding verwerkt. De oudere statusbijdrage hierboven beschrijft de toestand vóór deze implementatie.
