import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import re
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

class loginMedicaid():
    def Login(self):
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option("detach",True)
        driver = webdriver.Chrome(options = options)
        driver.get("https://portal.indianamedicaid.com/hcp/provider/Home/tabid/135/Default.aspx")
        driver.maximize_window()
        time.sleep(3)
#       fill User Id
        UserId = driver.find_element(By.XPATH, "//input[@type='text']")
        UserId.send_keys("Abhi$2611")
        # Clic On Login Button
        login = driver.find_element(By.XPATH,"//input[@value='Log In']")
        login.click()
        time.sleep(1)

#       getting Challenge Question:
        getText = driver.find_element(By.XPATH,"//span[@id='dnn_ctr1854_ChallengeQuestion_ChallengeQuestionCmnTextBox_ControlLabel']")
        Gettext = getText.text
        print(Gettext)
        Employe = "Who was your first employer?"
        City = "In what city were you born?"
        Sport  = "India"
        # Check The Challenge Question If match The Question then Type the Answer.
        if Gettext in Employe:
            Answer = driver.find_element(By.XPATH,"//input[@name='dnn$ctr1854$ChallengeQuestion$ChallengeResponseCmnTextBox$Control']")
            Answer.send_keys("Pacific")
        elif Gettext in City:
            Answer = driver.find_element(By.XPATH,"//input[@name='dnn$ctr1854$ChallengeQuestion$ChallengeResponseCmnTextBox$Control']")
            Answer.send_keys("Ghaziabad")
        else:
            Answer = driver.find_element(By.XPATH,"//input[@name='dnn$ctr1854$ChallengeQuestion$ChallengeResponseCmnTextBox$Control']")
            Answer.send_keys("India")
        #     Click On Continue.
        Continue = driver.find_element(By.XPATH,"//input[@value='Continue']")
        Continue.click()
        time.sleep(2)
        # Type The Password
        Password = driver.find_element(By.XPATH,"//input[@type='password']")
        Password.send_keys("Hello@12345")
        SignIn = driver.find_element(By.XPATH,"//input[@value ='Sign In']")
        SignIn.click()
        # Click On Ent Angola
        EntAngola = driver.find_element(By.XPATH,"//input[@value='100050300e']")
        EntAngola.click()

        Submit = driver.find_element(By.XPATH,"//div[@class='RowButtons']//input[@value='Submit']")
        Submit.click()
        time.sleep(4)


        # click eligibility
        element = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"a#dnn_DropDownMenu_PrimaryMenuRepeater_PrimaryItemCmnHyperlink_1"))
        )
        element.click()

        # Read input
        df = pd.read_excel("Ent.xlsx")
        for index,row in df.iterrows():

            # policy Number
            policyN = row['Policy Number']
            PolicyNumber = driver.find_element(By.CSS_SELECTOR,"input#dnn_ctr21318_EligibilityVerificationFull_MemberIDCmnTextBox_Control")
            PolicyNumber.clear()
            PolicyNumber.send_keys(policyN)

            # PatientName
            LastName = re.split('\s', row['Patient Name'])[0].replace(",", "")
            lName = driver.find_element(By.CSS_SELECTOR,"input#dnn_ctr21318_EligibilityVerificationFull_LastNameCmnTextBox_Control")
            lName.clear()
            lName.send_keys(LastName)
            FirstName = re.split('\s', row['Patient Name'])[1].replace(",", "")
            fname = driver.find_element(By.CSS_SELECTOR,"input#dnn_ctr21318_EligibilityVerificationFull_FirstNameCmnTextBox_Control")
            fname.clear()
            fname.send_keys(FirstName)

            # DateofBirth
            DateOfBirth = re.split('\s', row['DOB (Age)'])[0]
            dob = driver.find_element(By.CSS_SELECTOR,"input#dnn_ctr21318_EligibilityVerificationFull_BirthDateCmnDate_Control")
            dob.clear()
            dob.send_keys(DateOfBirth)

            # AppointmentDate
            AppintmentDate = re.split('\s', row['Appointment Date'])[0]
            date_obj = datetime.strptime(AppintmentDate, "%m/%d/%y")
            format_date = date_obj.strftime("%m/%d/%Y")
            print(format_date)
            AfDate = driver.find_element(By.CSS_SELECTOR,"input#dnn_ctr21318_EligibilityVerificationFull_DateRangeCmnDateRange_StartDateControl_Control")
            AfDate.clear()
            AfDate.send_keys(format_date)
            AtDate = driver.find_element(By.CSS_SELECTOR,"input#dnn_ctr21318_EligibilityVerificationFull_DateRangeCmnDateRange_EndDateControl_Control")
            AtDate.clear()
            AtDate.send_keys(format_date)
            # submit
            element1 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "input#dnn_ctr21318_EligibilityVerificationFull_SubmitCmnButton"))
            )
            element1.click()
            table_data = []
            first_table = driver.find_element(By.CSS_SELECTOR, 'table:nth-of-type(1)')

            # Extract headers
            headers = [header.text for header in first_table.find_elements(By.TAG_NAME, 'th')]
            table_data.append(headers)

            # Extract rows
            rows = first_table.find_elements(By.TAG_NAME, 'tr')[1:]  # Skip the header row
            for row in rows:
                cols = row.find_elements(By.TAG_NAME, 'td')
                table_data.append([col.text.strip() for col in cols])

            # Create a DataFrame
            df = pd.DataFrame(table_data)



            print("DataFrame:")
            print(df)
            print("Columns:", df.columns)

            # check column exit or not
            if 0 in df.columns:
                if (df[0] == 'Not Eligible').any():
                    print("Inactive")
                else:
                    print("Active")
                    ManagedCare = driver.find_element(By.ID,"dnn_ctr21318_EligibilityVerificationFull_ToggleManagedCareImage")
                    ManagedCare.click()
                    time.sleep(5)


            else:
                print("Column 'Coverage' does not exist in the DataFrame.")


            # Step 7: Close the WebDriver
            # driver.quit()
            break



lgastro = loginMedicaid()
lgastro.Login()


