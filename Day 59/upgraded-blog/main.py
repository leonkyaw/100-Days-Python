from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_url = 'https://api.npoint.io/674f5423f73deab1e9a7'
blog_posts = requests.get(blog_url).json()


@app.route('/')
def get_all_posts():
    return render_template('index.html', posts=blog_posts)


@app.route('/about')
def about_page():
    return render_template('about.html')


@ app.route('/contact')
def contact_page():
    return render_template('contact.html')


@ app.route('/post/<int:num>')
def individual_post(num):
    for post in blog_posts:
        if post['id'] == num:
            return render_template('post.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)
