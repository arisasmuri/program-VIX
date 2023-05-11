from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome()
driver.get("https://app.jubelio.com/login")

elem = driver.find_element(By.NAME, "email")
elem.send_keys("qa.rakamin.jubelio@gmail.com")

elem = driver.find_element(By.NAME, "password")
elem.send_keys("Jubelio123!")

elem = driver.find_element(By.CLASS_NAME,"ladda-label").click()



while(True):
    pass