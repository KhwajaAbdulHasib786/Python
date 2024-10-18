import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
from selenium.webdriver.common.by import By
searchbox=driver.find_element(By.XPATH,"//input[@type='text']")
searchbox.send_keys("one plus Headphones")
time.sleep(2)
first_option=driver.find_element(By.XPATH,"(//form[contains(@class,'header-form-search OpXDaO')]//a)[1]")
print(first_option.get_attribute("href"))
print(first_option.text)
first_option.click()
print(driver.current_url)
