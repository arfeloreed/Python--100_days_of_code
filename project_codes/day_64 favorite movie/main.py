from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests


# create the extension objects
db = SQLAlchemy()

# create and configure the app
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection.db'
Bootstrap(app)

# link the extensions with the app
db.init_app(app)

# create the database models
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(700), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return f'<Movie {self.title}>'


# create the form to edit the rate and review
class EditRateForm(FlaskForm):
    rating = FloatField(label="Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


# create the form to add a new movie
class AddMovieForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


# create the database tables
# with app.app_context():
#     db.create_all()

# create route for home page
@app.route("/")
def home():
    # get all the movies from the database base on their rating
    movies = db.session.query(Movie).order_by(Movie.rating.desc()).all()

    # assign a rank to each movie
    for i in range(len(movies)):
        movies[i].ranking = i + 1
        db.session.commit()

    return render_template(
        "index.html",
        movies=movies,
    )

# create route for edit page
@app.route("/edit", methods=["GET", "POST"])
def edit():
    # create the form
    form = EditRateForm()

    # get the movie id from the request
    movie_id = request.args.get("id")
    # get the movie from the database
    movie_selected = db.session.query(Movie).get(movie_id)

    # handle the form submission
    if form.validate_on_submit():
        # get the data from the form
        new_rating = form.rating.data
        new_review = form.review.data

        # update the movie in the database
        movie_selected.rating = new_rating
        movie_selected.review = new_review
        # commit the changes to the database
        db.session.commit()

        # redirect to the home page
        return redirect(url_for("home"))

    return render_template(
        "edit.html",
        form=form,
        movie=movie_selected,
    )

# create a route for delete
@app.route("/delete")
def delete():
    # get the movie id from the request
    movie_id = request.args.get("id")
    # get the movie from the database
    movie_selected = db.session.query(Movie).get(movie_id)
    # delete the movie from the database
    db.session.delete(movie_selected)
    # commit the changes to the database
    db.session.commit()

    # redirect to the home page
    return redirect(url_for("home"))

# create a route for add page
@app.route("/add", methods=["GET", "POST"])
def add():
    # create the form
    form = AddMovieForm()

    # get the movie title from the form
    if form.validate_on_submit():
        movie_title = form.title.data

        # search for the movie using the API on themovieDB and send the request to the API and get the response
        params = {
            "api_key": "your api key from themoviedb",
            "query": movie_title,
        }
        response = requests.get("https://api.themoviedb.org/3/search/movie", params=params)
        data = response.json()["results"]

        # pass the data and render select page
        return render_template(
            "select.html",
            movies=data,
        )


    return render_template(
        "add.html",
        form=form,
    )

# create a route for select page
@app.route("/select")
def select():
    # get the movie id from the request
    movie_id = request.args.get("id")
    # search for the movie using the API on themovieDB and send the request to the API and get the response
    params = {"api_key": "your api key from themoviedb"}
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}", params=params)
    data = response.json()

    # add the movie data to the database
    with app.app_context():
        new_movie = Movie(
            title=data["title"],
            description=data["overview"],
            year=data["release_date"].split("-")[0],
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
        )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("edit", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
