import streamlit as st
import plotly.express as px
import pandas as pd
import requests

# Base URL of the API
API_BASE_URL = "http://localhost:8080"

# Page 1: Dashboard
st.title("Li-ion Cell Dashboard")

# Calculate State of Health (SoH) for each cell
soh_5308 = (2992.02 / 3000) * 100
soh_5329 = (2822.56 / 3000) * 100

# Sidebar selection
selected_page = st.sidebar.selectbox("Select Page", ["Dashboard", "Cell ID 5308", "Cell ID 5329"], key="page_selector")

# Page 1: Dashboard with two pie charts
if selected_page == "Dashboard":
    col1, col2 = st.columns(2)

    with col1:
        fig = px.pie(names=['SoH', 'Remaining'], values=[soh_5308, 100-soh_5308], title="State of Health - Cell 5308")
        st.plotly_chart(fig)

    with col2:
        fig = px.pie(names=['SoH', 'Remaining'], values=[soh_5329, 100-soh_5329], title="State of Health - Cell 5329")
        st.plotly_chart(fig)

# Page 2: Cell ID 5308 Data
elif selected_page == "Cell ID 5308":
    st.header("Cell ID 5308 Data")
    response = requests.get(f"{API_BASE_URL}/data/5308")
    data_5308 = response.json()

    if data_5308:
        # Convert the JSON response into a DataFrame
        df_5308 = pd.DataFrame(data_5308)
        
        # Current Data
        fig = px.line(df_5308, x='time', y='current', title="Current Data - Cell 5308")
        st.plotly_chart(fig)

        # Voltage Data
        fig = px.line(df_5308, x='time', y='voltage', title="Voltage Data - Cell 5308")
        st.plotly_chart(fig)

        # Capacity Data
        fig = px.line(df_5308, x='time', y='capacity', title="Capacity Data - Cell 5308")
        st.plotly_chart(fig)

        # Temperature Data
        fig = px.line(df_5308, x='time', y='temperature', title="Temperature Data - Cell 5308")
        st.plotly_chart(fig)

# Page 3: Cell ID 5329 Data
elif selected_page == "Cell ID 5329":
    st.header("Cell ID 5329 Data")
    response = requests.get(f"{API_BASE_URL}/data/5329")
    data_5329 = response.json()

    if data_5329:
        # Convert the JSON response into a DataFrame
        df_5329 = pd.DataFrame(data_5329)

        # Current Data
        fig = px.line(df_5329, x='time', y='current', title="Current Data - Cell 5329")
        st.plotly_chart(fig)

        # Voltage Data
        fig = px.line(df_5329, x='time', y='voltage', title="Voltage Data - Cell 5329")
        st.plotly_chart(fig)

        # Capacity Data
        fig = px.line(df_5329, x='time', y='capacity', title="Capacity Data - Cell 5329")
        st.plotly_chart(fig)

        # Temperature Data
        fig = px.line(df_5329, x='time', y='temperature', title="Temperature Data - Cell 5329")
        st.plotly_chart(fig)
