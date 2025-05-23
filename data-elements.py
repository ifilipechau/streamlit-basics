
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

# Static Table
st.subheader("Static Table")
st.table(df) # Display the dataframe as a static table

# Metrics
st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df)) # Display the number of rows in the dataframe
st.metric(label="Average Age", value=round(df['Age'].mean(), 2)) # Display the average age of the people in the dataframe

# JSON and Dict Display
st.subheader("JSON and Dictionary Display")
sample_dict = {
    "name": "John",
    "age": 30,
    "skills": ["Python", "Streamlit", "Data Science"]
}
st.json(sample_dict) # Display the dictionary as JSON

# Display a dictionary with a different format
st.write("Dictionary Display:", sample_dict)