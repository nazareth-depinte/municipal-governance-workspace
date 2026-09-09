---
title: Werkruimte gebruiken op een andere computer
updated: 2026-09-09
status: werkinstructie
agent_role: repositorybeheerder
agent_system: OpenAI Codex / GPT-6
reviewer: gebruiker-als-opdrachtgever
disposition: synchronisatie-op-expliciet-verzoek
---

# Werkruimte gebruiken op een andere computer

Deze werkruimte bestaat uit vijf zelfstandige Git-repositories. De vier repositories onder `repos/` zijn geen submodules: het clonescript haalt ze afzonderlijk op. De publieke hoofdrepository bevat geen kopie van de private website of outreachdocumenten.

## Eenmalige installatie

Installeer Git en Node.js >=22.12.0. Meld je aan bij GitHub met een account dat toegang heeft tot de twee private repositories (bijvoorbeeld met `gh auth login` en `gh auth setup-git`).

```sh
git clone https://github.com/nazareth-depinte/municipal-governance-workspace.git
cd municipal-governance-workspace
bash scripts/clone-repos.sh
```

| Repository | Lokale map | Werkbranch op 9 september 2026 | Zichtbaarheid |
|---|---|---|---|
| municipal-governance-workspace | `.` | `main` | Publiek |
| municipal-website | `repos/municipal-website` | `codex/website-rebuild` | Privaat |
| municipal-official-operations | `repos/official-operations` | `main` | Privaat |
| municipal-oversight | `repos/oversight` | `main` | Publiek |
| municipal-service-platform | `repos/service-platform` | `main` | Publiek |

Het clonescript gebruikt de standaardbranch van iedere remote; op de controledatum komen die overeen met bovenstaande branches. Bestaande checkouts worden overgeslagen. Om die bij te werken: controleer eerst lokale wijzigingen met `git status` en voer vervolgens per repository `git pull --ff-only` uit. Bewaar lokale wijzigingen voordat je van branch wisselt of integreert.

## Lokaal starten

Voor de werkruimte-interface, vanuit de hoofdmap:

```sh
cd workspace-web
npm ci
npm run dev
```

Voor de website en demo's, in een tweede terminal vanuit de hoofdmap:

```sh
cd repos/municipal-website
npm ci
npm run dev
```

De website draait op `http://127.0.0.1:4328/`; de voorbeelden staan op `/innovatie/` en `/meldpunt/`. De ingecheckte inhoud en bronbestanden volstaan om de website te bouwen. Een nieuwe crawl is daarvoor niet nodig. De broncode van het meldpunt staat in `repos/service-platform/apps/meldpunt`; de website bevat een distributiekopie.

De outreachbriefing staat in `repos/official-operations/outreach/2026-09-07-ai-proeftuin/BRIEFING.md`. Het outreachplan blijft een concept voor één e-mail met demo-toegang, zonder bijlagen; Git-synchronisatie verstuurt die e-mail niet.

## Wat niet via Git verhuist

- `.env` en credentials blijven lokaal. Voor gewoon ontwikkelen zijn deploymentcredentials niet nodig. Gebruik bij deployment de bestaande 1Password-instructies in `config/README.md`; deel secrets via het daarvoor bestemde systeem.
- `node_modules`, buildoutput, Astro-/Wrangler-caches en gegenereerde indexen worden lokaal opnieuw opgebouwd.
- Het tijdelijke crawlarchief onder `/private/tmp/nazareth-depinte-p1-crawl` en de lokale crawlstatus zijn geen Git-back-up. De geïmporteerde website-inhoud en bronbestanden staan wel in de private website-repository. Een onderbroken crawl hervatten vereist het oorspronkelijke archief of een nieuwe crawl.
- Browser-localStorage, geopende terminals en ontwikkelservers gaan niet mee. Bewaarde fictieve democoncepten zijn browsergebonden.

Bronnen: lokale Git-status, `repos/_registry.yml`, `.gitignore`-bestanden, packagescripts en GitHub-repositorymetadata, gecontroleerd op 9 september 2026. Bijdrage: inventarisatie en overdrachtsinstructie door OpenAI Codex / GPT-6; input expliciete gebruikersopdracht om alle repositories te synchroniseren; menselijke opdrachtgever de gebruiker. Geen wijziging van repositoryzichtbaarheid of gemeentelijke dienstverlening.
