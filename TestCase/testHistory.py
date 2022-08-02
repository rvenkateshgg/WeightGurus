from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
s = Service(executable_path='../drivers/chromedriver')

driver = webdriver.Chrome(service=s)
driver.get("http://192.168.0.162:8104/landing")
driver.implicitly_wait(5)


driver.find_element(By.XPATH,"//ion-button[@color='primary']").click()
time.sleep(3)

driver.find_element(By.XPATH,"//input[@class='native-input sc-ion-input-md']").send_keys("venkateshrv307@gmail.com")
driver.find_element(By.XPATH,"(//input[@class='native-input sc-ion-input-md'])[2]").send_keys("123456")
driver.find_element(By.XPATH,"//ion-button[@color='primary']").click()
time.sleep(4)

driver.find_element(By.XPATH,"//ion-tab-button[@tab='history']").click()
time.sleep(2)

history = driver.find_element(By.XPATH,"(//ion-content[@class='md hydrated'])[3]")
print(history.text)