import streamlit as st
import streamlit_timeline as sl
import pandas as pd

skills_n_tools = pd.DataFrame([
    {'SKILLS & TOOLS': 'Python', 'PROFICIENT-LEVEL': 'Expert', 'YEAR-EXP': 10, 'ADDITIONAL-NOTES': 'Pandas, Numpy, Requests'},
    {'SKILLS & TOOLS': 'SQL', 'PROFICIENT-LEVEL': 'Expert', 'YEAR-EXP': 10, 'ADDITIONAL-NOTES': 'PostgreSQL, MySQL'},
    {'SKILLS & TOOLS': 'Blockchain', 'PROFICIENT-LEVEL': 'Advanced', 'YEAR-EXP': 9, 'ADDITIONAL-NOTES': 'Ethereum, Bitcoin, Solana, Polygon'},
    {'SKILLS & TOOLS': 'Data Vis (Looker & Tableau)', 'PROFICIENT-LEVEL': 'Proficient', 'YEAR-EXP': 3, 'ADDITIONAL-NOTES': ''},
    {'SKILLS & TOOLS': 'Data Analysis', 'PROFICIENT-LEVEL': 'Advanced', 'YEAR-EXP': 6, 'ADDITIONAL-NOTES': ''},
    {'SKILLS & TOOLS': 'Sentiment Analysis', 'PROFICIENT-LEVEL': 'Proficient', 'YEAR-EXP': 1, 'ADDITIONAL-NOTES': ''},
    {'SKILLS & TOOLS': 'Descriptive Analysis', 'PROFICIENT-LEVEL': 'Advanced', 'YEAR-EXP': 3, 'ADDITIONAL-NOTES': ''},
    {'SKILLS & TOOLS': 'Predictive Analysis', 'PROFICIENT-LEVEL': 'Proficient', 'YEAR-EXP': 2, 'ADDITIONAL-NOTES': ''}

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



