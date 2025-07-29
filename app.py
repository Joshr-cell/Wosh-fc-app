import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

st.title("⚽ Wosh FC Analyzer")
st.subheader("From the Streets to the Stars")

# === Player Card Display ===
st.header("🎮 Player Profiles (FIFA Style)")

players = [
    {"Name": "Ian", "Position": "Striker", "Traits": "Fast, Brave", "Ambition": "Top Scorer"},
    {"Name": "Willy", "Position": "Midfielder", "Traits": "Tactical, Calm", "Ambition": "Playmaker"},
    {"Name": "Sammy", "Position": "Defender", "Traits": "Strong, Composed", "Ambition": "Wall of Defense"},
    {"Name": "Branton", "Position": "Winger", "Traits": "Speedy, Technical", "Ambition": "Assist King"},
    {"Name": "Samson", "Position": "Goalkeeper", "Traits": "Tall, Alert", "Ambition": "Clean Sheet Leader"},
    {"Name": "Pasi", "Position": "Striker", "Traits": "Accurate, Sharp", "Ambition": "Top Finisher"},
    {"Name": "Ole", "Position": "Midfielder", "Traits": "Creative, Balanced", "Ambition": "Engine Room"},
    {"Name": "Byron", "Position": "Defender", "Traits": "Tough, No Nonsense", "Ambition": "Captain"},
    {"Name": "Munene", "Position": "Winger", "Traits": "Dribbler, Vision", "Ambition": "Pro Contract"},
    {"Name": "Victor", "Position": "Midfielder", "Traits": "Vision, Control", "Ambition": "National Team"},
    {"Name": "Mose", "Position": "Goalkeeper", "Traits": "Diving, Reflex", "Ambition": "Elite Keeper"},
    {"Name": "Jamo", "Position": "Striker", "Traits": "Agile, Finisher", "Ambition": "Golden Boot"},
]

cols = st.columns(3)
for i, player in enumerate(players):
    with cols[i % 3]:
        st.markdown(f"**{player['Name']}**")
        st.markdown(f"🧍 Position: *{player['Position']}*")
        st.markdown(f"🎯 Traits: *{player['Traits']}*")
        st.markdown(f"🚀 Ambition: *{player['Ambition']}*")
        st.markdown("---")

# === Match Analysis ===
st.header("📋 Match Performance Form")

with st.form("match_form"):
    col1, col2 = st.columns(2)
    with col1:
        opponent = st.text_input("Opponent Team")
        match_date = st.date_input("Match Date", datetime.today())
        goals_for = st.number_input("Goals Scored by Wosh FC", 0)
    with col2:
        goals_against = st.number_input("Goals Conceded", 0)
        mvp = st.text_input("Player of the Match")
        notes = st.text_area("Coach's Match Notes")

    submit_match = st.form_submit_button("Submit Match Report")

if submit_match:
    st.success(f"✅ Match vs {opponent} on {match_date} submitted!")
    st.info(f"Score: {goals_for} - {goals_against} | MVP: {mvp}")
    st.write(f"📝 Notes: {notes}")

# === Video Upload ===
st.header("🎥 Video Upload & Coach Comments")
video = st.file_uploader("Upload a training/match clip", type=["mp4", "mov", "avi"])
comment = st.text_area("Coach's Notes for Video")

if video:
    st.video(video)
    st.success("Video uploaded. Review with players.")
    if comment:
        st.markdown(f"🧠 Coach's Feedback: *{comment}*")

# === Tactical Board ===
st.header("⚽ Tactical Notes Board")
formation = st.selectbox("Preferred Formation", ["4-4-2", "4-3-3", "3-5-2", "Custom"])
tactic_notes = st.text_area("Tactical Plan or Adjustments")

if st.button("Save Tactical Plan"):
    st.success(f"Tactical plan ({formation}) saved.")
    st.write(f"📋 Plan: {tactic_notes}")

# === Report Summary ===
st.header("📄 Report Preview")
if submit_match:
    st.subheader("📊 Match Summary")
    st.markdown(f"- **Opponent:** {opponent}")
    st.markdown(f"- **Date:** {match_date}")
    st.markdown(f"- **Result:** {goals_for} - {goals_against}")
    st.markdown(f"- **MVP:** {mvp}")
    st.markdown(f"- **Notes:** {notes}")
