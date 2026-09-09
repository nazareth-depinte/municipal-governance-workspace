---
title: "Cloudflare, Europese alternatieven en gemeentelijke compliance"
topic: Hosting
summary: "Cloudflare, Europese alternatieven en de afwegingen voor gemeentelijke test- en productieomgevingen."
status: onderzoeksbriefing-niet-menselijk-beoordeeld
language: nl-BE
updated: 2026-09-07
agent_role: infrastructuuronderzoeker
agent_system: OpenAI Codex / GPT-6
reviewer: nog-niet-toegewezen
disposition: onderzoek-vastgelegd-testhosting-door-gebruiker-gekozen
publication_approval: alleen-beveiligde-proefdeployment-door-gebruiker-gevraagd
---

# Cloudflare, Europese alternatieven en gemeentelijke compliance

**Cloudflare is niet automatisch verboden voor een Belgische gemeente omdat het een Amerikaanse onderneming is. De concrete gegevensverwerking, contracten, internationale doorgiften en beveiliging bepalen de beoordeling.** Voor een publieke informatieve website is een andere afweging nodig dan voor medewerkersportalen en gevoelige burgerdossiers.

Onderzoeksdatum: **7 september 2026**. Dit is agentanalyse op basis van de hieronder vermelde primaire bronnen, geen juridisch advies van de gemeente, aanbestedingsbesluit of productieacceptatie. Deze Nederlandstalige samenvatting is nog niet menselijk beoordeeld. Leveranciersclaims zijn geen onafhankelijk uitgevoerde beveiligingsaudit.

## Keuze van de gebruiker voor de proefomgeving

De gebruiker kiest op 7 september 2026 voor de eigen Cloudflare-account en een reeds aangekocht .net-domein, met testtoepassingen **achter Cloudflare Access**. Credentials worden uit een beperkte 1Password-kluis opgehaald met een service-account. Deze keuze geldt voor de experimentele omgeving; zij is geen gemeentelijke goedkeuring om gevoelige dossiers op Cloudflare te verwerken.

Actualisering op 7 september 2026: de gevalideerde Astro-build is naar Cloudflare geüpload. Accounttoegang via 1Password en de actieve domeinzone zijn bevestigd. De gebruiker heeft de toelatingen bevestigd; de testhostname is geactiveerd achter Access. Vijf anonieme verzoeken, inclusief API en PDF, verwezen naar de Access-login. Standaard-URL en previews blijven uitgeschakeld; menselijke aanmelding moet nog worden bevestigd. Er worden geen tokens, accountgegevens of toegelaten e-mailadressen in deze publieke briefing opgenomen.

## Recht, toezichthouder en technische beoordeling

### AVG en internationale doorgiften — juridisch kader

