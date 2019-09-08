import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

time.sleep(2)
searchBox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
searchBox.send_keys("Banjo smash bros")
searchBox.send_keys(Keys.ENTER)
driver.save_screenshot('img/screenshot.png')
time.sleep(2)

driver.quit()
