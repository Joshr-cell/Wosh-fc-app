import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# Logo & Title
st.sidebar.image("wosh_fc_logo.png", use_column_width=True)
st.sidebar.markdown("⚽ **Wosh FC Tactical Hub**")
st.sidebar.markdown("---")

# Main Title
st.markdown("""
    <style>
        .main-title {
            font-size: 40px;
            color: #00C1D4;
            font-weight: bold;
            text-align: center;
        }
    </style>
    <p class="main-title">Wosh FC Performance Analyzer</p>
""", unsafe_allow_html=True)

# Sample data
data = {
    'Player': ['Branton', 'Ian', 'Pasi', 'Samson', 'Ole'],
    'Distance Covered (km)': [7.2, 6.5, 8.1, 7.8, 6.9],
    'Pass Accuracy (%)': [85, 78, 90, 82, 76],
    'Possession (%)': [60, 52, 65, 58, 50],
    'Shots on Target': [4, 2, 5, 3, 1],
    'Goals': [1, 0, 2, 1, 0]
}
df = pd.DataFrame(data)

# Tabs for different analysis
tab1, tab2, tab3 = st.tabs(["📊 Team Overview", "📈 Player Stats", "📅 Match Summary"])

with tab1:
    st.subheader("Team Summary")
    st.dataframe(df, use_container_width=True)

    st.markdown("### Average Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Distance", f"{df['Distance Covered (km)'].mean():.2f} km")
    col2.metric("Avg Pass Accuracy", f"{df['Pass Accuracy (%)'].mean():.1f}%")
    col3.metric("Avg Possession", f"{df['Possession (%)'].mean():.1f}%")

with tab2:
    st.subheader("Player Comparison")

    player_select = st.selectbox("Select Player", df['Player'].unique())
    player_data = df[df['Player'] == player_select].iloc[0]

    st.markdown(f"### Stats for **{player_select}**")

    st.metric("Distance Covered", f"{player_data['Distance Covered (km)']} km")
    st.metric("Pass Accuracy", f"{player_data['Pass Accuracy (%)']}%")
    st.metric("Possession", f"{player_data['Possession (%)']}%")
    st.metric("Shots on Target", player_data['Shots on Target'])
    st.metric("Goals", player_data['Goals'])

    # Visual chart for the player
    chart_data = {
        "Metric": ["Distance", "Pass Accuracy", "Possession", "Shots", "Goals"],
        "Value": [
            player_data['Distance Covered (km)'],
            player_data['Pass Accuracy (%)'],
            player_data['Possession (%)'],
            player_data['Shots on Target'],
            player_data['Goals']
        ]
    }
    chart_df = pd.DataFrame(chart_data)
    fig = px.bar(chart_df, x='Metric', y='Value', title=f"{player_select}'s Stats", color='Metric')
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Match Summary")
    st.write("Upload match performance data or summarize key highlights here.")
    st.file_uploader("Upload CSV (Match Data)", type="csv")

# Footer
st.markdown("---")
st.markdown("© 2025 Wosh FC – From The Streets To The Stars ✨")


