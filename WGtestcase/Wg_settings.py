from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s = Service(executable_path='../drivers/chromedriver')

driver = webdriver.Chrome(service=s)
driver.get("http://192.168.0.103:8102/landing")
driver.implicitly_wait(10)
time.sleep(1)
driver.find_element(By.XPATH,"//ion-button[@size='large']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@class='native-input sc-ion-input-md']").send_keys("venkateshrv307@gmail.com")
driver.find_element(By.XPATH,"(//input[@class='native-input sc-ion-input-md'])[2]").send_keys("123456")
driver.find_element(By.XPATH,"//ion-button[@color='primary']").click()
time.sleep(7)

driver.find_element(By.XPATH,"//img[@alt='Settings']").click()
time.sleep(2)

# EDIT
driver.find_element(By.XPATH,"(//ion-button[@shape='round'])[6]").click()

FName = driver.find_element(By.XPATH,"//input[@class='native-input sc-ion-input-md']")
FName.clear()
FName.send_keys("Rajkumar")
time.sleep(1)

LName = driver.find_element(By.XPATH,"(//input[@class='native-input sc-ion-input-md'])[2]")
LName.clear()
LName.send_keys("K")
time.sleep(1)

EMail = driver.find_element(By.XPATH,"(//input[@class='native-input sc-ion-input-md'])[3]")
EMail.clear()
EMail.send_keys("venkatesh307@gmail.com")
time.sleep(1)

PINcode = driver.find_element(By.XPATH,"(//input[@class='native-input sc-ion-input-md'])[4]")
PINcode.clear()
PINcode.send_keys("612204")
time.sleep(1)
