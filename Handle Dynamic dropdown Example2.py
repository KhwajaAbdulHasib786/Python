from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
import time
from selenium.webdriver.common.by import By
searchbox=driver.find_element(By.XPATH,"//input[@type='text']")
searchbox.send_keys("one plus")
time.sleep(2)
dropdown_option=driver.find_elements(By.XPATH,"//form[contains(@class,'_2rslOn header-form-search OpXDaO')]//a")
for index,option in enumerate(dropdown_option):
    print(f"link present in{index+1} option:{option.get_attribute('href')}")
    print(f"text present in {index+1} option:{option.text}")
    if "headphones" in option.text:
        option.click()
        break
else:
   print("headphones not present in dropdown")