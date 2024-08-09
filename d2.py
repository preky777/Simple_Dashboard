import streamlit as st
import pandas as pd
import plotly.express as px

# Load Excel files
file_5308 = pd.ExcelFile('5308.xls')
file_5329 = pd.ExcelFile('5329.xls')

def create_cell_page(cell_id, excel_file):
    data_sheet = excel_file.parse(sheet_name='Detail_67_3_5')
    temperature_sheet = excel_file.parse(sheet_name='DetailTemp_67_3_5')

    # Extract data
    time_data = data_sheet.iloc[:, 10]
    current_data = data_sheet.iloc[:, 5]
    voltage_data = data_sheet.iloc[:, 6]
    capacity_data = data_sheet.iloc[:, 7]
    temperature_data = temperature_sheet.iloc[:, 4]

    # Create charts
    fig_current = px.line(x=time_data, y=current_data, title='Current vs Time')
    fig_voltage = px.line(x=time_data, y=voltage_data, title='Voltage vs Time')
    fig_capacity = px.line(x=time_data, y=capacity_data, title='Capacity vs Time')
    fig_temperature = px.line(x=time_data, y=temperature_data, title='Temperature vs Time')

    # Display charts
    st.subheader(f'Cell ID: {cell_id}')
    
    st.plotly_chart(fig_current)
    st.plotly_chart(fig_voltage)
    st.plotly_chart(fig_capacity)
    st.plotly_chart(fig_temperature)

# Create pages for each cell
st.sidebar.title('Navigation')
page = st.sidebar.selectbox("Select Page", ["Dashboard", "Cell 5308", "Cell 5329"])

if page == "Dashboard":
    # Call the Dashboard code (as shown in the first section)
    pass
elif page == "Cell 5308":
    create_cell_page(5308, file_5308)
elif page == "Cell 5329":
    create_cell_page(5329, file_5329)
