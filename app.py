import streamlit as st
from streamlit_option_menu import option_menu

# App configuration
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# Apply black background and white text using custom CSS
st.markdown("""
    <style>
        body, .stApp {
            background-color: black !important;
            color: white !important;
        }
        .stSidebar, .css-1d391kg, .css-1v3fvcr, .css-1dp5vir {
            background-color: #111 !important;
        }
        .css-18e3th9 {
            background-color: black;
        }
        .st-bc, .st-c4, .stButton>button {
            background-color: #333;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
selected = option_menu(
    menu_title="Wosh FC App",
    options=["Dashboard", "Players", "Analytics", "About"],
    icons=["bar-chart", "people", "graph-up", "info-circle"],
    menu_icon="cast",
    default_index=0,
    orientation="vertical"
)

# Page logic
if selected == "Dashboard":
    st.title("📊 Wosh FC Dashboard")
    st.write("Welcome to the official Wosh FC Analyzer App. Select an option from the left to get started.")

elif selected == "Players":
    st.title("⚽ Player Profiles")
    st.write("Here you can view or add player data.")
    # Sample data – editable later
    sample_players = [
        {"Name": "Zekiah Roy", "Position": "Forward", "Strength": "Leadership"},
        {"Name": "Telo", "Position": "Midfielder", "Strength": "Courage"},
        {"Name": "Mungai Theuri", "Position": "Goalkeeper", "Strength": "Potential"}
    ]
    for player in sample_players:
        st.subheader(player["Name"])
        st.write(f"**Position:** {player['Position']}")
        st.write(f"**Strength:** {player['Strength']}")
        st.markdown("---")

elif selected == "Analytics":
    st.title("📈 Team Analytics")
    st.write("Charts and performance data will be added here.")

elif selected == "About":
    st.title("ℹ️ About Wosh FC")
    st.write("Wosh FC is dedicated to empowering youth from the streets through football. This app helps track their progress and manage player data.")







