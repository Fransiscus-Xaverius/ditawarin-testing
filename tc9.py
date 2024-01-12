import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("http://localhost:5173/")
driver.maximize_window()

# LOGIN USER (Failed - Not registered)
time.sleep(2)

email = 'jakdasjdiejoqweifej'
password = '12345678'

driver.find_element(By.ID, 'login-btn').click()
driver.find_element(By.ID, 'email_inp').send_keys(email)
driver.find_element(By.ID, 'pass_inp').send_keys(password)
driver.find_element(By.ID,'submit_btn').click()
time.sleep(2)
driver.switch_to.alert.accept()

if driver.find_element(By.ID, 'submit_btn'):
    print("Testing passed")
else:
    print("Testing failed")

driver.quit()