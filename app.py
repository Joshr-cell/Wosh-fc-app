import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Wosh FC Dashboard", layout="wide")
st.markdown("""
    <style>
        body {font-family: 'Segoe UI', sans-serif;}
        .stApp {background-color: #f8f9fa;}
        .big-font {font-size: 26px !important; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
with st.sidebar:
    selected = option_menu("Wosh FC Menu", [
        "Home", "Players", "Training Drills", "Match Analysis", "Tactical Board", "Video Analysis"
    ], icons=['house', 'people', 'activity', 'bar-chart', 'map', 'camera-video'], menu_icon="cast", default_index=0)

# --- Data ---
team_structure = {
    "Under 7": 12,
    "Under 10": 12,
    "Under 12": 12,
    "Under 14": 12,
    "Under 16": 7
}

players = [
    {"name": "Munene", "team": "Under 14", "strength": 80, "ambition": 90, "area_of_improvement": "Passing", "coach_remarks": "Very disciplined."},
    {"name": "Byron", "team": "Under 14", "strength": 75, "ambition": 85, "area_of_improvement": "Tackling", "coach_remarks": "Shows improvement weekly."},
    {"name": "Victor", "team": "Under 14", "strength": 72, "ambition": 88, "area_of_improvement": "Positioning", "coach_remarks": "Needs confidence."},
]

# --- Home Page ---
if selected == "Home":
    st.title("🏠 Welcome to Wosh FC")
    st.markdown("""
    This dashboard supports coaching, analysis, and player development across these age groups:
    - Under 7 (12 players)
    - Under 10 (12 players)
    - Under 12 (12 players)
    - Under 14 (12 players)
    - Under 16 (7 players)
    
    Explore profiles, upload drills, break down stats and visualize match dynamics.
    """)

# --- Player Profiles ---
elif selected == "Players":
    st.title("👥 Player Profiles")
    for player in players:
        with st.expander(player['name']):
            st.write(f"**Team:** {player['team']}")
            st.write(f"**Strength:** {player['strength']}")
            st.write(f"**Ambition:** {player['ambition']}")
            st.write(f"**Area of Improvement:** {player['area_of_improvement']}")
            st.write(f"**Coach's Remarks:** {player['coach_remarks']}")

            # Radar Chart for player
            radar = go.Figure()
            radar.add_trace(go.Scatterpolar(
                r=[player['strength'], player['ambition'], 100],
                theta=['Strength', 'Ambition', 'Max'],
                fill='toself',
                name=player['name']
            ))
            radar.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                showlegend=False,
                height=350
            )
            st.plotly_chart(radar, use_container_width=True)

# --- Training Drills ---
elif selected == "Training Drills":
    st.title("🏋️‍♂️ Training Drills")
    uploaded_file = st.file_uploader("Upload Drill Image or Video")
    description = st.text_area("Drill Description")
    if uploaded_file and description:
        st.success("Drill uploaded successfully!")
        if uploaded_file.name.endswith('.mp4'):
            st.video(uploaded_file)
        else:
            st.image(uploaded_file)
        st.write(description)

# --- Match Analysis ---
elif selected == "Match Analysis":
    st.title("📊 Match Analysis")
    col1, col2, col3 = st.columns(3)
    with col1:
        possession = st.slider("Possession %", 0, 100, 50)
        attempts = st.number_input("Attempts on Goal", 0)
    with col2:
        corners = st.number_input("Corners", 0)
        fouls = st.number_input("Fouls Committed", 0)
    with col3:
        distance = st.number_input("Avg Distance Covered (km)", 0.0)
        passes = st.number_input("Passes Completed", 0)

    if st.button("Analyze Match"):
        st.success("Match stats analyzed.")
        st.metric("Possession", f"{possession}%")
        st.metric("Attempts", attempts)
        st.metric("Passes", passes)
        st.metric("Distance (km)", distance)
        st.metric("Fouls", fouls)

# --- Tactical Board ---
elif selected == "Tactical Board":
    st.title("📌 Tactical Board")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Football_pitch_metric.svg/2560px-Football_pitch_metric.svg.png", caption="Tactical Field")
    st.info("Interactive tactical features coming soon.")

# --- Video Analysis ---
elif selected == "Video Analysis":
    st.title("🎥 Video Analysis")
    video = st.file_uploader("Upload Match or Training Video")
    notes = st.text_area("Coach's Notes")
    if video:
        st.video(video)
    if notes:
        st.write("**Coach Notes:**")
        st.write(notes)






