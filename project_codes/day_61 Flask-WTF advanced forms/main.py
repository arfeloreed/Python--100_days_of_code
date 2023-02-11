from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


# create a class for the login form and inherit from the FlaskForm class
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Login')


# create an instance of the Flask class
app = Flask(__name__)
app.config['SECRET_KEY'] = 'reed is so handsome'

# convert the bootstrap css to a flask extension
Bootstrap(app)

# create a route for home
@app.route("/")
def home():
    return render_template('index.html')

# create a route for login
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    email_add = "test.puropose.00@gmail.com"
    password = "12345678"
    if form.validate_on_submit():
        print(form.email.data)
        print(form.password.data)
        if form.email.data == email_add and form.password.data == password:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    
    return render_template(
        'login.html',
        form=form,
    )


if __name__ == '__main__':
    app.run(debug=True)