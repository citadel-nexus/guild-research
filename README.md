# Guild: Research

> *"Knowledge is the only resource that compounds without limit."*

The Research Guild is the intellectual core of Citadel Nexus — the College system,
domain mastery tracking, professor profiles, and the knowledge base that powers
Zayara's answers, Sorting Hat assessments, and Dossier enrichment.

---

## Identity

| | |
|---|---|
| **Sigil** | The Open Tome |
| **Vibe** | Deep focus. Long memory. The library that never closes. |
| **Color** | Forest Green `#1A5C38` |
| **NATS Prefix** | `citadel.research.*` |
| **Port** | `8200` |
| **Parent Guild** | Intelligence |
| **Sub-guild** of | Intelligence |

---

## Purpose

- Manage **College domains** — 28 professors mapped across 8 guild tracks
- Track **mastery scores**, quiz pass rates, EVO cycle participation
- Sync knowledge base to **Notion** and **Supabase** (`college_domains` table)
- Feed professor context into **Sorting Hat** question generation
- Power **Zayara Bot** knowledge responses via sake/facts/memory

---

## Domains of Operation

### College System
| Role | Count | Source |
|------|-------|--------|
| Professors | 28 | Notion College Domain Tracker |
| Guild tracks | 8 | Mapped to GitLab Group 83 |
| Domains | ~52 | Production files |
| Metabase dashboards | 19 | Live analytics |

### CAPS Assessment
Grades: **S / A / B / C / D** — based on mastery score + quiz pass rate + EVO cycles

### Knowledge Base Sync
```
Notion → college_domains (Supabase) via vcc_notion_feedback_loop.py --sync-from-notion
Supabase → Notion via college_notion_sync.py
```

---

## Services & Integrations

| Service | Role |
|---------|------|
| **Notion** | `EVO_COLLEGE_DB_DATA_SOURCE` — professor/domain data |
| **Supabase** | `college_domains`, `college_cases`, `user_dossiers` |
| **GitLab** | Group 83 — professor→guild placement |
| **Perplexity** | Learning context injection in control loop |
| **NATS** | `citadel.research.*` event subjects |

---

## NATS Event Subjects

```
citadel.research.domain.updated     — Professor domain score changed
citadel.research.assessment.sync    — College DB synced from Notion
citadel.research.kb.hydrated        — Knowledge base refresh complete
citadel.research.professor.placed   — Professor assigned to GitLab guild
```

---

## Getting Started

```bash
npm install
cp .env.example .env
# Fill NOTION_API_TOKEN, SUPABASE_SERVICE_ROLE_KEY, GITLAB_PAT
npm run dev
```

## Environment Variables

```
NATS_URL=nats://<your-nats-host>:4222
SUPABASE_SERVICE_ROLE_KEY=<key>
NOTION_API_TOKEN=<key>
NOTION_DB_ID=<your-college-db-id>
GITLAB_PAT=<token>
GUILD_PORT=8200
```
