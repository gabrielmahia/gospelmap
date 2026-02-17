"""
GospelMap — Global Catholic Ecosystem Intelligence Platform
Find your people. Measure justice. Hold leadership accountable.

Architecture: Multi-page Streamlit, zero infrastructure deps.
Data: OSM (real church search), computed indices, demo parish profiles.
Deployment: Streamlit Cloud free tier.
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, date
import math

st.set_page_config(
    page_title="GospelMap 🌍",
    page_icon="✝️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Shared CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
.gm-hero { font-size:2.4em; font-weight:800; color:#1a3a5c; margin-bottom:0.3rem; }
.gm-sub  { font-size:1.1em; color:#5a7290; margin-bottom:1.5rem; }
.gm-card {
    border:1px solid #e0e7ef; border-radius:10px;
    padding:1.2rem 1.4rem; margin-bottom:1rem;
    background:#f8fbff;
}
.crisis-red    { background:#fee2e2; border-left:4px solid #ef4444; padding:.8rem 1rem; border-radius:6px; margin:.5rem 0; }
.health-green  { background:#dcfce7; border-left:4px solid #22c55e; padding:.8rem 1rem; border-radius:6px; margin:.5rem 0; }
.warning-yellow{ background:#fef9c3; border-left:4px solid #eab308; padding:.8rem 1rem; border-radius:6px; margin:.5rem 0; }
</style>
""", unsafe_allow_html=True)

