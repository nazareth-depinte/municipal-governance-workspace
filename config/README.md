# Gedeelde deploymentconfiguratie

`deployment.json` is de gedeelde bron voor de Cloudflare-account, zone, testhostname en 1Password-referenties. Deze identifiers en `op://`-verwijzingen zijn geen credentials: de referenties verlenen geen toegang zonder een bevoegd 1Password-account.

Alleen de daadwerkelijke `OP_SERVICE_ACCOUNT_TOKEN` staat lokaal in de genegeerde `.env`. Iedere medewerker of CI-run gebruikt een eigen bevoegd token. De Cloudflare-tokenwaarde blijft in 1Password. `scripts/with-1password.mjs` combineert de gedeelde configuratie met de lokale token, haalt credentials tijdelijk op en geeft de vault-token niet door aan deploymentprocessen.

`onePassword.cloudflareAccessEmailsRef` verwijst naar de expliciet toegelaten individuele adressen in de teamkluis. `cloudflare.accessEmailDomains` bevat daarnaast de uitdrukkelijk toegelaten e-maildomeinen. De gebruiker heeft op 7 september 2026 één individueel adres en het volledige gemeentelijke e-maildomein toegestaan. Deze regels gelden als alternatieven: een toegestaan individueel adres **of** een adres binnen het toegelaten domein. Alle gebruikers moeten zich aanmelden met een e-mailcode. Persoonlijke adressen staan niet in deze publieke repository.


Controle: `node scripts/with-1password.mjs status`. Volledige werkwijze: [1Password en testdeployment](../docs/architecture/SECRETS-EN-TESTDEPLOYMENT.md).

Bijdrage op 7 september 2026: configuratiecorrectie op expliciet verzoek van de gebruiker. Rol: workspaceontwikkelaar. Inputs: bestaande geteste accountconfiguratie en gebruikerscorrectie. Systeem: OpenAI Codex / GPT-6. Reviewer: nog niet toegewezen. Dispositie: gedeelde configuratie; tokenwaarden uitsluitend lokaal of in 1Password; geen wijziging aan Cloudflare-toegang of deployment.

Vervolg op 7 september 2026: expliciete toelating van één individueel adres en het gemeentelijke e-maildomein. Rol: deploymentontwikkelaar; systeem OpenAI Codex / GPT-6; reviewer nog niet toegewezen; dispositie Access geconfigureerd en bestaande upload geactiveerd, met vijf geslaagde anonieme toegangscontroles.
