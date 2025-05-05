
import streamlit as st
import pandas as pd

# Set the title of the app
st.title("Data Elements in Streamlit")

# Dataframe creation
st.subheader("Dataframe Example")
df = pd.DataFrame({ 
    'Name': ['Micas', 'Anselmo', 'Lorenzo', 'Charlie', 'Ester'],
    'Age': [23, 45, 43, 28, 56],
    'Occupation': ['Engineer', 'Doctor', 'Artist', 'Teacher', 'Phylosopher']
})
st.dataframe(df) # Display the dataframe with a scrollbar

# Data Editor, edits the dataframe in place
st.subheader("Dataframe Editor")
editable_df = st.data_editor(df)