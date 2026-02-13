# Catholic Network Tools ↔ GospelMap Integration Guide

## Architecture Overview

**Federation Model: Local Autonomy + Global Coordination**

```
EACH PARISH
└─ Runs Catholic Network Tools (Streamlit Cloud)
   ├─ Manages own data (sacraments, pastoral, justice, stewardship, etc.)
   ├─ Auto-syncs with GospelMap hourly
   └─ Receives global opportunities

GLOBAL LAYER
└─ GospelMap
   ├─ Aggregates data from all parishes running Tools
   ├─ Enables global discovery
   ├─ Coordinates justice campaigns
   ├─ Tracks bishop accountability
   ├─ Maps diaspora networks
   └─ Sends opportunities back to parishes
```

---

## How It Works (Simplified)

### STEP 1: Parish Deploys Catholic Network Tools

```bash
# Parish A: Consolata Shrine (Kenya)
Repository: gabrielmahia/catholic-network-tools
Deploy to: Streamlit Cloud
URL: consolata-westlands.streamlit.app

# What they get:
✅ Local sacrament scheduling
✅ Pastoral care tracking (homebound, grief support)
✅ Material aid management (food, shelter, medical)
✅ Justice work coordination
✅ Volunteer + stewardship tracking
✅ Formation programs
```

### STEP 2: Auto-Sync to GospelMap

```
Catholic Network Tools                GospelMap
(Local Parish)                        (Global)

Hourly Sync ────────────────────→
├─ Parish profile
├─ Sacrament availability
├─ Material aid (food, shelter)
├─ Justice campaigns
├─ Stewardship data
├─ Volunteer capacity
└─ Formation programs

        ←──────────────────
        ← Global opportunities
        ← Nearby parishes
        ← Bishop updates
        ← Campaign insights
```

### STEP 3: GospelMap Makes Parish Discoverable

**User searches GospelMap:**
- "Find LGBTQ+-welcoming parishes in Nairobi"
- **GospelMap discovers** → Consolata Shrine (synced data)
- Shows: Mass times, languages, welcome indices, justice work, transparency

### STEP 4: Join Global Campaigns

**In Catholic Network Tools:**
```
Consolata Shrine sees:
├─ "Living Wage Campaign - East Africa"
├─ "Parishes involved: 150+"
├─ "Workers benefited: 5,000+"
├─ [JOIN CAMPAIGN BUTTON]

Clicks Join → Adds 89 volunteers
Sync → GospelMap updates global campaign
Campaign dashboard shows: 
  "Consolata Shrine: 89 volunteers, 800 workers helped"
```

### STEP 5: Report Impact Back

**Consolata reports to Catholic Network Tools:**
```
Impact Report:
- 800 tea farmers
- 26% wage increase
- Kiambu region

Auto-syncs → GospelMap aggregates:
"Living Wage Campaign - Global Impact"
├─ Kenya: 5,000 workers, 26% average increase ✅
├─ USA: 15,000 workers, $2/hr increase ✅
├─ Brazil: 8,000 workers, in progress
└─ Total: 26,000+ workers benefited
```

---

## Deployment Setup

### For a Parish (Catholic Network Tools)

```bash
# 1. Deploy Catholic Network Tools
   Go to: https://share.streamlit.io/deploy
   
   Repository: gabrielmahia/catholic-network-tools
   Branch: main
   Main file: app/01_Home.py
   
   Result: consolata-westlands.streamlit.app

# 2. Get API Keys
   Catholic Network Tools API key: [auto-generated]
   GospelMap API key: [request from GospelMap admin]

# 3. Configure Integration
   In Catholic Network Tools settings:
   ├─ Enable GospelMap sync: [✓]
   ├─ Sync frequency: hourly
   ├─ GospelMap API key: [paste]
   ├─ Welcome indices: [set manually]
   │  ├─ LGBTQ+ welcome: 9/10
   │  ├─ Immigrant welcome: 9/10
   │  ├─ Poor welcome: 9/10
   │  └─ Divorced welcome: 8/10
   └─ [SAVE]

# 4. First Sync
   ✅ Parish data sent to GospelMap
   ✅ Parish appears in global discovery
   ✅ Start receiving global campaign opportunities
```

### For GospelMap (Global Admin)

