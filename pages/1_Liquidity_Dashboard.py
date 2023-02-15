import streamlit as st
import pandas as pd
import plotly.express as plx
from api import paxos_api
import time

px = paxos_api()

# Config
st.set_page_config(
    page_title='Liquidity Dashboard', 
    page_icon=':bar_chart:', 
    layout='wide'
)

options = st.selectbox(
    'Markets: ',
    ('BTCUSD', 'ETHUSD', 'LTCUSD', 'BCHUSD','SOLUSD','UNIUSD','PAXGUSD','AAVEUSD','LINKUSD','MATICUSD')
)

placeholder = st.empty()

while True:

    with placeholder.container():

        data1=px.get_paxos_data_single_market(options)
        df1 = pd.DataFrame.from_dict(data1['orderbook_full'],orient='index', columns=['price','qty','side'])
        df2 = pd.DataFrame(list(data1.items()), columns=['key', 'value'])
        df_25bps = df2[df2['key'].str.contains('25bps')]
        df_50bps = df2[df2['key'].str.contains('50bps')]
        df_100bps = df2[df2['key'].str.contains('100bps')]
        df_200bps = df2[df2['key'].str.contains('200bps')]

        df_ask = df1[df1['side']=='ask']['qty'].cumsum()
        df_bid = df1[df1['side']=='bid']['qty'].cumsum()
        
        accum = pd.concat([df_ask, df_bid]).sort_index()
        df1.loc[:, 'Accumulated'] = accum


        vol, volusd, price, spread, spreadbps  = st.columns(5)
        
        vol.metric(label=f"Vol in {data1['asset']}", value=f"{data1['vol_today']:,.6f}")
        volusd.metric(label='Today Vol (USD)', value=f"${data1['vol_today_usd']:,.2f}")
        price.metric(label='Mid Price', value=f"${data1['mid_price']:,.2f}")
        spread.metric(label='Spread', 
            value=f"${data1['spread']:,.4f}", 
        )
        spreadbps.metric(label='Spread (BPS)', 
            value=f"{((data1['spread']/data1['mid_price'])*10000):.4f}"
        )
        
        st.markdown('###')

        col1,col2 = st.columns(2)

        with col1:
            st.markdown('##### Oderbook Details - BID Side')
            st.metric(
                label= "Total Orderbook Depth",
                value=f"${data1['bid_total_liq']:,.2f}"
            )
            st.metric(
                label= "Total Orders Count",
                value=f"{data1['bid_cnt']:,.0f}"
            )
            st.markdown('##### Oderbook Details - ASK Side')
            st.metric(
                label= "Total Orderbook Depth",
                value=f"${data1['ask_total_liq']:,.2f}"
            )
            st.metric(
                label= "Total Orders Count",
                value=f"{data1['ask_cnt']:,.0f}"
            )



        with col2: 
            st.markdown('##### Orderbook Depth')
            st.write(plx.area(df1, x='price', y='Accumulated', color='side', height=400))
            

        bpsc1, bpsc2, bpsc3, bpsc4 = st.columns(4)

        with bpsc1: 
            st.markdown('##### Liq at 25bps from MidPrice')   
            st.metric(
                label='Total Liq at 25bps Bid+Ask', 
                value=f"${(data1['bid_liq_25bps']+data1['ask_liq_25bps']):,.2f}"
            )
            st.dataframe(df_25bps)
        with bpsc2: 
            st.markdown('##### Liq at 50bps from MidPrice')   
            st.metric(
                label='Total Liq at 50bps Bid+Ask', 
                value=f"${(data1['bid_liq_50bps']+data1['ask_liq_50bps']):,.2f}"
            )
            st.dataframe(df_50bps)
        with bpsc3: 
            st.markdown('##### Liq at 100bps from MidPrice')   
            st.metric(
                label='Total Liq at 100bps Bid+Ask', 
                value=f"${(data1['bid_liq_100bps']+data1['ask_liq_100bps']):,.2f}"
            )
            st.dataframe(df_100bps)
        with bpsc4: 
            st.markdown('##### Liq at 200bps from MidPrice')   
            st.metric(
                label='Total Liq at 200bps Bid+Ask', 
                value=f"${(data1['bid_liq_200bps']+data1['ask_liq_200bps']):,.2f}"
            )
            st.dataframe(df_200bps)
    


    time.sleep(3)