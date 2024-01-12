import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)
driver.get("http://localhost:5173/")
driver.maximize_window()