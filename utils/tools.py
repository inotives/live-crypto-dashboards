import os

def load_posts():
    posts = []
    if not os.path.exists('posts'):
        os.makedirs('posts')
    for filename in os.listdir('posts'):
        if filename.endswith('.md'):
            with open(os.path.join('posts', filename), 'r') as file:
                posts.append(file.read())
    return posts

def save_post(title, content):
    filename = f'posts/{title}.md'
    with open(filename, 'w') as file:
        file.write(content)