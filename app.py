import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

# --- Page config ---
st.set_page_config(page_title="Wosh FC Dashboard", layout="wide")

# --- Main App Header ---
st.markdown("""
    <style>
        .main-title {
            font-size:48px;
            font-weight:700;
            color:#1f77b4;
        }
        .subtext {
            font-size:20px;
            color:gray;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>⚽ Wosh FC Analyzer</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Analyze, Train, and Improve Players from U7 to U16</div><br>", unsafe_allow_html=True)

# --- Sidebar Navigation ---
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "Players", "Training", "Match Analysis", "Tactical Board", "Video Review"],
        icons=["house", "people", "activity", "bar-chart", "clipboard", "camera-video"],
        menu_icon="cast", default_index=0)

# --- Sample Player Data ---
players = [
    {"name": "Munene", "team": "Under 14", "strength": 80, "ambition": 90, "area_of_improvement": "Passing", "coach_remarks": "Very disciplined."},
    {"name": "Byron", "team": "Under 14", "strength": 75, "ambition": 85, "area_of_improvement": "Tackling", "coach_remarks": "Shows improvement weekly."},
    {"name": "Victor", "team": "Under 14", "strength": 72, "ambition": 88, "area_of_improvement": "Positioning", "coach_remarks": "Needs confidence."},
]

# --- HOME ---
if selected == "Home":
    st.subheader("Welcome to Wosh FC")
    st.info("""
        This dashboard helps monitor and manage:
        - Players across U7 to U16 age groups
        - Tactical and match analysis
        - Video sessions and performance tracking
    """)

# --- PLAYER PROFILES ---
elif selected == "Players":
    st.subheader("👥 Player Profiles")
    col1, col2 = st.columns(2)
    for i, player in enumerate(players):
        with (col1 if i % 2 == 0 else col2):
            with st.expander(player['name'], expanded=False):
                st.write(f"**Team:** {player['team']}")
                st.write(f"**Area of Improvement:** {player['area_of_improvement']}")
                st.write(f"**Coach Remarks:** {player['coach_remarks']}")

                fig = go.Figure()
                fig.add_trace(go.Scatterpolar(
                    r=[player['strength'], player['ambition'], player['strength']],
                    theta=['Strength','Ambition','Strength'],
                    fill='toself',
                    name=player['name']
                ))
                fig.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=False)
                st.plotly_chart(fig, use_container_width=True)

                st.markdown("### Match Stats")
                st.write("- Possession: 65%")
                st.write("- Attempts on Goal: 4")
                st.write("- Distance Covered: 6.5 km")
                st.write("- Passes Completed: 32")
                st.write("- Fouls Committed: 1")

# --- TRAINING DRILLS ---
elif selected == "Training":
    st.subheader("🏋️ Training Module")
    uploaded_file = st.file_uploader("Upload Drill Image or Video")
    description = st.text_area("Describe the Drill")
    if uploaded_file and description:
        st.success("Drill uploaded successfully!")
        st.video(uploaded_file) if uploaded_file.name.endswith('.mp4') else st.image(uploaded_file, use_column_width=True)
        st.markdown(f"**Description:** {description}")

# --- MATCH ANALYSIS ---
elif selected == "Match Analysis":
    st.subheader("📊 Match Stats Analysis")
    possession = st.slider("Possession %", 0, 100, 50)
    attempts = st.number_input("Attempts on Goal", 0)
    corners = st.number_input("Corners", 0)
    fouls = st.number_input("Fouls", 0)
    distance = st.number_input("Avg Distance Covered (km)", 0.0)
    passes = st.number_input("Passes Completed", 0)

    if st.button("Analyze Match"):
        st.success("Analysis Complete")
        st.metric("Possession", f"{possession}%")
        st.metric("Attempts", attempts)
        st.metric("Corners", corners)
        st.metric("Fouls", fouls)
        st.metric("Distance Covered", f"{distance} km")
        st.metric("Passes", passes)

# --- TACTICAL BOARD ---
elif selected == "Tactical Board":
    st.subheader("📌 Tactical Board")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Football_pitch_metric.svg/2560px-Football_pitch_metric.svg.png", caption="Tactical Field")
    st.warning("Drag-and-drop tactical simulation coming soon.")

# --- VIDEO MODULE ---
elif selected == "Video Review":
    st.subheader("🎥 Video Analysis")
    video = st.file_uploader("Upload Match or Training Video")
    notes = st.text_area("Coach Notes")
    if video:
        st.video(video)
    if notes:
        st.markdown("**Coach Notes:**")
        st.write(notes)





