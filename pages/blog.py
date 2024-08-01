# pages/_4_blog.py
import streamlit as st
import os

POSTS_PER_PAGE = 5

def load_posts():
    posts = []
    for filename in os.listdir('posts'):
        if filename.endswith('.md'):
            with open(os.path.join('posts', filename), 'r') as file:
                content = file.read()
                title = filename[:-3]
                excerpt = content[:150] + "..."  # Show first 150 characters
                posts.append({"title": title, "content": content, "excerpt": excerpt})
    return posts

def get_paginated_posts(posts, page, posts_per_page):
    start = page * posts_per_page
    end = start + posts_per_page
    return posts[start:end]

def app():
    st.title("Blog Page")

    st.subheader("Blog Posts")
    posts = load_posts()
    total_posts = len(posts)
    total_pages = (total_posts - 1) // POSTS_PER_PAGE + 1

    # Pagination controls
    page = st.number_input('Page', min_value=1, max_value=total_pages, step=1, value=1) - 1

    paginated_posts = get_paginated_posts(posts, page, POSTS_PER_PAGE)
    for post in paginated_posts:
        st.markdown(f"### {post['title']}")
        st.markdown(post['excerpt'])

        if st.button(f"Read More {post['title']}", key=post['title']):
            st.session_state.selected_post = post
            with st.popover(f"Details of {post['title']}"):
                st.write(post['content'])
                if st.button("Close"):
                    st.session_state.selected_post = None
                    st.rerun()

    

    # Display pagination information
    st.text(f"Page {page + 1} of {total_pages}")