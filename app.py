import streamlit as st
import pathlib

CURRENT_DIR = pathlib.Path(__file__).parent.resolve()

# Initialize session_state
if 'page' not in st.session_state:
    st.session_state.page = 'Home Page'
if 'fetch_data_running' not in st.session_state:
    st.session_state.fetch_data_running = False


st.logo(str(CURRENT_DIR / "logo.png"), link="https://www.linkedin.com/in/inotives/", icon_image=str(CURRENT_DIR / "logo.png"))

# Import all pages
from pages import home,liquidity_dashboard, about, exchanges_metrics, stablecoin_metrics, article

# Navigations
pg = st.navigation({
    "Overview": [
        st.Page(home.app, title='Home', default=True, icon=':material/home:', url_path=""),
        st.Page(about.app, title='About Me', icon=':material/grade:', url_path="/about"),
        st.Page(article.app, title='Articles', icon=':material/grade:', url_path="/article")
    ],
    "Dashboards Showcase": [
        st.Page(liquidity_dashboard.app, title='Liquidity Dashboard', icon=':material/analytics:', url_path="/liquidity_dashboard"),
        st.Page(exchanges_metrics.app, title='Exchanges Metrics', icon=':material/analytics:', url_path="/exchanges_metrics"),
        st.Page(stablecoin_metrics.app, title='Stablecoins Metrics', icon=':material/analytics:', url_path="/stablecoins_metrics")
    ]
})

pg.run()
