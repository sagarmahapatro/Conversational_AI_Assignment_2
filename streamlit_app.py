import streamlit as st

st.title("App with External HTML")

with open("index.html", "r") as f:
    html_data = f.read()

st.markdown(html_data, unsafe_allow_html=True)