# ── Navigation ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🌍 GospelMap")
    st.caption("Global Catholic Ecosystem Intelligence")
    st.divider()

    page = st.radio("Navigate", [
        "🏠 Home",
        "🔍 Find My Church",
        "📊 Ecosystem Health",
        "⚖️ Justice Network",
        "📋 Accountability",
        "🌏 Diaspora",
        "🆘 Crisis Response",
    ], label_visibility="collapsed")

    st.divider()
    st.markdown("### 📊 Global Stats (Demo)")
    st.metric("Parishes Mapped", "5,000+")
    st.metric("Countries", "150+")
    st.metric("Justice Campaigns", "50+")
    st.divider()
    st.caption("🟢 **Demo Mode** — Spiritual content live, parish metrics illustrative")
    st.caption("AGPL-3.0 | community-owned forever")

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: HOME
# ═══════════════════════════════════════════════════════════════════════════════
if page == "🏠 Home":
    st.markdown('<div class="gm-hero">🌍 GospelMap</div>', unsafe_allow_html=True)
    st.markdown('<div class="gm-sub">Find Your People. Measure Justice. Hold Leadership Accountable.</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Parishes", "5,000+", "Global coverage")
    with col2: st.metric("Dioceses", "500+", "150 countries")
    with col3: st.metric("Justice Campaigns", "50+", "Active globally")
    with col4: st.metric("Catholics Served", "1.3B", "Universal church")

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### What GospelMap Does")
        for item in [
            ("🔍", "**Find My Church** — Search by location, language, values, accessibility"),
            ("📊", "**Ecosystem Health** — Real-time indices: pastoral, material, justice, financial"),
            ("⚖️", "**Justice Network** — Coordinate campaigns globally, track impact"),
            ("📋", "**Accountability** — Bishop + diocese transparency scores"),
            ("🌏", "**Diaspora** — Connect Filipino, Nigerian, Korean, Polish communities"),
            ("🆘", "**Crisis Response** — Refugee coordination, disaster response"),
        ]:
            st.markdown(f"{item[0]} {item[1]}")

    with col2:
        st.markdown("### Theological Foundation")
        st.markdown("""
**Vatican II (Gaudium et Spes):** The Church exists *in and for* the world.

**Catholic Social Teaching:**
- Option for the poor (not optional)
- Justice is integral to the Gospel
- Human dignity is non-negotiable
- Subsidiarity: parishes own their data

**Gospel Radicalism:**
*"Nothing hidden will not be revealed."* — Luke 12:2  
*"Whatever you did for the least..."* — Matthew 25:40
        """)

    st.divider()
    st.markdown("### ⚡ Start Now")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**🔍 Find a Church**\nSearch by city → real OSM data\nFilter by language, values, accessibility")
    with col2:
        st.info("**⚖️ Join a Campaign**\nLiving wage, refugee rights, housing\nConnect with parishes near you")
    with col3:
        st.info("**📊 Check Health**\nPastoral, material, justice indices\nSee where crisis signals are rising")

    st.markdown("---")
    st.caption("*'Nothing is hidden that will not be revealed.'* — Luke 12:2 | AGPL-3.0 | [GitHub](https://github.com/gabrielmahia/gospelmap)")

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: FIND MY CHURCH
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "🔍 Find My Church":
    st.title("🔍 Find My Local Church")
    st.markdown("Search by location, values, and accessibility. Powered by OpenStreetMap — real global data, no API key required.")

    col1, col2 = st.columns([1, 1])
    with col1:
        city    = st.text_input("City", placeholder="Nairobi / Manila / São Paulo / Rome")
        country = st.text_input("Country (optional, improves accuracy)", placeholder="Kenya / Philippines / Brazil")
        radius  = st.slider("Search radius (km)", 5, 80, 30)
    with col2:
        st.markdown("**Language preference**")
        languages = st.multiselect("Languages", ["English","Swahili","Spanish","Tagalog","French","Portuguese","Polish","Vietnamese","Korean","Arabic","Luganda"], default=["English"])
        st.markdown("**Accessibility**")
        wheelchair = st.checkbox("Wheelchair accessible")
        nursery    = st.checkbox("Childcare / nursery")

    st.markdown("**Values matching** *(for discovery — not visible to parishes)*")
    c1, c2, c3 = st.columns(3)
    with c1:
        v_justice     = st.slider("Social justice engagement", 0, 10, 5)
        v_lgbtq       = st.slider("LGBTQ+ welcome", 0, 10, 5)
    with c2:
        v_immigrant   = st.slider("Immigrant / refugee welcome", 0, 10, 5)
        v_transparency= st.slider("Financial transparency", 0, 10, 5)
    with c3:
        v_youth       = st.slider("Youth engagement", 0, 10, 5)
        v_women       = st.slider("Women in leadership", 0, 10, 5)

    search_btn = st.button("🔍 Find Churches Near Me", type="primary", use_container_width=True)

    if search_btn:
        if not city.strip():
            st.warning("Please enter a city name")
        else:
            with st.spinner(f"Searching for Catholic churches in {city}... (OSM live data)"):
                try:
                    from gospelmap.church_search import search_by_city
                    churches = search_by_city(city.strip(), country.strip() or None, limit=15)
                except Exception as e:
                    churches = []
                    st.error(f"Search error: {e}")

            if not churches:
                st.warning(f"No churches found in {city}. Try a larger city or different spelling.")
                st.info("💡 OSM coverage varies by region. Major cities in East Africa, Philippines, Brazil, Europe have good coverage.")
            else:
                st.success(f"Found **{len(churches)} Catholic churches** near {city}")
                st.divider()

                for i, c in enumerate(churches, 1):
                    with st.container():
                        col1, col2, col3 = st.columns([3, 1, 1])
                        with col1:
                            st.subheader(f"{i}. {c.name}")
                            if c.address:
                                st.caption(f"📍 {c.address}")
                            elif c.city:
                                st.caption(f"📍 {c.city}{', ' + c.country if c.country else ''}")
                        with col2:
                            if c.distance_km:
                                st.metric("Distance", f"{c.distance_km:.1f} km")
                        with col3:
                            gmaps = f"https://www.google.com/maps?q={c.latitude},{c.longitude}"
                            st.markdown(f"[📍 Google Maps]({gmaps})")

                        detail_cols = st.columns(3)
                        with detail_cols[0]:
                            if c.phone:
                                st.write(f"📞 {c.phone}")
                        with detail_cols[1]:
                            if c.website:
                                st.write(f"🌐 [{c.website[:30]}]({c.website})")
                        with detail_cols[2]:
                            osm_link = f"https://www.openstreetmap.org/node/{c.osm_id}" if c.osm_id else None
                            if osm_link:
                                st.markdown(f"[🗺️ OSM]({osm_link})")
                        st.divider()

    st.info("""
**Data Source:** OpenStreetMap (crowdsourced, real-time)
Coverage is best in Europe and East Africa, growing globally.
Help improve coverage: [openstreetmap.org](https://openstreetmap.org)
    """)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: ECOSYSTEM HEALTH
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "📊 Ecosystem Health":
    st.title("📊 Ecosystem Health Dashboard")
    st.markdown("Real-time crisis signal indices for parishes and dioceses.")

    st.divider()
    st.markdown("### 🧮 Calculate Indices (Interactive)")
    st.markdown("Enter your parish data to calculate actual health indices.")

    with st.expander("📊 Pastoral Crisis Index (PCI) Calculator"):
        c1, c2, c3 = st.columns(3)
        with c1:
            priest_vacancies = st.number_input("Priest vacancies", 0, 50, 2)
            total_priests    = st.number_input("Current priests", 1, 100, 6)
        with c2:
            abuse_allegations= st.number_input("Abuse allegations (last 5 yrs)", 0, 50, 0)
            youth_pct        = st.slider("Youth engagement %", 0, 100, 20)
        with c3:
            integration_score= st.slider("Immigrant integration (0–10)", 0, 10, 5)
            opacity_score    = st.slider("Leadership opacity (0=transparent, 10=opaque)", 0, 10, 3)

        if st.button("Calculate PCI"):
            from gospelmap.indices import EcosystemIndices
            try:
                pci = EcosystemIndices.calculate_pastoral_crisis_index(
                    priest_vacancies, total_priests, abuse_allegations,
                    youth_pct, integration_score, opacity_score
                )
                level = "🔴 CRISIS" if pci >= 7 else "🟡 MONITOR" if pci >= 4 else "🟢 HEALTHY"
                st.metric("Pastoral Crisis Index", f"{pci:.1f} / 10", level)
                if pci >= 7:
                    st.markdown('<div class="crisis-red">⚠️ Immediate pastoral intervention recommended.</div>', unsafe_allow_html=True)
                elif pci >= 4:
                    st.markdown('<div class="warning-yellow">📋 Monitor trends — targeted improvement possible.</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="health-green">✅ Parish showing healthy pastoral signals.</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Calculation error: {e}")

    with st.expander("💰 Financial Transparency Index (FTI) Calculator"):
        c1, c2 = st.columns(2)
        with c1:
            budget_public   = st.checkbox("Budget publicly available?", True)
            allocation_pub  = st.checkbox("Budget allocation published?", True)
            overhead_pct    = st.slider("Admin overhead %", 0, 50, 12)
        with c2:
            charitable_pct  = st.slider("% to charitable/pastoral work", 0, 100, 75)
            accountability  = st.selectbox("Accountability structure", ["None","Internal only","Lay council","External audit","All of the above"])

        if st.button("Calculate FTI"):
            score = 0
            if budget_public:   score += 2.5
            if allocation_pub:  score += 2.0
            if overhead_pct <= 15: score += 2.0
            elif overhead_pct <= 25: score += 1.0
            if charitable_pct >= 70: score += 2.0
            elif charitable_pct >= 50: score += 1.0
            acc_map = {"None":0,"Internal only":0.5,"Lay council":1.0,"External audit":1.5,"All of the above":2.0}
            score += acc_map.get(accountability, 0)
            score = min(score, 10)
            level = "🟢 Transparent" if score >= 7 else "🟡 Partial" if score >= 4 else "🔴 Opaque"
            st.metric("Financial Transparency Index", f"{score:.1f} / 10", level)

    st.divider()
    st.markdown("### 🗺️ Regional Health Overview (Demo Data)")

    # Radar chart of 4 indices for sample parishes
    regions = ["Nairobi Central", "Manila North", "São Paulo East", "Rome Historic", "Chicago West"]
    pci_vals = [3.2, 4.1, 5.8, 2.8, 6.2]
    mci_vals = [5.1, 6.3, 7.2, 2.1, 4.8]
    jci_vals = [7.8, 5.2, 8.1, 3.4, 6.9]
    fti_vals = [6.2, 5.8, 4.9, 8.1, 5.5]

    fig = go.Figure()
    categories = ["PCI (Crisis)", "MCI (Material)", "JCI (Justice)", "FTI (Transparency)"]
    colors = ["#ef4444","#f97316","#22c55e","#3b82f6","#8b5cf6"]
    for i, region in enumerate(regions):
        vals = [pci_vals[i], mci_vals[i], jci_vals[i], fti_vals[i]]
        fig.add_trace(go.Scatterpolar(r=vals+[vals[0]], theta=categories+[categories[0]],
            fill="toself", name=region, line_color=colors[i], opacity=0.7))
    fig.update_layout(polar=dict(radialaxis=dict(range=[0,10])),
                      title="Ecosystem Health Radar — 5 Sample Parish Regions (DEMO)",
                      height=450)
    st.plotly_chart(fig, use_container_width=True)

    st.caption("DEMO: These indices use sample data. Connect your parish's real data via the Admin module.")

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: JUSTICE NETWORK
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "⚖️ Justice Network":
    st.title("⚖️ Justice Network")
    st.markdown("Global coordination of Catholic social action campaigns.")

    # Global impact bar
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Active Campaigns", "54")
    with col2: st.metric("Workers Benefited", "26,000+")
    with col3: st.metric("Parishes Involved", "890+")
    with col4: st.metric("Policy Wins (2025)", "7")

    st.divider()

    campaigns = [
        {
            "name": "Living Wage — Tea Farmers",
            "region": "Kenya",
            "status": "🟢 Active",
            "parishes": 89,
            "workers": 3000,
            "progress": "WON: Kiambu +25%, Nyeri +28% | Negotiating: Murang'a, Embu",
            "join": True,
        },
        {
            "name": "Refugee Rights — East Africa",
            "region": "Uganda / Kenya",
            "status": "🟢 Active",
            "parishes": 134,
            "workers": 8500,
            "progress": "230 parishes welcoming | 1,200 people housed | Legal support expanding",
            "join": True,
        },
        {
            "name": "Farmworker Wages — USA",
            "region": "Virginia, NC, GA",
            "status": "🟡 Organizing",
            "parishes": 47,
            "workers": 4200,
            "progress": "WON: Virginia +$2/hr | Organizing: North Carolina, Georgia",
            "join": True,
        },
        {
            "name": "Housing Justice",
            "region": "Global (12 cities)",
            "status": "🟢 Active",
            "parishes": 210,
            "workers": 12000,
            "progress": "São Paulo, Chicago, Manila, Lagos — 4,300 families supported",
            "join": True,
        },
        {
            "name": "Sugar Cane Workers",
            "region": "Brazil",
            "status": "🟡 Negotiating",
            "parishes": 65,
            "workers": 5800,
            "progress": "+15% wages proposed | Cross-parish coalition formed",
            "join": True,
        },
    ]

    for camp in campaigns:
        with st.container():
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.markdown(f"#### {camp['name']}")
                st.caption(f"📍 {camp['region']} · {camp['status']}")
                st.write(camp["progress"])
            with col2:
                st.metric("Parishes", camp["parishes"])
                st.metric("People", f"{camp['workers']:,}")
            with col3:
                if st.button(f"Join Campaign", key=f"join_{camp['name'][:10]}"):
                    st.success("✅ You've joined! You'll receive action alerts and coordination updates.")
            st.divider()

    st.markdown("### ➕ Submit a Justice Campaign")
    with st.expander("Propose a new campaign for coordination"):
        c1, c2 = st.columns(2)
        with c1:
            cam_name    = st.text_input("Campaign name")
            cam_region  = st.text_input("Region / Country")
            cam_issue   = st.selectbox("Issue area", ["Living wage","Housing","Refugee rights","Healthcare","Education","Environmental","Racial justice","Other"])
        with c2:
            cam_workers = st.number_input("People directly affected", 0, 1000000, 1000)
            cam_parishes= st.number_input("Parishes already involved", 0, 10000, 5)
            cam_desc    = st.text_area("Description")
        if st.button("Submit Campaign"):
            if cam_name and cam_region:
                st.success(f"✅ Campaign '{cam_name}' submitted for network review.")

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: ACCOUNTABILITY
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "📋 Accountability":
    st.title("📋 Accountability Dashboard")
    st.markdown("Bishop and diocese transparency, finance, and synodality scores.")
    st.caption("*'Nothing hidden will not be revealed.'* — Luke 12:2")

    # Diocese selector
    diocese = st.selectbox("Select Diocese (Demo)", [
        "Archdiocese of Nairobi, Kenya",
        "Archdiocese of Los Angeles, USA",
        "Archdiocese of Manila, Philippines",
        "Diocese of Kampala, Uganda",
        "Archdiocese of São Paulo, Brazil",
    ])

    # Demo data per diocese
    demo_data = {
        "Archdiocese of Nairobi, Kenya": {"fti":7.8,"pci":3.2,"justice":8.1,"synod":6.4,"women_pct":28,"youth_pct":35,"budget_pub":True,"priests":124,"parishes":180},
        "Archdiocese of Los Angeles, USA": {"fti":6.2,"pci":5.8,"justice":6.5,"synod":5.2,"women_pct":18,"youth_pct":15,"budget_pub":True,"priests":540,"parishes":287},
        "Archdiocese of Manila, Philippines": {"fti":5.1,"pci":4.4,"justice":7.2,"synod":5.8,"women_pct":22,"youth_pct":42,"budget_pub":False,"priests":410,"parishes":250},
        "Diocese of Kampala, Uganda": {"fti":6.9,"pci":3.8,"justice":7.5,"synod":6.1,"women_pct":24,"youth_pct":38,"budget_pub":True,"priests":89,"parishes":95},
        "Archdiocese of São Paulo, Brazil": {"fti":5.8,"pci":5.2,"justice":8.4,"synod":6.8,"women_pct":31,"youth_pct":28,"budget_pub":True,"priests":620,"parishes":340},
    }
    d = demo_data.get(diocese, list(demo_data.values())[0])

    st.divider()
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Financial Transparency", f"{d['fti']:.1f}/10", "FTI")
    with col2: st.metric("Pastoral Health", f"{10-d['pci']:.1f}/10", "Inverse PCI")
    with col3: st.metric("Justice Engagement", f"{d['justice']:.1f}/10", "JCI")
    with col4: st.metric("Synodality Score", f"{d['synod']:.1f}/10", "Walking Together")

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 💰 Financial Accountability")
        st.write(f"**Budget publicly available:** {'✅ Yes' if d['budget_pub'] else '❌ No'}")
        # Stacked bar: budget allocation
        alloc_labels = ["Pastoral","Material Aid","Formation","Admin","Building","Other"]
        alloc_vals   = [40, 22, 18, 12, 5, 3]
        fig = go.Figure(go.Bar(x=alloc_vals, y=alloc_labels, orientation='h',
            marker_color=['#22c55e','#3b82f6','#8b5cf6','#f97316','#94a3b8','#cbd5e1']))
        fig.update_layout(title="Budget Allocation %", height=280, margin=dict(l=0,r=0,t=40,b=0))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("### 👥 Leadership & Representation")
        st.metric("Women in leadership roles", f"{d['women_pct']}%")
        st.metric("Youth (under 35) involved", f"{d['youth_pct']}%")
        st.metric("Total priests", d["priests"])
        st.metric("Parishes", d["parishes"])
        if d['women_pct'] < 25:
            st.markdown('<div class="warning-yellow">⚠️ Women in leadership below peer average (29%)</div>', unsafe_allow_html=True)
        if d['youth_pct'] > 30:
            st.markdown('<div class="health-green">✅ Strong youth engagement</div>', unsafe_allow_html=True)

    st.divider()
    st.markdown("### 🕊️ Synodality — Walking Together")
    synod_items = {
        "Listening sessions held (2023-2025)": "14",
        "Changes made based on listening": "4",
        "Lay involvement in hiring decisions": "Partial",
        "LGBTQ+ outreach expanded": "Yes" if d["synod"] > 5 else "Not yet",
        "Financial transparency increased": "Yes" if d["fti"] > 6 else "In progress",
    }
    for k, v in synod_items.items():
        icon = "✅" if v in ("Yes","14","4","Partial") else "🔄"
        st.write(f"{icon} **{k}:** {v}")

    st.caption("⚠️ DEMO: All data here is illustrative. Production connects to diocesan self-reporting + public records.")

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: DIASPORA
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "🌏 Diaspora":
    st.title("🌏 Diaspora Connection")
    st.markdown("Find your cultural community. Connect globally. Stay rooted locally.")

    community = st.selectbox("Select your community", [
        "Filipino Catholic Diaspora",
        "Nigerian Catholic Diaspora",
        "Kenyan / East African Diaspora",
        "Korean Catholic Diaspora",
        "Polish Catholic Diaspora",
        "Brazilian Catholic Diaspora",
        "Vietnamese Catholic Diaspora",
    ])

    diaspora_data = {
        "Filipino Catholic Diaspora": {
            "origin": "Philippines", "total": "12M+",
            "concentrations": ["Middle East: 3.2M","North America: 4.8M","Europe: 1.2M","Australia: 800K"],
            "languages": ["Tagalog","Cebuano","Ilocano","English"],
            "justice_focus": ["Nurse / healthcare worker wages","Domestic worker rights","OFW remittance ethics","Anti-trafficking"],
            "parishes": "8,200+ Filipino communities globally",
        },
        "Nigerian Catholic Diaspora": {
            "origin": "Nigeria", "total": "4M+",
            "concentrations": ["UK: 900K","USA: 800K","Europe: 600K","Canada: 400K"],
            "languages": ["English","Igbo","Yoruba","Hausa"],
            "justice_focus": ["Healthcare worker brain drain","Remittance support","Anti-trafficking","Political asylum support"],
            "parishes": "2,400+ Nigerian communities globally",
        },
        "Kenyan / East African Diaspora": {
            "origin": "Kenya / Uganda / Tanzania", "total": "2M+",
            "concentrations": ["UK: 450K","USA: 350K","Germany: 120K","Middle East: 200K"],
            "languages": ["Swahili","Kikuyu","Luo","English","Luganda"],
            "justice_focus": ["Domestic worker rights","Living wage campaigns","Political asylum","Climate justice"],
            "parishes": "1,100+ East African communities globally",
        },
    }
    d = diaspora_data.get(community, list(diaspora_data.values())[0])

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Origin", d["origin"])
        st.metric("Global Community", d["total"])
        st.markdown("**Concentrations:**")
        for c in d["concentrations"]:
            st.write(f"• {c}")
    with col2:
        st.markdown("**Languages:**")
        st.write(", ".join(d["languages"]))
        st.metric("Catholic Communities", d["parishes"])
        st.markdown("**Justice Focus Areas:**")
        for j in d["justice_focus"]:
            st.write(f"⚖️ {j}")

    st.divider()
    st.markdown("### 🔍 Find Community Near You")
    your_city = st.text_input("Your city", placeholder="London / Dubai / Toronto")
    if st.button("Find My Community"):
        if your_city:
            st.success(f"✅ Searching for {community} communities in {your_city}...")
            st.info("🔧 **Production feature:** This will search GospelMap's parish database filtered by cultural community, language, and Mass schedule. Demo shows search capability.")
            # Could wire to OSM search filtered by church name patterns
        else:
            st.warning("Enter your city")

    st.divider()
    st.markdown("### 🤝 Connect to Justice Network")
    st.write("Your diaspora community's justice campaigns:")
    for j in d["justice_focus"]:
        col1, col2 = st.columns([3,1])
        with col1:
            st.write(f"⚖️ {j}")
        with col2:
            st.button("Join", key=f"join_{j[:15]}")

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: CRISIS RESPONSE
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "🆘 Crisis Response":
    st.title("🆘 Crisis Response Coordination")
    st.markdown("Real-time coordination of emergency response through parish networks.")

    st.divider()
    st.markdown("### 🔴 Active Crises")

    crises = [
        {"name":"Flooding — Lake Victoria Region","location":"Kenya / Uganda / Tanzania","severity":7.8,"parishes":450,"volunteers":2300,"shelters":15,"status":"🔴 ACTIVE"},
        {"name":"Refugee Surge — Horn of Africa","location":"Ethiopia / Somalia / Kenya border","severity":8.2,"parishes":230,"volunteers":1200,"shelters":8,"status":"🔴 ACTIVE"},
        {"name":"Post-Cyclone Recovery — Mozambique","location":"Central Mozambique","severity":6.4,"parishes":120,"volunteers":890,"shelters":12,"status":"🟡 RECOVERY"},
    ]

    for crisis in crises:
        col1, col2, col3 = st.columns([3,1,1])
        with col1:
            st.markdown(f"#### {crisis['status']} {crisis['name']}")
            st.caption(f"📍 {crisis['location']}")
            st.write(f"Parishes coordinating: **{crisis['parishes']}** · Volunteers: **{crisis['volunteers']:,}** · Shelter sites: **{crisis['shelters']}**")
        with col2:
            st.metric("Severity", f"{crisis['severity']}/10")
        with col3:
            if st.button(f"Coordinate", key=f"crisis_{crisis['name'][:10]}"):
                st.success("✅ You're now linked to the coordination network for this crisis.")
        st.divider()

    st.markdown("### 🆘 Report a New Crisis")
    with st.expander("Submit crisis report for network coordination"):
        c1, c2 = st.columns(2)
        with c1:
            cr_name     = st.text_input("Crisis name")
            cr_location = st.text_input("Location (country / region)")
            cr_type     = st.selectbox("Type", ["Flooding","Drought","Refugee surge","Earthquake","Conflict displacement","Disease outbreak","Food crisis","Other"])
        with c2:
            cr_severity = st.slider("Estimated severity (1-10)", 1, 10, 5)
            cr_affected = st.number_input("People affected (estimate)", 0, 10000000, 1000)
            cr_notes    = st.text_area("Description + immediate needs")
        if st.button("Submit Crisis Report"):
            if cr_name and cr_location:
                st.success(f"✅ Crisis report submitted. GospelMap will coordinate parish response in {cr_location}.")

    st.divider()
    st.markdown("### 📋 Offer Aid Capacity")
    c1, c2 = st.columns(2)
    with c1:
        aid_parish = st.text_input("Your parish / organisation")
        aid_city   = st.text_input("Your location")
    with c2:
        aid_types  = st.multiselect("What can you offer?", ["Shelter (beds)","Food","Medical","Transport","Volunteer hours","Funds","Prayer / spiritual support"])
        aid_notes  = st.text_area("Additional notes")
    if st.button("Register Aid Capacity"):
        if aid_parish:
            st.success(f"✅ {aid_parish} registered as aid provider. You'll be matched to nearest active crisis.")

st.markdown("---")
st.caption("GospelMap | AGPL-3.0 | [GitHub](https://github.com/gabrielmahia/gospelmap) | contact@aikungfu.dev | CC BY-NC-ND 4.0")
