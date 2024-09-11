import streamlit as st
import pandas as pd
import utils.settings as config
import ta

cryptos = {
    'Bitcoin': {'name': 'Bitcoin', 'symbol': 'BTC', 'filepath': f"{config.DATA_DIR}/ohlcv_bitcoin.csv"},
    'Ethereum': {'name': 'Ethereum', 'symbol': 'ETH', 'filepath': f"{config.DATA_DIR}/ohlcv_ethereum.csv"}
}
    
def select_crypto_data(crypto_name):
    return cryptos[crypto_name]['filepath']

def load_dataframe(filepath): 
    data = pd.read_csv(filepath)
    
    return data

def app(): 
    selected_post = st.selectbox("Select a crypto asset", [crypto[0] for crypto in cryptos.items()])
    
    st.write(selected_post)
    
    df = load_dataframe(select_crypto_data(selected_post))

    st.write(df)
    