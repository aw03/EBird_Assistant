import streamlit as st
import pandas as pd
import ebird_analyze
from region import Region 

desired_columns = ["locName","lat","lng","latestObsDt","numSpeciesAllTime"]

st.title("Find Hotspots!")

if "region" not in st.session_state or str(st.session_state['region']) == "World":
    st.warning("Please Select a Region")
else:
    st.header(st.session_state['region'])
    hotspots = ebird_analyze.region_hotspots_dataframe(repr(st.session_state['region'])).reindex(columns=desired_columns)
    st.dataframe(hotspots)
    
    selected_hotspot_name = st.selectbox("Select a Hotspot", hotspots['locName'])
    # hot_spot_map = pd.
    # st.map()
    