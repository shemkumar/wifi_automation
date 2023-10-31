from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("#ipadress of wifi login page")

username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "username"))
)
username.send_keys("#username")
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "password"))
)
password.send_keys("pass")
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "loginbutton"))
)
login_button.click()
import time
time.sleep(5)
driver.quit()
