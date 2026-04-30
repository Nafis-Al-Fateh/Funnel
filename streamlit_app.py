import streamlit as st
import requests
import pandas as pd
import os

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Sales Funnel CRM", layout="wide")

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
DATABASE_ID = os.getenv("NOTION_DB_ID")

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

STAGES = [
    "Lead",
    "Qualified",
    "Discovery",
    "Strategy",
    "Closed Won",
    "Closed Lost",
]

# =========================
# NOTION FUNCTIONS
# =========================
def get_leads():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    res = requests.post(url, headers=HEADERS)

    data = res.json().get("results", [])

    leads = []
    for item in data:
        try:
            name = item["properties"]["Name"]["title"][0]["plain_text"]
        except:
            name = "Unnamed"

        stage = item["properties"]["Stage"]["select"]["name"]

        leads.append({
            "id": item["id"],
            "name": name,
            "stage": stage
        })

    return pd.DataFrame(leads)


def create_lead(name, stage):
    url = "https://api.notion.com/v1/pages"

    payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Name": {
                "title": [{"text": {"content": name}}]
            },
            "Stage": {
                "select": {"name": stage}
            }
        }
    }

    requests.post(url, headers=HEADERS, json=payload)


def update_stage(page_id, new_stage):
    url = f"https://api.notion.com/v1/pages/{page_id}"

    payload = {
        "properties": {
            "Stage": {
                "select": {"name": new_stage}
            }
        }
    }

    requests.patch(url, headers=HEADERS, json=payload)


# =========================
# UI HEADER
# =========================
st.title("🚀 Sales Funnel CRM Dashboard")

# =========================
# ADD LEAD
# =========================
with st.expander("➕ Add New Lead"):
    name = st.text_input("Lead Name")
    stage = st.selectbox("Stage", STAGES)

    if st.button("Create Lead"):
        if name:
            create_lead(name, stage)
            st.success("Lead Created!")
            st.rerun()
        else:
            st.error("Enter a name")

# =========================
# LOAD DATA
# =========================
df = get_leads()

if df.empty:
    st.warning("No leads found")
    st.stop()

# =========================
# METRICS
# =========================
st.subheader("📊 Funnel Metrics")

metrics = df["stage"].value_counts().to_dict()

cols = st.columns(len(STAGES))

for i, stage in enumerate(STAGES):
    cols[i].metric(stage, metrics.get(stage, 0))

# Conversion rates
def conversion(a, b):
    return round((b / a) * 100, 1) if a else 0

lead = metrics.get("Lead", 0)
qualified = metrics.get("Qualified", 0)
discovery = metrics.get("Discovery", 0)
closed = metrics.get("Closed Won", 0)

st.write("### Conversion Rates")
st.write(f"Lead → Qualified: {conversion(lead, qualified)}%")
st.write(f"Qualified → Discovery: {conversion(qualified, discovery)}%")
st.write(f"Discovery → Closed: {conversion(discovery, closed)}%")

# =========================
# PIPELINE (KANBAN STYLE)
# =========================
st.subheader("🧩 Pipeline View")

cols = st.columns(len(STAGES))

for i, stage in enumerate(STAGES):
    with cols[i]:
        st.markdown(f"### {stage}")

        stage_df = df[df["stage"] == stage]

        for _, row in stage_df.iterrows():
            with st.container():
                st.markdown(f"**{row['name']}**")

                new_stage = st.selectbox(
                    "Move to",
                    STAGES,
                    index=STAGES.index(stage),
                    key=row["id"]
                )

                if new_stage != stage:
                    if st.button("Update", key=row["id"] + "_btn"):
                        update_stage(row["id"], new_stage)
                        st.rerun()

                st.markdown("---")

# =========================
# TABLE VIEW
# =========================
st.subheader("📋 All Leads")

st.dataframe(df, use_container_width=True)
