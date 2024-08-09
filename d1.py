import streamlit as st
import pandas as pd
import plotly.express as px

# Calculate SoH
soh_5308 = (2992.02 / 3000) * 100
soh_5329 = (2822.56 / 3000) * 100

# Data for pie charts
data = {
    'Cell ID': ['5308', '5329'],
    'SoH (%)': [soh_5308, soh_5329],
    'Remaining (%)': [100 - soh_5308, 100 - soh_5329]
}

df = pd.DataFrame(data)

# Create pie charts
fig_5308 = px.pie(df, values='SoH (%)', names='Cell ID', title=f'Cell ID 5308 SoH: {soh_5308:.2f}%')
fig_5329 = px.pie(df, values='SoH (%)', names='Cell ID', title=f'Cell ID 5329 SoH: {soh_5329:.2f}%')

# Display pie charts
st.title('Dashboard')
st.subheader('State of Health (SoH) Overview')

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_5308)
with col2:
    st.plotly_chart(fig_5329)
