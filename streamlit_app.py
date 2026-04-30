import streamlit as st

st.set_page_config(layout="wide")

# ======================
# STYLE
# ======================
st.markdown("""
<style>

.stApp {
    background: #f8fafc;
    font-family: Inter, sans-serif;
}

.wrapper {
    max-width: 1100px;
    margin: auto;
    position: relative;
}

.row {
    display: flex;
    justify-content: center;
    gap: 12px;
    margin: 10px 0;
    flex-wrap: wrap;
}

.box {
    padding: 10px 14px;
    border-radius: 10px;
    font-size: 13px;
    text-align: center;
    border: 2px solid;
    background: white;
    min-width: 160px;
}

/* Colors */
.blue { border-color: #60a5fa; background:#eff6ff; }
.purple { border-color: #a78bfa; background:#f5f3ff; }
.green { border-color: #86efac; background:#f0fdf4; }
.orange { border-color: #fdba74; background:#fff7ed; }
.red { border-color: #fca5a5; background:#fef2f2; }

/* Arrows */
.arrow {
    text-align:center;
    font-size:26px;
    margin:10px 0;
    color:#64748b;
}

.h-arrow {
    font-size:20px;
    display:flex;
    align-items:center;
    color:#94a3b8;
}

/* Section text */
.section {
    text-align:center;
    font-size:13px;
    color:#64748b;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ======================
# WRAPPER + SVG LAYER
# ======================
st.markdown("""
<div class="wrapper">

<svg width="100%" height="2600" style="
position:absolute;
top:0;
left:0;
pointer-events:none;
z-index:0;
">

<!-- Main vertical -->
<path d="M550 120 C550 180, 550 180, 550 240" stroke="#94a3b8" stroke-width="2" fill="none"/>
<path d="M550 240 C550 300, 550 300, 550 360" stroke="#94a3b8" stroke-width="2" fill="none"/>

<!-- Qualification split -->
<path d="M550 360 C400 420, 300 420, 250 480" stroke="#94a3b8" stroke-width="2" fill="none"/>
<path d="M550 360 C550 420, 550 420, 550 480" stroke="#94a3b8" stroke-width="2" fill="none"/>
<path d="M550 360 C700 420, 800 420, 850 480" stroke="#94a3b8" stroke-width="2" fill="none"/>

<!-- Back -->
<path d="M250 520 C350 580, 450 600, 550 640" stroke="#94a3b8" stroke-width="2" fill="none"/>
<path d="M850 520 C750 580, 650 600, 550 640" stroke="#94a3b8" stroke-width="2" fill="none"/>

<!-- Discovery split -->
<path d="M550 760 C400 820, 300 820, 250 880" stroke="#94a3b8" stroke-width="2" fill="none"/>
<path d="M550 760 C550 820, 550 820, 550 880" stroke="#94a3b8" stroke-width="2" fill="none"/>
<path d="M550 760 C700 820, 800 820, 850 880" stroke="#94a3b8" stroke-width="2" fill="none"/>

<!-- Closing split -->
<path d="M550 1100 C400 1160, 300 1160, 250 1220" stroke="#94a3b8" stroke-width="2" fill="none"/>
<path d="M550 1100 C550 1160, 550 1160, 550 1220" stroke="#94a3b8" stroke-width="2" fill="none"/>
<path d="M550 1100 C700 1160, 800 1160, 850 1220" stroke="#94a3b8" stroke-width="2" fill="none"/>

</svg>

<div style="position:relative; z-index:1;">
""", unsafe_allow_html=True)

# ======================
# TOP CHANNELS
# ======================
st.markdown("""
<div class="row">
<div class="box purple">LinkedIn</div>
<div class="box purple">Paid ads</div>
<div class="box purple">Email outreach</div>
<div class="box purple">Website / SEO</div>
<div class="box purple">Referrals / partners</div>
<div class="box blue">Postcode business search</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="arrow">⬇️</div>', unsafe_allow_html=True)

# ======================
# LEAD CAPTURE
# ======================
st.markdown("""
<div class="row">
<div class="box purple">Lead captured (lead magnet / landing page)</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="arrow">⬇️</div>', unsafe_allow_html=True)

# ======================
# QUALIFICATION
# ======================
st.markdown("""
<div class="row">
<div class="box purple">Quick qualification filter<br>Budget, need, authority – eliminate mismatch</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="arrow">⬇️</div>', unsafe_allow_html=True)

# ======================
# SPLIT
# ======================
st.markdown("""
<div class="row">
<div class="box green">High fit<br>A — Ideal client</div>
<div class="h-arrow">→</div>
<div class="box blue">Medium fit<br>B — Maybe, nurture</div>
<div class="h-arrow">→</div>
<div class="box red">Low fit<br>C — not a fit / not active</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="arrow">⬇️</div>', unsafe_allow_html=True)

# ======================
# BOOK CALL
# ======================
st.markdown("""
<div class="row">
<div class="box blue">Book discovery call</div>
<div class="box orange">Nurture sequence<br>7–30day email + SMS cadence</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section">2 — Discovery call (45–60m)</div>', unsafe_allow_html=True)

# ======================
# DISCOVERY
# ======================
st.markdown("""
<div class="row">
<div class="box blue">Discovery call<br>Understand goals, challenges, current situation</div>
</div>
""", unsafe_allow_html=True)

# RESULT
st.markdown("""
<div class="row">
<div class="box blue">Maybe<br>Needs more info</div>
<div class="h-arrow">→</div>
<div class="box green">Good fit<br>Hot budget + need</div>
<div class="h-arrow">→</div>
<div class="box red">Not a fit<br>No budget / wrong fit</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="row">
<div class="box blue">Send case studies<br>Testimonial + paid POV</div>
<div class="box red">CRM tag + nurture<br>Reconnect in 30 days</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section">3 — Strategy session (paid) (30–60m)</div>', unsafe_allow_html=True)

# ======================
# STRATEGY
# ======================
st.markdown("""
<div class="row">
<div class="box purple">Paid growth strategy session<br>Marketing audit delivery + growth roadmap</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="row">
<div class="box purple">Present opportunities + growth roadmap</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="row">
<div class="box green">Free trial offer (optional close tool)<br>2-week sample content + ad creative</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="row">
<div class="box blue">Present 3 packages (starter / growth / scale)</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="row">
<div class="box blue">Objection handling + final question</div>
</div>
""", unsafe_allow_html=True)

# ======================
# CLOSING
# ======================
st.markdown("""
<div class="row">
<div class="box red">Hard no<br>CRM tag (valid) ⌀</div>
<div class="h-arrow">→</div>
<div class="box green">Deal closed — contract + payment</div>
<div class="h-arrow">→</div>
<div class="box orange">Stalled deal<br>Follow up D+7, D+14</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section">4 — Onboarding & kick-off</div>', unsafe_allow_html=True)

# ======================
# ONBOARDING
# ======================
st.markdown("""
<div class="row">
<div class="box blue">Onboarding kickoff call<br>Welcome, align expectation, set KPIs</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="row">
<div class="box blue">Collect assets + access<br>Branding, ad accounts, social logins, website</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="row">
<div class="box blue">Define KPIs + 90-day growth roadmap</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section">5 — Delivery (ongoing paid team workstream)</div>', unsafe_allow_html=True)

# ======================
# DELIVERY
# ======================
st.markdown("""
<div class="row">
<div class="box purple">Marketing<br>Ads, content, analytics</div>
<div class="box green">Design team<br>Creative, branding</div>
<div class="box green">Video team<br>Reels, edits</div>
<div class="box orange">Dev team<br>Website, tech, tracking</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="row">
<div class="box purple">Ad management</div>
<div class="box green">Ad creatives</div>
<div class="box green">Video ads</div>
<div class="box orange">Build + landing pages</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="row">
<div class="box purple">Analytics + reports</div>
<div class="box green">Ongoing creative</div>
<div class="box green">Editing + optimize</div>
<div class="box orange">Tracking + CRM setup</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="row">
<div class="box green">Content published + ads live<br>All assets live weekly output – reaching audience</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section">6 — Reporting & growth engine</div>', unsafe_allow_html=True)

# ======================
# REPORTING
# ======================
st.markdown("""
<div class="row">
<div class="box purple">Monthly reporting call<br>Results, insights, ROI, next steps</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="row">
<div class="box purple">Review performance + ROI</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="row">
<div class="box green">Upsell / cross-sell</div>
<div class="box green">Optimize + scale</div>
<div class="box orange">At-risk client</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="row">
<div class="box green">Happy client referral request</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="row">
<div class="box green">Google review + warm referral intro</div>
</div>
""", unsafe_allow_html=True)

# CLOSE WRAPPER
st.markdown('</div></div>', unsafe_allow_html=True)
