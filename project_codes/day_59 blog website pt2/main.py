from flask import Flask, render_template
import requests


# set up the api for blog posts
response = requests.get("https://api.npoint.io/d0bb023bde51d82be1df")
posts = response.json()

# Create the application instance
app = Flask(__name__)

# set up the home route
@app.route('/')
def home():
    return render_template(
        'index.html',
        posts=posts,
    )

# set up the about route
@app.route('/about')
def about():
    return render_template(
        'about.html',
    )

# set up the contact route
@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
    )
    
# set up the post route
@app.route('/post/<int:num>')
def post(num):
    return render_template(
        'post.html',
        post=posts[num-1],
    )

if __name__ == '__main__':
    app.run(debug=True)
