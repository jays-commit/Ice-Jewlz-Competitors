from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

PATH = '/Users/jesseocean/Documents/Python Lessons/Chromedriver/chromedriver'
chrono = "https://www.chrono24.co.uk/"
a_j = "https://www.instagram.com/a_jewellers/?hl=en"
ice = 'https://bryanni.com/'

s = Service(PATH)
browser = webdriver.Chrome(service=s)
browser.get(ice)

search = browser.find_element(By.XPATH, '//*[@id="section-header"]/div/div[3]/a[2]')
search.click()

search_bar = browser.find_element(By.XPATH, '//*[@id="Search"]/div/div[1]/form/input[1]')
search_bar.send_keys("chains")
search_bar.send_keys(Keys.ENTER)





# browser.quit()
