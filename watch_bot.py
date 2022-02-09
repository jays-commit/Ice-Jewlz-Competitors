from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

PATH = '/Users/jesseocean/Documents/Python Lessons/Chromedriver/chromedriver'
s = Service(PATH)
ice = 'https://bryanni.com/'


class WatchBot:
    def __init__(self):
        self.browser = webdriver.Chrome(service=s)

    def search(self):
        self.browser.get(ice)
        self.browser.implicitly_wait(10)
        search = self.browser.find_element(By.XPATH, '//*[@id="section-header"]/div/div[3]/a[2]')
        search.click()
        search = self.browser.find_element(By.XPATH, '//*[@id="Search"]/div/div[1]/form/input[1]')
        search.send_keys("rolex")
        search.send_keys(Keys.ENTER)
        # self.browser.implicitly_wait(5)
        view_all = self.browser.find_element(By.XPATH, '//*[@id="Search"]/div/div[2]/div/div[1]/div/div[1]/a')
        view_all.click()

    def sidebar_search(self):
        self.browser.get(ice)
        self.browser.implicitly_wait(15)
        # time.sleep(3)

        sidebar = self.browser.find_element(By.XPATH, '//*[@id="section-header"]/div/div[1]/button')
        sidebar.click()
        # self.browser.implicitly_wait(5)
        shop_btn = self.browser.find_element(By.XPATH, '/html/body/div[4]/section/div/div/div/nav[1]/div[2]/button')
        shop_btn.click()
        # self.browser.implicitly_wait(5)
        watches = self.browser.find_element(By.XPATH,
                                              '/html/body/div[4]/section/div/div/div/nav[1]/div[2]/div/div/div[5]/a')
        watches.click()


bot = WatchBot()
bot.sidebar_search()
