import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
s = Service(executable_path="/Users/venkateshr/PycharmProjects/WeightGurus/drivers/chromedriver")

class TestBrowser():
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_LaunchBrowser(self,setup):
        self.driver.get("https://www.selenium.dev/")
        time.sleep(5)
        print("Pass")