```bash
# 1. Deploy GospelMap
   Go to: https://share.streamlit.io/deploy
   
   Repository: gabrielmahia/gospelmap
   Branch: main
   Main file: app.py
   
   Result: gospelmap-global.streamlit.app

# 2. Backend Setup
   ├─ Neo4j instance (for parish relationships)
   ├─ InfluxDB (for real-time indices)
   ├─ MongoDB (for parish profiles)
   ├─ Elasticsearch (for discovery)
   └─ Redis (for caching)

# 3. API Setup
   Create endpoints for:
   ├─ POST /parishes (receive synced data)
   ├─ GET /opportunities/:parish_id (send campaigns)
   ├─ POST /campaigns/:id/join (parish joins campaign)
   └─ POST /campaigns/:id/impact (parish reports impact)

# 4. Configure Sync
   ├─ Allow Catholic Network Tools instances to connect
   ├─ Validate API keys
   ├─ Enable hourly sync pulls
   └─ Aggregate data in real-time
```

---

## Data Flow Diagram

```
PARISH LEVEL (Catholic Network Tools)
════════════════════════════════════════════════════════════════

Consolata Shrine (Kenya)          All Saints (USA)          São João (Brazil)
Local Instance                     Local Instance            Local Instance

Sacraments ────┐                  Sacraments ────┐         Sacraments ────┐
Pastoral ──────┤                  Pastoral ──────┤         Pastoral ──────┤
Material ──────┤→ Sync Hourly    Material ──────┤→ Sync   Material ──────┤→ Sync
Justice ───────┤                  Justice ───────┤         Justice ───────┤
Stewardship ───┤                  Stewardship ───┤         Stewardship ───┤
Formation ─────┘                  Formation ─────┘         Formation ─────┘
                    │                              │                   │
                    └──────────────────┬───────────┴───────────────────┘
                                       │
                                       ↓
GLOBAL LEVEL (GospelMap)
════════════════════════════════════════════════════════════════

GospelMap Central Platform
├─ Parish Aggregation
│  ├─ 5,000 parishes synced
│  ├─ 50,000 profiles indexed
│  └─ Real-time data (updated hourly)
│
├─ Discovery Engine
│  ├─ "Find parishes welcoming to LGBTQ+"
│  ├─ "Find parishes active in justice"
│  └─ "Find diaspora communities"
│
├─ Justice Coordination
│  ├─ Living Wage Campaign
│  │  ├─ Kenya: 150 parishes, 5,000 workers, +26%
│  │  ├─ USA: 47 parishes, 15,000 workers, +$2/hr
│  │  └─ Brazil: 65 parishes, 8,000 workers, in progress
│  │
│  ├─ Refugee Rights Campaign
│  ├─ Housing Justice Campaign
│  └─ Climate Action Campaign
│
├─ Accountability Dashboard
│  ├─ Bishop transparency scores
│  ├─ Diocesan financial disclosure
│  ├─ Abuse record tracking
│  └─ Synodality measurement
│
└─ Diaspora Mapping
   ├─ Filipino communities (11 million worldwide)
   ├─ Nigerian communities (5 million)
   └─ Korean communities (2 million)

                                       ↑
                    ┌──────────────────┴───────────────────┬─────┐
                    │                                       │     │
        ↓ Global Opportunities Sent Back                   │     │
        
Campaign Alerts          Bishop Updates         Nearby Parishes
"Living Wage"           "Diocese improving"     "All Saints"
"Action needed"         "New transparency"      "4 miles away"
"45 volunteers"         "Higher scores"         "Shared campaigns"

                    │                                       │     │
                    └──────────────────┬───────────────────┴─────┘
                                       │
                    Received by Catholic Network Tools (Hourly)
```

---

## Real Example: Living Wage Campaign

### Timeline

**Week 1: Consolidation**
```
GospelMap detects:
├─ Consolata Shrine (Kenya) - 89 volunteers - Running living wage campaign
├─ All Saints (USA) - 47 volunteers - Running living wage campaign
├─ São João (Brazil) - 65 volunteers - Running living wage campaign
└─ 150+ total parishes - same campaign

GospelMap creates GLOBAL CAMPAIGN with all synced data
```

**Week 2-4: Coordination**
```
Catholic Network Tools shows each parish:
├─ Global campaign stats
├─ Nearby parishes doing same work
├─ Sharing tactics/strategies
├─ Weekly impact aggregation
└─ Joint action calendar

Each parish reports impact hourly/daily to GospelMap
```

