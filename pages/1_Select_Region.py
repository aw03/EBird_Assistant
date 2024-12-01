import streamlit as st
import pandas as pd
import ebird_analyze
from region import Region 

world_region = Region("World","world",None)

if "region" not in st.session_state:
    st.session_state["region"] = world_region

if 'subregions' not in st.session_state:
    st.session_state['subregions'] = ebird_analyze.sub_regions_dataframe(repr(st.session_state["region"]))

def update_region(selected_region_name):
    st.session_state["region"] = Region(selected_region_name, st.session_state['subregions'].at[st.session_state['subregions'].index[st.session_state['subregions']['name'] == selected_region_name][0], 'code'],st.session_state['region'])
    st.session_state['subregions'] = ebird_analyze.sub_regions_dataframe(repr(st.session_state["region"]))
    st.rerun()

def previous_region():
    st.session_state['region'] = st.session_state['region'].get_parent()
    st.session_state['subregions'] = ebird_analyze.sub_regions_dataframe(repr(st.session_state["region"]))
    st.rerun()

st.title("Select a Region!")

st.header(f"Current Region: {st.session_state["region"]}")  

st.header("Subregions:")
if not st.session_state['subregions'].empty:
    st.dataframe(st.session_state['subregions']['name'], width=5000, hide_index=True)
    selected_region_name = st.selectbox("Choose a New Region", st.session_state['subregions']['name'])

    if st.button(label="Submit New Region"):
        update_region(selected_region_name)
else:
    st.info("No Subregions of this Region")

if st.button("Go Back One Region"):
    if st.session_state['region'] == world_region:
        pass
    else:
        previous_region()

