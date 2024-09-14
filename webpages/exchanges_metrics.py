# pages/1_Home.py
import streamlit as st
import pandas as pd
import plotly.express as plx
import requests

from utils.api import CryptoPubAPI

def app():
    st.session_state.page = 'Exchanges Metrics'
    st.set_page_config(
        page_title='Exchange Metrics',
        page_icon=':bar_chart:',
        layout='wide'
    )

    st.title('Detail Markets Metrics on Exchange')
    st.text('<Loading Data will take a while. around 20 sec.>')

    placeholder = st.empty()

    try:
        px = CryptoPubAPI()
        # data pull in here ...
        paxos_data = px.get_paxos_data_all()
        paxos_df = pd.DataFrame.from_dict(paxos_data, orient='index',
                    columns=[
                        'market',
                        'today_vol',
                        'today_vol_usd',
                        'mid_price',
                        'spread',
                        'spread_bps',
                        'top_asks',
                        'top_bids',
                        'ask_cnt',
                        'bid_cnt',
                        'ask_total_liq',
                        'bid_total_liq',
                        'bid_liq_25bps',
                        'ask_liq_25bps',
                        'bid_liq_50bps',
                        'ask_liq_50bps',
                        'bid_liq_100bps',
                        'ask_liq_100bps',
                        'bid_liq_200bps',
                        'ask_liq_200bps'
                    ])

        paxos_df['total_liq_25bps'] = paxos_df['bid_liq_25bps']+paxos_df['ask_liq_25bps']
        paxos_df['total_liq_50bps'] = paxos_df['bid_liq_50bps']+paxos_df['ask_liq_50bps']
        paxos_df['total_liq_100bps'] = paxos_df['bid_liq_100bps']+paxos_df['ask_liq_100bps']
        paxos_df['total_liq_200bps'] = paxos_df['bid_liq_200bps']+paxos_df['ask_liq_200bps']



        with placeholder.container():

            col1, col2 = st.columns(2)

            col1.metric(label='Total Combine Volume (USD)', value=f"${paxos_df['today_vol_usd'].sum():,.2f}")

            chart_col1, chart_col2 = st.columns(2)

            with chart_col1:
                fig = plx.pie(
                    paxos_df,
                    title="Volume Breakdown by Markets",
                    values='today_vol_usd',
                    names='market',
                    hole=.3)
                fig.update_layout(legend=dict(
                    yanchor="top",
                    y=0.99,
                    xanchor="left",
                    x=0.01,
                    font=dict(
                        size=10
                    )
                ))
                st.write(fig)

            with chart_col2:
                fig = plx.bar(
                        paxos_df.sort_values(by='spread_bps'),
                        title="Spread in Bps on all Markets",
                        x='spread_bps',
                        y='market',
                        color='spread_bps',
                        orientation='h'
                    )
                st.write(fig)

            liqcol1a, liqcol1b, liqcol1c = st.columns(3)
            liqcol2a, liqcol2b, liqcol2c = st.columns(3)

            liqcol1a.markdown("##### Price, Volume & Spread by Market")
            liqcol1a.dataframe(paxos_df[['today_vol_usd', 'mid_price', 'spread', 'spread_bps']])

            liqcol2a.markdown("##### Orderbook Health")
            liqcol2a.dataframe(paxos_df[['ask_cnt', 'ask_total_liq', 'bid_cnt','bid_total_liq']])

            liqcol1b.markdown("##### Liquidity @25bps from Mid-Price")
            liqcol1b.dataframe(paxos_df[['bid_liq_25bps', 'ask_liq_25bps', 'total_liq_25bps']])

            liqcol1c.markdown("##### Liquidity @50bps from Mid-Price")
            liqcol1c.dataframe(paxos_df[['bid_liq_50bps', 'ask_liq_50bps', 'total_liq_50bps']])

            liqcol2b.markdown("##### Liquidity @100bps from Mid-Price")
            liqcol2b.dataframe(paxos_df[['bid_liq_100bps', 'ask_liq_100bps', 'total_liq_100bps']])

            liqcol2c.markdown("##### Liquidity @200bps from Mid-Price")
            liqcol2c.dataframe(paxos_df[['bid_liq_200bps', 'ask_liq_200bps', 'total_liq_200bps']])


    except requests.exceptions.RequestException as e:
        st.error(f"Failed to fetch data from the API: {e}")
