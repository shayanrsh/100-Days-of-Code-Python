from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os

PROMISED_DOWN = 40
PROMISED_UP = 10
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
SPEEDTEST_URL = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)
        sleep(2)
        go_button = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div[1]/div['
                                                                '1]/div[1]/div[2]/div[3]/div[1]/a[1]/span[4]')
        go_button.click()
        sleep(60)
        self.down = self.driver.find_element(by=By.CLASS_NAME, value="download-speed").text
        self.up = self.driver.find_element(by=By.CLASS_NAME, value="upload-speed").text
        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        # login to twitter
        self.driver.get("https://twitter.com/i/flow/login")
        sleep(2)
        email = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                            '2]/div/div/div[2]/div[2]/div/div/div/div['
                                                            '5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)

        email_next_button = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[1]/div[1]/div[1]/div['
                                                                        '1]/div[1]/div[1]/div[2]/div[2]/div[1]/div['
                                                                        '1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[6]')
        email_next_button.click()
        sleep(2)
        password = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[1]/div[1]/div[1]/div[1]/div['
                                                               '1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div['
                                                               '2]/div[1]/div[1]/div[1]/div[3]/div[1]/label[1]/div['
                                                               '1]/div[2]/div[1]/input[1]')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(2)

        # compose tweet
        tweet_text = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]')
        tweet_text.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay "
                             f"for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        sleep(2)
        tweet = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/span[1]')
        tweet.click()
        sleep(2)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
