from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select
import time
# if select Attribute is available in html page then do like it
# static_Dropdown=driver.find_element(By.ID,"dropdown-class-example")
# select=Select(static_Dropdown)
# select.select_by_index(1)
# time.sleep(2)
# select.select_by_value("option2")
# time.sleep(1)
# select.select_by_visible_text("Option3")
# *****************************************************

dropdown=driver.find_element(By.XPATH,"//option[@value='option2']")
dropdown.click()
