# import time
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
import time

import  pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class loginGastro():
    def Login(self):

        # fill User Id
        UserId = self.driver.find_element(By.XPATH, "//input[@type='text']")
        UserId.send_keys("Abhi$2611")
        # Clic On Login Button
        login = self.driver.find_element(By.XPATH,"//input[@value='Log In']")
        login.click()
        time.sleep(1)

        # getting Challenge Question:
        getText = self.driver.find_element(By.XPATH,"//span[@id='dnn_ctr1854_ChallengeQuestion_ChallengeQuestionCmnTextBox_ControlLabel']")
        Gettext = getText.text
        print(Gettext)
        Employe = "Who was your first employer?"
        City = "In what city were you born?"
        Sport  = "India"
        # Check The Challenge Question If match The Question then Type the Answer.
        if Gettext in Employe:
            Answer = self.driver.find_element(By.XPATH,"//input[@name='dnn$ctr1854$ChallengeQuestion$ChallengeResponseCmnTextBox$Control']")
            Answer.send_keys("Pacific")
        elif Gettext in City:
            Answer = self.driver.find_element(By.XPATH,"//input[@name='dnn$ctr1854$ChallengeQuestion$ChallengeResponseCmnTextBox$Control']")
            Answer.send_keys("Ghaziabad")
        else:
            Answer = self.driver.find_element(By.XPATH,"//input[@name='dnn$ctr1854$ChallengeQuestion$ChallengeResponseCmnTextBox$Control']")
            Answer.send_keys("India")
        #     Click On Continue.
        Continue = self.driver.find_element(By.XPATH,"//input[@value='Continue']")
        Continue.click()
        time.sleep(2)
        # Type The Password
        Password = self.driver.find_element(By.XPATH,"//input[@type='password']")
        Password.send_keys("Hello@12345")
        SignIn = self.driver.find_element(By.XPATH,"//input[@value ='Sign In']")
        SignIn.click()
        # Click On Ent Angola
        EntAngola = self.driver.find_element(By.XPATH,"//input[@value='100050300e']")
        EntAngola.click()
        # Submit
        Submit = self.driver.find_element(By.XPATH,"//div[@class='RowButtons']//input[@value='Submit']")
        Submit.click()
        time.sleep(4)

        # dnn_QuickLinkMenu_RedirectCmnPopupConfirmation_vdcZuaib_OKButton
        # dnn_QuickLinkMenu_RedirectCmnPopupConfirmation_ytj6kPTh_OKButton


        try:
            element = self.WebDriverWait(self.driver, 10).until(
                self.EC.element_to_be_clickable(By.XPATH,"//input[@src='/hcp/portals/_default/skins/ushc-default/images/icon_close1.gif']"))
            for i in element:
                print(i)




        except Exception as e:
            print("Element not found:", e)

        finally:
            print("selector not found")


# lgastro = loginGastro()
# lgastro.Login()


# lunch the gastro portal
# provide user id
# login
# challenge question
# continue
# password
# entangola
# submit
