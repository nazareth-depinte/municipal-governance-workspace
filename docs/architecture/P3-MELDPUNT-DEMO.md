---
title: "Meldpuntdemo — architectuur, werking en draaiboek"
status: geimplementeerde-synthetische-demo
language: nl-BE
updated: 2026-09-07
agent_role: civic-serviceontwikkelaar
agent_system: OpenAI Codex / GPT-6
reviewer: nog-niet-toegewezen
disposition: beveiligde-testdeployment-gecontroleerd
---

# Meldpuntdemo — architectuur, werking en draaiboek

De eerste meldingsketen is gebouwd en op 7 september 2026 gedeployed op [de beveiligde testwebsite](https://website.nazarethdepinte.net/meldpunt/). Dit is een onafhankelijk prototype met fictieve gegevens, geen officiële gemeentelijke dienst. De route is ook lokaal beschikbaar op `http://127.0.0.1:4328/meldpunt/`.

## Eén website, zelfstandig ontwikkelbare dienst

Inwoners komen via “Iets melden” op de homepage of via de dienstpagina in dezelfde huisstijl terecht. Broncode, workflowmodel en tests staan afzonderlijk in `repos/service-platform/apps/meldpunt`. De private Astro-repository neemt vier expliciet toegelaten browserbestanden over met `scripts/sync-meldpunt.mjs`; een manifest registreert SHA-256-hashes en herkomst. De website kan daarna bouwen zonder de service-platformcheckout. Dezelfde app kan zelfstandig worden geserveerd; een extra domein of login is voor deze demo niet nodig.

De inzet is bewust klein: native JavaScript, CSS en SVG, zonder externe clientbibliotheken, kaartdiensten of taalmodelaanroepen. De bronbestanden zijn de ontwikkelbasis; de distributiekopie in de website wordt niet handmatig aangepast. Ruwe crawlarchieven worden niet door deze integratie gepubliceerd.

## Gebouwde keten

1. Kies de losse tegel, de straatlamp of een lege demomelding.
2. Beschrijf het fictieve probleem. Controleer het trefwoordgebaseerde categorievoorstel en corrigeer indien nodig.
3. Kies een synthetische locatie via de schematische kaart of de gelijkwaardige tekstkeuze. Voeg een herkenningspunt toe. Het concept blijft na herladen beschikbaar.
4. Controleer het overzicht en bewaar de demomelding. Het lokale kenmerk opent dezelfde tijdlijn voor inwoner en medewerker.
5. Schakel zichtbaar naar de medewerkerdemo. Controleer het routevoorstel en een eventuele mogelijke dubbelmelding. Bevestig of corrigeer categorie en demoteam met een reden.
6. Neem de melding in behandeling en vraag een aanvulling. Schakel terug naar de inwoner en voeg een fictieve reactie toe. Een reactie verandert de status niet automatisch.
7. Laat de medewerker na controle opnieuw in behandeling nemen, inplannen en op uitgevoerd zetten. Download eventueel het JSON-demoverslag of zet de drie voorbeelden terug via de resetbevestiging.

Voorstellen kunnen worden gecorrigeerd; er is geen automatische prioritering, samenvoeging, verzending of sluiting. De routeuitleg verwijst naar de lokale dienstinformatie, gebaseerd op de publieke diensteninventaris van 6 september 2026. De regels zijn nog niet door gemeentelijke proceseigenaars gevalideerd.

## Gegevens en rollen

LocalStorage bewaart uitsluitend demodata onder `civic.meldpunt.demo.v1`. Tabbladen van dezelfde website delen wijzigingen; verschillende apparaten, browsers en localhost versus Cloudflare doen dat niet. Onleesbare opslag wordt niet stilzwijgend overschreven; een blokkade of vol opslagquotum levert een zichtbare melding op. Reset raakt alleen de meldpuntdemodata.

De rolwissel is een demonstratie, geen beveiligde medewerkerslogin. Cloudflare Access beschermt de hele testwebsite met de bestaande toegelaten identiteiten, maar verleent geen verschillende rechten aan deze twee demorollen. Echte accounts, server-side autorisatie, dossieropslag en auditlogging zijn vereist vóór gebruik met echte gegevens. Geen contactgegevens, foto-upload, geolocatie, e-mails, externe aanvragen of echte meldingen zijn aangesloten. De getoonde foto en kaart zijn illustraties.

## Verificatie op 7 september 2026

- Vier modeltests slagen: volledige levenscyclus met reacties, rol- en statusbeperkingen, invoervalidatie/opslagherstel en deterministische voorstellen.
- De Astro-check en volledige websitebuild met route-, collectie- en linkaudits slagen.
- Browsercontrole bevestigt hervatten na herladen, dezelfde melding aan beide kanten, verplichte routebevestiging, aanvullende vraag en inwonerreactie, blijvende tijdlijn en reset naar drie voorbeelden. De mobiele opvolging is gecontroleerd op 390px breedte.
- Cloudflare-deployment `415b2c95-e096-412b-ac3f-2907c7719d6a` is actief. De ingelogde browser toont de werkende startpagina. Zeven anonieme routes, inclusief `/meldpunt/` en `/meldpunt-app/app.js`, verwijzen naar Access.

Deze controles zijn geen WCAG-certificering, onafhankelijke securityaudit of gemeentelijke inhoudsacceptatie. Benoem die grenzen tijdens de demo.

## Volgende implementatie na de demo

Laat eerst de gemeentelijke proceseigenaar met twee medewerkers de categorieën, bevoegdheden, statusbetekenissen en terugkoppeling beoordelen. Bouw vervolgens een afzonderlijke beveiligde alfa met serveropslag, identiteit, autorisatie per dossier, auditlog en bewaartermijnen. Sluit notificaties en gemeentelijke systemen pas aan binnen expliciet bevestigde bevoegdheden en gegevensgrenzen. Een live model kan later beoordeelde publieke broninformatie helpen samenvatten; het krijgt geen beslis- of verzendbevoegdheid.

Bijdrage: civic-serviceontwikkelaar. Inputs: gebruikersopdracht, P3-project, demoplan, bestaande Astro-huisstijl, lokale broncode, tests, browsercontrole en deploymentreceipt. Systeem: OpenAI Codex / GPT-6. Reviewer: nog niet toegewezen. Dispositie: geïmplementeerde synthetische demo op de eerder door de gebruiker toegestane beveiligde testomgeving; geen echte dossiers verwerkt of officiële dienst gepubliceerd.
