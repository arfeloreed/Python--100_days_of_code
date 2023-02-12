from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open_time = StringField(label='Opening Time e.g. 8AM', validators=[DataRequired()])
    close_time = StringField(label='Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField(
        label='Coffee Rating',
        validators=[DataRequired()],
        choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
    )
    wifi_rating = SelectField(
        label='Wifi Strength Rating',
        validators=[DataRequired()],
        choices=["✘", "⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
    )
    power_rating = SelectField(
        label='Power Socket Availability',
        validators=[DataRequired()],
        choices=["✘", "⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
    )
    submit = SubmitField(label='Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        cafe = form.cafe.data
        location = form.location.data
        open_time = form.open_time.data
        close_time = form.close_time.data
        coffee_rating = form.coffee_rating.data
        wifi_rating = form.wifi_rating.data
        power_rating = form.power_rating.data
        
        # create a list of the data
        new_cafe = [cafe, location, open_time, close_time, coffee_rating, wifi_rating, power_rating]
        
        # update the csv file
        with open('cafe-data.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(new_cafe)
            
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        headers = next(csv_data)
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
            
    return render_template('cafes.html', cafes=list_of_rows, headers=headers)


if __name__ == '__main__':
    app.run(debug=True)
