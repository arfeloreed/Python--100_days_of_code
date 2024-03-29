from flask import Flask, render_template


# Create the application instance
app = Flask(__name__, template_folder="templates", static_folder="static")

# Create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
