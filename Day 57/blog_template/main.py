from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)
content = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
post_objects = []
for post in content:
    post_obj = Post(post['id'], post['title'], post['subtitle'], post['body'])
    post_objects.append(post_obj)


@app.route('/')
def home():
    return render_template('index.html', posts=post_objects)


@app.route('/post/<int:index>')  # change the string variable to int
def show_post(index):
    requested_post = post_objects[index-1]
    return render_template('post.html', post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)
