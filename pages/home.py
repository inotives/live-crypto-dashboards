import streamlit as st

def app():
    st.session_state.page = 'Home Page'
    st.title(st.session_state.page)
    st.write("Welcome to the Home page!")
    st.write(st.session_state.page)
    st.markdown(
        """
        This is a real-time data dashboard that make use of the publically available API endpoint and re-arrange the data to display certain metrics that is useful to see.

        All the dashboards preseneted are updating in real-time to show the latest changes in the price, volumes and liquidity situation of exchange.
        This can help to determine the health of the exchange as well as for trader to make decision when placing order.

        Currently there are 3 Dashboards in this tool, more will be added in future. These dashboards are:
        - Liquidity Dashboard: It display various metrics of a market (BTCUSD, ETHUSD, etc..) such as pricing, volume, liquidity at different pricing bps.
        - Market Metrics: It show metrics of all market in single page.
        - Stablecoin Metrics: It show the comparison of various stablecoin onchain metrics in single page
        """
    )
