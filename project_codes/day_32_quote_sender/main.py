import random as rn
import smtplib
import datetime as dt

with open("quotes.txt", "r") as file:
    data_quotes = [line.strip() for line in file]
quote_of_day = rn.choice(data_quotes)
print(quote_of_day)

now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)

my_email = "your_email@gmail.com"
password = "your_password"
if day_of_week == 5:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Quote of the day\n\n{quote_of_day}"
        )
