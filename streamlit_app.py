import streamlit as st

st.set_page_config(page_title="Sales Funnel", layout="wide")

st.title("📊 Sales Funnel Dashboard")

st.markdown("---")

# Sidebar navigation
stage = st.sidebar.radio(
    "Select Funnel Stage",
    [
        "Lead Generation",
        "Qualification",
        "Discovery Call",
        "Strategy & Offer",
        "Closing",
        "Onboarding",
        "Delivery",
        "Reporting & Growth"
    ]
)

# Stage content
if stage == "Lead Generation":
    st.header("1. Lead Generation Engine")
    st.write("Channels:")
    st.button("LinkedIn")
    st.button("Paid Ads")
    st.button("Email Outreach")
    st.button("Website / SEO")
    st.button("Referrals / Partners")

elif stage == "Qualification":
    st.header("2. Qualification Filter")
    budget = st.selectbox("Budget", ["Low", "Medium", "High"])
    need = st.selectbox("Need", ["Weak", "Moderate", "Strong"])
    authority = st.selectbox("Authority", ["No", "Partial", "Yes"])

    if budget == "High" and need == "Strong" and authority == "Yes":
        st.success("High Fit (Ideal Client)")
    elif budget == "Medium":
        st.warning("Medium Fit (Nurture)")
    else:
        st.error("Low Fit (Not a match)")

elif stage == "Discovery Call":
    st.header("3. Discovery Call")
    st.text_area("Client Goals")
    st.text_area("Challenges")
    st.text_area("Current Situation")

    decision = st.radio("Outcome", ["Good Fit", "Maybe", "Not a Fit"])

    if decision == "Good Fit":
        st.success("Proceed to Strategy Session")
    elif decision == "Maybe":
        st.info("Send Case Studies")
    else:
        st.error("Add to CRM Nurture")

elif stage == "Strategy & Offer":
    st.header("4. Strategy Session")
    st.write("Deliverables:")
    st.checkbox("Marketing Audit")
    st.checkbox("Growth Roadmap")

    st.subheader("Offer")
    package = st.selectbox("Select Package", ["Starter", "Growth", "Scale"])
    st.write(f"Selected: {package}")

elif stage == "Closing":
    st.header("5. Closing")
    decision = st.radio("Deal Status", ["Closed", "Stalled", "Lost"])

    if decision == "Closed":
        st.success("Contract Signed & Payment Received")
    elif decision == "Stalled":
        st.warning("Follow up in 7-14 days")
    else:
        st.error("Mark as Lost in CRM")

elif stage == "Onboarding":
    st.header("6. Onboarding")
    st.checkbox("Kickoff Call Completed")
    st.checkbox("Assets Collected")
    st.checkbox("KPIs Defined")

elif stage == "Delivery":
    st.header("7. Delivery")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.subheader("Marketing")
        st.write("Ads, Analytics")

    with col2:
        st.subheader("Design")
        st.write("Creatives, Branding")

    with col3:
        st.subheader("Video")
        st.write("Reels, Edits")

    with col4:
        st.subheader("Development")
        st.write("Website, Tracking")

elif stage == "Reporting & Growth":
    st.header("8. Reporting & Growth")
    st.write("Monthly Reporting")

    roi = st.slider("ROI", 0, 300, 100)

    if roi > 150:
        st.success("Scale Campaign")
    elif roi > 80:
        st.info("Optimize")
    else:
        st.error("At Risk Client")

st.markdown("---")
st.caption("Interactive funnel visualization built with Streamlit")
