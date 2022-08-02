from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.color import Color
s = Service(executable_path='../drivers/chromedriver')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://192.168.0.164:8101/landing")
time.sleep(1)

rgb = driver.find_element(By.XPATH,"//ion-button[@size='large']").value_of_css_property('color')
print(rgb)
hexvalue = Color.from_string(rgb).hex
print("Hexvalue :", hexvalue,"\n")
time.sleep(2)

rgb1 = driver.find_element(By.XPATH,"(//ion-button[@size='large'])[2]").value_of_css_property('color')
print(rgb1)
hexvalue = Color.from_string(rgb1).hex
print("Hexvalue :", hexvalue,"\n")

driver.find_element(By.XPATH,"//ion-button[@size='large']").click()
time.sleep(1)

rgb2 = driver.find_element(By.XPATH,"//ion-button[@shape='round']").value_of_css_property('color')
print(rgb2)
hexvalue = Color.from_string(rgb2).hex
print("Hex value :", hexvalue)
