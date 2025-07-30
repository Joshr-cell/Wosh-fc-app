import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# Sidebar logo
st.sidebar.image("A_digital_graphic_features_the_branding_for_WOSH_.png", use_column_width=True)

st.title("🏆 Wosh FC Player Analyzer")
st.markdown("From the Streets to the Stars — Analyzing Player Data for Impact & Growth.")

# Sample data (replace with real one later)
data = pd.DataFrame({
    'Name': ['Sammy', 'Byron', 'Ian', 'Victor'],
    'Distance Covered (km)': [8.5, 7.2, 9.1, 6.7],
    'Pass Accuracy (%)': [85, 76, 90, 70],
    'Shots on Target': [3, 1, 4, 2]
})

st.subheader("📊 Team Performance Overview")
col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(data, x='Name', y='Distance Covered (km)', color='Name', title="Distance Covered by Players")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.pie(data, names='Name', values='Pass Accuracy (%)', title="Pass Accuracy Distribution")
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("⚽ Individual Stats")
selected_player = st.selectbox("Select a player", data['Name'])

player_stats = data[data['Name'] == selected_player]
st.write(player_stats)

st.markdown("---")
st.markdown("🔍 *Data Powered by Waves of Street Hope*")



