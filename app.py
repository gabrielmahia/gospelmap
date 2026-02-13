"""
GospelMap - Global Catholic Ecosystem Intelligence Platform
Main entry point
"""

import streamlit as st
from streamlit_option_menu import option_menu
import json
from datetime import datetime

# Page config
st.set_page_config(
    page_title="GospelMap 🌍",
    page_icon="✝️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    
    .crisis-red {
        background: #ff6b6b;
        color: white;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .health-green {
        background: #51cf66;
        color: white;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .warning-yellow {
        background: #ffd43b;
        color: #333;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .header-title {
        font-size: 3em;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        font-size: 1.3em;
        color: #7f8c8d;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 🌍 GospelMap")
    st.markdown("---")
    
    # Global stats
    st.subheader("Global Stats (Demo)")
    st.metric("Parishes Mapped", "5,000")
    st.metric("Dioceses", "500+")
    st.metric("Countries", "150+")
    st.metric("Justice Campaigns", "50+")
    st.metric("Active Users", "10K+")
    st.markdown("---")
    
    # Data status
    st.subheader("Data Status")
    st.write("🟢 **Demo Mode Active**")
    st.write("All data is sample/realistic. Not for operational use.")
    st.write(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    st.markdown("---")
    st.markdown("**Built on Vatican II theology**  \n**AGPL-3.0 Licensed**  \n**Forever Community-Owned**")

# Main content
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown('<div class="header-title">🌍 GospelMap</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Find Your People. Measure Justice. Hold Leadership Accountable.</div>', unsafe_allow_html=True)

with col2:
    st.write("")

st.write("")

# Navigation tabs (Pages)
tab_home, tab_discover, tab_health, tab_justice, tab_accountability, tab_diaspora, tab_formation, tab_crisis = st.tabs([
    "🏠 Home",
    "🔍 Find My Church",
    "📊 Ecosystem Health",
    "⚖️ Justice Network",
    "📋 Accountability",
    "🌏 Diaspora",
    "📖 Formation",
    "🆘 Crisis"
])

with tab_home:
    st.header("Welcome to GospelMap")
    st.write("")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🗺️ Find My Local Church
        
        Search by location, language, values
        - LGBTQ+ welcoming?
        - Active in justice?
        - Transparent finances?
        - Community reviews
        """)
    
    with col2:
        st.markdown("""
        ### 📊 Ecosystem Health
        
        Real-time crisis signals
        - Pastoral health
        - Material security
        - Justice alignment
        - Financial transparency
        """)
    
    with col3:
        st.markdown("""
        ### ⚖️ Global Justice
        
        Coordinate campaigns worldwide
        - Living wage organizing
        - Refugee rights
        - Housing justice
        - Climate action
        """)
    
    st.write("")
    st.write("")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 👥 Accountability
        
        Track bishop transparency
        - Finances (public?)
        - Abuse records
        - Leadership diversity
        - Synodality progress
        """)
    
    with col2:
        st.markdown("""
        ### 🌏 Diaspora Connect
        
        Find your ethnic community
        - Filipino networks
        - Nigerian communities
        - Korean parishes
        - Support services
        """)
    
    with col3:
        st.markdown("""
        ### 📖 Spiritual Formation
        
        Journey matched to your needs
        - Exploring → Committed → Leader
        - In your language
        - Justice integrated
        - Local mentors
        """)
    
    st.write("")
    st.divider()
    st.write("")
    
    # Key stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><h3>5,000+</h3><p>Parishes Mapped</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>150+</h3><p>Countries</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h3>50+</h3><p>Justice Campaigns</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><h3>1.3B</h3><p>Catholics Served</p></div>', unsafe_allow_html=True)

with tab_discover:
    st.header("🔍 Find My Local Church")
    st.write("Search by location, values, and accessibility needs")
    st.write("")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Search Parameters")
        
        location = st.text_input("Your Location", "Los Angeles, CA")
        distance = st.slider("How far willing to travel?", 1, 50, 15, label_visibility="collapsed")
        
        st.write("")
        st.subheader("Language")
        languages = st.multiselect(
            "Languages you speak",
            ["English", "Spanish", "Tagalog", "Swahili", "Polish", "Vietnamese", "Korean", "French"],
            default=["English"]
        )
        
        st.write("")
        st.subheader("Accessibility")
        wheelchair = st.checkbox("Wheelchair accessible needed")
        hearing_loop = st.checkbox("Hearing loop needed")
        nursery = st.checkbox("Childcare/nursery")
        
    with col2:
        st.subheader("Welcome Indices (0-10)")
        
        lgbtq_welcome = st.slider("LGBTQ+ Welcome", 0, 10, 5)
        divorced_welcome = st.slider("Divorced/Remarried Welcome", 0, 10, 5)
        immigrant_welcome = st.slider("Immigrant/Refugee Welcome", 0, 10, 5)
        poor_welcome = st.slider("Poor/Economically Marginalized Welcome", 0, 10, 5)
        
        st.write("")
        st.subheader("Values")
        
        values = st.multiselect(
            "What matters most to you?",
            ["Social Justice", "Traditional Liturgy", "Community Warmth", "Intellectual Engagement",
             "Environmental Stewardship", "Women in Leadership", "Financial Transparency"],
            default=["Social Justice"]
        )
    
    st.write("")
    
    if st.button("🔍 Find My People", use_container_width=True, type="primary"):
        st.success("✅ Searching for matching parishes...")
        st.write("")
        
        # Mock results
        results = [
            {
                "name": "Blessed Sacrament Church",
                "location": "Los Angeles, CA",
                "distance": "2.3 miles",
                "match": "88%",
                "summary": "Spanish/English, 9/10 LGBTQ+ welcome, active in living wage campaigns",
                "mass_times": ["9am Spanish", "11am English", "5pm English"],
                "justice_campaigns": ["Living Wage Organizing", "Refugee Rights"],
                "welcome_score": 9,
                "transparency_score": 8
            },
            {
                "name": "St. Mary's Cathedral",
                "location": "Los Angeles, CA",
                "distance": "4.8 miles",
                "match": "76%",
                "summary": "English only, 7/10 LGBTQ+ welcome, moderate justice involvement",
                "mass_times": ["8am", "10am", "12pm", "5:30pm"],
                "justice_campaigns": ["Housing Justice"],
                "welcome_score": 7,
                "transparency_score": 6
            },
            {
                "name": "Our Lady of Guadalupe",
                "location": "Los Angeles, CA",
                "distance": "6.2 miles",
                "match": "71%",
                "summary": "Spanish dominant, 8/10 LGBTQ+ welcome, strong justice presence",
                "mass_times": ["7am Spanish", "9am Spanish", "11am Spanish", "1pm English"],
                "justice_campaigns": ["Living Wage", "Immigrant Rights", "Housing"],
                "welcome_score": 8,
                "transparency_score": 7
            }
        ]
        
        for i, parish in enumerate(results, 1):
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.subheader(f"{i}. {parish['name']}")
                st.write(f"📍 {parish['location']} ({parish['distance']})")
                st.write(f"💚 {parish['summary']}")
            
            with col2:
                st.metric("Match", parish['match'])
                st.metric("Welcome", f"{parish['welcome_score']}/10")
            
            with col3:
                st.metric("Transparency", f"{parish['transparency_score']}/10")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("**Mass Times:**")
                for time in parish['mass_times']:
                    st.write(f"- {time}")
            
            with col2:
                st.write("**Justice Work:**")
                for campaign in parish['justice_campaigns']:
                    st.write(f"- {campaign}")
            
            with col3:
                if st.button(f"Learn More", key=f"parish_{i}"):
                    st.write("Detailed parish profile would load here...")
            
            st.divider()

with tab_health:
    st.header("📊 Ecosystem Health Dashboard")
    st.write("Real-time crisis signals for parishes and dioceses")
    st.write("")
    
    # Global stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Avg Pastoral Health", "6.2/10", "-0.3")
    with col2:
        st.metric("Avg Material Health", "5.8/10", "+0.2")
    with col3:
        st.metric("Avg Justice Engagement", "3.4/10", "+0.1")
    with col4:
        st.metric("Avg Transparency", "5.1/10", "+0.4")
    
    st.write("")
    st.divider()
    st.write("")
    
    # Crisis alerts
    st.subheader("🔴 Crisis Alerts (Red Status)")
    st.markdown("""
    **Priest Shortage Crisis**
    - Diocese: Archdiocese of Detroit
    - 45 vacant positions, 120 parishes
    - Pastoral Health: 8.2/10 (CRISIS)
    - Recommendation: Ordain deacons, redistribute pastors
    
    **Abuse Allegation Alert**
    - Diocese: Diocese of Covington
    - 3 recent allegations (past 6 months)
    - Transparency: 2/10 (OPAQUE)
    - Recommendation: Implement public record system
    """)
    
    st.write("")
    st.divider()
    st.write("")
    
    # Search specific diocese/parish
    st.subheader("Search Specific Parish/Diocese")
    
    col1, col2 = st.columns(2)
    
    with col1:
        search_type = st.radio("Search by:", ["Parish", "Diocese"])
    
    with col2:
        search_name = st.text_input(f"Enter {search_type} name")
    
    if search_name:
        st.write("")
        st.subheader(f"Health Report: {search_name}")
        
        # Mock data
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Pastoral Crisis", "4.2/10", "Good")
        with col2:
            st.metric("Material Crisis", "5.8/10", "Fair")
        with col3:
            st.metric("Justice Crisis", "6.1/10", "Monitor")
        with col4:
            st.metric("Transparency", "7.2/10", "Good")
        
        st.write("")
        st.metric("Ecosystem Health Score", "6.1/10", "Fair - Improvements recommended")

with tab_justice:
    st.header("⚖️ Global Justice Network")
    st.write("Coordinate campaigns across dioceses and continents")
    st.write("")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        campaign = st.selectbox(
            "Active Campaign",
            ["Living Wage - Global", "Refugee Rights", "Housing Justice", "Climate Action", "Migrant Worker Rights"]
        )
    
    with col2:
        if st.button("View All Campaigns"):
            pass
    
    st.write("")
    
    if campaign == "Living Wage - Global":
        st.subheader("🌍 Living Wage Campaign - Global Overview")
        st.write("")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Workers", "26,000+")
        with col2:
            st.metric("Parishes Involved", "250+")
        with col3:
            st.metric("Policy Wins", "3")
        with col4:
            st.metric("Income Increase", "$45M/year")
        
        st.write("")
        st.subheader("Regional Progress")
        
        regions = {
            "Kenya": {"status": "WON in 3 regions", "workers": "1,400", "wage_increase": "+26%"},
            "USA (Virginia)": {"status": "WON", "workers": "15,000", "wage_increase": "+$2/hr"},
            "Brazil": {"status": "Negotiating", "workers": "8,000", "wage_increase": "pending"},
            "UK": {"status": "Organizing", "workers": "2,000", "wage_increase": "pending"}
        }
        
        for region, data in regions.items():
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.write(f"**{region}**")
            with col2:
                st.write(data['status'])
            with col3:
                st.write(f"{data['workers']} workers")
            with col4:
                st.write(data['wage_increase'])
        
        st.write("")
        st.write("---")
        st.write("")
        
        if st.button("✋ I Want to Join This Campaign!", use_container_width=True, type="primary"):
            st.success("✅ You've been added to the Living Wage campaign!")
            st.write("Next steps: Join orientation call this Saturday at 2pm PT")

with tab_accountability:
    st.header("📋 Bishop & Diocese Accountability Dashboard")
    st.write("Transparency tracked globally")
    st.write("")
    
    bishop_search = st.text_input("Search bishop or diocese name")
    
    if bishop_search or True:  # Show default
        st.subheader("Archbishop John Smith - Los Angeles")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Accountability", "6.2/10", "Improving")
        with col2:
            st.metric("Transparency", "7.1/10", "Good")
        with col3:
            st.metric("Diversity", "4/10", "Low")
        with col4:
            st.metric("Synodality", "5.8/10", "Moderate")
        
        st.write("")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("💰 Finances")
            st.write("Budget: $120M (2023)")
            st.write("- Pastoral: 45%")
            st.write("- Admin: 12%")
            st.write("- Charitable: 43%")
            st.write("✅ Budget Public: YES")
            st.write("✅ External Audit: YES")
        
        with col2:
            st.subheader("🛡️ Abuse Accountability")
            st.write("Allegations (10 years): 8")
            st.write("- Cases settled: 7")
            st.write("- Cases pending: 1")
            st.write("Victim support: ✅ YES")
            st.write("Transparency: 7/10 (could improve)")

with tab_diaspora:
    st.header("🌏 Diaspora Community Connection")
    st.write("Connect with your ethnic community worldwide")
    st.write("")
    
    community = st.selectbox(
        "Select Your Community",
        ["Filipino", "Nigerian", "Korean", "Polish", "Vietnamese", "Mexican", "Haitian", "Congolese"]
    )
    
    st.write("")
    st.subheader(f"🇵🇭 {community} Catholics Worldwide")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if community == "Filipino":
            st.metric("Global Population", "11 million")
        else:
            st.metric("Global Population", "~5 million")
    with col2:
        st.metric("Countries", "100+")
    with col3:
        st.metric("Major Hub", "Middle East")
    with col4:
        st.metric("Growing Region", "Europe")
    
    st.write("")
    st.write(f"**Local Communities Near You (Example: Los Angeles)**")
    st.write(f"- St. Charles Lwanga (85% {community}, 12 Masses/week)")
    st.write(f"- Our Lady of [Community Name] (70% {community}, 8 Masses/week)")
    st.write(f"- [2 more parishes]")
    
    st.write("")
    st.write(f"**Justice Networks for {community} Workers**")
    st.write("- Healthcare worker wages: 156 nurses organizing")
    st.write("- Domestic worker rights: 89 parishes")
    st.write("- Migrant family support: resources + advocacy")

with tab_formation:
    st.header("📖 Spiritual Formation Pathway")
    st.write("Your personalized journey to deeper faith")
    st.write("")
    
    journey = st.radio(
        "Where are you in your faith journey?",
        ["Exploring Catholicism", "Returning to Faith", "Lifelong Catholic", "Converting from Another Faith", "Questioning My Faith"]
    )
    
    st.write("")
    st.subheader("Recommended Path for You")
    st.write("")
    
    path = [
        ("1. Find Community", "Join a parish that welcomes you", "This week"),
        ("2. Small Group", "Join Bible study, prayer circle, or book club", "Month 1"),
        ("3. Sacraments", "Baptism, confirmation, or reconnection", "Month 2-3"),
        ("4. Leadership", "Volunteer, join ministry, justice work", "Month 4+"),
        ("5. Deep Formation", "Theology, contemplative practice, mentorship", "Ongoing")
    ]
    
    for step, description, timeline in path:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            st.write(f"**{step}**")
        with col2:
            st.write(description)
        with col3:
            st.write(f"*{timeline}*")

with tab_crisis:
    st.header("🆘 Crisis Response System")
    st.write("Coordinate emergency response globally")
    st.write("")
    
    st.subheader("Active Crisis Alerts")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.write("**Earthquake - Turkey/Syria Border**")
    with col2:
        st.metric("Severity", "9.2/10")
    with col3:
        st.metric("Status", "🔴 ACTIVE")
    
    st.write("Parishes coordinating: 450+ | Volunteers: 2,300 | Shelters: 15")
    
    st.write("")
    st.write("---")
    st.write("")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.write("**Refugee Surge - Mexico-USA Border**")
    with col2:
        st.metric("Scale", "8,500 people")
    with col3:
        st.metric("Status", "🟡 ACTIVE")
    
    st.write("Parishes welcoming: 230 | Housing capacity: 1,200 | Support coordinated")

st.write("")
st.divider()
st.write("")

# Footer
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown("""
    **🙏 GospelMap**
    
    Making the invisible Church visible
    """)

with col2:
    st.markdown("""
    **📧 Contact**
    
    gabriel@aikungfu.dev
    """)

with col3:
    st.markdown("""
    **⚖️ License**
    
    AGPL-3.0  
    Forever Community-Owned
    """)

st.markdown("---")
st.markdown("*'Nothing is hidden that will not be revealed.' — Luke 12:2*")
