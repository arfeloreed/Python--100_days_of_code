from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


url_zillow = "https://mylinksnow.com/xIUqI"
url_form = "https://forms.gle/wxJk3CP36dcAJNo47"
req_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}

# set the properties of the chrome driver
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Get the HTML from the URL zillow
response = requests.get(url_zillow, headers=req_headers)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

# get the address of all the houses and put them in a list
all_addresses = soup.find_all(name="address")
addresses = [address.getText().split("|")[-1] for address in all_addresses]

# get all the prices of the houses and put them in a list
all_prices = soup.select("li article div.property-card-data span")
prices = []
for price in all_prices:
    if "+" not in price.getText():
        prices.append(price.getText().split("/")[0])
    else:
        prices.append(price.getText().split("+")[0])

# get all the links of the houses and put them in a list
all_links = soup.select("li article div.property-card-data a")
links = []
for link in all_links:
    if "https://www.zillow.com/" in link["href"]:
        links.append(link["href"])
    else:
        links.append("https://www.zillow.com/" + link["href"])

# import the data into the google form
time.sleep(5)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
for i in range(len(addresses)):
    driver.get(url_form)
    time.sleep(3)
    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(addresses[i])
    time.sleep(3)
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(prices[i])
    time.sleep(3)
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(links[i])
    time.sleep(3)
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()
print()
print("Done")
