from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

PATH = '/Users/jesseocean/Documents/Python Lessons/Chromedriver/chromedriver'
chrono = "https://www.chrono24.co.uk/"
a_j = "https://www.instagram.com/a_jewellers/?hl=en"
ice = 'https://bryanni.com/'

s = Service(PATH)
browser = webdriver.Chrome(service=s)
browser.get(ice)

print()
print(browser.title)

# search = browser.find_elements_by_class_name("prestige--v4")
# search.send_keys("rolex")
# search.send_keys(Keys.RETURN)


time.sleep(3)
browser.quit()
