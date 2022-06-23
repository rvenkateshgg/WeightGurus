from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
s = Service(executable_path='../drivers/chromedriver')

download = '../Download_image/download0342.png'

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://192.168.0.103:8102/landing")
time.sleep(3)
driver.find_element(By.XPATH,"//ion-button[@color='primary']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//ion-input[@type='email']/input").send_keys("venkateshrv307@gmail.com")
driver.find_element(By.XPATH, "//input[@name='ion-input-1']").send_keys("Venkat@2000")
time.sleep(2)
driver.find_element(By.XPATH, "//ion-button[@size='large']").click()
time.sleep(4)
driver.find_element(By.XPATH, "//ion-tab-button[@tab='settings']").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//ion-label[@class='sc-ion-label-md-h sc-ion-label-md-s md hydrated'])[9]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@class='native-input sc-ion-input-md']").send_keys("0342")
time.sleep(1)
driver.find_element(By.XPATH,"(//ion-button[@color='primary'])[3]").click()
time.sleep(2)
with open(download,'wb') as file:
     file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0342.png']").screenshot_as_png)
