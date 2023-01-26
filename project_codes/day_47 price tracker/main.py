import requests
from bs4 import BeautifulSoup
import smtplib
import os


url = "https://benstore.com.ph/lenovo/5521-lenovo-legion-slim-7-16-gaming-laptop-165hz-ryzen-9-6900hx-amd-radeon-rx-" \
      "6800s-8gb-16gb-ddr5-1tb-ssd-onyx-grey-.html"
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PASSWORD")

response = requests.get(url=url, headers=header)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
price = soup.find(name="span", class_="current-price-display price").getText()
price = price.split("₱")[1].split(",")
price = int("".join(price))
title = soup.find(name="h1", class_="product_title h1").getText()

if price < 100000:
    print("buy now")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Benstore PC Price Tracker\n\n{title} is now {price} php.\n{url}"
        )
    print("email sent.")
else:
    print("check again next time.")
