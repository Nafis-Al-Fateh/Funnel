import streamlit as st
from graphviz import Digraph

st.set_page_config(page_title="Sales Funnel Flowchart", layout="wide")

st.title("🚀 Sales Funnel Flowchart")

# Create flowchart
dot = Digraph()
dot.attr(rankdir='TB', size='8,12')

# ======================
# STYLES
# ======================
dot.attr('node', shape='box', style='filled', fontname="Helvetica")

# Lead Gen
dot.node('LinkedIn', 'LinkedIn', fillcolor='#E3F2FD')
dot.node('Ads', 'Paid Ads', fillcolor='#E3F2FD')
dot.node('Email', 'Email Outreach', fillcolor='#E3F2FD')
dot.node('SEO', 'Website / SEO', fillcolor='#E3F2FD')
dot.node('Referral', 'Referrals', fillcolor='#E3F2FD')

# Capture
dot.node('Capture', 'Lead Captured', fillcolor='#F3E5F5')
dot.node('Qualify', 'Qualification\n(Budget • Need • Authority)', fillcolor='#F3E5F5')

# Qualification Outcomes
dot.node('HighFit', 'High Fit', fillcolor='#E8F5E9')
dot.node('MedFit', 'Medium Fit', fillcolor='#E3F2FD')
dot.node('LowFit', 'Low Fit', fillcolor='#FFEBEE')

# Discovery
dot.node('Discovery', 'Discovery Call', fillcolor='#E3F2FD')
dot.node('GoodFit', 'Good Fit', fillcolor='#E8F5E9')
dot.node('Maybe', 'Maybe', fillcolor='#FFF3E0')
dot.node('NotFit', 'Not Fit', fillcolor='#FFEBEE')

# Strategy
dot.node('Strategy', 'Strategy Session', fillcolor='#F3E5F5')
dot.node('Offer', 'Present Offer', fillcolor='#E3F2FD')

# Closing
dot.node('ClosedWon', 'Closed Won 🎉', fillcolor='#E8F5E9')
dot.node('Stalled', 'Stalled', fillcolor='#FFF3E0')
dot.node('Lost', 'Lost', fillcolor='#FFEBEE')

# Onboarding
dot.node('Onboarding', 'Onboarding', fillcolor='#E3F2FD')

# Delivery
dot.node('Delivery', 'Service Delivery', fillcolor='#E8F5E9')

# Reporting
dot.node('Reporting', 'Reporting & Growth', fillcolor='#F3E5F5')

# ======================
# EDGES (ARROWS)
# ======================

# Lead sources → capture
for source in ['LinkedIn', 'Ads', 'Email', 'SEO', 'Referral']:
    dot.edge(source, 'Capture')

dot.edge('Capture', 'Qualify')

# Qualification branching
dot.edge('Qualify', 'HighFit')
dot.edge('Qualify', 'MedFit')
dot.edge('Qualify', 'LowFit')

# High + Medium → Discovery
dot.edge('HighFit', 'Discovery')
dot.edge('MedFit', 'Discovery')

# Low fit exit
dot.edge('LowFit', 'NotFit')

# Discovery outcomes
dot.edge('Discovery', 'GoodFit')
dot.edge('Discovery', 'Maybe')
dot.edge('Discovery', 'NotFit')

# Good fit → Strategy
dot.edge('GoodFit', 'Strategy')

# Maybe → nurture loop
dot.edge('Maybe', 'Discovery')

# Strategy → Offer → Closing
dot.edge('Strategy', 'Offer')
dot.edge('Offer', 'ClosedWon')
dot.edge('Offer', 'Stalled')
dot.edge('Offer', 'Lost')

# Closed → Onboarding → Delivery → Reporting
dot.edge('ClosedWon', 'Onboarding')
dot.edge('Onboarding', 'Delivery')
dot.edge('Delivery', 'Reporting')

# ======================
# RENDER
# ======================
st.graphviz_chart(dot)
