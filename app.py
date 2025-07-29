import streamlit as st
import pandas as pd

# Example Wosh FC player data
players = [
    {
        "name": "Zekiah Roy", "position": "Midfielder", "rating": 89,
        "speed": 85, "shooting": 78, "passing": 90, "defense": 76,
        "image": "https://i.imgur.com/E7hQzJF.png"
    },
    {
        "name": "Telo", "position": "Striker", "rating": 91,
        "speed": 92, "shooting": 89, "passing": 70, "defense": 60,
        "image": "https://i.imgur.com/MOonDdN.png"
    },
    {
        "name": "Zekiah Eli", "position": "Defender", "rating": 84,
        "speed": 78, "shooting": 65, "passing": 82, "defense": 88,
        "image": "https://i.imgur.com/yVm22tW.png"
    }
]

st.set_page_config(page_title="Wosh FC - FIFA Player Cards", layout="wide")
st.title("⚽ Wosh FC Squad - FIFA Style Cards")

cols = st.columns(3)

for i, player in enumerate(players):
    with cols[i % 3]:
        st.image(player["image"], width=150)
        st.subheader(player["name"])
        st.text(f"Position: {player['position']}")
        st.markdown(f"**Rating: {player['rating']}**")
        st.progress(player["rating"])
        st.text(f"Speed: {player['speed']}")
        st.text(f"Shooting: {player['shooting']}")
        st.text(f"Passing: {player['passing']}")
        st.text(f"Defense: {player['defense']}")
