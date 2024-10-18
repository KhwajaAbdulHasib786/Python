import time

from  selenium import webdriver
from selenium.webdriver.common.by import By


class DemoIframe():
    def Iframe(self, themeSnipe=None):
        from  selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option("detach",True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.yatra.com/")
        driver.maximize_window()



iframe = DemoIframe
iframe.Iframe()