**Month 1: Results**
```
GospelMap Dashboard - Living Wage Campaign:

Global Impact
├─ Workers helped: 26,000+
├─ Average wage increase: 24% (Kenya 26%, USA 13%, Brazil 18%)
├─ Parishes coordinated: 250+
├─ Policy wins: 3 (Kenya Kiambu/Nyeri, USA Virginia)
└─ Estimated income increase: $45 million annually

By Region
├─ 🇰🇪 Kenya: 5,000 workers, 150 parishes, 26% (+$15M)
├─ 🇺🇸 USA: 15,000 workers, 47 parishes, +$2/hr (+$25M)
└─ 🇧🇷 Brazil: 8,000 workers, 65 parishes, 18% (+$5M)

Each Parish Sees Globally
├─ "You helped 5,000 workers alongside 150 other parishes"
├─ "Your region gained 26% while others negotiated $2/hr"
├─ "Would you like to connect with All Saints (4 miles away)?"
└─ "Ready to scale to other workers in your region?"
```

---

## API Endpoints (To Implement)

### Catholic Network Tools → GospelMap (Data Push)

```
POST /api/v1/parishes/sync
Headers: Authorization: Bearer {cnet_api_key}
Body:
{
  "parish_id": "consolata-westlands",
  "name": "Consolata Shrine",
  "location": {"lat": -1.2345, "lng": 36.7890},
  "sacraments": {...},
  "pastoral_care": {...},
  "material_aid": {...},
  "justice_work": {
    "campaigns": [
      {
        "id": "living-wage",
        "name": "Living Wage - Tea Farmers",
        "status": "active",
        "volunteers": 89,
        "impact": {
          "workers_affected": 800,
          "wage_increase_pct": 26,
          "region": "Kiambu"
        }
      }
    ]
  },
  "stewardship": {...},
  "formation": {...},
  "volunteer_capacity": 156
}

Response: 200 OK
{
  "synced": true,
  "timestamp": "2024-02-13T11:30:00Z",
  "global_opportunities": [...]
}
```

### GospelMap → Catholic Network Tools (Opportunities)

```
GET /api/v1/parishes/{parish_id}/opportunities
Headers: Authorization: Bearer {gm_api_key}

Response: 200 OK
{
  "campaigns_to_join": [
    {
      "id": "living-wage-global",
      "name": "Living Wage - East Africa",
      "status": "active",
      "parishes_involved": 150,
      "volunteers_needed": 50,
      "workers_affected": 5000
    }
  ],
  "nearby_parishes": [
    {
      "id": "all-saints-nairobi",
      "name": "All Saints - Nairobi",
      "distance_km": 12,
      "shared_campaigns": ["living-wage"]
    }
  ],
  "bishop_updates": {
    "accountability_score": 6.2,
    "transparency_trend": "improving"
  }
}
```

---

## Benefits of This Integration

| Benefit | For Parish | For Global |
|---------|-----------|-----------|
| **Autonomy** | Run own data locally | Respect local control |
| **Discoverability** | Automatically discoverable | Find & connect parishes |
| **Justice Scale** | Join global campaigns | Coordinate 250+ parishes |
| **Real-Time Data** | Hourly sync | Live dashboards |
| **Accountability** | Transparent locally | Bishops measured globally |
| **Network Effects** | Connect with nearby parishes | 1.3B Catholics coordinated |

---

## Implementation Checklist

### Phase 1: Core Integration (Month 1)
- [ ] API endpoints built (sync, opportunities)
- [ ] Catholic Network Tools can push data
- [ ] GospelMap receives + indexes
- [ ] Parishes visible in discovery
- [ ] Manual campaign creation in GospelMap

### Phase 2: Automation (Month 2)
- [ ] Hourly sync fully automated
- [ ] Justice campaigns auto-aggregate
- [ ] Impact reporting automated
- [ ] Nearby parish discovery working
- [ ] Bishop accountability tracking live

### Phase 3: Scale (Months 3-6)
- [ ] 100+ dioceses deployed
- [ ] 5,000 parishes synced
- [ ] Justice campaigns producing real policy wins
- [ ] Diaspora networks active
- [ ] Crisis response coordination

---

## Next Steps

1. **For Parishes:**
   - Deploy Catholic Network Tools (Streamlit)
   - Get API credentials
   - Enable GospelMap sync
   - Set welcome indices
   - Join campaigns

2. **For GospelMap Admin:**
   - Deploy GospelMap backend
   - Set up API endpoints
   - Configure parish validation
   - Create initial campaigns
   - Test syncs with pilot parishes

3. **For First Pilot (Kenya):**
   - Consolata Shrine (Nairobi)
   - All Saints (Manassas) 
   - São João (Brazil)
   - St. Mary's (DRC)
   - **Goal:** Prove living wage campaign impact globally

---

**This federation model gives parishes full autonomy while enabling global coordination.**

**The Church becomes both LOCAL and GLOBAL at once.**

🌍 **One Church. One Platform. Local Autonomy. Global Justice.** 🌍
