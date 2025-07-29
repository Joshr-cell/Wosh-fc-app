import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# --- Set page config ---
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# --- Header ---
st.title("⚽ Wosh FC Analyzer App")
st.markdown("Analyze, Train, and Improve Players from U7 to U16")

# --- Sidebar Navigation ---
menu = st.sidebar.radio("Navigation", [
    "Home", "Players", "Training Drills", "Match Analysis", "Tactical Board", "Video Analysis"
])

# --- Data ---
team_structure = {
    "Under 7": 12,
    "Under 10": 12,
    "Under 12": 12,
    "Under 14": 12,
    "Under 16": 7
}

# --- Sample Players Data ---
players = [
    {"name": "Munene", "team": "Under 14", "strength": 80, "ambition": 90, "area_of_improvement": "Passing", "coach_remarks": "Very disciplined."},
    {"name": "Byron", "team": "Under 14", "strength": 75, "ambition": 85, "area_of_improvement": "Tackling", "coach_remarks": "Shows improvement weekly."},
    {"name": "Victor", "team": "Under 14", "strength": 72, "ambition": 88, "area_of_improvement": "Positioning", "coach_remarks": "Needs confidence."},
]

# --- Home Page ---
if menu == "Home":
    st.subheader("🏠 Welcome to Wosh FC")
    st.markdown("""
    This app is designed to monitor, evaluate, and manage players across various age groups:
    - Under 7 (12 players)
    - Under 10 (12 players)
    - Under 12 (12 players)
    - Under 14 (12 players)
    - Under 16 (7 players)
    """)

# --- Player Profiles ---
elif menu == "Players":
    st.subheader("👥 Player Profiles")
    for player in players:
        with st.expander(player['name']):
            st.write(f"**Team:** {player['team']}")
            st.write(f"**Strength:** {player['strength']}")
            st.write(f"**Ambition:** {player['ambition']}")
            st.write(f"**Area of Improvement:** {player['area_of_improvement']}")
            st.write(f"**Coach's Remarks:** {player['coach_remarks']}")

            # Plot individual performance chart
            df = pd.DataFrame({
                'Metric': ['Strength', 'Ambition'],
                'Value': [player['strength'], player['ambition']]
            })
            fig = px.bar(df, x='Metric', y='Value', title=f"Performance for {player['name']}")
            st.plotly_chart(fig)

            # Placeholder for stats
            st.markdown("### Match Stats")
            st.write("Possession: 65%")
            st.write("Attempts on Goal: 4")
            st.write("Distance Covered: 6.5 km")
            st.write("Passes Completed: 32")
            st.write("Fouls Committed: 1")
            st.write("Heatmap: Coming soon 🔥")

# --- Training Drills ---
elif menu == "Training Drills":
    st.subheader("🏋️‍♂️ Training Drills")
    uploaded_file = st.file_uploader("Upload Drill Image/Video")
    description = st.text_area("Describe the Drill")
    if uploaded_file and description:
        st.success("Drill uploaded successfully!")
        st.video(uploaded_file) if uploaded_file.name.endswith('.mp4') else st.image(uploaded_file)
        st.write(description)

# --- Match Analysis ---
elif menu == "Match Analysis":
    st.subheader("📊 Match Analysis")
    st.markdown("Upload match stats and get analysis.")
    possession = st.slider("Possession %", 0, 100, 50)
    attempts = st.number_input("Attempts on Goal", 0)
    corners = st.number_input("Corners", 0)
    fouls = st.number_input("Fouls Committed", 0)
    distance = st.number_input("Average Distance Covered (km)", 0.0)
    passes = st.number_input("Passes Completed", 0)

    if st.button("Analyze"):
        st.success("Match stats analyzed.")
        st.write("Possession vs Opponent: ", possession, "%")
        st.write("Attempts: ", attempts)
        st.write("Corners: ", corners)
        st.write("Fouls: ", fouls)
        st.write("Distance Covered: ", distance, "km")
        st.write("Passes Completed: ", passes)

# --- Tactical Board ---
elif menu == "Tactical Board":
    st.subheader("📌 Tactical Board")
    st.markdown("(Drag-and-drop tactical board simulation coming soon)")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Football_pitch_metric.svg/2560px-Football_pitch_metric.svg.png", caption="Tactical Pad")

# --- Video Analysis ---
elif menu == "Video Analysis":
    st.subheader("🎥 Video Module")
    video = st.file_uploader("Upload Match or Training Video")
    notes = st.text_area("Coach Notes")
    if video:
        st.video(video)
    if notes:
        st.write("**Coach Notes:**")
        st.write(notes)

