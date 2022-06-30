import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from dataDriven.XLUtils import XLutils
import time
s = Service(executable_path="/Users/venkateshr/PycharmProjects/WeightGurus/drivers/chromedriver")


class MyTestCase(unittest.TestCase):
    driver = None
    path = "/Users/venkateshr/Desktop/datadrivenwglogin.xlsx"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.maximize_window()

    def test_Loginddt(self):
        self.driver.get("http://192.168.0.118:8100/landing")
        time.sleep(1)
        self.rows = XLutils.getRowcount(self.path, 'Sheet1')
        print("No of rows:", self.rows)

        for r in range(2, self.rows + 1):
            self.username = XLutils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLutils.readData(self.path, 'Sheet1', r, 2)

            self.driver.find_element(By.XPATH, "(//ion-button[@shape='round'])[1]").click()
            time.sleep(2)

            username1 = self.driver.find_element(By.XPATH, "//ion-input[@type='email']/input")
            username1.clear()
            username1.send_keys(self.username)
            time.sleep(1)
            password1 = self.driver.find_element(By.XPATH, "//input[@name='ion-input-1']")
            password1.clear()
            password1.send_keys(self.password)
            self.driver.find_element(By.XPATH, "//ion-button[@size='large']").click()
            time.sleep(8)

            try:
                self.driver.find_element(By.XPATH, "//ion-label[text()='Body Fat']")
                print("PASS")
                XLutils.writeData(self.path, 'Sheet1', r, 3,"Test Passed")
            except:
                print("FAIL")
                XLutils.writeData(self.path, 'Sheet1', r, 3,"Test Failed")

    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
