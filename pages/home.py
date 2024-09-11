import streamlit as st

def app():
    st.session_state.page = 'Home Page'
    st.title("inoTives Showcase!")
    st.caption("Welcome to inoTives Showcase!")
    st.markdown(
        """
        Hi my name is Toni (@inotives). I am a data enthusiat. This streamlit webapps was meant for experiment and showcase some data projects i worked on. 
        It is also record for my journey in the field of data science. 
        """
    )

    
