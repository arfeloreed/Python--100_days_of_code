from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime as dt


## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    author = StringField(label="Your Name", validators=[DataRequired()])
    img_url = StringField(label="Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField(label="Blog Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit Post")


@app.route('/')
def get_all_posts():
    # get the blog posts from the database
    posts = db.session.query(BlogPost).all()

    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    # get the blog posts data from the database and assign to a variable posts
    posts = db.session.query(BlogPost).all()
    requested_post = None
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


# create a route called new_post that will render a form to create a new blog post.
@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    form = CreatePostForm()

    if form.validate_on_submit():
        # get the current date
        date = dt.datetime.now().strftime("%B %d, %Y")
        # add the new blog post to the database
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            author=form.author.data,
            img_url=form.img_url.data,
            body=form.body.data,
            date=date,
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    
    return render_template("make-post.html", form=form)


# create a route called edit_post that will render a form to edit an existing blog post.
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    
    # get the blog post to be edited by id
    post = db.session.query(BlogPost).get(post_id)
    # populate the form with the existing data
    form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        author=post.author,
        img_url=post.img_url,
        body=post.body,
    )

    # update the blog post in the database
    if form.validate_on_submit():
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.author = form.author.data
        post.img_url = form.img_url.data
        post.body = form.body.data
        db.session.commit()
            
        return redirect(url_for('show_post', index=post_id))
    
    return render_template("make-post.html", form=form, is_edit=True)


# create a route called delete_post that will delete a blog post.
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    # get the blog post to be deleted by id
    post = db.session.query(BlogPost).get(post_id)
    # delete the blog post from the database
    db.session.delete(post)
    db.session.commit()
    
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
