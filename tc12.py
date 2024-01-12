import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
from selenium.webdriver.support.ui import WebDriverWait

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

print("login is done")

#sell item section
time.sleep(2)

driver.find_element(By.ID, 'sell_btn').click()
driver.find_element(By.ID, 'add_btn').click()

time.sleep(1)

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