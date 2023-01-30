from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


TWITTER_EMAIL = "your twitter_email"
TWITTER_PASSWORD = "your twitter_password"
TWITTER_USERNAME = "your twitter_username"
PROMISED_DOWN = "your internet provider's promised download speed"
PROMISED_UP = "your internet provider's promised upload speed"

url_speedtest = "https://www.speedtest.net/"
url_twitter = "https://twitter.com/login"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

class InternetSpeedTwitterBot:
    """a class that will tweet your internet speed"""
    def __init__(self):
        """initializes the driver and the up and down speed"""
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.up = 0
        self.down = 0
    
    def get_internet_speed(self):
        """gets the internet speed from speedtest.net"""
        self.driver.get(url_speedtest)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Go')]").click()
        time.sleep(60)
        self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)

    def tweet_at_provider(self):
        """tweets at the internet provider"""
        self.driver.get(url_twitter)
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(TWITTER_EMAIL)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span').click()
        try:
            time.sleep(5)
            self.driver.find_element(By.NAME, "password").send_keys(TWITTER_PASSWORD)
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span').click()
            time.sleep(5)
            tweet = f"Hey @PLDT, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
            self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block").send_keys(tweet)
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').send_keys(Keys.ENTER)
        except NoSuchElementException:
            time.sleep(5)
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(TWITTER_USERNAME)
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div').click()
            time.sleep(5)
            self.driver.find_element(By.NAME, "password").send_keys(TWITTER_PASSWORD)
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span').click()
            time.sleep(5)
            tweet = f"Hey @PLDT, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
            self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block").send_keys(tweet)
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()


# create an object from the class and call the methods
complaint_bot = InternetSpeedTwitterBot()

# get the internet speed and tweet at the provider if the speed is not as promised
complaint_bot.get_internet_speed()
print(f"down: {complaint_bot.down} up: {complaint_bot.up}")
if complaint_bot.down < PROMISED_DOWN or complaint_bot.up < PROMISED_UP:
    complaint_bot.tweet_at_provider()

time.sleep(3)
complaint_bot.driver.quit()
