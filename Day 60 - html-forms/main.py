import smtplib

import requests
from flask import Flask, render_template, request

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/df44589626d58ccff735").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        smtp = smtplib.SMTP("smtp.gmail.com", port=587)
        smtp.starttls()
        smtp.login("YOUR EMAIL ADDRESS", "YOUR EMAIL PASSWORD")
        smtp.sendmail("YOUR EMAIL ADDRESS", "DESTINATION EMAIL ADDRESS", f"Subject:New Message\n\nName: "
                                                                         f"{data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage:"
                                                                         f"{data['message']}")

        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
