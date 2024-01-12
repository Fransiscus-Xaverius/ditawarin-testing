import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)
driver.get("http://localhost:5173/")
driver.maximize_window()

# REGISTER USER (FAILED)
time.sleep(2)

driver.find_element(By.ID, 'register-btn').click()
driver.find_element(By.ID, 'submit_regis').click()

testpass = False

if driver.find_elements(By.XPATH, '//p[@style="color: red;"]'):
    print("Warning Element exists")
    testpass = True
else:
    print("Element does not exist")

if testpass:
    print("Testing passed")
else:
    print("Testing failed")

time.sleep(2)

driver.quit()
