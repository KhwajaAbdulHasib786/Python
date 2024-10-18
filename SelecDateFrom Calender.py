import time

from  selenium import webdriver

from selenium.webdriver.common.by import By

class SelectDate():
    def Auto(self):
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options = options)
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(1)
        Date = driver.find_element(By.XPATH, " //input[@id='BE_flight_origin_date']")
        Date.click()

        selectDate = driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        print(selectDate)
        for x in selectDate:
            print(x)
        # for date in selectDate:
        #     if date.get_attribute("data-date") == "18/09/2024":
        #         date.click()
        #         break

Date = SelectDate()
Date.Auto()