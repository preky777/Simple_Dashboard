import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Database connection
engine = create_engine('mysql+pymysql://root:rp#$9882@localhost/li_ion_dashboard')

# Load data from database
def load_data(cell_id):
    query = f"SELECT * FROM cell_data WHERE cell_id={cell_id}"
    df = pd.read_sql(query, con=engine)
    return df

# Calculate SoH
def calculate_soh(discharge_capacity, nominal_capacity=3000):
    return (discharge_capacity / nominal_capacity) * 100

# Streamlit App
st.title("Li-Ion Dashboard")

# Page 1: Overview
st.header("State of Health (SoH)")

# SoH for 5308 and 5329
soh_5308 = calculate_soh(2992.02)
soh_5329 = calculate_soh(2822.56)

# Pie charts
st.subheader("SoH for Cell 5308")
st.write(f"SoH: {soh_5308:.2f}%")
st.subheader("SoH for Cell 5329")
st.write(f"SoH: {soh_5329:.2f}%")

# Page 2: Cell-specific data
st.header("Cell Data")
cell_id = st.selectbox("Select Cell ID", [5308, 5329])

# Load data for the selected cell
df = load_data(cell_id)

# Display graphs
st.subheader(f"Current vs Time for Cell {cell_id}")
st.line_chart(df[['time', 'current']].set_index('time'))

st.subheader(f"Voltage vs Time for Cell {cell_id}")
st.line_chart(df[['time', 'voltage']].set_index('time'))

st.subheader(f"Capacity vs Time for Cell {cell_id}")
st.line_chart(df[['time', 'capacity']].set_index('time'))

st.subheader(f"Temperature vs Time for Cell {cell_id}")
st.line_chart(df[['time', 'temperature']].set_index('time'))