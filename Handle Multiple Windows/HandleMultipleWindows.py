import time

from  selenium import webdriver
from selenium.webdriver.common.by import By


class Handle():
    def Windows(self, themeSnipe=None):
        from  selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option("detach",True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        Parent_Handle = driver.current_window_handle
        time.sleep(2)

        american =driver.find_element(By.XPATH,"/html/body/div[2]/div/section/div[2]/section[4]/div/div[2]/div/div[1]/div/a[2]/div/img")
        american.click()
        All_Handel = driver.window_handles
        print(All_Handel)
        for Handle in All_Handel:
            if Handle !=Parent_Handle:
                driver.switch_to.window(Handle)
                time.sleep(2)
                cabs = driver.find_element(By.XPATH,"//a[@id='booking_engine_cabs']")
                cabs.click()
                time.sleep(2)
                driver.close()
                time.sleep(2)
                break
        driver.switch_to.window(Parent_Handle)
        american = driver.find_element(By.XPATH,"/html/body/div[2]/div/section/div[2]/section[4]/div/div[2]/div/div[1]/div/a[2]/div/img")
        american.click()


windows = Handle()
windows.Windows()

