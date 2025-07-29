# Wosh FC Analyzer App (Inspired by FIFA Gameplay Style)

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# ---------- Sidebar Navigation ----------
with st.sidebar:
    st.title("Wosh FC Dashboard")
    section = st.radio("Navigate", [
        "Home", "Player Profiles", "Training & Drills", "Match Analysis", "Tactical Board", "Video Module", "Game Statistics"
    ])

# ---------- Placeholder Player Data ----------
players_data = {
    "Under 7": ["Player A", "Player B"],
    "Under 10": ["Player C", "Player D"],
    "Under 12": ["Player E", "Player F"],
    "Under 14": ["Munene", "Sammy"],
    "Under 16": ["Player G", "Player H"]
}

# ---------- Section: Home ----------
if section == "Home":
    st.title("🏆 Wosh FC: From the Streets to the Stars")
    st.write("Welcome to the official Wosh FC Dashboard. Track player performance, manage training, analyze matches, and more.")

# ---------- Section: Player Profiles ----------
elif section == "Player Profiles":
    st.title("📋 Player Profiles")
    age_group = st.selectbox("Select Age Group", list(players_data.keys()))
    selected_player = st.selectbox("Select Player", players_data[age_group])

    st.subheader(f"{selected_player} - Profile Overview")
    st.write("**Position:** Midfielder")
    st.write("**Captain:** Yes" if selected_player == "Munene" else "**Captain:** No")

    st.write("**Dream/Ambition:** Become a professional footballer.")
    st.write("**Strengths:** Speed, Vision, Passing")
    st.write("**Areas of Improvement:** Shooting, Stamina")

    st.subheader("📊 Player Development Graph")
    fig = px.line(
        pd.DataFrame({
            "Date": pd.date_range(start="2025-01-01", periods=6, freq="M"),
            "Rating": [68, 70, 72, 74, 75, 77]
        }),
        x="Date", y="Rating", title=f"Progression for {selected_player}"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📝 Coach Remarks")
    st.text_area("Remarks", placeholder="Enter notes about player's attitude, form, and development...")

# ---------- Section: Training & Drills ----------
elif section == "Training & Drills":
    st.title("⚽ Training Sessions & Drills")
    st.write("Organize tactical training by age group:")
    group = st.selectbox("Select Age Group", list(players_data.keys()))
    st.text_area("Drills for Today", placeholder="e.g., 1v1, Passing Triangle, High-Pressing Game")
    st.text_area("Objectives", placeholder="e.g., Improve reaction speed, master off-the-ball movement")

# ---------- Section: Match Analysis ----------
elif section == "Match Analysis":
    st.title("📈 Match Analysis")
    match_name = st.text_input("Match Title")
    st.text_area("Coach Comments", placeholder="Summarize the team's performance and areas to improve")

# ---------- Section: Tactical Board ----------
elif section == "Tactical Board":
    st.title("📌 Tactical Board")
    st.write("(Future Feature) Drag and Drop Tactical Tool – coming soon!")

# ---------- Section: Video Module ----------
elif section == "Video Module":
    st.title("🎥 Match Footage + Notes")
    uploaded_video = st.file_uploader("Upload Match Video", type=["mp4", "mov"])
    if uploaded_video:
        st.video(uploaded_video)
        st.text_area("Timestamp Notes", placeholder="e.g., 12:34 – Excellent pressing by midfield.")

# ---------- Section: Game Statistics ----------
elif section == "Game Statistics":
    st.title("📊 Full Match Stats")

    st.subheader("Team Stats")
    team_stats = {
        "Possession (%)": 62,
        "Attempts on Goal": 14,
        "Total Attempts": 20,
        "Saves": 5,
        "Corners": 7,
        "Offsides": 2,
        "Distance Covered (KM)": 96,
        "Passes Completed": 480,
        "Fouls Committed": 11
    }
    st.table(pd.DataFrame.from_dict(team_stats, orient='index', columns=['Value']))

    st.subheader("📈 Individual Player Stats")
    selected_stat_player = st.selectbox("Select Player for Stats", players_data["Under 14"])
    player_stats = {
        "Match Rating": 7.5,
        "Distance Covered": "10.2 KM",
        "Passes Made": 48,
        "Shots on Target": 3,
        "Fouls Committed": 1,
        "Assists": 1,
        "Goals": 1
    }
    st.table(pd.DataFrame.from_dict(player_stats, orient='index', columns=['Value']))

    st.subheader("🔥 Heatmap / Movement")
    st.image("https://raw.githubusercontent.com/Joshr-cell/assets/main/heatmap_sample.png", caption="Sample Heatmap")

    st.subheader("🧠 Coach Rating Input")
    st.slider("Rate Player Performance", 1, 10, 7)
    st.text_area("Coach Match Remarks", placeholder="Enter remarks specific to this player's performance.")


