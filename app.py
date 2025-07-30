import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="Wosh FC Analyzer", layout="wide")

# Title
st.title("Wosh FC Analyzer App")

# Sidebar Filters
st.sidebar.header("Filter Player Data")

# Sample player data
data = {
    'Name': ['Ian', 'Willy', 'Sammy', 'Branton', 'Samson', 'Pasi', 'Ole', 'Byron', 'Munene', 'Victor', 'Mose', 'Jamo'],
    'Age': [13, 14, 14, 13, 12, 14, 13, 13, 14, 12, 13, 14],
    'Position': ['Forward', 'Midfielder', 'Defender', 'Midfielder', 'Goalkeeper', 'Forward', 'Defender', 'Forward', 'Defender', 'Midfielder', 'Midfielder', 'Forward'],
    'Speed': [7.5, 8.0, 7.2, 6.5, 6.0, 8.5, 7.0, 8.3, 7.4, 6.9, 6.8, 8.1],
    'Stamina': [8.0, 7.5, 7.2, 6.8, 7.0, 8.2, 7.5, 8.3, 7.0, 6.7, 7.1, 8.0],
    'Goals': [10, 4, 1, 3, 0, 8, 2, 7, 0, 1, 2, 9]
}

df = pd.DataFrame(data)




