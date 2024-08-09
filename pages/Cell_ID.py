import streamlit as st
import plotly.express as px
import pandas as pd
import requests

# Base URL of the API
API_BASE_URL = "http://localhost:8051"

# Sidebar selection
selected_page = st.sidebar.selectbox("Select Cell ID", ["5308", "5329"], key="main_page_selector")

# Function to create and display graphs
def display_graphs(df, cell_id):
    # Define the columns layout with equal width
    col1, col2 = st.columns([1, 1])  # Equal width columns

    # Define the chart height
    chart_height = 400  # Adjust height as needed

    # Display Current Data and Voltage Data in the first row
    with col1:
        fig = px.line(df, x='time', y='current', title=f"Current Data - Cell {cell_id}")
        st.plotly_chart(fig, use_container_width=True, height=chart_height)

    with col2:
        fig = px.line(df, x='time', y='voltage', title=f"Voltage Data - Cell {cell_id}")
        st.plotly_chart(fig, use_container_width=True, height=chart_height)

    # Define the second row for Capacity Data and Temperature Data
    col1, col2 = st.columns([1, 1])  # Equal width columns

    with col1:
        fig = px.line(df, x='time', y='capacity', title=f"Capacity Data - Cell {cell_id}")
        st.plotly_chart(fig, use_container_width=True, height=chart_height)

    with col2:
        fig = px.line(df, x='time', y='temperature', title=f"Temperature Data - Cell {cell_id}")
        st.plotly_chart(fig, use_container_width=True, height=chart_height)

# Page 1: Dashboard with two pie charts
if selected_page == "5308":
    st.title("Cell ID 5308")
    response = requests.get(f"{API_BASE_URL}/data/5308")
    data_5308 = response.json()

    if data_5308:
        # Convert the JSON response into a DataFrame
        df_5308 = pd.DataFrame(data_5308)
        display_graphs(df_5308, "5308")

# Page 2: Cell Data with Dropdown
elif selected_page == "5329":
    st.title("Cell ID 5329")
    response = requests.get(f"{API_BASE_URL}/data/5329")
    data_5329 = response.json()

    if data_5329:
        # Convert the JSON response into a DataFrame
        df_5329 = pd.DataFrame(data_5329)
        display_graphs(df_5329, "5329")
