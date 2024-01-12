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
driver.find_element(By.ID, 'productname_inp').send_keys('test item')
driver.find_element(By.ID, 'startprice_inp').send_keys('10000')
driver.find_element(By.ID, 'askprice_inp').send_keys('20000')
driver.find_element(By.ID, 'kec_inp').send_keys('Wiyung')
driver.find_element(By.ID, 'kota_inp').send_keys('Surabaya')
driver.find_element(By.ID, 'prov_inp').send_keys('Jawa Timur')

driver.find_element(By.XPATH, "//input[@type='checkbox']").click()

driver.find_element(By.ID, 'tanggal_selesai').send_keys('12-12-2024')
driver.find_element(By.ID, 'jam_selesai').send_keys('12:00')

driver.find_element(By.ID, 'desc_inp').send_keys('test description')

input('Input anything to continue: ')

driver.find_element(By.ID, 'add_btn').click()

time.sleep(1)

driver.find_element(By.ID, 'ubah_btn').click()

time.sleep(1)
driver.find_element(By.ID, 'edit_btn').click()
time.sleep(1)

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

driver.quit()

