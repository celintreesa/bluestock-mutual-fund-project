import streamlit as st

st.set_page_config(page_title="Bluestock MF Dashboard", layout="wide")

st.title("Bluestock Mutual Fund Analytics Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Investment", "₹4 Billion")

with col2:
    st.metric("Total Investors", "5,000")

st.subheader("Project Overview")

st.write("""
This dashboard provides insights into:
- Fund Performance
- Investor Analytics
- SIP & Market Trends
- Advanced Mutual Fund Analytics
""")