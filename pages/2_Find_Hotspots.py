import streamlit as st
import pandas as pd
import ebird_analyze
from region import Region 

if "region" not in st.session_state or str(st.session_state['region']) == "World":
    st.warning("Please Select a Region")
else:
    st.text(st.session_state['region'])
    st.dataframe(ebird_analyze.region_hotspots_dataframe(repr(st.session_state['region']))[["locName","lat","lng","latestObsDt","numSpeciesAllTime"]])