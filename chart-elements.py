# import the necessary libraries

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# set the title of the app
st.title("Chart elements in Streamlit: ")

# Generate some random data for the charts
chart_data = pd.Dataframe(
    np.random.randn(20,3),
    columns=['X','Y','Z']
)

# Area chart 
st.subheader("Area Chart")
st.area_chart(chart_data)

# Bar Chart
st.subheader("Bar Chart")
st.bar_chart(chart_data)

# Line Chart
st.subheader("Line Chart")
st.line_chart(chart_data)

# Map Chart (display a map with random data)
st.subheader("Map Chart")
map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50,50] + [37.76, -122.4],
    columns=['lat','lon']
)
st.map(map_data)

# Scatter chart (using matplotlib)
st.subheader("Scatter Chart")
scatter_data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})
st.scatter_chart(scatter_data)

# Pyplot chart
st.subheader("Pyplot Chart")
fig, ax = plt.subplots()
ax.plot(chart_data['X'], label='X')
ax.plot(chart_data['Y'], label='Y')
ax.plot(chart_data['Z'], label='Z')
ax.set_title('Pyplot Chart')
ax.legend()
st.pyplot(fig)