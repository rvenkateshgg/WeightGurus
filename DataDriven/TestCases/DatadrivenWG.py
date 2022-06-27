import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from DataDriven.XLUtils import XLutils
import time

s = Service(executable_path='/Users/venkateshr/PycharmProjects/WeightGurus/drivers/chromedriver')
driver = webdriver.Chrome(service=s)

driver.get("http://192.168.0.115:4201/landing")
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(1)
path = "/Users/venkateshr/Desktop/WGdatadriven.xlsx"

rows = XLutils.getRowcount(path, 'Sheet1')
for r in range(2, rows+1):
    firstname = XLutils.readData(path,'Sheet1', r,1)
    lastname = XLutils.readData(path,'Sheet1',r,2)
    Cweight = XLutils.readData(path,'Sheet1',r,3)
    Gweight = XLutils.readData(path,'Sheet1',r,4)
    Email = XLutils.readData(path, 'Sheet1', r, 5)
    password = XLutils.readData(path,'Sheet1',r,6)
    Cpassword = XLutils.readData(path,'Sheet1',r,7)
    zipcode = XLutils.readData(path,'Sheet1',r,8)

    driver.find_element(By.XPATH,"(//ion-button[@shape='round'])[2]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@class='native-input sc-ion-input-md']").send_keys(firstname)
    time.sleep(1)
    driver.find_element(By.XPATH,"(//input[@class='native-input sc-ion-input-md'])[2]").send_keys(lastname)
    Nextbtn = driver.find_element(By.XPATH,"//ion-button[@slot='end']")
    Nextbtn.click()
    time.sleep(1)
    Nextbtn.click()

    driver.find_element(By.XPATH,"//ion-button[@shape='round']").click()
    Nextbtn.click()
    time.sleep(2)

    driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys(Cweight)
    driver.find_element(By.XPATH,"(//input[@type='text'])[4]").send_keys(Gweight)
    Nextbtn.click()
    time.sleep(1)
    Nextbtn.click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@type='email']").send_keys(Email)
    Nextbtn.click()
    time.sleep(2)

    driver.find_element(By.XPATH,"(//input[@type='password'])[1]").send_keys(password)
    driver.find_element(By.XPATH,"(//input[@type='password'])[2]").send_keys(Cpassword)
    driver.find_element(By.XPATH,"(//input[@type='text'])[5]").send_keys(zipcode)
    driver.find_element(By.XPATH,"//ion-button[@slot='end']").click()
    time.sleep(2)

    text = driver.find_element(By.XPATH,"//ion-text[@color='primary']").text

    if text == 'Settings':
        print("Pass")
        XLutils.writeData(path,'Sheet1',r,9,"Test Pass")
    else:
        print("Fail")
        XLutils.writeData(path,'Sheet1',r,9,"Test Fail")
        time.sleep(3)

    driver.find_element(By.XPATH,"//ion-tab-button[@tab='settings']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//ion-label[text()='Log Out']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"(//button[@type='button'])[2]").click()








