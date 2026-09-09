---
title: Voorstel voor bronbestanden in R2
updated: 2026-09-09
status: voorstel-niet-geimplementeerd
agent_role: opslagarchitect
agent_system: OpenAI Codex / GPT-6
reviewer: gebruiker-nog-te-beoordelen
disposition: analyse-op-verzoek
---

# Bronbestanden verplaatsen naar R2

De private website-repository bevat ongeveer 1,37 GiB bronbestanden onder `public/source-files/`. Vooral PDF's bepalen de omvang. R2 is een passende kandidaat voor deze bestanden; code, gestructureerde inhoud, bronverwijzingen en een controlemanifest blijven in Git. Dit document is een voorstel: er is nog geen bucket aangemaakt, bestand verwijderd of Git-historie herschreven.

## Gemeten omvang

Lokale inventarisatie op 9 september 2026, afgerond in MiB:

| Type | Bestanden | Omvang |
|---|---:|---:|
| PDF | 631 | 1.260,37 |
| MP3 | 10 | 39,72 |
| JPG | 418 | 35,06 |
| PNG | 86 | 16,46 |
| MP4 | 1 | 4,04 |
| Overige bronbestanden | 35 | 3,60 |

De 279 bestanden van minstens 1 MiB vormen samen 1.223,14 MiB. De 80 bestanden van minstens 5 MiB vormen 717,18 MiB. De belangrijkste winst zit dus bij documenten; alleen afbeeldingen verplaatsen lost het grootste deel niet op.

## Voorgestelde inrichting

Verplaats uiteindelijk de volledige verzameling geïmporteerde bronbestanden naar één private R2-bucket. Begin voor een proef met een grote PDF, een afbeelding en een audiobestand. Behoud bestaande URL's onder `/source-files/`: de website-Worker haalt deze objecten via een R2-binding op. De rest van de website blijft statisch. Zo hoeft de inhoud niet overal nieuwe links te krijgen.

De bucket krijgt geen rechtstreeks publiek `r2.dev`-adres of onbeschermd publiek domein. De huidige Cloudflare Access-grens voor het testdomein moet ook voor documenten blijven gelden. R2-buckets zijn standaard privaat; een Worker-binding kan toegang verlenen aan de Worker zonder dat de bucket zelf publiek wordt. Dit is een ontwerpkeuze op basis van de [R2-documentatie over publieke buckets](https://developers.cloudflare.com/r2/buckets/public-buckets/) en de [Workers API](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/), geraadpleegd op 9 september 2026.

Behoud de huidige hashgebaseerde bestandsnamen. Leg per object de objectkey, SHA-256 van de bytes, grootte, MIME-type en bron-/importdatum vast in een manifest in de private website-repository. Verifieer de bytes afzonderlijk; ga er niet zonder controle van uit dat iedere bestaande bestandsnaam een inhoudshash is.

## Uitvoering en acceptatie

1. Controleer R2-beschikbaarheid, benodigde accountrechten, regio-/jurisdictiekeuze en kosten voor het gekozen account. Maak de private bucket en een minimale proefinrichting.
2. Upload drie proefbestanden, controleer omvang en SHA-256, en test uitlevering via de Worker achter Access. Ondersteun `GET`, `HEAD`, correcte MIME-types en byte ranges voor PDF/audio. Accepteer alleen bekende objectkeys uit het manifest.
3. Controleer dat anonieme bezoekers geen objectbytes ontvangen, aangemelde gebruikers bestanden kunnen openen en alternatieve Worker-/bucketadressen geen toegangscontrole omzeilen. Controleer cachegedrag en foutafhandeling.
4. Maak een hervatbaar uploadcommando en een downloadcommando voor lokaal ontwikkelen. Downloads komen in een genegeerde lokale cache. Een schone checkout moet met duidelijke instructies de bestanden kunnen ophalen of een afgebakende demoselectie gebruiken; bouw- en linkaudits moeten dit onderscheid begrijpen.
5. Upload de overige bronbestanden en controleer het volledige manifest. Pas importer, deployscript en audits aan: het huidige lokale bestandenmodel mag ontbrekende bestanden niet stilzwijgend als geslaagde migratie behandelen.
6. Schakel de testsite pas over na geslaagde controles. Behoud de huidige bestanden als terugvalmogelijkheid totdat de R2-versie is geverifieerd. Verwijder daarna de gemigreerde bestanden uit de actuele Git-tree en voeg de cache aan `.gitignore` toe.

## Bestaande Git-historie

Bestanden verwijderen in een nieuwe commit maakt eerdere commits niet kleiner. Een gewone volledige clone blijft oude bestandsversies ophalen. Voor directe vermindering op een nieuwe computer is een shallow clone een tijdelijke optie zodra de actuele tree geen grote bestanden meer bevat. Structurele verkleining vraagt een afzonderlijk geplande historieschoonmaak of een nieuwe repository.

Historieschoonmaak verandert commit-ID's en vereist gecoördineerde pushes en hernieuwde checkouts. Dit hoort niet stilzwijgend bij de huidige synchronisatie. Leg eerst vast welke branches en tags behouden blijven, maak een gecontroleerde back-up en stem de omschakeling met alle gebruikers van de repository af.

De huidige Git-synchronisatie blijft een afzonderlijke overdracht van de bestaande werkstand. Een latere R2-migratie vereist naast GitHub-toegang ook geautoriseerde toegang tot de objecten voor lokaal ontwikkelen.

Bijdrage: OpenAI Codex / GPT-6; inputs gebruikerssuggestie, lokale bestandsinventaris, bestaande Cloudflare-configuratie en bovengenoemde officiële documentatie; datum 9 september 2026; reviewer gebruiker, nog te beoordelen; dispositie voorstel, geen infrastructuurwijziging.
