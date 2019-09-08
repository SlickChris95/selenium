from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
driver.get('https://www.reddit.com/')
time.sleep(2)
images = driver.find_elements_by_tag_name('img')
#must have wget installed on your windows machine
for image in images:
    imgsrc = image.get_attribute('src')
    os.system("wget " + imgsrc + " -P img ")
driver.close()
