from flask import render_template
#app.py file ile baglanti qurulur
from app import app

post_list=['Post 1', 'Post 2', 'Post 3', 'Post 4']

@app.route("/post/<int:post_index>")
def post_detail(post_index):
    if post_index < len(post_list)+1:
        post_choose = post_list[post_index-1]
        # return "Hello, World!"
        return render_template("index.html", post=post_choose)
    else:
        return "index out of range"


@app.route("/posts")
def post_full():
    return render_template("posts.html", show_block=True, posts=post_list)