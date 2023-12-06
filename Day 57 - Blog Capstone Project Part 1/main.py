from flask import Flask, render_template
from post import Post

app = Flask(__name__)

post = Post()
all_titles = post.titles
all_subtitles = post.subtitles
all_bodies = post.bodies


@app.route('/')
def home():
    return render_template("index.html", all_titles=all_titles,
                           all_subtitles=all_subtitles, all_bodies=all_bodies)


@app.route('/post/<int:index>')
def show_post(index):
    return render_template("post.html", title=all_titles[index],
                           subtitle=all_subtitles[index], body=all_bodies[index])


if __name__ == "__main__":
    app.run(debug=True)
