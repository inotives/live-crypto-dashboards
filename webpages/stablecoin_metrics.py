# pages/1_Home.py
import streamlit as st
import pandas as pd
import plotly.express as plx
import time


def app():
    st.session_state.page = 'Stablecoin Metrics'
    st.set_page_config(
        page_title='Exchange Metrics',
        page_icon=':bar_chart:',
        layout='wide'
    )
    st.title("Stablecoin Metrics")
    st.text('... under constructions ...')
