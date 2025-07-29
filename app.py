import streamlit as st
import plotly.express as px
from PIL import Image
import pandas as pd

st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

st.title("⚽ Wosh FC Analyzer App")
st.markdown("---")

# Sidebar Navigation
page = st.sidebar.selectbox("Select Section", [
    "Team Overview",
    "Player Profiles",
    "Training Drills",
    "Tactical Board",
    "Video Analysis",
    "Match Analysis"
])

# Player Data (Organized by Age Group)
team_structure = {
    "Under 7": 12,
    "Under 10": 12,
    "Under 12": 12,
    "Under 14": 12,
    "Under 15": 7
}

# Sample player database for demonstration
players = [
    {"name": "Munene", "age_group": "Under 14", "strength": "Speed", "ambition": "Play for Kenya", "improvement": "Passing", "rating": 8.2, "distance": 7.5, "passes": 45, "coach_note": "Strong mentality."},
    # Add more player entries here for each group
]

# Team Overview Section
if page == "Team Overview":
    st.header("👥 Team Structure")
    for group, count in team_structure.items():
        st.write(f"**{group}**: {count} players")

# Player Profiles Section
elif page == "Player Profiles":
    st.header("📋 Player Profiles")
    for player in players:
        st.subheader(player["name"])
        st.write(f"**Age Group:** {player['age_group']}")
        st.write(f"**Strength:** {player['strength']}")
        st.write(f"**Ambition:** {player['ambition']}")
        st.write(f"**Area of Improvement:** {player['improvement']}")
        st.write(f"**Coach's Remark:** {player['coach_note']}")

        fig = px.bar(
            x=["Rating", "Distance (km)", "Passes Completed"],
            y=[player['rating'], player['distance'], player['passes']],
            labels={'x': 'Metric', 'y': 'Value'},
            title=f"Performance Graph for {player['name']}"
        )
        st.plotly_chart(fig)

# Training Drills
elif page == "Training Drills":
    st.header("🏋️ Training & Drills")
    st.write("Upload training drills, describe th

