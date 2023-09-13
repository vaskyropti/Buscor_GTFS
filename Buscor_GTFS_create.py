import streamlit as st
import pandas as pd

core_data = st.file_uploader("upload core data", type = ["xlsx"])
route_data = st.file_uploader("upload route data", type = ["xlsx"])

if core_data and route_data: 
    core_df = pd.read_excel(core_data)
    route_df = pd.read_excel(route_data)
    st.write(core_df)
    st.write(route_df)
    