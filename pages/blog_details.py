# pages/_5_blog_detail.py
import streamlit as st
import os

def load_post(title):
    post_path = os.path.join('posts', f"{title}.md")
    if os.path.exists(post_path):
        with open(post_path, 'r') as file:
            return file.read()
    return None

def app():
    query_params = st.experimental_get_query_params()
    title = query_params.get('post_title', [None])[0]
    
    if title:
        content = load_post(title)
        if content:
            st.title(title)
            st.markdown(content)
            if st.button("Back to Blog"):
                st.experimental_set_query_params(page='blog')
        else:
            st.warning("Post not found.")
    else:
        st.warning("No post selected.")
