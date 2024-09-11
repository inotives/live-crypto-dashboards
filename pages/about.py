import streamlit as st
import streamlit_timeline as sl

def app():
    st.session_state.page = 'about'
    st.subheader("About me")
    st.markdown(
        """
        I began my career as a web developer, proficient in PHP (Laravel), JavaScript (React, Node.js), and Python (Flask). My interest in cryptocurrencies led me to join ItBit, a prominent cryptocurrency exchange, in 2015.

        During my time at ItBit (Paxos), I gained hands-on experience with various aspects of cryptocurrency technology, including wallet key management, blockchain investigation, and developing Python scripts for data ingestion and manipulations. 

        Leveraging my technical skills and passion for data, I transitioned into a data analyst role. This allowed me to combine my expertise in web development with my interest in cryptocurrencies, enabling me to contribute significantly to data-driven decision-making in ever changing crypto space.
        """
    )
    
    st.subheader('Career Timeline')

    with st.spinner(text="Career Timeline"):
        with open('timeline.json', "r") as f:
            data = f.read()
            sl.timeline(data, height=600)