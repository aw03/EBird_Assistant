import streamlit as st

st.set_page_config(
    page_title="Home",
)

st.write("# Page for my bird app!")

if 'user_data' not in st.session_state:
    st.session_state['user_data'] = {}