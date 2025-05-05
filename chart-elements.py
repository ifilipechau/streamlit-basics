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
