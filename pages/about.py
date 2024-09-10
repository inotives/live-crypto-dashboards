import streamlit as st

def app():
    st.session_state.page = 'about'
    st.markdown(
        """
        # About me 

        I began my career as a web developer, proficient in PHP (Laravel), JavaScript (React, Node.js), and Python (Flask). My interest in cryptocurrencies led me to join ItBit, a prominent cryptocurrency exchange, in 2015.

        During my time at ItBit, I gained hands-on experience with various aspects of cryptocurrency technology, including wallet key management, blockchain investigation, and developing Python tools for exchange API testing.

        Leveraging my technical skills and passion for data, I transitioned into a data analyst role. This allowed me to combine my expertise in web development with my interest in cryptocurrencies, enabling me to contribute significantly to data-driven decision-making in the crypto space.
        """
    )
    
