from flask import Flask, render_template, request
import requests
import smtplib
from dotenv import load_dotenv
import os

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

load_dotenv()
app = Flask(__name__)
SENDER_USERNAME = os.getenv('SENDER_USERNAME')
PASSWORD = os.getenv('PASSWORD')
RECEIVER_USERNAME = os.getenv('RECEIVER_USERNAME')


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        send_message(name, email, phone, message)

        return render_template("contact.html", message_sent=True)

    return render_template("contact.html", message_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


def send_message(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(SENDER_USERNAME, PASSWORD)
        connection.sendmail(from_addr=SENDER_USERNAME,
                            to_addrs=RECEIVER_USERNAME,
                            msg=f"Subject:Reminder\n\n{email_message}")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
