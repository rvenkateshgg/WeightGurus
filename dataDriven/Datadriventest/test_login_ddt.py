import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from dataDriven.XLUtils import XLutils
import time
s = Service(executable_path="/Users/venkateshr/PycharmProjects/WeightGurus/drivers/chromedriver")

class TestWgLogin():
    path = "/Users/venkateshr/Desktop/datadrivenwglogin.xlsx"

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_loginddt(self,setup):
        self.driver.get("http://192.168.0.118:8100/landing")
        time.sleep(2)
        self.rows = XLutils.getRowcount(self.path,'Sheet1')
        print("No of rows:",self.rows)

        for r in range (2, self.rows+1):
            self.username = XLutils.readData(self.path,'Sheet1',r,1)
            self.password = XLutils.readData(self.path,'Sheet1',r,2)
            self.results = XLutils.readData(self.path,'Sheet1',r,3)

            self.driver.find_element(By.XPATH, "(//ion-button[@shape='round'])[1]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//ion-input[@type='email']/input").send_keys(self.username)
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//input[@name='ion-input-1']").send_keys(self.password)
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//ion-button[@size='large']").click()
            time.sleep(4)

            try:
                self.driver.find_element(By.XPATH,"//ion-label[text()='Body Fat']")
                print("PASS")
            except:
                print("FAIL")








