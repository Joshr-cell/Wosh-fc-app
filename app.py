# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

st.title("⚽ Wosh FC Player Analyzer Dashboard")

# Sidebar navigation
menu = st.sidebar.radio("Navigation", [
    "Overview", "Players", "Training Drills", "Match Analysis", "Tactical Board", "Video Module"
])

# Dummy player data setup (replace with Firebase or database later)
players = {
    "Under 7": [{"Name": f"Player U7-{i+1}", "Captain": (i==0), "Strength": 65+i, "Ambition": 70+i, "Improvement": 50+i} for i in range(35)],
    "Under 10": [{"Name": f"Player U10-{i+1}", "Captain": (i==0), "Strength": 67+i, "Ambition": 72+i, "Improvement": 52+i} for i in range(35)],
    "Under 12": [{"Name": f"Player U12-{i+1}", "Captain": (i==0), "Strength": 69+i, "Ambition": 74+i, "Improvement": 54+i} for i in range(35)],
    "Under 14": [{"Name": f"Player U14-{i+1}", "Captain": (i==0), "Strength": 71+i, "Ambition": 76+i, "Improvement": 56+i} for i in range(35)],
    "Under 16": [{"Name": f"Player U16-{i+1}", "Captain": (i==0), "Strength": 73+i, "Ambition": 78+i, "Improvement": 58+i} for i in range(35)],
}

if menu == "Overview":
    st.subheader("🏟️ Our Playing Style")
    st.markdown("""
        - Possession-based play
        - High pressing
        - Quick transitions
        - Development focused
    """)

    st.subheader("📈 General Team Stats")
    age_group = st.selectbox("Choose Age Group", list(players.keys()))
    df = pd.DataFrame(players[age_group])
    fig = px.line(df, x="Name", y="Improvement", title=f"Improvement Graph: {age_group}")
    st.plotly_chart(fig, use_container_width=True)

elif menu == "Players":
    st.subheader("🧍‍♂️ Player Profiles")
    group = st.selectbox("Age Group", list(players.keys()))
    df = pd.DataFrame(players[group])
    for index, row in df.iterrows():
        with st.expander(f"{row['Name']} {'🌟 (Captain)' if row['Captain'] else ''}"):
            st.write(f"**Strength:** {row['Strength']}")
            st.write(f"**Ambition:** {row['Ambition']}")
            st.write(f"**Area of Improvement:** {row['Improvement']}")
            st.progress(int(row['Improvement']))

elif menu == "Training Drills":
    st.subheader("🏋️ Training Drills")
    st.markdown("""
    - **Drill 1:** Passing Circuit
    - **Drill 2:** Shooting Accuracy
    - **Drill 3:** 1v1 Duel Mastery
    - **Drill 4:** Tactical Position Play
    """)

elif menu == "Match Analysis":
    st.subheader("📊 Match Analysis")
    match_date = st.date_input("Match Date")
    opponent = st.text_input("Opponent")
    notes = st.text_area("Match Notes")
    rating = st.slider("Team Performance Rating", 0, 10)
    if st.button("Save Analysis"):
        st.success("Analysis Saved!")

elif menu == "Tactical Board":
    st.subheader("📋 Tactical Board (Concept)")
    st.info("Drag-and-drop functionality to be added. Currently under development.")
    st.image("https://tacticalpad.com/images/screens/tacticalpad1.png", caption="Sample Tactical Board")

elif menu == "Video Module":
    st.subheader("🎥 Video Module")
    video_file = st.file_uploader("Upload Match or Training Video", type=["mp4", "mov"])
    if video_file:
        st.video(video_file)
        notes = st.text_area("Add Time-Stamped Notes Below")
        if st.button("Save Notes"):
            st.success("Notes Saved!")

