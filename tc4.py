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

# Register user (Unsuccessful - Account not validated)
time.sleep(2)

email = input('Enter your email: ')
password = input('Enter your password: ')
phone = input('Enter your phone number: ')

driver.find_element(By.ID, 'register-btn').click()
driver.find_element(By.ID, 'fullname_inp').send_keys('Test User')
driver.find_element(By.ID, 'email2_inp').send_keys(email)
driver.find_element(By.ID, 'phone_inp').send_keys(phone)
driver.find_element(By.ID, 'password_inp').send_keys(password)

driver.find_element(By.ID, 'address_inp').send_keys('Jl. Test')
driver.find_element(By.ID, 'city_inp').send_keys('Test')
driver.find_element(By.ID, 'province_inp').send_keys('Test')
driver.find_element(By.ID, 'confirm_inp').send_keys(password)

time.sleep(2)

driver.find_element(By.ID, 'submit_regis').click()

time.sleep(5)

driver.find_element(By.ID, 'login-btn').click()

time.sleep(2)

driver.find_element(By.ID, 'email_inp').send_keys(email)
driver.find_element(By.ID, 'pass_inp').send_keys(password)

driver.find_element(By.ID, 'submit_btn').click()

time.sleep(2)

if driver.find_element(By.ID, 'redeem_otp_btn'):
    print('Testing passed')
else:
    print('Testing failed')

time.sleep(2)

driver.quit()