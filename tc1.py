import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)
driver.get("http://localhost:5173/")
driver.maximize_window()

#Register user (Sucessful)
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

otp = input('Enter your OTP: ')

driver.find_element(By.XPATH, '//input').send_keys('a').send_keys(otp)

driver.find_element(By.ID, 'redeem_otp_btn').click()

time.sleep(5)

print("Testing passed")
driver.quit()