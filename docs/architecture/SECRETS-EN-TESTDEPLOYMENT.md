---
title: "1Password en Cloudflare-testdeployment"
status: testwebsite-actief-achter-access
language: nl-BE
updated: 2026-09-07
agent_role: workspace-en-deploymentontwikkelaar
agent_system: OpenAI Codex / GPT-6
reviewer: nog-niet-toegewezen
disposition: access-policy-en-vijf-anonieme-redirects-geverifieerd
---

# 1Password en Cloudflare-testdeployment

De testwebsite is op 7 september 2026 geactiveerd op [website.nazarethdepinte.net](https://website.nazarethdepinte.net), achter Cloudflare Access. De gebruiker heeft één individueel adres en alle adressen van het gemeentelijke e-maildomein expliciet toegestaan. De opgeslagen policy en vijf anonieme redirects zijn gecontroleerd; aanmelden als toegelaten gebruiker moet nog door een mens worden uitgevoerd. Het betreft geen officiële gemeentelijke dienst.

## Lokale tokeninvoer

In de workspace-root staat `.env`, uitgesloten van Git en aangemaakt met bestandsrechten `0600`. Plak uitsluitend daar de **1Password service-accounttoken** bij `OP_SERVICE_ACCOUNT_TOKEN`. De CLI `op` is lokaal beschikbaar, gecontroleerde versie 2.39.0. Geef het service-account leestoegang tot alleen de kluis die de deploymentcredentials bevat.

De gedeelde instellingen staan in [`config/deployment.json`](../../config/deployment.json): Cloudflare-account-ID, zone-ID, hostname en 1Password-referenties. `onePassword.vaultId` identificeert de teamkluis; de service-accountconfiguratie bepaalt de feitelijke toegang.

`onePassword.cloudflareApiTokenRef` bevat de gedeelde verwijzing naar het API-tokenveld, bijvoorbeeld `op://vault/item/field`, nooit de echte tokenwaarde. Iedere medewerker gebruikt een eigen bevoegd service-accounttoken in `.env`; `.env.example` bevat alleen dat lege tokenveld. Bewaar bevestigde toegelaten e-mailadressen als kommagescheiden veld in 1Password en zet de verwijzing in `onePassword.cloudflareAccessEmailsRef`. De referentie is ingevuld na de expliciete gebruikersopdracht. `cloudflare.accessEmailDomains` bevat de eveneens expliciet toegelaten e-maildomeinen. Zo zijn instellingen en verwijzingen deelbaar, terwijl persoonlijke e-mailadressen buiten de publieke repository blijven.

De workspace `.env` staat buiten de Astro-website en wordt niet in de publieke build opgenomen. Geen secrets toevoegen aan `PUBLIC_*` variabelen, contentcollecties, browsercode of GitHub. Gebruik geen `cat .env`, `printenv`, shell tracing of `op read` met terminaluitvoer om de waarden te controleren.

## Geheimen alleen beschikbaar tijdens de opdracht

Controle zonder waarden te tonen, vanaf de workspace-root:

```sh
node scripts/with-1password.mjs status
```

Een Cloudflare-controle uitvoeren:

```sh
node scripts/with-1password.mjs -- node repos/municipal-website/scripts/deploy-cloudflare.mjs --check
```

De wrapper leest alleen de service-accounttoken uit `.env` als data, niet als shellcode. De overige instellingen komen uit `config/deployment.json`, niet uit lokale of geërfde Cloudflare-variabelen. `op run` lost de gedeelde 1Password-referenties op en maskeert secretwaarden in uitvoer. Een tussenproces verwijdert alle `OP_*` variabelen voordat het deploymentcommando start, zodat dat commando niet zelf bij de kluis kan. De wrapper schrijft opgehaalde geheimen niet naar schijf. Gebruik de wrapper alleen voor vertrouwde opdrachten: een proces met credentials kan die technisch gebruiken of doorsturen.

[1Password service-accounts](https://www.1password.dev/service-accounts/get-started), [op run](https://www.1password.dev/cli/reference/commands/run), geraadpleegd 07-09-2026.

## Cloudflare-inrichting vóór de eerste upload

1. Controleer het bedoelde account, de actieve .net-zone en de testhostname in `config/deployment.json`: `website.nazarethdepinte.net`.
2. Activeer Zero Trust en een beschikbare aanmeldmethode. Maak één self-hosted Access-app voor de **volledige hostname**, zonder padbeperking.
3. Voeg een Allow-policy met de uitdrukkelijk toegelaten e-mailadressen toe. Geen Everyone- of Bypass-regel. Een volledige e-maildomeinregel is alleen toegestaan voor een expliciet door de gebruiker genoemd domein. Controleer ook op onderliggende padregels die de hoofdpolicy zouden overschrijven.
4. Het API-token moet op het bedoelde account en de zone worden beperkt. Nodig zijn de relevante Workers-deployrechten, zone-inzage/custom-domainrechten en Access-leesrechten op account- en zoneniveau. Voor de eerste Access-inrichting zijn tevens de bijbehorende Access-schrijfrechten nodig. Valideer de precieze rechten tegen de API-responses; gebruik geen globale API-key.
5. Voer `--check` uit. Dit leest de zone, Access-apps en policies en vergelijkt de toelatingen met de via 1Password opgehaalde lijst; het maakt of wijzigt nog niets.

Na het opslaan van de bevestigde e-mailadressen in de teamkluis en hun referentie in de gedeelde configuratie kan de eerste Access-inrichting worden uitgevoerd met de opdracht hieronder. Deze hergebruikt of maakt een e-mailcode-provider en maakt een hostname-app met uitsluitend de opgegeven adressen en expliciet toegelaten e-maildomeinen. Bestaande apps worden niet overschreven. Daarna controleert `--check` de daadwerkelijk opgeslagen policy opnieuw. Zonder e-mailadressen schrijft dit script niets naar Cloudflare.

```sh
node scripts/with-1password.mjs -- node repos/municipal-website/scripts/setup-cloudflare-access.mjs
```

Dit is ontbrekende configuratie, geen nieuwe algemene toestemmingseis. Het opvragen van een aanmeldcode wordt pas door de gebruiker zelf op de loginpagina gestart.

## Website uploaden en controleren

### Afbakening van de upload

Cloudflare ontvangt alleen de gebouwde website uit `repos/municipal-website/dist`, zoals ingesteld in `wrangler.json`. Het bronarchief (`content/source-archive`), crawlstatus, importbestanden, ontwikkelscripts, rapporten en lokale secrets horen niet in de deployment. Een wijziging aan uitsluitend het crawlarchief vereist geen nieuwe deployment; pas wanneer de wijziging in de website of haar aangeboden content is verwerkt, is een nieuwe build en deployment relevant.

Controle op 7 september 2026: het bestaande buildresultaat bevatte geen `source-archive`, `catalog.json`, `resources.json`, `import-index` of `.env`. Alle 1.181 bestanden onder `dist/source-files` werden verwezen vanuit gebouwde websitebestanden. Daarbij tellen ook de expliciet aangeboden collectie-API's mee: de huidige website publiceert alle geïmporteerde document- en mediacollecties, ook wanneer een bestand niet op de homepage staat. Astro kopieert de volledige map `public` naar de build; alleen de keuze voor `dist` sluit ongebruikte bestanden in `public` dus niet automatisch uit. Bij uitbreiding van de import moet deze scheiding behouden blijven.

Verantwoording van deze afbakening: rol deployment-auditor; inputs gebruikersvraag, lokale Wrangler-configuratie, importscript, collectie-API en bestaand buildresultaat; systeem OpenAI Codex / GPT-6; reviewer nog niet toegewezen; dispositie lokale controle en documentatie, geen nieuwe upload uitgevoerd.

```sh
node scripts/with-1password.mjs -- node repos/municipal-website/scripts/deploy-cloudflare.mjs --deploy
```

De deployment gebruikt de bestaande statische Astro-build via **Workers Static Assets**. `wrangler.json` bevat geen credentials of werkende domeinroute; standaardhostnamen en preview-URL's staan uit. Alleen na Access-controle schrijft de launcher een lokaal genegeerde `.wrangler/deploy.json` met de gekozen custom domain. De volledige build, linkaudit en content/routeaudit moeten slagen vóór Wrangler uploadt. De geïnstalleerde Wrangler-versie bij voorbereiding is 4.125.0.

Na upload controleert het script anonieme verzoeken naar homepage, Agenda, Bestuur, collectie-API en een PDF: deze moeten naar Access-aanmelding verwijzen. Een mislukte controle is geen geslaagde deploymentacceptatie. Controleer vervolgens met de toegelaten gebruiker dat aanmelden, navigatie en documenten werken; er wordt geen login of OTP gesimuleerd. Controleer ook in Cloudflare dat standaard- en previewhostnamen uitgeschakeld zijn.

Bronnen, geraadpleegd 07-09-2026: [Workers Access](https://developers.cloudflare.com/workers/configuration/cloudflare-access/), [workers.dev uitschakelen](https://developers.cloudflare.com/workers/configuration/routing/workers-dev/), [Wrangler-configuratie](https://developers.cloudflare.com/workers/wrangler/configuration/), [Static Assets](https://developers.cloudflare.com/workers/static-assets/get-started/), [Access API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/methods/list).

## Gecontroleerde lokale fout: lege content in de preview

Op 7 september retourneerde de draaiende preview voor Agenda HTTP 200 met nul activiteiten en voor `/themas/bestuur-inspraak/` HTTP 404. De contentbestanden waren aanwezig, maar de reeds draaiende Astro-server had de nieuw ingevoerde collections niet geladen. Na een volledige herstart leverde de collectie-API alle twaalf gevulde collecties; Agenda bevatte 325 evenementen en Bestuur opnieuw inhoudskaarten.

De handmatige globale module-invalidation op het diagnostische catalogusbestand is verwijderd; Astro's collectionloaders beheren de inhoudsupdates. Een guard voorkomt stil renderen met lege kerncollecties. De nieuwe `audit:routes` controleert de echte inhoud van de API, alle negen thema's, de hoofdmenu-ingangen en representatieve detailpagina's. Deze audit draait op de build én is expliciet op de lokale preview uitgevoerd. Een succesvolle build alleen is geen bewijs dat een oude preview-server dezelfde inhoud toont.

## Verantwoording

Rol: workspace- en deploymentontwikkelaar. Inputs: gebruikersopdracht, lokale website, root/private AGENTS.md, officiële 1Password- en Cloudflare-documentatie. Systeem: OpenAI Codex / GPT-6. Reviewer: nog niet toegewezen. Dispositie: lokale implementatie en verificatie; 1Password- en Cloudflare-authenticatie zijn gecontroleerd; Access-toelatingen en externe deployment zijn nog openstaand. Tokens en toegelaten identiteiten worden niet in dit document geregistreerd.

## Verificatie op 7 september 2026

De 1Password service-accounttoegang en API-toegang tot Cloudflare zijn echt getest; geheimen werden niet getoond. Op verzoek van de gebruiker zijn de `op://`-referentie en account-, zone- en hostnamevelden vervolgens naar `config/deployment.json` verplaatst. Alleen de service-accounttoken blijft in `.env`. Deze token wordt niet aan het deployment-subproces doorgegeven.

Website: twintig unit tests geslaagd, geen Astro-checkfouten, 3.208 gebouwde routes, nul fouten in de standalone-linkaudit. De aanvullende audit controleerde twintig responses, twaalf gevulde collecties, alle negen thema's en 325 evenementkaarten. De live preview doorstond deze controle ook na een build. De Workspace Web-build en -check slaagden; de briefing is via de lokale UI bereikbaar. Wrangler 4.125.0 accepteert de configuratie in een dry run. Dit bewijst nog geen werkende externe Access-aanmelding; daarvoor ontbreken de bevestigde toelatingen.

## Upload voltooid — 7 september 2026

De Astro-build is werkelijk naar het eigen Cloudflare-account geüpload. De volledige upload bevatte 3.921 nieuwe unieke bestanden; 500 bestanden waren al aanwezig. Alle 3.208 HTML-routes en lokale content maakten deel uit van de gevalideerde build. De Cloudflare API bevestigt een actieve Worker-versie. `workers.dev` en preview-URL's zijn uitgeschakeld; er zijn geen custom domains of zone routes aan deze Worker gekoppeld. Er is dus nog geen publiek bereikbare testwebsite.

De credentials voor 1Password en Cloudflare zijn operationeel en behoeven voor deze stap geen verdere invoer. Alleen de expliciet toegelaten e-mailadressen ontbreken nog. Zodra die bevestigd zijn, kan de voorbereide Access-inrichting worden uitgevoerd en de testhostname worden geactiveerd. De versie-ID en technische verificatie staan in `repos/municipal-website/reports/cloudflare-deployment.json` in de private repository. Deze actualisering vervangt eerdere vermeldingen dat nog niets naar Cloudflare is geüpload.

Configuratiecorrectie op 7 september 2026: rol workspaceontwikkelaar; inputs gebruikerscorrectie en bestaande geteste deploymentinstellingen; systeem OpenAI Codex / GPT-6; reviewer nog niet toegewezen; dispositie gedeelde configuratie en aangepaste launcher, zonder wijziging aan Cloudflare-toegang of deployment.

## Access geactiveerd — 7 september 2026

De gebruiker heeft één individueel adres (opgeslagen in 1Password) en het volledige e-maildomein `nazarethdepinte.be` (gedeelde configuratie) expliciet toegelaten. De Include-regels zijn alternatieven. De Access-app beschermt de volledige hostname, gebruikt uitsluitend de e-mailcode-provider en een sessie van acht uur. Vier gerichte policytests zijn geslaagd; de opgeslagen policy is gecontroleerd op de exacte toegelaten adressen en domeinen en op afwezigheid van bredere regels.

De bestaande gevalideerde Worker-versie is geactiveerd zonder nieuwe contentupload. `workers.dev` en previews blijven uitgeschakeld. Homepage, Agenda, Bestuur, collectie-API en een PDF retourneerden elk HTTP 302 naar de verwachte Access-login. Een tijdelijke negatieve lokale DNS-cache is ondervangen met verse DNS-resolutie en volledige TLS-certificaatcontrole. Er is geen aanmeldcode aangevraagd en geen aanmelding namens een gebruiker uitgevoerd.

Activering van een reeds gevalideerde upload: `node scripts/with-1password.mjs -- node repos/municipal-website/scripts/deploy-cloudflare.mjs --activate-existing`. Dit controleert Access en de actieve versie tegen het eerdere deploymentrapport en stopt bij een afwijkende versie. Nieuwe website-inhoud gebruikt nog steeds `--deploy` voor build en upload.

Bronnen: lokale API- en HTTPS-verificatie van 7 september 2026, het private deploymentrapport, [Cloudflare Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) en [Custom Domain API](https://developers.cloudflare.com/api/resources/workers/subresources/domains/methods/update/), geraadpleegd 7 september 2026. Rol: deploymentontwikkelaar en verificateur. Inputs: expliciete gebruikersopdracht, gedeelde configuratie, 1Password, eerdere upload en Cloudflare API. Systeem: OpenAI Codex / GPT-6. Reviewer: nog niet toegewezen. Dispositie: testhostname actief en anonieme toegang gecontroleerd; menselijke aanmelding nog te bevestigen. Deze status vervangt eerdere wachtstatussen hierboven.

## Correctie op de browsercontrole — 7 september 2026

Na de melding dat de testwebsite niet laadt, is `ERR_NAME_NOT_RESOLVED` in de browser vastgesteld. De macOS-systeemresolver retourneert `ENOTFOUND`, terwijl publieke en geconfigureerde DNS-servers correcte adressen teruggeven. De live Cloudflare Access-policy en HTTPS-redirects met verse DNS zijn opnieuw gecontroleerd. Dit bevestigt de werking van de externe toegangslaag, maar bewijst geen geslaagde lokale browserverbinding.

Een cacheflush zonder beheerdersrechten loste het probleem niet op; herladen van de macOS DNS-daemon vereist een beheerderswachtwoord. De agent heeft geen DNS-instellingen veranderd of toegangsbeveiliging verzwakt. De standaard deploymentcontrole gebruikt voortaan de normale systeemresolver; verse DNS is uitsluitend een expliciete diagnostische optie. De eerdere succesvolle controles met verse DNS mogen niet als bewijs voor lokale browserbereikbaarheid worden gelezen.

Rol: deploymentdiagnosticus. Inputs: gebruikersmelding, browserfout, lokale resolvermetingen en Cloudflare API. Systeem: OpenAI Codex / GPT-6. Reviewer: nog niet toegewezen. Dispositie: oorzaak gelokaliseerd; lokale beheerder moet de systeem-DNS-cache verversen; menselijke aanmelding nog openstaand.

## Naam op de Access-login — 7 september 2026

Op expliciet verzoek is de verouderde automatisch gegenereerde organisatienaam vervangen door **Nazareth-De Pinte · Testomgeving**. De gedeelde gewenste waarde staat in `config/deployment.json` onder `cloudflare.accessOrganizationName`. De bestaande authenticatiedomeinnaam en alle overige teruggelezen organisatie-instellingen zijn behouden. Een verse anonieme loginpagina retourneerde HTTP 200 en toonde de nieuwe naam na korte propagatie.

Rol: deploymentbeheerder. Inputs: gebruikersscreenshot, expliciete correctieopdracht en Cloudflare-organisatie-API. Systeem: OpenAI Codex / GPT-6. Reviewer: nog niet toegewezen. Dispositie: alleen weergavenaam aangepast en live gecontroleerd. Bron: [Cloudflare organization update API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/organizations/methods/update/), geraadpleegd 7 september 2026.

## Meldpuntdemo — 7 september 2026

De meldpuntdemo is geïntegreerd op `/meldpunt/` en gebruikt een expliciete distributiesnapshot uit `repos/service-platform/apps/meldpunt`. De bestaande Access-policy is behouden. De deploymentcontrole omvat nu ook `/meldpunt/` en `/meldpunt-app/app.js`; alle zeven anonieme probes verwijzen naar Access. De ingelogde browser toont de werkende app. Demorollen zijn geen afzonderlijke accounts: lokale browseropslag en fictieve gegevens blijven de grens. Zie [architectuur en verificatie](/knowledge/docs/architecture/P3-MELDPUNT-DEMO/).

Bijdrage: civic-serviceontwikkelaar; inputs gebruikersopdracht, bestaande deploymentconfiguratie, P3-code en verificatie; systeem OpenAI Codex / GPT-6; reviewer nog niet toegewezen; dispositie toevoeging aan de toegestane beveiligde testwebsite, geen nieuwe toegangsrechten of echte dossiers.
