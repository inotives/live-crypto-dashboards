import streamlit as st
import pandas as pd
import plotly.express as plx
import time

from api import paxos_api
px = paxos_api()

# Config
st.set_page_config(
    page_title='Exchange Metrics', 
    page_icon=':bar_chart:', 
    layout='wide'
)

st.title('Stablecoin Comparison Metrics')
st.text('< data source: Messari.io >')

placeholder = st.empty()


with placeholder.container():
    
    col1,col2,col3,col4 = st.columns(4)

    busd = px.get_messari_asset_metrics('busd')
    usdc = px.get_messari_asset_metrics('usdc')
    time.sleep(1)
    usdt = px.get_messari_asset_metrics('usdt')
    usdp = px.get_messari_asset_metrics('pax-dollar')
    time.sleep(1)



    with col1: 
        st.markdown('#### USDT ')
        st.metric(label='Market Cap', value=f"${usdt['data']['marketcap']['current_marketcap_usd']:,.2f}")
        st.metric(label='Reported Volume', value=f"${usdt['data']['market_data']['volume_last_24_hours']:,.2f}")
        st.metric(label='Actual Volume', value=f"${usdt['data']['market_data']['real_volume_last_24_hours']:,.2f}")
        st.metric(label='Volume overstatement', value=f"{usdt['data']['market_data']['volume_last_24_hours_overstatement_multiple']:,.2f}x")
        st.metric(label='Active Addresses', value=f"{usdt['data']['blockchain_stats_24_hours']['count_of_active_addresses']:,.0f}")
        st.metric(label='24H OnChain Tx Vol', value=f"${usdt['data']['blockchain_stats_24_hours']['transaction_volume']:,.2f}")
        st.metric(label='24H OnChain Tx Count', value=f"{usdt['data']['blockchain_stats_24_hours']['count_of_tx']:,.0f}")

    with col2: 
        st.markdown('#### USDC ')
        st.metric(label='Market Cap', value=f"${usdc['data']['marketcap']['current_marketcap_usd']:,.2f}")
        st.metric(label='Reported Volume', value=f"${usdc['data']['market_data']['volume_last_24_hours']:,.2f}")
        st.metric(label='Actual Volume', value=f"${usdc['data']['market_data']['real_volume_last_24_hours']:,.2f}")
        st.metric(label='Volume overstatement', value=f"{usdc['data']['market_data']['volume_last_24_hours_overstatement_multiple']:,.2f}x")
        st.metric(label='Active Addresses', value=f"{usdc['data']['blockchain_stats_24_hours']['count_of_active_addresses']:,.0f}")
        st.metric(label='24H OnChain Tx Vol', value=f"${usdc['data']['blockchain_stats_24_hours']['transaction_volume']:,.2f}")
        st.metric(label='24H OnChain Tx Count', value=f"{usdc['data']['blockchain_stats_24_hours']['count_of_tx']:,.0f}")

    with col3: 
        st.markdown('#### BUSD ')
        st.metric(label='Market Cap', value=f"${busd['data']['marketcap']['current_marketcap_usd']:,.2f}")
        st.metric(label='Reported Volume', value=f"${busd['data']['market_data']['volume_last_24_hours']:,.2f}")
        st.metric(label='Actual Volume', value=f"${busd['data']['market_data']['real_volume_last_24_hours']:,.2f}")
        st.metric(label='Volume overstatement', value=f"{busd['data']['market_data']['volume_last_24_hours_overstatement_multiple']:,.2f}x")
        st.metric(label='Active Addresses', value=f"{busd['data']['blockchain_stats_24_hours']['count_of_active_addresses']:,.0f}")
        st.metric(label='24H OnChain Tx Vol', value=f"${busd['data']['blockchain_stats_24_hours']['transaction_volume']:,.2f}")
        st.metric(label='24H OnChain Tx Count', value=f"{busd['data']['blockchain_stats_24_hours']['count_of_tx']:,.0f}")
    
    with col4: 
        st.markdown('#### USDP ')
        st.metric(label='Market Cap', value=f"${usdp['data']['marketcap']['current_marketcap_usd']:,.2f}")
        st.metric(label='Reported Volume', value=f"${usdp['data']['market_data']['volume_last_24_hours']:,.2f}")
        st.metric(label='Actual Volume', value=f"${usdp['data']['market_data']['real_volume_last_24_hours']:,.2f}")
        st.metric(label='Volume overstatement', value=f"{usdp['data']['market_data']['volume_last_24_hours_overstatement_multiple']:,.2f}x")
        st.metric(label='Active Addresses', value=f"{usdp['data']['blockchain_stats_24_hours']['count_of_active_addresses']:,.0f}")
        st.metric(label='24H OnChain Tx Vol', value=f"${usdp['data']['blockchain_stats_24_hours']['transaction_volume']:,.2f}")
        st.metric(label='24H OnChain Tx Count', value=f"{usdp['data']['blockchain_stats_24_hours']['count_of_tx']:,.0f}")
    