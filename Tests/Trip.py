import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

services_obj = Service(r'C:\Users\Prith\Downloads\Testing\sel\chromedriver.exe')
driver = webdriver.Chrome(service=services_obj)

driver.get("https://www.tripadvisor.in/")


#click on Holiday Homes

HolidayHomes=driver.find_element(By.XPATH,"(//span[@class='biGQs _P ttuOS'])[7]")
HolidayHomes.click()
driver.implicitly_wait(10)
#Display total amount and charges per night for 3 holiday homes:

wait=WebDriverWait(driver,10)
time.sleep(10)
Enter_city=driver.find_element(By.XPATH,"(//input[@title='Search'])[3]")
# wait.until(expected_conditions.presence_of_element_located((Enter_city)))
# driver.find_element(By.CSS_SELECTOR,"qjfqs _G B- z _J Cj R0").send_keys("Pune")
Enter_city.send_keys("Pune")

# Storing dd in list
CityList=driver.find_elements(By.XPATH,"//div[@role='listbox']/a")
for city in CityList:
    if city.text=="Pune":
        city.click()
        break





time.sleep(20)

