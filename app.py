import streamlit as st
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

# --- Streamlit Config ---
st.set_page_config(page_title="Wosh FC Dashboard", layout="wide")

# --- Dark Theme Styling ---
st.markdown("""
    <style>
        html, body, [class*="css"] {
            background-color: #0e1117;
            color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
        }
        .stApp {
            background-color: #0e1117;
        }
        .st-bc, .st-c4, .stButton>button {
            background-color: #222222;
            color: white;
        }
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: #f9fafb;
        }
        .css-1v3fvcr {
            background-color: #1e222a;
        }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
with st.sidebar:
    selected = option_menu("Wosh FC Menu", [
        "Home", "Players", "Training Drills", "Match Analysis", "Tactical Board", "Video Analysis"
    ], icons=['house', 'people', 'activity', 'bar-chart', 'map', 'camera-video'], menu_icon="cast", default_index=0)

# --- Data ---
team_structure = {
    "Under 7": [],
    "Under 10": [],
    "Under 12": [],
    "Under 14": [],
    "Under 16": []
}

# --- Home ---
if selected == "Home":
    st.title("🏠 Welcome to Wosh FC")
    st.markdown("Manage training, tactics, and performance across all age groups.")
    for team, players in team_structure.items():
        st.markdown(f"### {team} — {len(players)} Players")

# --- Players ---
elif selected == "Players":
    st.title("👥 Player Profiles by Category")

    for team in team_structure:
        with st.expander(f"{team} — {len(team_structure[team])} players", expanded=False):
            with st.form(f"add_player_form_{team}"):
                st.subheader(f"➕ Add Player to {team}")
                name = st.text_input("Name", key=f"name_{team}")
                strength = st.slider("Strength", 0, 100, 50, key=f"strength_{team}")
                ambition = st.slider("Ambition", 0, 100, 50, key=f"ambition_{team}")
                improvement = st.text_input("Area of Improvement", key=f"improve_{team}")
                remarks = st.text_area("Coach's Remarks", key=f"remarks_{team}")
                submitted = st.form_submit_button("Add Player")
                if submitted and name:
                    new_player = {
                        "name": name,
                        "team": team,
                        "strength": strength,
                        "ambition": ambition,
                        "area_of_improvement": improvement,
                        "coach_remarks": remarks
                    }
                    team_structure[team].append(new_player)
                    st.success(f"{name} added to {team}.")

            if team_structure[team]:
                for player in team_structure[team]:
                    with st.expander(f"🧍‍♂️ {player['name']}"):
                        st.write(f"**Team:** {player['team']}")
                        st.write(f"**Strength:** {player['strength']}")
                        st.write(f"**Ambition:** {player['ambition']}")
                        st.write(f"**Area of Improvement:** {player['area_of_improvement']}")
                        st.write(f"**Coach's Remarks:** {player['coach_remarks']}")

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
                            height=300,
                            paper_bgcolor="#0e1117",
                            font_color="#ffffff"
                        )
                        st.plotly_chart(radar, use_container_width=True)

                        st.markdown("#### 📊 Match Analysis")
                        col1, col2 = st.columns(2)
                        with col1:
                            goals = st.number_input(f"{player['name']} - Goals", 0, key=f"goals_{player['name']}")
                            assists = st.number_input(f"{player['name']} - Assists", 0, key=f"assists_{player['name']}")
                        with col2:
                            distance = st.number_input(f"{player['name']} - Distance Covered (km)", 0.0, key=f"dist_{player['name']}")
                            passes = st.number_input(f"{player['name']} - Passes Completed", 0, key=f"passes_{player['name']}")
                        st.success(f"Stats recorded for {player['name']}.")

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
    st.markdown("### 💡 Formation Strategy")
    formation = st.text_input("Enter Team Formation (e.g., 4-3-3, 4-4-2):")
    if formation:
        st.success(f"📋 Current Formation: {formation}")
    st.info("Interactive drawing tools coming soon!")

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
