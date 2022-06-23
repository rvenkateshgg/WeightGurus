import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
s = Service(executable_path="/Users/venkateshr/PycharmProjects/WeightGurus/drivers/chromedriver")


class TestWeightGuru():
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_Homepagetitle(self,setup):
        self.driver.get("http://192.168.0.103:8102/landing")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//ion-button[@color='primary']").click()
        time.sleep(2)
        helpbtn = self.driver.find_element(By.XPATH,"(//img[@class='responsive-img'])[2]").is_enabled()
        helpbtn1 = self.driver.find_element(By.XPATH,"(//img[@class='responsive-img'])[2]").is_displayed()
        print(helpbtn)
        print(helpbtn1)

        closebtn = self.driver.find_element(By.XPATH,"//img[@class='responsive-img']").is_enabled()
        closebtn1 = self.driver.find_element(By.XPATH,"//img[@class='responsive-img']").is_displayed()
        print(closebtn)
        print(closebtn1)

        eyebtn = self.driver.find_element(By.XPATH,"//ion-icon[@slot='end']").is_enabled()
        eyebtn1 = self.driver.find_element(By.XPATH,"//ion-icon[@slot='end']").is_displayed()
        print(eyebtn)
        print(eyebtn1)

        login = self.driver.find_element(By.XPATH,"//*[@id='login']/ion-grid/ion-card/ion-card-content/ion-grid/ion-row[3]/ion-button").is_enabled()
        login1 = self.driver.find_element(By.XPATH,"//*[@id='login']/ion-grid/ion-card/ion-card-content/ion-grid/ion-row[3]/ion-button").is_displayed()
        print(login)
        print(login1)

        time.sleep(2)




