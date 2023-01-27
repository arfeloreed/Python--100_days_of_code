import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# time limit
timeout = 60 * 5
time_start = int(time.time())
time_check = 10 + time_start

store = driver.find_elements(By.CSS_SELECTOR, "div#store b")
prices = [price.text.split("-")[1] for price in store[:-1]]
cookie = driver.find_element(By.ID, "cookie")

while int(time.time()) < time_start + timeout:
    cookie.click()
    if int(time.time()) == time_check:
        # print("entered the if loop_1")
        store_2 = driver.find_elements(By.CSS_SELECTOR, "div#store .grayed b")
        unavailable_prices = [price.text.split("-")[1] for price in store_2[:-1]]

        available_prices = [price.strip() for price in prices if price not in unavailable_prices]
        to_buy = available_prices[-1]
        # print(to_buy)
        index_num = available_prices.index(to_buy)
        # print(index_num)

        # check money
        money = driver.find_element(By.ID, "money").text

        if money > to_buy:
            # print("entered if loop_2")
            buy = driver.find_elements(By.CSS_SELECTOR, "div#store b")
            buy[index_num].click()
            # print("success 1")

        time_check += 10
        # print("success 2")
        # print()

time.sleep(0.5)
cookies_per_second = driver.find_element(By.ID, "cps")
cookies_per_second = cookies_per_second.text.split(":")[1].strip()
print(f"cookies per second: {cookies_per_second}")

time.sleep(3)
driver.quit()
