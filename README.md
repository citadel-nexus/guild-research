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

## Mission System

Research missions reward knowledge synthesis, domain mastery, and College system contributions.

| Mission | Description | XP | Unlock |
|---------|-------------|-----|--------|
| First Sync | Sync 10+ College domain records from Notion | 100 | Default |
| Assessment Cycle | Complete a professor assessment cycle | 200 | Default |
| KB Article | Contribute a reviewed knowledge base article | 150 | Default |
| Grade S Domain | Achieve CAPS Grade S on a domain assessment | 300 | Researcher rank |
| Full Sync | Complete a bidirectional Notion ↔ Supabase sync | 250 | Researcher rank |
| Professor Placed | Map a professor to their GitLab guild | 100 | Default |
| Domain Master | 5 domains at Grade A or above simultaneously | 500 | Scholar rank |

**Daily missions (reset 00:00 UTC):**
- Emit a `citadel.research.domain.updated` event — 25 XP
- Complete a quiz pass rate update for a domain — 25 XP

CAPS grades map directly to domain trust:
**S** (90–100) → Hall of Fame | **A** (75–89) → Active | **B** (60–74) → Monitor | **C/D** → Refactor

---

## Guild Expectations

**Members:**
- Maintain at least 3 active domains at Grade B or above
- Participate in at least 1 EVO cycle per sprint
- Complete Research onboarding (College system primer) within 7 days of placement
- Post in `#research-lab` and `#knowledge-base` lobby channels

**Contributors:**
- All Notion sync scripts must be idempotent (safe to re-run without duplicating data)
- Knowledge base articles must include sources and a confidence score
- Changes to `college_domains` schema require a migration file
- Code review turnaround: 48 hours

**Guild Lead (Chief Knowledge Officer):**
- Weekly CAPS grade summary posted to `#announcements`
- Coordinate professor placements with GitLab guild leads monthly
- Review and merge knowledge base PRs within 48 hours

---

## Contributing

**Branch naming:**
```
feat/<srs-code>/<short-description>
fix/<srs-code>/<short-description>
research/<srs-code>/<short-description>
```

**PR checklist:**
- [ ] SRS code referenced (e.g., `SRS: RES-COLLEGE-004`)
- [ ] `npm test` passes
- [ ] Notion sync scripts tested against staging DB first
- [ ] New domain schemas include Pydantic model + migration
- [ ] No live Notion DB IDs hardcoded — use env vars

**Commit format:** `<type>(<srs-code>): <description>`
Example: `feat(RES-COLLEGE-004): add cybersec professor to Intelligence guild`

**SAKE compliance:** New knowledge extraction modules require a `.sake` file stub.
See [guild-sdk](https://github.com/citadel-nexus/guild-sdk) for the format.

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