De Europese Commissie vermeldt het EU–US Data Privacy Framework als adequaatheidsmechanisme voor deelnemende Amerikaanse ondernemingen. Het bestaan van dat mechanisme keurt niet automatisch een volledige toepassing of gegevensverwerking goed. De actuele certificering en toepasselijke contractpartij moeten bij inkoop opnieuw worden gecontroleerd. Cloudflare vermeldt het framework en standaardcontractbepalingen voor beperkte doorgiften in zijn DPA, versie 6.4 van 3 april 2026. [Europese Commissie](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/eu-us-data-transfers_en), [Cloudflare DPA](https://www.cloudflare.com/en-gb/cloudflare-customer-dpa/), geraadpleegd 07-09-2026.

### Vlaanderen — toezichtadvies

De Vlaamse Toezichtcommissie publiceert algemene cloudadviezen en een specifieke aanvulling voor lokale besturen. De VTC noemt verwerkingen waarvoor publieke cloud volgens haar criteria niet aanvaardbaar is, waaronder bepaalde grootschalige verwerkingen over kwetsbare groepen en zeer gevoelige gegevens. Zij benadrukt onder meer pseudonimisering, een exitstrategie en een DPIA wanneer de daarvoor geldende criteria vervuld zijn. Dit is toezichtadvies dat bij de concrete gemeentelijke beoordeling betrokken moet worden; geen algemene wet die iedere Amerikaanse hostingdienst verbiedt. [VTC cloudadviezen](https://www.vlaanderen.be/vlaamse-toezichtcommissie/domeinen/cloud), geraadpleegd 07-09-2026.

### NIS2 — toepassingsgebied niet veronderstellen

De Belgische CCB-FAQ verduidelijkt dat gemeenten, provincies en OCMW's niet automatisch als openbare besturen onder NIS2 vallen. Bepaalde diensten of een specifieke aanwijzing kunnen wel tot toepasselijkheid leiden. Toets de concrete entiteit en activiteit; schrijf niet dat elke gemeente automatisch onder NIS2 valt. [CCB FAQ, versie 2.0.1](https://ccb.belgium.be/sites/default/files/2025-02/NIS2%20FAQ%20Website%20v2.0.1%20EN.pdf), [actuele NIS2-ingang](https://ccb.belgium.be/regulation/nis2), geraadpleegd 07-09-2026.

## Wat Cloudflare wel en niet oplost

Een publieke website verwerkt ook bezoekersgegevens: IP-adressen en beveiligingslogs; Access voegt gebruikersnamen, e-mailadressen en aanmeldactiviteit toe. Cloudflare beschrijft deze categorieën in zijn DPA. TLS-beveiliging betekent niet dat een reverse proxy geen inhoud kan verwerken: TLS-terminatie en inspectie zijn onderdeel van de dienst. [DPA](https://www.cloudflare.com/en-gb/cloudflare-customer-dpa/), [Regional Services](https://developers.cloudflare.com/data-localization/regional-services/), geraadpleegd 07-09-2026.

De **Data Localization Suite** is een betaalde Enterprise-uitbreiding met afzonderlijke instellingen voor sleutelbeheer, regionale verwerking en opslag van bepaalde metadata. Customer Metadata Boundary dekt niet alle gegevens: onder meer bepaalde account-, configuratie-, operationele en netwerkgegevens vallen erbuiten. Een EU-regio verandert bovendien de juridische vestiging van de leverancier niet. Verifieer de dekking afzonderlijk voor Pages/Workers, Access, logs en eventuele opslagproducten. [Overzicht](https://developers.cloudflare.com/data-localization/), [uitsluitingen](https://developers.cloudflare.com/data-localization/metadata-boundary/faq/), [Zero Trust](https://developers.cloudflare.com/data-localization/how-to/zero-trust/), [Pages](https://developers.cloudflare.com/data-localization/how-to/pages/), geraadpleegd 07-09-2026.

Access is een toegangslaag. Het vervangt geen dossierautorisatie, wettelijk vereiste burgeridentificatie of bevoegdheidsbeslissing. Bescherming moet alle bereikbaarheidsroutes omvatten: eigen domein, previews, standaardhostnamen en bestanden/API's. Cloudflare ondersteunt bescherming per hostname of Worker en documenteert verschillen tussen deze opties. [Access voor Workers](https://developers.cloudflare.com/workers/configuration/cloudflare-access/), geraadpleegd 07-09-2026.

## Europese alternatieven — functies en afweging

| Optie | Relevante functies | Afweging voor deze workspace |
|---|---|---|
| IONOS Deploy Now, Duitsland | GitHub-builds, expliciete Astro-ondersteuning, HTTPS en branchpreviews | Eenvoudige route voor de statische website. Een aparte identity-gateway is nodig voor het gewenste Access-achtige gebruik. |
| bunny.net, Slovenië | CDN, Shield met WAF, DDoS, rate limiting en botbescherming; Magic Containers met GitHub-workflows | Interessant voor levering en websitebeveiliging. IP-/ASN-lijsten zijn geen gebruikers-SSO. Wereldwijd netwerk: Europese vestiging bewijst geen exclusieve EU-verwerking. |
| Scaleway, Frankrijk | Object Storage, containers, Edge Services met caching, TLS en WAF | Brede basis voor website en latere toepassingen; meer infrastructuurwerk en een aparte identiteitstoegangslaag. |
| NetBird, Duitsland | Beveiligde netwerken, reverse proxy met browser-SSO en TLS, managed of self-hosted | Relevante Access/Tunnel-kandidaat; de reverse proxy is in de geraadpleegde documentatie nog beta. Geen websitehostingplatform. |
| Authelia, zelf gehost op EU-infrastructuur | SSO, MFA/passkeys en toegang per gebruiker/groep via reverse proxy | Controle over hosting en configuratie. Eigen verantwoordelijkheid voor updates, beschikbaarheid, back-ups en monitoring; geen CDN of DDoS-platform. |

Primaire productbronnen, geraadpleegd 07-09-2026: [IONOS Astro/static sites](https://docs.ionos.space/docs/deploy-static-sites/), [bunny.net vestiging](https://bunny.net/blog/sovereign-cloud-and-edge-bunny-net-and-upcloud-partner-to-power-your-global-growth/), [Shield](https://support.bunny.net/hc/en-us/articles/22699526402332-Understanding-and-enabling-Bunny-Shield), [Magic Containers](https://bunny.net/blog/skip-the-setup-with-full-stack-templates-on-magic-containers/), [Scaleway Edge Services](https://www.scaleway.com/en/developers/api/edge-services), [NetBird bedrijf](https://netbird.io/press), [NetBird reverse proxy](https://docs.netbird.io/manage/reverse-proxy), [Authelia](https://www.authelia.com/).

**Analyse:** push-to-deploy is ook met Europese hosting haalbaar. Voor een vergelijkbare combinatie van deployment, CDN, firewall en identity-gateway zijn meestal meerdere componenten en meer beheer nodig. Europese vestiging vervangt de controle op subprocessors, ondersteuningslocaties en internationale doorgiften niet. Er is geen volledige functionele benchmark, offertevergelijking of contractaudit uitgevoerd.

## Voorgestelde scheiding van toepassingen

1. **Publieke website en agenda:** portable Astro-build, alleen publieke broninhoud; testversie achter Access. Geen browsersecrets. De eigen bronbestanden blijven in de private website-repository.
2. **Interne workspace en beheertools:** afzonderlijke hostname en Access-toelatingen; eigen rollen binnen de toepassing waar nodig.
3. **Aanvragen, meldingen en burgerdossiers:** afzonderlijke gegevens- en risicoanalyse vóór echte persoonsgegevens worden aangesloten. Gevoelige dossiers blijven buiten Git en in daarvoor beoordeelde systemen.

## Nog te beoordelen vóór gemeentelijke productie

- exacte contractpartij, DPA, subprocessors en supporttoegang;
- toepasselijke doorgiftegrond en actualiteit van certificering/adequaatheid;
- logvelden, bewaartermijnen, toegang en verwijdering;
- data-classificatie, DPIA-plicht en toepasselijke VTC-criteria;
- beschikbaarheid, incidentmelding, herstel en uitvoerbaar exitplan;
- concrete kosten van de vereiste functies, inclusief eventuele Enterprise-localisatie;
- onafhankelijke controle dat anonieme toegang tot pagina's, documenten, API's en alternatieve hostnamen is geblokkeerd.

## Bijdrageverantwoording

Rol: infrastructuuronderzoeker en technisch adviseur. Inputs: gebruikersvragen en leveranciers-/overheidsdocumentatie hierboven. Systeem: OpenAI Codex / GPT-6. Reviewer: nog niet toegewezen. Dispositie: onderzoeksbriefing vastgelegd; gebruiker verkiest Cloudflare voor beveiligde tests. Geen gemeentelijke productieacceptatie of juridische goedkeuring verleend.

Ordeningsbijdrage 7 september 2026: rol workspace-informatiearchitect; inputs gebruikersopdracht en bestaande briefing; systeem OpenAI Codex / GPT-6; reviewer nog niet toegewezen; dispositie verplaatst naar de briefingsbibliotheek, inhoudelijke beoordeling en publicatiestatus ongewijzigd.
