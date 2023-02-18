from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# create a LoginManager object
login_manager = LoginManager()
# initialize the login_manager
login_manager.init_app(app)

# create a user loader function takes userid as input
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    # check if the method is POST and if so, get the data from the form
    if request.method == "POST":
        email = request.form.get("email")
        # check if email already exists
        if User.query.filter_by(email=email).first():
            # if a user is found, we want to redirect back to signup page so user can try again
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
        
        # if email doesn't exist, add new user to DB
        new_user = User(
            email=email,
            password=generate_password_hash(
                request.form.get("password"),
                method='pbkdf2:sha256',
                salt_length=8,
            ),
            name=request.form.get("name"),
        )
        db.session.add(new_user)
        db.session.commit()

        # log in and authenticate user after adding details to database
        login_user(new_user)
        
        return redirect(url_for('secrets', name=new_user.name))
    
    # if the method is GET, just serve the signup page
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # look for the email in the database
        email = request.form.get("email")
        user_for_login = User.query.filter_by(email=email).first()

        # if the email exists and the password is correct, log the user in
        if user_for_login:
            if check_password_hash(user_for_login.password, request.form.get("password")):
                login_user(user_for_login)
                return redirect(url_for('secrets', name=user_for_login.name))
            else:
                flash("Incorrect password, try again.")
                return redirect(url_for('login'))
        
        # if the email doesn't exist, send the user back to the login page
        if not user_for_login:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    # using the user_name variable in the URL to personalize the welcome message
    name=request.args.get("name")

    return render_template("secrets.html", name=name, logged_in=current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


# send a file from the static folder and display it in the browser
@app.route('/download')
@login_required
def download():
    return send_from_directory('static', 'files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)



# delete the data from database file to start from scratch
# with app.app_context():
#     user = db.session.query(User).all()
#     for u in user:
#         db.session.delete(u)
#     db.session.commit()