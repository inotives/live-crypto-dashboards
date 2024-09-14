import streamlit as st
import pandas as pd
import ta 

import utils.settings as config
import utils.data_preprocess as dp

cryptos = {
    'Bitcoin': {'name': 'Bitcoin', 'symbol': 'BTC', 'filepath': f"{config.DATA_DIR}/ohlcv_bitcoin.csv", 'infos': ''},
    'Ethereum': {'name': 'Ethereum', 'symbol': 'ETH', 'filepath': f"{config.DATA_DIR}/ohlcv_ethereum.csv", 'infos': ''}
}


def select_crypto_data(crypto_name):
    return cryptos[crypto_name]


def load_dataframe(filepath): 
    data = pd.read_csv(filepath)
    return data


def app(): 
    crypto = st.selectbox("Select a crypto asset", [crypto[0] for crypto in cryptos.items()])
        
    crypto_details = select_crypto_data(crypto)
    df = load_dataframe(crypto_details['filepath'])

    st.write(f"{crypto_details['name']} ({crypto_details['symbol']})")
    st.caption("Here are the preview of OHLCV data.")
    st.table(df.tail())

    df_ti = dp.add_technical_indicitors(df)
    st.write(df_ti)
    
    col1, col2, col3 = st.columns((1, 1, 2))
    
    with col1: 
        st.button('1')
    
    with col2: 
        st.button('2')

    with col3: 
        st.button('3')