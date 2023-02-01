from flask import Flask, render_template
import requests


# set up url variables
url_blog = "https://api.npoint.io/c790b4d5cab58020d391"

# set up the requests and variables
response = requests.get(url_blog)
blog_data = response.json()

# Create a Flask instance
app = Flask(__name__)

# set up the route for the home page
@app.route('/')
def home():
    return render_template(
        "index.html",
        posts=blog_data,
    )

# set up route for the post page
@app.route('/blog/<int:num>')
def get_post(num):
    return render_template(
        "post.html",
        post=blog_data[num - 1]
    )

if __name__ == "__main__":
    app.run(debug=True)
