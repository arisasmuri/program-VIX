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

time.sleep(4)
elem = driver.find_element(By.CSS_SELECTOR,"#wrapper > nav > div > div > ul > li:nth-child(2) > a").click()
elem = driver.find_element(By.CSS_SELECTOR,"#wrapper > nav > div > div > ul > li:nth-child(2) > ul > li:nth-child(2) > a").click()
time.sleep(2)
elem = driver.find_element(By.NAME, "select-all-checkbox").click()

elem = driver.find_element(By.CSS_SELECTOR, "#page-wrapper > div.wrapper.wrapper-content > div > div > div > div:nth-child(2) > div > div > div > div > div > div.row > div.col-sm-6.col-lg-8 > div > button.ladda-button.btn.btn-primary.m-l-xs").click()
time.sleep(2)
elem = driver.find_element(By.CSS_SELECTOR, "#page-wrapper > div.wrapper.wrapper-content > div > div > div > div:nth-child(2) > div > div > div > div > div:nth-child(4) > div > div.row.m-t-md > div > div > div:nth-child(2) > div > div.react-grid-Container > div > div > div.react-grid-Header > div > div > div.react-grid-HeaderCell.react-grid-HeaderCell--frozen.rdg-row-actions-cell > div").click()
time.sleep(2)
elem = driver.find_element(By.ID, "x-delete-button").click()
time.sleep(1)
elem = driver.find_element(By.ID, "x-delete-button-confirm").click()

while(True):
    pass