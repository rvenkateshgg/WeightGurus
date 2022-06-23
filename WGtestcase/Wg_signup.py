from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s = Service(executable_path='../drivers/chromedriver')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("http://192.168.0.103:8102/landing")
driver.implicitly_wait(5)
time.sleep(1)
driver.find_element(By.XPATH,"(//ion-button[@color='primary'])[2]").click()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@class='native-input sc-ion-input-md']").send_keys("venkatesh")
driver.find_element(By.XPATH,"(//input[@class='native-input sc-ion-input-md'])[2]").send_keys("Rk")
driver.find_element(By.XPATH,"//ion-button[@slot='end']").click()
time.sleep(2)

element = driver.find_element(By.XPATH,"//ion-content[@class='md hydrated']").text
print(element)

driver.find_element(By.XPATH,"//ion-button[@slot='end']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//ion-button[@size='large']").click()

driver.find_element(By.XPATH,"//ion-button[@slot='end']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//ion-toggle[@class='md in-item interactive hydrated']").click()
driver.find_element(By.XPATH,"(//input[@class='native-input sc-ion-input-md'])[3]").send_keys("55.0")
driver.find_element(By.XPATH,"(//input[@class='native-input sc-ion-input-md'])[4]").send_keys("65.0")
driver.find_element(By.XPATH,"//ion-button[@slot='end']").click()
time.sleep(2)

driver.find_element(By.XPATH,"(//ion-chip[@class='md ion-activatable hydrated'])[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//button[@type='button'])[7]").click()
driver.find_element(By.XPATH,"(//button[@type='button'])[17]").click()
time.sleep(1)
driver.find_element(By.XPATH,"(//button[@type='button'])[2]").click()

driver.find_element(By.XPATH,"//ion-button[@slot='end']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//input[@name='ion-input-4']").send_keys("venkatrk@gmail.com")
driver.find_element(By.XPATH,"//ion-button[@slot='end']").click()
time.sleep(1)

driver.find_element(By.XPATH,"(//input[@class='native-input sc-ion-input-md'])[6]").send_keys("123456")
driver.find_element(By.XPATH,"(//input[@class='native-input sc-ion-input-md'])[7]").send_keys("123456")
driver.find_element(By.XPATH,"(//input[@class='native-input sc-ion-input-md'])[8]").send_keys("600077")
time.sleep(1)
driver.find_element(By.XPATH,"//ion-button[@slot='end']").click()




#driver.find_element(By.XPATH,"(//button[@type='button'])[3]").click()
#driver.find_element(By.XPATH,"(//button[@type='button'])[12]").click()
#driver.find_element(By.XPATH,"(//button[@type='button'])[21]").click()
#driver.find_element(By.XPATH,"(//button[@type='button'])[2]").click()

