from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome('c:/chromedriver/chromedriver.exe', options=chrome_options)
driver.get("https://demo.guru99.com/test/newtours/index.php")
#assert "Python" in driver.title
elem = driver.find_element(By.NAME, "userName")
elem.send_keys("Pedro27")
elem = driver.find_element(By.NAME, "password")
elem.send_keys("221103")
elem = driver.find_element(By.NAME, "submit")
elem.click()
assert "Enter your userName and password correct" in driver.page_source
#driver.close()