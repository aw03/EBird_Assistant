import streamlit as st
import pandas as pd
import ebird_analyze
from region import Region
from region import Hotspot

desired_columns = ["locName","lat","lng","latestObsDt","numSpeciesAllTime"]

st.session_state["hotspot"] = None

st.title("Find Hotspots!")

def update_hotspot(hotspots, selected_hotspot_name):
    locId = hotspots.at[hotspots.index[hotspots['locName'] == selected_hotspot_name][0], 'locId']
    st.session_state['hotspot'] = Hotspot(name=selected_hotspot_name,code=locId)
    hotspot_observations = ebird_analyze.hot_spot_observations_dataframe( [str(locId)] )
    if hotspot_observations.empty:
        st.info("This hotspot has no observations in the past 30 days")
    else:
        st.dataframe(hotspot_observations)

if "region" not in st.session_state or str(st.session_state['region']) == "World":
    st.warning("Please Select a Region")
else:
    st.header(st.session_state['region'])
    hotspots = ebird_analyze.region_hotspots_dataframe(repr(st.session_state['region']))
    st.dataframe(hotspots.reindex(columns=desired_columns))
    
    selected_hotspot_name = st.selectbox("Select a Hotspot", hotspots['locName'])
    if st.button("Chose Hotspot"):
        update_hotspot(hotspots,selected_hotspot_name)
    