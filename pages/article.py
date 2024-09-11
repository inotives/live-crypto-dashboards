# pages/_4_blog.py
import streamlit as st
from utils.blogs import BLOGS
from datetime import datetime

def find_posts(query, posts):
    results = []
    for post in posts:
        if query.lower() in post["post_title"].lower():
            results.append(post)
    return results

# Function to update the container based on the selected post
def update_container(selected_post, container):
    with container:
        st.markdown(selected_post["post_md"])

# Function to sort posts by date
def sort_posts_by_date(posts):
    return sorted(posts, key=lambda x: datetime.strptime(x["post_date"], '%Y-%m-%d'), reverse=True)


def app():
    st.caption("Use the search button to search for post and articles i wrote related to my analysis and my knowledge sharing. happy reading!!")

    # Search query input
    st.markdown('<div id="search-box"></div>', unsafe_allow_html=True)
    search_query = st.text_input("Search for a post")

    # Sort posts by date (latest to earliest)
    sorted_posts = sort_posts_by_date(BLOGS)

    # Filter posts based on the search query
    if search_query:
        filtered_posts = find_posts(search_query, sorted_posts)
    else:
        filtered_posts = sorted_posts

    # Create a container to display the post content
    container = st.container()

    # Create a panel with buttons and images for each filtered post
    for post in filtered_posts:
        col1, col2 = st.columns([1, 5])  # Create two columns: one for the image, one for the title/button
        
        with col1:
            if post["post_image_url"]:
                st.image(post["post_image_url"], width=100)
            else:
                st.image("https://via.placeholder.com/100", width=100)  # Placeholder if no image is available

        with col2:
            if st.button(f"{post["post_title"]} ... ... {post['post_date']}"):  # Button for each post title
                # Update the container with the selected post's content
                update_container(post, container=container)
    
