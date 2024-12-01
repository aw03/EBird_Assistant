import streamlit as st

if "region" not in st.session_state and str(st.session_state['region']) != "World":
    st.warning("Please Select a Region")
else:
    pass