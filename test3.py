from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pprint

driver = webdriver.Chrome()
driver.get('https://reddit.com')
time.sleep(2)

links = driver.find_elements_by_xpath("//*[@href]")
# pprint.pprint(links)
for link in links:
    print(link.get_attribute('href'))
driver.quit()
