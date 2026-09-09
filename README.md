---
title: Nazareth-De Pinte Municipal Governance Workspace
status: experimental
visibility: public
---

# Nazareth-De Pinte Municipal Governance Workspace

An experimental, version-controlled operating layer for municipal government. It helps residents, elected bodies, administrators, and oversight functions connect public knowledge, policy, delivery, and explanation while keeping authority with lawful institutions.

This is an independent prototype. It is not an official service and is not affiliated with the municipality of Nazareth-De Pinte.

Start with [the complete architecture](docs/architecture/GOVERNANCE-ARCHITECTURE.md), then read [MAP.md](MAP.md), [AUTHORITY.md](AUTHORITY.md), and [repos/_registry.yml](repos/_registry.yml).

## Local setup

Requires Git, Node.js >=22.12.0, and GitHub access to the private website and operations repositories. The clone script includes all four nested repositories. See [working on another computer](docs/WORKSPACE-OVERDRACHT.md) for branches, startup commands, and local configuration.

```sh
git clone https://github.com/nazareth-depinte/municipal-governance-workspace.git
cd municipal-governance-workspace
bash scripts/clone-repos.sh
cd workspace-web && npm install && npm run dev
```

The municipal website stores large source files in private R2 storage. Its [setup guide](docs/WORKSPACE-OVERDRACHT.md) includes the authenticated download step and the fresh-clone requirement after the September 2026 history cleanup.
