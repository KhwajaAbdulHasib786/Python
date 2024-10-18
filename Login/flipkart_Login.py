from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
class findElementByXpath():
    def locate_by_Id(self):
        from selenium.webdriver.chrome.options import Options
        options = Options()

        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.flipkart.com/")
        driver.maximize_window()
        from selenium.webdriver.common.by import By
        inputElement = driver.find_element(By.XPATH,"//input[@class='Pke_EE']")
        inputElement.send_keys("I phone mobile")
        SearchBar = driver.find_element(By.XPATH,"//button[@type='submit']")

        SearchBar.send_keys(Keys.ENTER)
        getPrice = driver.find_element(By.XPATH,"//div[@class='KzDlHZ']")
        print(getPrice)
findbyid = findElementByXpath()
findbyid.locate_by_Id()



#Define Columns Name:
# ColumnsName=["Mobile Name"]
#
# # Write Columns Name to First Row:
# for col_num,col_title in enumerate(ColumnsName,start=1):
#     ws.cell(row=1,column=col_num,value=col_title)
# # Write Data to sheet
#
# for  row_num,row_data in enumerate(M):
#     for col_num,cell_value in enumerate(row_data,)


