from flask import Flask, render_template
import requests

app = Flask(__name__)

blogs = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
print(blogs)

@app.route('/')
def home():
    return render_template("index.html", all_posts=blogs)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/post/<int:id>')
def post(id):
    returned_post = None
    for blog in blogs:
        if blog["id"] == id:
            returned_post = blog
    return render_template("post.html", post=returned_post)

if __name__ == "__main__":
    app.run(debug=True)
