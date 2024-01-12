import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("http://localhost:5173/")
driver.maximize_window()

# LOGIN USER (Failed - No input)
time.sleep(2)

driver.find_element(By.ID, 'login-btn').click()
driver.find_element(By.ID,'submit_btn').click()
time.sleep(2)

if driver.find_elements(By.XPATH, '//p[@style="color: red;"]'):
    print("Warning Element exists")
    testpass = True
else:
    print("Element does not exist")

if testpass:
    print("Testing passed")
else:
    print("Testing failed")

driver.quit()