import streamlit as st

st.set_page_config(layout="wide")

# ======================
# MODERN UI STYLE
# ======================
st.markdown("""
<style>

/* Background */
.stApp {
    background: radial-gradient(circle at top, #0f172a, #020617);
    color: white;
    font-family: 'Inter', sans-serif;
}

/* Title */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 30px;
    letter-spacing: -0.5px;
}

/* Section spacing */
.section {
    margin-top: 40px;
}

/* Glass Cards */
.card {
    padding: 18px;
    border-radius: 16px;
    text-align: center;
    font-weight: 600;
    font-size: 16px;
    margin: 10px auto;
    width: 240px;

    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);

    border: 1px solid rgba(255,255,255,0.08);

    transition: all 0.3s ease;
}

/* Hover Effect */
.card:hover {
    transform: translateY(-6px) scale(1.03);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}

/* Highlight (main funnel steps) */
.main {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
}

/* Status Colors */
.green { background: linear-gradient(135deg, #22c55e, #16a34a); }
.orange { background: linear-gradient(135deg, #f59e0b, #ea580c); }
.red { background: linear-gradient(135deg, #ef4444, #dc2626); }
.blue { background: linear-gradient(135deg, #3b82f6, #2563eb); }

/* Arrow */
.arrow {
    text-align: center;
    font-size: 26px;
    margin: 10px 0;
    color: #64748b;
}

/* Section Label */
.label {
    text-align: center;
    font-size: 14px;
    color: #94a3b8;
    margin-bottom: 10px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

</style>
""", unsafe_allow_html=True)

# ======================
# TITLE
# ======================
st.markdown('<div class="title">🚀 Sales Funnel</div>', unsafe_allow_html=True)

# ======================
# LEAD SOURCES
# ======================
st.markdown('<div class="label">Lead Sources</div>', unsafe_allow_html=True)

cols = st.columns(5)
channels = ["LinkedIn", "Paid Ads", "Email", "SEO", "Referrals"]

for col, ch in zip(cols, channels):
    with col:
        st.markdown(f'<div class="card">{ch}</div>', unsafe_allow_html=True)

st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

# ======================
# CORE FUNNEL
# ======================
center = st.columns([1,2,1])[1]

with center:
    st.markdown('<div class="card main">Lead Captured</div>', unsafe_allow_html=True)
    st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

    st.markdown('<div class="card main">Qualification (BANT)</div>', unsafe_allow_html=True)

st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

# ======================
# QUALIFICATION SPLIT
# ======================
st.markdown('<div class="label">Lead Quality</div>', unsafe_allow_html=True)

left, mid, right = st.columns([1,2,1])

with left:
    st.markdown('<div class="card green">High Fit</div>', unsafe_allow_html=True)

with mid:
    st.markdown('<div class="card blue">Medium Fit</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card red">Low Fit</div>', unsafe_allow_html=True)

st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

# ======================
# DISCOVERY
# ======================
with center:
    st.markdown('<div class="card main">Discovery Call</div>', unsafe_allow_html=True)

# ======================
# DISCOVERY RESULT
# ======================
st.markdown('<div class="label">Discovery Outcome</div>', unsafe_allow_html=True)

left, mid, right = st.columns([1,2,1])

with left:
    st.markdown('<div class="card green">Good Fit</div>', unsafe_allow_html=True)

with mid:
    st.markdown('<div class="card orange">Maybe</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card red">Not Fit</div>', unsafe_allow_html=True)

st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

# ======================
# STRATEGY + OFFER
# ======================
with center:
    st.markdown('<div class="card main">Strategy Session</div>', unsafe_allow_html=True)
    st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

    st.markdown('<div class="card blue">Present Offer</div>', unsafe_allow_html=True)

st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

# ======================
# CLOSING
# ======================
st.markdown('<div class="label">Closing Outcome</div>', unsafe_allow_html=True)

left, mid, right = st.columns([1,2,1])

with left:
    st.markdown('<div class="card red">Lost</div>', unsafe_allow_html=True)

with mid:
    st.markdown('<div class="card green">Closed Won 🎉</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card orange">Stalled</div>', unsafe_allow_html=True)

st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

# ======================
# POST-SALE FLOW
# ======================
with center:
    st.markdown('<div class="card main">Onboarding</div>', unsafe_allow_html=True)
    st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

    st.markdown('<div class="card green">Delivery</div>', unsafe_allow_html=True)
    st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

    st.markdown('<div class="card blue">Reporting & Growth</div>', unsafe_allow_html=True)
