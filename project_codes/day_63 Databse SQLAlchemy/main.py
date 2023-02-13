from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


# create the extension object
db = SQLAlchemy()

# create an instance of the Flask class
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Reed is so handsome'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'

# initialize the extension
db.init_app(app)


# create a model
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# create the database
# with app.app_context():
#     db.create_all()

# create a route for home page
@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.query(Books).all()
    
    return render_template(
        "index.html",
        books=all_books,
    )

# create a route for add page
@app.route("/add", methods=["GET", "POST"])
def add():
    
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]
        
        # add the book to the database
        with app.app_context():
            new_book = Books(title=title, author=author, rating=rating)
            db.session.add(new_book)
            db.session.commit()
        
        return redirect(url_for("home"))
    
    return render_template(
        "add.html",
    )

# create a route for edit page
@app.route("/edit/<int:num>", methods=["GET", "POST"])
def edit(num):
    if request.method == "POST":
        book_id = num
        new_rating = request.form["rating"]
        
        # update the book in the database
        with app.app_context():
            book_to_update = Books.query.get(book_id)
            book_to_update.rating = new_rating
            db.session.commit()
        
        return redirect(url_for("home"))
    
    with app.app_context():
        book_selected = Books.query.get(num)
    
    return render_template(
        "edit.html",
        book=book_selected,
    )

# create a route for delete page
@app.route("/delete")
def delete():
    book_id = request.args.get("num")
    
    # delete the book from the database
    with app.app_context():
        book_to_delete = Books.query.get(book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
    
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
