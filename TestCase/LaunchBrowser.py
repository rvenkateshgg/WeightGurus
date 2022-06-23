from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
s = Service(executable_path='../drivers/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("https://www.selenium.dev/")
driver.maximize_window()
time.sleep(5)

