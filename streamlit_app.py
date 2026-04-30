import streamlit as st

st.set_page_config(layout="wide")

# ======================
# STYLES
# ======================
st.markdown("""
<style>
body {
    background: #0f172a;
}

/* Title */
.title {
    text-align: center;
    font-size: 40px;
    font-weight: 700;
    color: white;
    margin-bottom: 30px;
}

/* Cards */
.card {
    padding: 14px 18px;
    border-radius: 14px;
    text-align: center;
    font-weight: 500;
    color: white;
    margin: 6px auto;
    width: 220px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.3);
}

/* Colors */
.blue { background: linear-gradient(135deg, #3b82f6, #2563eb); }
.green { background: linear-gradient(135deg, #22c55e, #16a34a); }
.orange { background: linear-gradient(135deg, #f59e0b, #ea580c); }
.red { background: linear-gradient(135deg, #ef4444, #dc2626); }
.purple { background: linear-gradient(135deg, #8b5cf6, #6d28d9); }

/* Arrow */
.arrow {
    text-align: center;
    font-size: 22px;
    color: #94a3b8;
    margin: 2px 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🚀 Sales Funnel</div>', unsafe_allow_html=True)

# ======================
# LEAD GEN (TOP ROW)
# ======================
cols = st.columns([1,1,1,1,1])
channels = ["LinkedIn", "Ads", "Email", "SEO", "Referrals"]

for col, ch in zip(cols, channels):
    with col:
        st.markdown(f'<div class="card blue">{ch}</div>', unsafe_allow_html=True)

st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

# ======================
# CORE FUNNEL (CENTERED)
# ======================
center = st.columns([1,2,1])[1]

with center:
    st.markdown('<div class="card purple">Lead Captured</div>', unsafe_allow_html=True)
    st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

    st.markdown('<div class="card purple">Qualification (BANT)</div>', unsafe_allow_html=True)
    st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

# ======================
# SPLIT (3 WAY)
# ======================
left, mid, right = st.columns(3)

with left:
    st.markdown('<div class="card green">High Fit</div>', unsafe_allow_html=True)

with mid:
    st.markdown('<div class="card blue">Medium Fit</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card red">Low Fit</div>', unsafe_allow_html=True)

st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

# ======================
# DISCOVERY (CENTER)
# ======================
with center:
    st.markdown('<div class="card blue">Discovery Call</div>', unsafe_allow_html=True)

# ======================
# DISCOVERY SPLIT
# ======================
left, mid, right = st.columns(3)

with left:
    st.markdown('<div class="card green">Good Fit</div>', unsafe_allow_html=True)

with mid:
    st.markdown('<div class="card orange">Maybe</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card red">Not Fit</div>', unsafe_allow_html=True)

st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

# ======================
# STRATEGY → OFFER
# ======================
with center:
    st.markdown('<div class="card purple">Strategy Session</div>', unsafe_allow_html=True)
    st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

    st.markdown('<div class="card blue">Present Offer</div>', unsafe_allow_html=True)
    st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

# ======================
# CLOSING SPLIT
# ======================
left, mid, right = st.columns(3)

with left:
    st.markdown('<div class="card red">Lost</div>', unsafe_allow_html=True)

with mid:
    st.markdown('<div class="card green">Closed Won 🎉</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card orange">Stalled</div>', unsafe_allow_html=True)

st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

# ======================
# FINAL FLOW
# ======================
with center:
    st.markdown('<div class="card blue">Onboarding</div>', unsafe_allow_html=True)
    st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

    st.markdown('<div class="card green">Delivery</div>', unsafe_allow_html=True)
    st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

    st.markdown('<div class="card purple">Reporting & Growth</div>', unsafe_allow_html=True)
