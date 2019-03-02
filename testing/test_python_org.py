from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get"http://www.python.org")
assert "Python" in browser.title



browser.close()