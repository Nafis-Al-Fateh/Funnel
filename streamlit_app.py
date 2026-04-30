import streamlit as st

st.set_page_config(page_title="Sales Funnel", layout="wide")

# ======================
# STYLES
# ======================
st.markdown("""
    <style>
    .box {
        padding: 16px;
        border-radius: 12px;
        text-align: center;
        font-weight: 500;
        margin: 6px 0;
    }
    .blue { background-color: #E3F2FD; }
    .green { background-color: #E8F5E9; }
    .orange { background-color: #FFF3E0; }
    .red { background-color: #FFEBEE; }
    .purple { background-color: #F3E5F5; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 Sales Funnel Flow")

# ======================
# TOP CHANNELS
# ======================
st.subheader("1. Lead Generation")

cols = st.columns(5)
channels = ["LinkedIn", "Paid Ads", "Email Outreach", "Website / SEO", "Referrals"]

for col, ch in zip(cols, channels):
    col.markdown(f'<div class="box blue">{ch}</div>', unsafe_allow_html=True)

st.markdown("---")

# ======================
# CAPTURE + QUALIFY
# ======================
st.markdown('<div class="box purple">Lead Captured (Landing Page)</div>', unsafe_allow_html=True)
st.markdown('<div class="box purple">Quick Qualification (Budget • Need • Authority)</div>', unsafe_allow_html=True)

# ======================
# FIT SPLIT
# ======================
st.subheader("2. Qualification Outcome")

col1, col2, col3 = st.columns(3)

col1.markdown('<div class="box green">High Fit<br>Ideal Client</div>', unsafe_allow_html=True)
col2.markdown('<div class="box blue">Medium Fit<br>Nurture</div>', unsafe_allow_html=True)
col3.markdown('<div class="box red">Low Fit<br>Not a Match</div>', unsafe_allow_html=True)

st.markdown("---")

# ======================
# DISCOVERY
# ======================
st.subheader("3. Discovery Call")

st.markdown('<div class="box blue">Book Discovery Call</div>', unsafe_allow_html=True)
st.markdown('<div class="box blue">Understand Goals & Challenges</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

col1.markdown('<div class="box blue">Maybe<br>Send Case Studies</div>', unsafe_allow_html=True)
col2.markdown('<div class="box green">Good Fit<br>Proceed</div>', unsafe_allow_html=True)
col3.markdown('<div class="box red">Not a Fit<br>CRM Nurture</div>', unsafe_allow_html=True)

st.markdown("---")

# ======================
# STRATEGY
# ======================
st.subheader("4. Strategy & Offer")

st.markdown('<div class="box purple">Paid Strategy Session</div>', unsafe_allow_html=True)
st.markdown('<div class="box purple">Growth Roadmap</div>', unsafe_allow_html=True)
st.markdown('<div class="box orange">Free Trial (Optional)</div>', unsafe_allow_html=True)
st.markdown('<div class="box blue">Present Packages</div>', unsafe_allow_html=True)

st.markdown("---")

# ======================
# CLOSING
# ======================
st.subheader("5. Closing")

col1, col2, col3 = st.columns(3)

col1.markdown('<div class="box red">Lost Deal</div>', unsafe_allow_html=True)
col2.markdown('<div class="box green">Deal Closed 🎉</div>', unsafe_allow_html=True)
col3.markdown('<div class="box orange">Stalled → Follow-up</div>', unsafe_allow_html=True)

st.markdown("---")

# ======================
# ONBOARDING
# ======================
st.subheader("6. Onboarding")

st.markdown('<div class="box blue">Kickoff Call</div>', unsafe_allow_html=True)
st.markdown('<div class="box blue">Collect Assets</div>', unsafe_allow_html=True)
st.markdown('<div class="box blue">Define KPIs</div>', unsafe_allow_html=True)

st.markdown("---")

# ======================
# DELIVERY
# ======================
st.subheader("7. Delivery")

col1, col2, col3, col4 = st.columns(4)

col1.markdown('<div class="box purple">Marketing<br>Ads + Analytics</div>', unsafe_allow_html=True)
col2.markdown('<div class="box green">Design<br>Creatives</div>', unsafe_allow_html=True)
col3.markdown('<div class="box blue">Video<br>Reels + Edits</div>', unsafe_allow_html=True)
col4.markdown('<div class="box orange">Dev<br>Website + Tracking</div>', unsafe_allow_html=True)

st.markdown('<div class="box green">Content Live + Ads Running</div>', unsafe_allow_html=True)

st.markdown("---")

# ======================
# REPORTING
# ======================
st.subheader("8. Reporting & Growth")

st.markdown('<div class="box purple">Monthly Reporting</div>', unsafe_allow_html=True)
st.markdown('<div class="box purple">Review ROI</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

col1.markdown('<div class="box green">Upsell / Cross-sell</div>', unsafe_allow_html=True)
col2.markdown('<div class="box green">Optimize & Scale</div>', unsafe_allow_html=True)
col3.markdown('<div class="box red">At Risk Client</div>', unsafe_allow_html=True)

st.markdown('<div class="box green">Referrals + Reviews</div>', unsafe_allow_html=True)
