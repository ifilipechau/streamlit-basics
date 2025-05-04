
import streamlit as st

st.title("This is a Title for the App")
st.header("This is a Header")
st.subheader("This is a Subheader")
st.text("This is a text element")
st.markdown("This is a *Markdown* element _with_ **formatting**")
st.caption("This is a caption for an image")

code_example = """
def greet(name):
    print(f"Hello, this is my {name}!")
    """
st.code(code_example, language='python')

st.divider()