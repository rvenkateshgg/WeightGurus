import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
s = Service(executable_path="/Users/venkateshr/PycharmProjects/WeightGurus/drivers/chromedriver")

class TestBrowser():
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()
        self.driver.quit()

    def test_Login(self,setup):
        self.driver.get("http://192.168.0.103:8102/landing")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "(//ion-button[@shape='round'])[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//ion-input[@type='email']/input").send_keys("venkateshrv307@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@name='ion-input-1']").send_keys("Venkat@2000")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//ion-button[@size='large']").click()
        time.sleep(4)

    #def test_Settings(self):
        self.driver.find_element(By.XPATH, "//ion-tab-button[@tab='settings']").click()
        time.sleep(3)
        element = self.driver.find_element(By.TAG_NAME,"body").text
        print(element)
        self.driver.find_element(By.XPATH,"(//ion-label[@class='sc-ion-label-md-h sc-ion-label-md-s md hydrated'])[9]").click()
        self.driver.find_element(By.XPATH, "//input[@class='native-input sc-ion-input-md']").send_keys("0383")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//ion-button[@color='primary'])[3]").click()
        time.sleep(2)
