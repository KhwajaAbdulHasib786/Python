import time

from  selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Medicare():
    def Login(self):
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        url ='https://apps.availity.com/web/onboarding/availity-fr-ui/#/login'
        driver.get(url)
        driver.maximize_window()


        # Fill UserName
        userID='akandwal2'
        UserName=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,'userId')))
        UserName.clear()
        UserName.send_keys(userID)

        # fill  Password
        Password='Jorie@2026'
        pas = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@id='password-field']")))
        pas.clear()
        pas.send_keys(Password)

        # click on sign button
        driver.find_element(By.XPATH,"//button[@class='flex-fill btn btn-primary']").click()
        # Authentication
        auth= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@id='elect-Authenticate me using my Authenticator app-0-radio']")))
        auth.click()
        # Continue
        time.sleep(10)
        driver.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()
        # Wait for authentication
        #Eligibility and benefit
        driver.find_element(By.CLASS_NAME,".card-title.ng-binding:first-of-type").click()


medicare =Medicare()
medicare.Login()