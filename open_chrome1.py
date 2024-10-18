from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()

options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
from selenium.webdriver.common.by import By
# input_field = driver.find_element(By.XPATH,"//input[@id='name']")
# input_field.send_keys("Khwaja")
# input_field.clear()
# input_field.send_keys("Hasib")
# Alert_Example=driver.find_element(By.XPATH,"//legend[text()='Switch To Alert Example']")
# alert_example=Alert_Example.text
# print(alert_example)
# instructor_name=driver.find_element(By.XPATH,"//td[text()='Rahul Shetty']")
# Instructor_Name=instructor_name.text
# print(Instructor_Name)

# ****************************************
#how to click multiple checkbox
#
# checkbox=driver.find_elements(By.XPATH,"//input[starts-with(@name,'checkBoxOption')]")
#
# print(checkbox)
# print(len(checkbox))
# for checkboxes in checkbox:
#     checkboxes.click()



#**********************
# Another way to click multiple checkbox

# checkbox=driver.find_elements(By.XPATH,"//input[starts-with(@name,'checkBoxOption')]")
# for checkboxes in checkbox:
#     if checkbox.index(checkboxes)+1 !=2:
#         checkboxes.click()

# ******************************
# this is another way to select multiple checkbox by using xpath-position method
checkbox=driver.find_elements(By.XPATH,"(//input[starts-with(@name,'checkBoxOption')])[position()<4]")
for checkboxes in checkbox:
    checkboxes.click()




