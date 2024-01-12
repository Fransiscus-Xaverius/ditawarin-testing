import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("http://localhost:5173/")
driver.maximize_window()

# LOGIN USER 
time.sleep(2)

email = input('Enter your email: ')
password = input('Enter your password: ')

driver.find_element(By.ID, 'login-btn').click()
driver.find_element(By.ID, 'email_inp').send_keys(email)
driver.find_element(By.ID, 'pass_inp').send_keys(password)
driver.find_element(By.ID,'submit_btn').click()
time.sleep(2)
driver.switch_to.alert.accept()

print("Testing is done")
driver.quit()