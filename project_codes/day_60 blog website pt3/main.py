from flask import Flask, render_template, request
import requests
import smtplib


# set up the api for blog posts
response = requests.get("https://api.npoint.io/d0bb023bde51d82be1df")
posts = response.json()

# set up the variables for the email
my_email = "your email address"
password = "your email password"

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
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    message = "Contact Me"
    
    if request.method == 'POST':
        
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:New Message\n\nName: {request.form['name']}\nEmail: {request.form['email']}\nPhone: {request.form['phone_number']}\nMessage: {request.form['message']}",
            )
        
        message = "Successfully sent your message"
        return render_template(
            'contact.html',
            message=message,
        )
    
    return render_template(
        'contact.html',
        message=message,
    )
    
# set up the post route
@app.route('/post/<int:num>')
def post(num):
    return render_template(
        'post.html',
        post=posts[num-1],
    )

# set up the form route notification sent message
# @app.route('/form-entry')
# def form_entry():
#     data = request.form
#     name = data['name']
#     email = data['email']
#     phone = data['phone_number']
#     message = data['message']
#     print(name)
#     print(email)
#     print(phone)
#     print(message)
#     return f"<h1>Successfully sent your message.</h1>"

if __name__ == '__main__':
    app.run(debug=True)
