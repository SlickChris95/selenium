from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
#searches url
driver.get("http://www.python.org")
driver.close()
