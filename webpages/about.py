import streamlit as st
import streamlit_timeline as sl
import pandas as pd

def skillntool(name, level, exp_year, notes):
    return {
        'SKILLS & TOOLS': name,
        'PROFICIENT-LEVEL': level,
        'YEAR-EXP': exp_year,
        'ADDITIONAL-NOTES': notes
    }

skills_n_tools = pd.DataFrame([
    skillntool('Python', 'Expert', 10, 'Pandas, Numpy, Requests'),
    skillntool('SQL', 'Expert', 10, 'PostgreSQL, MySQL'),
    skillntool('Blockchain', 'Advanced', 9, 'Ethereum, Bitcoin, Solana, Polygon'),
    skillntool('Data Vis (Looker & Tableau)', 'Proficient', 4, ''),
    skillntool('Storytelling', 'Proficient', 4, ''),
    skillntool('Data Analysis', 'Advanced', 6, ''),
    skillntool('Descriptive Analysis', 'Advanced', 3, ''),
    skillntool('Predictive Analysis', 'Proficient', 2, 'Forecasting with ARIMA, SARIMAX, LSTM'),
    skillntool('Sentiment Analysis', 'Proficient', 1, '')
])
skills_n_tools.set_index('SKILLS & TOOLS', inplace=True) 



def app():
    st.session_state.page = 'about'
    st.subheader("About me")
    st.markdown(
        """
        I began my career as a web developer, proficient in PHP (Laravel), JavaScript (React, Node.js), and Python (Flask). My interest in cryptocurrencies led me to join ItBit, a prominent cryptocurrency exchange, in 2015.

        During my time at ItBit (Paxos), I gained hands-on experience with various aspects of cryptocurrency technology, including wallet key management, blockchain data analysis including data collection, data transformation and data warehousing of the blockchain data.  

        Drawing on my technical proficiency and enthusiasm for data, I successfully transitioned into a data analyst role. This new position allowed me to merge my web development expertise with my keen interest in cryptocurrencies. By leveraging tools like Looker, Tableau, and Streamlit, I created comprehensive dashboards to visualize and analyze cryptocurrency data, empowering stakeholders to make informed decisions.
        """
    )
    
    st.subheader('Career Timeline')

    with st.spinner(text="Career Timeline"):
        with open('timeline.json', "r") as f:
            data = f.read()
            sl.timeline(data, height=600)

    st.subheader('Skills & Tools')
    st.caption('Below are list of skillset i acquired through my years of experiences as well as tools or platform i used in my daily workflow as data scientist/analyst.')
    st.table(skills_n_tools)

    st.subheader('Connect with me')
    



