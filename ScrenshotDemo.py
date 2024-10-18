import time

from  selenium import webdriver

from selenium.webdriver.common.by import By

class ScreenShotDemo():
    def Screen(self):
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options = options)
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(2)
        SearchFlight = driver.find_element(By.XPATH,"//input[@value='Search Flights']")
        SearchFlight.screenshot(".\\hasib.png")
        SearchFlight.click()
        driver.get_screenshot_as_file(".\\Hasib1.png")



screen = ScreenShotDemo()
screen.Screen()