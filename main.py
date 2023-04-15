import requests
from flask import Flask, render_template
import datetime

app = Flask(__name__)

blog_posts = requests.get("https://api.npoint.io/01f04f4c1049bbc6c8eb").json()


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=blog_posts, current_year=datetime.datetime.now().year)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in blog_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)

