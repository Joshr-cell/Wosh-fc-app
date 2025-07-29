import streamlit as st
import pandas as pd
from PIL import Image
# Main Title
st.title("⚽ Wosh FC Analyzer – Tactical Planner & Drill Tracker")

# Section: Team Roster
st.subheader("📋 Team Roster")
team_data = pd.DataFrame({
    "Player Name": ["Ian", "Willy", "Sammy", "Branton", "Samson", "Pasi", "Ole", "Byron", "Munene", "Victor", "Mose", "Jamo"],
    "Position": ["Forward", "Midfielder", "Goalkeeper", "Defender", "Midfielder", "Forward", "Defender", "Goalkeeper", "Midfielder", "Forward", "Defender", "Midfielder"],
    "Strength": ["Speed", "Stamina", "Reflexes", "Tackling", "Vision", "Finishing", "Tackling", "Agility", "Passing", "Dribbling", "Marking", "Passing"],
    "Ambition": ["Top Scorer", "Team Captain", "National Team", "Defensive Wall", "Playmaker", "Striker", "Reliable Defender", "Safe Hands", "Assist Master", "Flair Player", "No Entry Zone", "Field General"]
})
st.dataframe(team_data, use_container_width=True)

# Section: Tactical Planner (drawing pad)
st.subheader("🧠 Tactical Drawing Board")
st.markdown("Use this board to draw your strategies. Take screenshots for saving.")

# Tactical drawing image or placeholder
canvas_placeholder = st.empty()
st.info("👉 Drawing tools will be added in a future update.")

# Section: Training Drills
st.subheader("🏃‍♂️ Training Drills")
drills = [
    {"Drill": "1v1 Pressure", "Focus": "Defending", "Duration": "10 min"},
    {"Drill": "Passing Triangles", "Focus": "Passing", "Duration": "15 min"},
    {"Drill": "Shooting Circuit", "Focus": "Finishing", "Duration": "20 min"},
    {"Drill": "Fitness Ladder", "Focus": "Stamina", "Duration": "10 min"},
]
drills_df = pd.DataFrame(drills)
st.table(drills_df)

# Footer
st.markdown("---")
st.caption("Wosh FC Academy – From the Streets to the Stars ✨")

