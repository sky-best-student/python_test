from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/inputs")
driver.find_element(By.XPATH, "//input[@type='number']").send_keys("1000")
sleep(3)
driver.find_element(By.XPATH, "//input[@type='number']").clear()
sleep(3)
driver.find_element(By.XPATH, "//input[@type='number']").send_keys("999")
sleep(3)
driver.quit()



