import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("http://localhost:5173/")
driver.maximize_window()

inp = input('Enter your search input: ')

# Find the input element by XPath
input_element = driver.find_element(By.XPATH,"//input")
input_element.send_keys(inp)
input_element.send_keys(Keys.ENTER)

time.sleep(2)

url = driver.current_url

testpass = False

if f"/search/{inp}" in url:
    print("URL contains the substring /search/{inp}")
    testpass = True
else:
    print("URL does not contain the substring /search/{inp}")

if testpass:
    # Find the first checkbox element by XPath
    checkbox_element = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    checkbox_element.click()
    print("Testing passed")
else:
    print("Testing failed")

