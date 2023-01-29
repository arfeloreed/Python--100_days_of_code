from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time


# set browser parameters and open browser
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://tinder.com/app/recs")

time.sleep(2)
accept = driver.find_element(By.XPATH, '//*[@id="s1221153819"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
accept.click()

# choose fb log-in
time.sleep(2)
log_in = driver.find_element(By.XPATH, '//*[@id="s1221153819"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
log_in.click()

time.sleep(3)
fb_log_in = driver.find_element(By.XPATH, '//*[@id="s1442494255"]/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]')
fb_log_in.click()

# switch to fb log-in window
time.sleep(3)
main_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# fill up form
time.sleep(2)
fb_email = driver.find_element(By.XPATH, '//*[@id="email"]')
fb_email.send_keys("your fb_email")
time.sleep(2)
fb_pass = driver.find_element(By.XPATH, '//*[@id="pass"]')
fb_pass.send_keys("your fb_password")
time.sleep(2)
fb_pass.send_keys(Keys.ENTER)

# switch back to tinder window
driver.switch_to.window(main_window)

# dismiss the pop-up notifications
time.sleep(7)
allow_button = driver.find_element(By.XPATH, '//*[@id="s1442494255"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
allow_button.click()
time.sleep(4)
not_interested_button = driver.find_element(By.XPATH, '//*[@id="s1442494255"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
not_interested_button.click()

# hit the like button
time.sleep(10)
liked = 0
for n in range(100):
    try:
        like_button = driver.find_element(By.XPATH, '//*[@id="s1221153819"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')
        like_button.click()
        liked += 1
    except NoSuchElementException:
        time.sleep(2)
    print(f"liked: {liked}")
    time.sleep(2)

time.sleep(2)
driver.quit()
