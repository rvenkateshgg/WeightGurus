from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
s = Service(executable_path='../drivers/chromedriver')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://192.168.0.103:8102/landing")
time.sleep(1)
driver.find_element(By.XPATH,"//ion-button[@size='large']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@class='native-input sc-ion-input-md']").send_keys("venkateshrv307@gmail.com")
driver.find_element(By.XPATH,"(//input[@class='native-input sc-ion-input-md'])[2]").send_keys("123456")
driver.find_element(By.XPATH,"//ion-button[@color='primary']").click()
time.sleep(2)

driver.find_element(By.XPATH,"").click()
time.sleep(1)

driver.find_element(By.XPATH,"(//ion-segment-button[@role='tab'])[2]").click()
time.sleep(1)

driver.find_element(By.XPATH,"(//ion-segment-button[@role='tab'])[3]").click()
time.sleep(1)

driver.find_element(By.XPATH,"(//ion-segment-button[@role='tab'])[4]").click()
time.sleep(1)

driver.find_element(By.XPATH,"//ion-tab-button[@tab='settings']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//ion-label[text()='Log Out']").click()
time.sleep(1)

driver.find_element(By.XPATH,"(//button[@type='button'])[2]").click()
element = driver.find_element(By.XPATH,"//ion-button[@size='large']").text
print(element)

if element == "LOG IN":
    print("Pass")
else:
    print("Fail")




#driver.find_element(By.XPATH,"(//ion-item[@class='item md item-lines-full item-fill-none in-list hydrated item-label'])[7]/ion-label").click()
#time.sleep(2)

#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#time.sleep(1)

#driver.execute_script("window.scrollBy(0,500)")

#demo_element = driver.execute_script("return document.getElementsByTagName('ion-item')[13];")
#driver.execute_script("arguments[0].click;",demo_element)
#time.sleep(2)
