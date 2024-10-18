import time
from selenium.webdriver.common.by import By
from selenium .webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.flipkart.com/")
driver.maximize_window()

inputdata = driver.find_element(By.XPATH, "//input[@type='text']")
inputdata.send_keys("One Plus headphones")
time.sleep(2)
dropdown_option = driver.find_element(By.XPATH, "(//form[@class='_2rslOn header-form-search OpXDaO']//a)[1]")
dropdown_option.click()
action = ActionChains(driver, duration=2000)
action.move_to_element(driver.find_element(By.XPATH, "//div[text()='More']")).double_click().perform()
action.click(driver.find_element(By.XPATH, "//a[contains(@class,'IKoe2r')]")).perform()
