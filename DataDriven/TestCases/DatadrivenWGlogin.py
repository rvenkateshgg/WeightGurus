from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from DataDriven.XLUtils import XLutils
import time

s = Service(executable_path='/Users/venkateshr/PycharmProjects/WeightGurus/drivers/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("http://192.168.0.115:4201/landing")
driver.implicitly_wait(10)
time.sleep(1)
path = "/Users/venkateshr/Desktop/datadrivenwglogin.xlsx"

rows = XLutils.getRowcount(path,'Sheet1')
for r in range(2, rows+1):
    username1 = XLutils.readData(path,'Sheet1',r,1)
    password1 = XLutils.readData(path,'Sheet1',r,2)

    driver.find_element(By.XPATH, "(//ion-button[@shape='round'])[1]").click()
    time.sleep(1)

    email = driver.find_element(By.XPATH, "//ion-input[@type='email']/input")
    email.clear()
    email.send_keys(username1)

    password = driver.find_element(By.XPATH, "//input[@name='ion-input-1']")
    password.clear()
    password.send_keys(password1)
    driver.find_element(By.XPATH, "//ion-button[@size='large']").click()

    text = driver.find_element(By.XPATH, "//ion-text[@color='primary']").text

    if text == 'Settings':
        print("Pass")
        XLutils.writeData(path,'Sheet1',r,3,"Test Pass")
    else:
        print("Fail")
        XLutils.writeData(path,'Sheet1',r,3,"Test Fail")
        time.sleep(3)