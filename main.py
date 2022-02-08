from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

PATH = '/Users/jesseocean/Documents/Python Lessons/Chromedriver/chromedriver'

s = Service(PATH)
browser = webdriver.Chrome(service=s)
url = 'https://www.google.com'
browser.get(url)
time.sleep(5)
browser.quit()