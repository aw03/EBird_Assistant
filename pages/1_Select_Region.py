import streamlit as st
import pandas as pd
import ebird_analyze
from region import Region 

world_region = Region("World","world",None,None,None)

if "region" not in st.session_state:
    st.session_state["region"] = world_region

if 'subregions' not in st.session_state:
    st.session_state['subregions'] = ebird_analyze.sub_regions_dataframe(repr(st.session_state["region"]))

st.title("Select a Region!")


st.dataframe(st.session_state['subregions'])