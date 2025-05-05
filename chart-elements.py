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
