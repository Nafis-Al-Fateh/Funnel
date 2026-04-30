import streamlit as st

st.set_page_config(layout="wide")

# ======================
# STYLE
# ======================
st.markdown("""
<style>
body { background: #0f172a; }

/* Title */
.title {
    text-align: center;
    font-size: 38px;
    font-weight: 700;
    color: white;
    margin-bottom: 20px;
}

/* Section spacing */
.section {
    margin-top: 30px;
}

/* Cards */
.card {
    padding: 16px;
    border-radius: 14px;
    text-align: center;
    font-weight: 500;
    color: white;
    margin: 10px auto;
    width: 260px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.35);
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
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🚀 Sales Funnel</div>', unsafe_allow_html=True)

# ======================
# LEAD GEN
# ======================
st.markdown('<div class="section"></div>', unsafe_allow_html=True)

cols = st.columns(5)
channels = ["LinkedIn", "Ads", "Email", "SEO", "Referrals"]

for col, ch in zip(cols, channels):
    with col:
        st.markdown(f'<div class="card blue">{ch}</div>', unsafe_allow_html=True)

st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

# ======================
# CORE FUNNEL
# ======================
center = st.columns([1,2,1])[1]

with center:
    st.markdown('<div class="card purple">Lead Captured</div>', unsafe_allow_html=True)
    st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

    st.markdown('<div class="card purple">Qualification (BANT)</div>', unsafe_allow_html=True)

# ======================
# SPLIT
# ======================
st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

left, mid, right = st.columns([1,2,1])

with left:
    st.markdown('<div class="card green">High Fit</div>', unsafe_allow_html=True)

with mid:
    st.markdown('<div class="card blue">Medium Fit</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card red">Low Fit</div>', unsafe_allow_html=True)

# ======================
# DISCOVERY
# ======================
st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

with center:
    st.markdown('<div class="card blue">Discovery Call</div>', unsafe_allow_html=True)

# ======================
# DISCOVERY SPLIT
# ======================
left, mid, right = st.columns([1,2,1])

with left:
    st.markdown('<div class="card green">Good Fit</div>', unsafe_allow_html=True)

with mid:
    st.markdown('<div class="card orange">Maybe</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card red">Not Fit</div>', unsafe_allow_html=True)

# ======================
# STRATEGY
# ======================
st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

with center:
    st.markdown('<div class="card purple">Strategy Session</div>', unsafe_allow_html=True)
    st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

    st.markdown('<div class="card blue">Present Offer</div>', unsafe_allow_html=True)

# ======================
# CLOSING
# ======================
st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

left, mid, right = st.columns([1,2,1])

with left:
    st.markdown('<div class="card red">Lost</div>', unsafe_allow_html=True)

with mid:
    st.markdown('<div class="card green">Closed Won 🎉</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card orange">Stalled</div>', unsafe_allow_html=True)

# ======================
# FINAL FLOW
# ======================
st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

with center:
    st.markdown('<div class="card blue">Onboarding</div>', unsafe_allow_html=True)
    st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

    st.markdown('<div class="card green">Delivery</div>', unsafe_allow_html=True)
    st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

    st.markdown('<div class="card purple">Reporting & Growth</div>', unsafe_allow_html=True)
