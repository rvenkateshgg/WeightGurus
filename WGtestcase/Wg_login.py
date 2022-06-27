from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
s = Service(executable_path='../drivers/chromedriver')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://192.168.0.103:8102/landing")
time.sleep(1)
driver.find_element(By.XPATH,"//ion-button[@size='large']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@class='native-input sc-ion-input-md']").send_keys("venkateshrv307@gmail.com")
driver.find_element(By.XPATH,"(//input[@class='native-input sc-ion-input-md'])[2]").send_keys("123456")
driver.find_element(By.XPATH,"//ion-button[@color='primary']").click()
time.sleep(7)


week = driver.find_element(By.XPATH,"//ion-segment-button[@value='week']")
week.click()
time.sleep(1)

month = driver.find_element(By.XPATH,"//ion-segment-button[@value='month']")
month.click()
time.sleep(1)

year = driver.find_element(By.XPATH,"//ion-segment-button[@value='year']")
year.click()
time.sleep(1)

total = driver.find_element(By.XPATH,"//ion-segment-button[@value='total']")
total.click()
time.sleep(1)

icon = driver.find_element(By.XPATH,"(//ion-icon[@class='md hydrated'])[2]")
icon.click()
time.sleep(2)

progress = driver.find_element(By.XPATH,"//app-stats-modal[@class='ion-page']").text
print(progress)

driver.find_element(By.CLASS_NAME,"responsive-img").click()
time.sleep(1)

driver.find_element(By.XPATH,"//img[@alt='ManualEntry']").click()

driver.find_element(By.XPATH,"(//ion-icon[@class='ion-accordion-toggle-icon md hydrated'])[2]").click()
time.sleep(2)
time.sleep(3)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")




