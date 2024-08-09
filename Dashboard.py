import streamlit as st
import plotly.express as px
import pandas as pd
import requests

# Base URL of the API
API_BASE_URL = "http://localhost:8051"

st.title("Li-ion Cell Dashboard SOH")

# Calculate State of Health (SoH) for each cell
soh_5308 = (2992.02 / 3000) * 100
soh_5329 = (2822.56 / 3000) * 100

# Create columns with a spacer between them
col1, spacer, col2 = st.columns([2, 1, 2])

with col1:
    fig = px.pie(names=['SoH', 'Remaining'], values=[soh_5308, 100-soh_5308], title="State of Health - Cell 5308")
    st.plotly_chart(fig)

with col2:
    fig = px.pie(names=['SoH', 'Remaining'], values=[soh_5329, 100-soh_5329], title="State of Health - Cell 5329")
    st.plotly_chart(fig)