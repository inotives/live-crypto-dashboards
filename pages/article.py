# pages/_4_blog.py
import streamlit as st
from utils.blogs import BLOGS

def find_posts(query, posts):
    results = []
    for post in posts:
        if query.lower() in post["post_title"].lower():
            results.append(post)
    return results

def app():
    st.title("My Articles")

    search_query = st.text_input("Search for a post")

    # Search for posts based on the search query
    filtered_posts = find_posts(search_query, BLOGS)

    # Display the filtered posts with a selectbox
    if filtered_posts:
        selected_post = st.selectbox("Select a post", filtered_posts, key="post_select")

        # Load the Markdown content only when a post is selected
        if selected_post:
            for post in BLOGS:
                if post["post_title"] == selected_post:
                    print('This is selected')
                    st.markdown(post["post_md"])
                    break
    else:
        st.write("No posts found.")