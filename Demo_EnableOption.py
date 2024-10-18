import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
class DemoEnable():
    def Demo(self):
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://training.openspan.com/login")
        driver.maximize_window()
        time.sleep(2)
        checkSigninEnableOrNot = driver.find_element(By.XPATH,"//input[@value='Sign In']").is_enabled()
        print(checkSigninEnableOrNot)
        if checkSigninEnableOrNot is True:
            print("SignIn Button is Enabled")
        else:
            print("SignIn button is Disabled")
            Username = driver.find_element(By.XPATH,"//input[@placeholder='User Name']")
            Username.send_keys("Khwaja")
            time.sleep(2)
            Password = driver.find_element(By.XPATH,"//input[@placeholder='Password']")
            Password.send_keys("hasib")
            time.sleep(2)
            click = driver.find_element(By.XPATH,"//input[@type='submit']")
            click.click()
            # driver.quit()

        class DemoDisplayed():
            def demoD(self):
                checkElement = driver.find_element(By.XPATH,"//h1[text()='ACME Product Search System']")
                print(checkElement)
                checkElement = checkElement.text
                if "ACME Product Search System" in checkElement:
                    print("item Is present")
                else:
                    print("Item is not present")
        Ddisplayd = DemoDisplayed()
        Ddisplayd.demoD()



DEnable = DemoEnable()
DEnable.Demo()


