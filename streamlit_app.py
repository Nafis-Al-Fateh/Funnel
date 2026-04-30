import streamlit as st

st.set_page_config(page_title="Beautiful Funnel", layout="wide")

# ======================
# STYLES
# ======================
st.markdown("""
<style>
body {
    background: linear-gradient(180deg, #0f172a, #1e293b);
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    color: white;
    margin-bottom: 30px;
}

.section {
    text-align: center;
    color: #cbd5f5;
    font-size: 20px;
    margin-top: 30px;
    margin-bottom: 10px;
}

.card {
    padding: 18px;
    border-radius: 16px;
    text-align: center;
    font-weight: 500;
    color: white;
    margin: 8px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.3);
    transition: 0.3s;
}
.card:hover {
    transform: translateY(-4px);
}

.blue { background: linear-gradient(135deg, #3b82f6, #2563eb); }
.green { background: linear-gradient(135deg, #22c55e, #16a34a); }
.orange { background: linear-gradient(135deg, #f59e0b, #ea580c); }
.red { background: linear-gradient(135deg, #ef4444, #dc2626); }
.purple { background: linear-gradient(135deg, #8b5cf6, #6d28d9); }

.arrow {
    text-align: center;
    font-size: 28px;
    color: #94a3b8;
    margin: -5px 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🚀 Sales Funnel</div>', unsafe_allow_html=True)

# ======================
# LEAD GEN
# ======================
st.markdown('<div class="section">Lead Generation</div>', unsafe_allow_html=True)

cols = st.columns(5)
channels = ["LinkedIn", "Ads", "Email", "SEO", "Referrals"]

for col, ch in zip(cols, channels):
    col.markdown(f'<div class="card blue">{ch}</div>', unsafe_allow_html=True)

st.markdown('<div class="arrow">⬇️</div>', unsafe_allow_html=True)

# ======================
# CAPTURE
# ======================
st.markdown('<div class="card purple">Lead Captured</div>', unsafe_allow_html=True)

st.markdown('<div class="arrow">⬇️</div>', unsafe_allow_html=True)

st.markdown('<div class="card purple">Qualification (BANT)</div>', unsafe_allow_html=True)

# ======================
# SPLIT
# ======================
st.markdown('<div class="arrow">⬇️</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

col1.markdown('<div class="card green">High Fit</div>', unsafe_allow_html=True)
col2.markdown('<div class="card blue">Medium Fit</div>', unsafe_allow_html=True)
col3.markdown('<div class="card red">Low Fit</div>', unsafe_allow_html=True)

# ======================
# DISCOVERY
# ======================
st.markdown('<div class="arrow">⬇️</div>', unsafe_allow_html=True)

st.markdown('<div class="card blue">Discovery Call</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

col1.markdown('<div class="card green">Good Fit</div>', unsafe_allow_html=True)
col2.markdown('<div class="card orange">Maybe</div>', unsafe_allow_html=True)
col3.markdown('<div class="card red">Not Fit</div>', unsafe_allow_html=True)

# ======================
# STRATEGY
# ======================
st.markdown('<div class="arrow">⬇️</div>', unsafe_allow_html=True)

st.markdown('<div class="card purple">Strategy Session</div>', unsafe_allow_html=True)

st.markdown('<div class="card blue">Offer Presented</div>', unsafe_allow_html=True)

# ======================
# CLOSING
# ======================
st.markdown('<div class="arrow">⬇️</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

col1.markdown('<div class="card green">Closed Won 🎉</div>', unsafe_allow_html=True)
col2.markdown('<div class="card orange">Stalled</div>', unsafe_allow_html=True)
col3.markdown('<div class="card red">Lost</div>', unsafe_allow_html=True)

# ======================
# DELIVERY
# ======================
st.markdown('<div class="arrow">⬇️</div>', unsafe_allow_html=True)

st.markdown('<div class="card blue">Onboarding</div>', unsafe_allow_html=True)
st.markdown('<div class="card green">Service Delivery</div>', unsafe_allow_html=True)

# ======================
# GROWTH
# ======================
st.markdown('<div class="arrow">⬇️</div>', unsafe_allow_html=True)

st.markdown('<div class="card purple">Reporting & Growth</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

col1.markdown('<div class="card green">Upsell</div>', unsafe_allow_html=True)
col2.markdown('<div class="card green">Scale</div>', unsafe_allow_html=True)
col3.markdown('<div class="card red">Churn Risk</div>', unsafe_allow_html=True)
