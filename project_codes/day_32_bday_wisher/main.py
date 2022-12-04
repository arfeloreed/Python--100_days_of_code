##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import smtplib

MY_EMAIL = "Youremail@gmail.com"
PASSWORD = "yourpassword"

# 1. Update the birthdays.csv
birthdays = pandas.read_csv("birthdays.csv")
print(birthdays)
birth_days = birthdays["day"].tolist()

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
month = today.month
day = today.day
print(f"today: {day}")

index = 0
for i in birth_days:
    print(index)
    if day == i:
        if month == birthdays["month"][index]:
            print("Happy Birthday!")
            with open("letter_templates/letter_3.txt") as file:
                data = file.read()
                letter = data.replace("[NAME]", birthdays["name"][index])
            print(letter)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=birthdays["email"][index],
                    msg=f"Subject:Happy Birthday!\n\n{letter}",
                )
            print("message sent")
    index += 1
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
