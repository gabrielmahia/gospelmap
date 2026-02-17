# 🌍 GospelMap — Global Catholic Ecosystem Intelligence Platform

**Find your people. Measure justice. Hold leadership accountable.**

🔗 **Live:** https://gospelmap-global.streamlit.app  
📁 **Code:** https://github.com/gabrielmahia/gospelmap

---

## ⚡ What You Can Do Right Now

1. **Find a Catholic church** — real OpenStreetMap data, any city globally
2. **Check ecosystem health** — calculate Pastoral Crisis Index for your parish
3. **Explore justice campaigns** — living wage, refugee rights, housing globally
4. **View accountability scores** — diocesan transparency, synodality, finances
5. **Connect diaspora communities** — Filipino, Nigerian, East African and more
6. **Coordinate crisis response** — refugee, disaster, emergency coordination

---

## 🎯 Core Features

| Feature | Status | Data |
|---------|--------|------|
| 🔍 Find My Church | ✅ Live | OpenStreetMap (real, global) |
| 📊 Ecosystem Health Indices | ✅ Live calculator | User input / demo |
| ⚖️ Justice Network | ✅ Interactive | Demo campaigns |
| 📋 Accountability Dashboard | ✅ Interactive | Demo data |
| 🌏 Diaspora Connection | ✅ Interactive | Demo data |
| 🆘 Crisis Response | ✅ Interactive | Demo data |

**Demo Mode:** Clearly labeled. Church search is live and real. All other data illustrative.

---

## 🏗️ Architecture (v1.0 — Deployable)

```
gospelmap/
├── app.py                          ← Main app (multi-page, zero infra deps)
├── gospelmap/
│   ├── church_search.py            ← OSM-based real church finder
│   ├── indices.py                  ← PCI, MCI, JCI, FTI calculators
│   ├── data_models.py              ← Parish, Diocese, Campaign schemas
│   └── catholic_network_tools_integration.py  ← Federation layer (future)
├── requirements.txt                ← Only Streamlit-Cloud-compatible deps
├── docs/                           ← Theology, data schema, governance
└── [governance files]
```

**Design principles:**
- Zero infrastructure dependencies (runs on Streamlit Cloud free tier)
- OSM-powered real church search (multi-endpoint failover)
- Progressive enhancement (demo → real data via env vars)
- Federated by design (each parish owns its data)

---

## 🚀 Deploy

```bash
git clone https://github.com/gabrielmahia/gospelmap
cd gospelmap
pip install -r requirements.txt
streamlit run app.py
```

Streamlit Cloud: push to `main` → auto-deploys.

---

## 📊 Index Framework

```
PASTORAL CRISIS INDEX (PCI)    — priest shortage, abuse, youth engagement
MATERIAL CRISIS INDEX (MCI)    — food, housing, healthcare gaps
JUSTICE CRISIS INDEX (JCI)     — wage campaigns, refugee, housing advocacy
FINANCIAL TRANSPARENCY (FTI)   — budget public, overhead, accountability
```

All calculators are live — enter your parish's data and get real scores.

---

## 🙏 Theological Foundation

Grounded in Vatican II (Gaudium et Spes), Catholic Social Teaching,  
and the conviction that *"nothing hidden will not be revealed."* — Luke 12:2

---

## 📜 License

CC BY-NC-ND 4.0 | contact@aikungfu.dev | community-owned

## Security

Vulnerabilities: email contact@aikungfu.dev — do NOT open public issues.
