# Nazareth-De Pinte Governance OS web

Static Astro 7 interface over the public allowlisted files in the main workspace. Its layout and interaction model are adapted from the Vermo workspace UI: persistent section navigation, dense record views, a command-search surface, and Git as the source of truth.

## Commands

```sh
npm install
npm run dev
npm run check
npm run build
```

## Boundary

`scripts/collect.ts` contains the initial public allowlist and hard exclusions. It never indexes nested repositories, environment files, protected case data, unredacted material, investigations, attachments, or exports. The private official interface must eventually be a separate build with a separate collector and authorization boundary, not a runtime toggle in this public application.

The site carries `noindex` and an explicit independent-prototype notice. No deployment configuration is included in this first experiment.

