import streamlit as st

def app():
    st.session_state.page = 'Home Page'
    st.title("inoTives Showcase!")
    st.caption("Welcome to inoTives Showcase!")
    st.markdown(
        """
        Hi, I'm Toni ([@inotives](https://www.linkedin.com/in/inotives/)), a passionate data enthusiast. This Streamlit web app serves as a showcase for my data science projects and a living record of my journey in this exciting field.

        My goal is to explore the vast potential of data analysis in various domains, including:
        - **Cryptocurrency**: Delving into market trends, sentiment analysis, and forecasting.
        - **Macroeconomics**: Examining economic indicators and their impact on financial markets and correlation to cryto markets
        - **Data exploration and visualization**: Experimenting with different techniques to uncover insights and trends.
        - **Machine learning**: Building and deploying machine learning models for various tasks.
        - **LLMs and generative AI**: Exploring the capabilities and applications of these cutting-edge technologies.

        This web app also serves as a personal journal, documenting my experiences, learnings, and challenges in the world of data science and AI. 
        I invite you to explore my projects, provide feedback, and join me on this exciting journey.
        """
    )


    
