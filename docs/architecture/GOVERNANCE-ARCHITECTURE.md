---
title: Nazareth-De Pinte Municipal Governance Workspace Architecture
status: proposed
visibility: public
updated: 2026-09-06
---

# Nazareth-De Pinte Municipal Governance Workspace Architecture

## Purpose and status

This experiment tests whether a municipality can make public work more legible, collaborative, and accountable through a version-controlled operating layer. It connects mandate, evidence, proposal, authorization, delivery, expenditure, outcome, and audit without replacing lawful institutions.

It is infrastructure for governing, not a machine governor. Agents organize information and prepare work. Elected bodies, authorized officials, and accountable staff retain every public power. This is an independent prototype, not an official municipal service.

## Real institutional context

Nazareth and De Pinte became the municipality of Nazareth-De Pinte on 1 January 2025. The workspace supports a newly merged administration, shared services, and the continuing identities and needs of Nazareth, Eke, De Pinte, and Zevergem.

```text
Residents and local organizations
├── municipal council
├── OCMW council
├── college of mayor and aldermen
├── permanent bureau
├── special committee for social services
├── autonomous municipal company
├── management team and administration
├── advisory councils and participation forums
└── external competent authorities and partnerships
    ├── Flemish and federal government
    ├── Province of East Flanders
    ├── Schelde-Leie police zone
    ├── emergency and intermunicipal services
    └── contracted delivery partners
```

The councils decide within their lawful competences. The college and permanent bureau prepare and execute decisions. The administration delivers services under delegated authority. The workspace records these distinctions and stops matters that belong elsewhere.

## Repository federation

| Repository | Visibility | Holds | Must not hold |
|---|---|---|---|
| `municipal-governance-workspace` | Public | Architecture, public policy records, competences, participation, standards, registry, and UI | Personal data, confidential drafts, secrets |
| `municipal-official-operations` | Private | Internal coordination, draft matters, operational metadata, protected-system references | Raw citizen files, plaintext secrets, unrestricted exports |
| `municipal-oversight` | Public | Audit findings, algorithm register, impact assessments, incidents, remediation | Unredacted complaints or active investigation material |
| `municipal-service-platform` | Public | Reusable service code, schemas, adapters, tests, deployment blueprints | Credentials, production datasets, citizen records |

The root registry enables discovery. It does not grant authority over the nested repositories.

## Information zones

| Zone | Municipal examples | Storage rule |
|---|---|---|
| Public | Council decisions, regulations, budgets, procurement notices, plans, aggregate outcomes | Public Git and official publication systems |
| Official use | Draft advice, coordination, operational planning | Private repositories with named teams and review rules |
| Protected | Civil registry, social services, permits, personnel, citizen correspondence | Certified systems of record; Git stores references and workflow state only |
| Restricted | Active enforcement, sealed cases, security-sensitive infrastructure | Purpose-built restricted systems, isolated from general agents |

Every transfer between zones needs a declared purpose, minimum data, provenance, authorization, retention rule, and audit log. Repository access is never equivalent to a lawful mandate.

## Governed matter model

```text
matter/
├── MATTER.yml
├── mandate-and-competence/
├── neighbourhood-impact/
├── evidence/
├── options/
├── budget-and-procurement/
├── rights-and-privacy/
├── participation/
├── decisions/
├── implementation/
├── outcomes/
└── audit/
```

Each matter names the responsible institution, legal basis, affected places and people, information class, decision owner, review and appeal routes, budget, dependencies, agent involvement, publication status, and retention rule.

## Municipal operating flow

```text
resident signal, council initiative, or service need
  -> municipal competence and subsidiarity check
  -> evidence and neighbourhood context
  -> policy or service options
  -> legal, financial, rights, privacy, security, and delivery review
  -> participation or advisory review where required
  -> authorized human decision
  -> administrative delivery and procurement
  -> publication, monitoring, and independent review
  -> continue, amend, escalate, or terminate
```

A failed competence check routes the matter to the correct authority or closes it with an explanation. Individual social-service, policing, permitting, taxation, and personnel decisions cannot be automated through this general workspace.

## Agent roles and limits

Initial agents are competence router, council-decision librarian, regulation researcher, evidence librarian, budget and procurement checker, rights and privacy reviewer, participation summarizer, implementation planner, delivery monitor, plain-language explainer, and audit assistant.

Every agent declares purpose, inputs, outputs, tools, prohibited actions, evaluations, model versions, incidents, and a named human owner. Agents may recommend and draft. They may not vote, sign, impose sanctions, approve expenditure, access protected records without a specific lawful workflow, or impersonate an official.

## Interfaces

The public interface answers what is happening, where, why, who may decide, what evidence and money are involved, how AI helped, how to participate, and how to challenge a decision.

The official interface adds drafts, dependencies, authorization queues, legal risks, deadlines, budget deviations, procurement state, and protected-system links. Both may share components but never an unrestricted search index or data connection.

## Pilot

The first pilot should track one already-public commitment from the Horizonplan 2026-2031. A suitable matter has a named objective, budget, responsible body, public milestones, participation route, and measurable outcome. It should not involve individual case decisions.

Success means a resident can trace the commitment from council mandate through money and implementation to outcome, see which institution is responsible, and identify every place where an agent assisted.

## Language, place, and accessibility

Dutch is the authoritative working language for local public records unless law specifies otherwise. Plain-language Dutch is a first-class publication form. Translations must be labelled until reviewed. Interfaces target WCAG 2.2 AA and low-bandwidth mobile devices. Records can be filtered by the four local centres, while municipality-wide matters remain visible to everyone.

## Security and continuity

Sensitive uses require proportional legal, rights, privacy, security, and procurement review. Systems record the model or agent version, inputs, reviewer, output, and final human decision. Protected data remains outside Git. Development uses public or synthetic data. Every AI-assisted service needs an incident process and an exit path.

Public repositories use secret scanning, dependency review, protected main branches, and content-boundary tests. The private repository uses least-privilege teams and explicit retention rules.

## Repository lifecycle

1. Name the municipal mandate, lawful owner, and intended public value.
2. Classify the information and identify the system of record.
3. Define review, appeal, publication, retention, and incident routes.
4. Create the repository and least-privilege teams.
5. Add agent instructions and automated boundaries.
6. Register it in `repos/_registry.yml`.
7. Pilot only with public or synthetic data.
8. Obtain independent review before operational use.
9. Publish appropriate outcomes, limitations, and incidents.
10. Archive with a durable public record and a protected-data decision.

## Source anchors

- [Municipal and OCMW council](https://www.nazarethdepinte.be/bestuur/bestuursorganen/gemeente-en-ocmw-raad)
- [College of mayor and aldermen](https://nazarethdepinte.be/bestuur/bestuursorganen/college-van-burgemeester-en-schepenen)
- [Municipal governing bodies](https://www.nazarethdepinte.be/besturen/bestuursorganen)
- [Horizonplan 2026-2031](https://nazarethdepinte.be/sites/default/files/2025-12/MJP-2026-2031-AG-correctie.pdf)

These sources describe the current context. They do not endorse this experiment, and the prototype must never imply that they do.
