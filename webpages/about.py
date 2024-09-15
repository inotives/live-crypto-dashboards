import streamlit as st
import streamlit_timeline as sl
import pandas as pd

def const_skillntool(name, level, exp_year, notes):
    return {
        'SKILLS & TOOLS': name,
        'PROFICIENT-LEVEL': level,
        'YEAR-EXP': exp_year,
        'ADDITIONAL-NOTES': notes
    }

def const_area_of_interest(name, description, icon):
    return {
        'name': name,
        'description': description,
        'icon': icon
    }

skills_n_tools = pd.DataFrame([
    const_skillntool('Python', 'Expert', 10, 'Pandas, Numpy, Requests'),
    const_skillntool('SQL', 'Expert', 10, 'PostgreSQL, MySQL'),
    const_skillntool('Blockchain', 'Advanced', 9, 'Ethereum, Bitcoin, Solana, Polygon'),
    const_skillntool('Data Vis (Looker & Tableau)', 'Proficient', 4, ''),
    const_skillntool('Storytelling', 'Proficient', 4, ''),
    const_skillntool('Data Analysis', 'Advanced', 6, ''),
    const_skillntool('Descriptive Analysis', 'Advanced', 3, ''),
    const_skillntool('Predictive Analysis', 'Proficient', 2, 'Forecasting with ARIMA, SARIMAX, LSTM'),
    const_skillntool('Sentiment Analysis', 'Proficient', 1, '')
])
skills_n_tools.set_index('SKILLS & TOOLS', inplace=True) 



# Create styled cards with a shadow

card_style = """
    {
        border: 1px groove #52546a;
        border-radius: 10px;
        padding-left: 25px;
        padding-top: 10px;
        padding-bottom: 10px;
        box-shadow: -6px 8px 20px 1px #00000052;
    }
"""


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
    
    # col1, _, col2 = st.columns([3, 1, 1.6])
    # with col1:
    #     with stylable_container("Card1", css_styles=card_style):
    #         "**Card 1**"
    #         "This is an example of basic card text."

    # with col2:
    #     with stylable_container("Card2", css_styles=card_style):
    #         st.metric("New York", "19.8M", "367K", help="Population growth")


