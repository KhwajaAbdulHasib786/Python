from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
from selenium.webdriver.common.by import By
get_Attribute=driver.find_element(By.XPATH,"//a[starts-with(@class,'blinkingText')]")
print(get_Attribute.get_attribute("href"))