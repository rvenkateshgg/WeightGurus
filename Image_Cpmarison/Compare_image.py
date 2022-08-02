import glob
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from PIL import Image, ImageChops, ImageStat

import time
s = Service(executable_path="../drivers/chromedriver")

input_logo = '../input/0345.png'
output_logo = '../output/0345.png'
comparison_result = 'output/result1.png'


def clear_result():
    files = glob.glob('output/*')
    for f in files:
        os.remove(f)


def capture_image():
    driver = webdriver.Chrome(service=s)
    driver.get("http://192.168.0.103:8102/landing")
    driver.maximize_window()
    driver.implicitly_wait(5)
    time.sleep(3)
    driver.find_element(By.XPATH,"//ion-button[@color='primary']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//ion-input[@type='email']/input").send_keys("venkateshrv307@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='ion-input-1']").send_keys("Venkat@2000")
    time.sleep(2)
    driver.find_element(By.XPATH, "//ion-button[@size='large']").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//ion-tab-button[@tab='settings']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//ion-label[@class='sc-ion-label-md-h sc-ion-label-md-s md hydrated'])[9]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@class='native-input sc-ion-input-md']").send_keys("0345")
    time.sleep(1)
    driver.find_element(By.XPATH,"(//ion-button[@color='primary'])[3]").click()
    time.sleep(2)
    with open(output_logo,'wb') as file:
         file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0341.png']").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0342.png']").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0343.png']").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0345.png']").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0346.png']").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0347.png']").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0358.png']").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0359.png']").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0364.png']").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0369.png']").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0370.png']").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0371.png']").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0375.png']").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0376.png']").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"(//img[@src='assets/img/scales/0383.png'])[1]").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0380.png']").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0382.png']").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"(//img[@src='assets/img/scales/0383.png'])[2]").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0384.png']").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0385.png']").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0396.png']").screenshot_as_png)
         #file.write(driver.find_element(By.XPATH,"//img[@src='assets/img/scales/0396.png']").screenshot_as_png)

    img1 = Image.open(input_logo)
    img2 = Image.open(output_logo)
    logoresult = ImageChops.difference(img1,img2)
    stat = ImageStat.Stat(logoresult)
    diff_value = sum(stat.mean)
    print(diff_value)
    if diff_value > 1:
        result = "FAIL"
        print(result)
    else:
        result = "PASS"
        print(result)
        logoresult.show()
        logoresult.save(comparison_result)

    driver.close()
    driver.quit()


if __name__ == '__main__':
    clear_result()
    capture_image()

