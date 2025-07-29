import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# Title
st.title("Wosh FC Analyzer")
st.subheader("From the Streets to the Stars ⭐")

# Team structure
team_structure = {
    "Under 7": 12,
    "Under 10": 12,
    "Under 12": 12,
    "Under 14": 12,
    "Under 16": 7
}

# Sidebar navigation
section = st.sidebar.selectbox("Navigate", [
    "Club Overview", "Players", "Training & Drills", 
    "Match Analysis", "Tactical Board", "Video Module"
])

# Club Overview
if section == "Club Overview":
    st.header("Wosh FC Teams")
    for team, count in team_structure.items():
        st.write(f"**{team}**: {count} players")

    st.markdown("### Playing Style")
    st.write("""
        Wosh FC emphasizes possession-based play, quick passing, 
        and positional discipline inspired by top European academies.
    """)

# Players Section
elif section == "Players":
    st.header("Player Database")

    player_name = st.selectbox("Select Player", [
        "Munene", "Ian", "Willy", "Sammy", "Branton", "Samson", 
        "Pasi", "Ole", "Byron", "Victor", "Mose", "Jamo"
    ])

    st.subheader(f"Profile: {player_name}")
    st.text("Captain: Yes" if player_name == "Munene" else "Captain: No")

    strength = st.text_area("Strength")
    ambition = st.text_area("Ambition")
    improvement = st.text_area("Area of Improvement")

    st.markdown("### Coach's Remarks")
    st.text_area("Remarks")

    st.markdown("### FIFA-style Graphs")
    data = {
        "Attribute": ["Pace", "Shooting", "Passing", "Dribbling", "Defending", "Physical"],
        "Rating": [82, 75, 78, 80, 70, 85]
    }
    df = pd.DataFrame(data)
    fig = px.bar(df, x="Attribute", y="Rating", title=f"{player_name}'s Abilities")
    st.plotly_chart(fig)

# Training and Drills
elif section == "Training & Drills":
    st.header("Training Drills")
    st.write("Upload training drills, describe them, and tag by age group.")
    
    uploaded = st.file_uploader("Upload Drill PDF/Image")
    description = st.text_area("Drill Description")
    age_group = st.selectbox("Age Group", list(team_structure.keys()))

# Match Analysis
elif section == "Match Analysis":
    st.header("Match Stats")
    match = st.text_input("Match Title")
    
    st.subheader("Team Stats")
    stats = {
        "Possession (%)": 60,
        "Attempts on Goal": 12,
        "Total Attempts": 15,
        "Saves": 4,
        "Corners": 5,
        "Offsides": 2,
        "Distance Covered (km)": 98,
        "Passes Completed": 480,
        "Fouls Committed": 10
    }
    stats_df = pd.DataFrame(stats.items(), columns=["Metric", "Value"])
    st.table(stats_df)

    st.subheader("Player Ratings & Stats")
    players = ["Munene", "Ian", "Willy", "Sammy", "Victor"]
    for player in players


