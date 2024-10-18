# from  openpyxl import Workbook
# wb = Workbook()
# ws = wb.active
#
# # define Columns Name:
#
# ColumnsName = ['Name',"Age","Email"]
#
# # Write Column Name to first row:
#
# for col_num,col_title in enumerate(ColumnsName,start=1):
#     ws.cell(row=1,column=col_num,value=col_title)
#
#
# # define data:
# data = [
#     ("John Doe", 30, "john.doe@example.com"),
#     ("Jane Smith", 25, "jane.smith@example.com"),
#     ("Emily Johnson", 35, "emily.johnson@example.com")
# ]
#
# for row_num,row_data in enumerate(data,start=2):
#     for col_num,cell_value in enumerate(row_data,start=1):
#         ws.cell(row=row_num,column=col_num,value=cell_value)
# wb.save('Practice.xlsx')
import datetime
# import time
#
# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# class DemoEnable():
#     def Demo(self):
#         from selenium.webdriver.chrome.options import Options
#         options = Options()
#         options.add_experimental_option("detach", True)
#         driver = webdriver.Chrome(options=options)
#         driver.get("https://training.openspan.com/login")
#         driver.maximize_window()
#         time.sleep(2)
#         checkSigninEnableOrNot=driver.find_element(By.XPATH,"//input[@value='Sign In']").is_enabled()
#         print(checkSigninEnableOrNot)
#         if checkSigninEnableOrNot is True:
#             print("SignIn Button is Enabled")
#         else:
#             print("SignIn button is Disabled")
#             Username = driver.find_element(By.XPATH,"//input[@placeholder='User Name']")
#             Username.send_keys("Khwaja")
#             time.sleep(2)
#             Password = driver.find_element(By.XPATH,"//input[@placeholder='Password']")
#             Password.send_keys("hasib")
#             time.sleep(2)
#             click = driver.find_element(By.XPATH,"//input[@type='submit']")
#             click.click()
#             # driver.quit()
#
#         class DemoDisplayed():
#             def demoD(self):
#                 checkElement = driver.find_element(By.XPATH,"//a[text()='Home']")
#                 checkElement.is_displayed()
#
#                 print(checkElement)
#                 if checkElement is True:
#                     print("item Is present")
#                 else:
#                     print("Item is not present")
#         Ddisplayd = DemoDisplayed()
#         Ddisplayd.demoD()

# DEnable = DemoEnable()
# DEnable.Demo()





#
# import pandas as pd
#
# # Load the Excel file into a DataFrame
# file_path = 'Input.xlsx'  # Replace with your file path
# df = pd.read_excel(file_path)
#
# # Define the columns you want to read
# columns_to_read = ['Patient Name', 'DOB (Age)', 'MRN']  # Replace with your column names
#
# # Check if the columns exist in the DataFrame
# missing_columns = [col for col in columns_to_read if col not in df.columns]
# if missing_columns:
#     print(f"Columns not found: {', '.join(missing_columns)}")
# else:
#     # Iterate over each row in the DataFrame
#     for index, row in df.iterrows():
#         print(f"Row {index + 1}:")
#         # Print values from each specified column for the current row
#         for column in columns_to_read:
#             print(f"  {column}: {row[column]}")
#         print()  # Add an empty line between rows for better readability





# import pandas as pd
#
# # Load the Excel file into a DataFrame
# file_path = 'Input.xlsx'  # Replace with your file path
# df = pd.read_excel(file_path, sheet_name='Rerun')  # Specify sheet name if necessary
#
# # List of columns you want to access
# columns_to_read = ['Patient Name', 'DOB (Age)', 'MRN']  # Replace with your column names
#
# # Check if all specified columns exist in the DataFrame
# missing_columns = [col for col in columns_to_read if col not in df.columns]
# if missing_columns:
#     print(f"Columns not found: {', '.join(missing_columns)}")
# else:
#     # Iterate over each row in the DataFrame
#     for index, row in df.iterrows():
#         print(f"Row {index + 1}:")
#         # Print values from each specified column for the current row
#         for column in columns_to_read:
#             name = row[column]
#             print(name)
#
#         print()  # Add an empty line between rows for better readability


# import pandas as pd
#
# # Load the Excel file into a DataFrame
# file_path = 'Input.xlsx'  # Replace with your file path
# df = pd.read_excel(file_path)
#
# # Define the column name you want to read
#   # Replace with your column name
#
# # Check if the column exists in the DataFrame
# print(df)
# for value in df:
#     print(value)


# import pandas as pd
#
# # Load the CSV file into a DataFrame
# file_path = 'Input.xlsx'  # Replace with the path to your file
# df = pd.read_excel(file_path)
#
# # Iterate over each row in the DataFrame
# for index, row in df.iterrows():
#    patientName = row['Patient Name']
#    dob_age = row['DOB (Age)']
#    print(patientName)
#    print(dob_age)

#
# a= 5
# b = 6
# c = 10
# if a > b:
#    print("A is greater than B")
# elif b>a:
#    print("B is Greater than A")
# else:
#    print("C is Greater Than A,B")



import time
from selenium.webdriver.support import expected_conditions as EC

import re

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Step 1: Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Step 2: Open the web page
url = 'https://portal.indianamedicaid.com/hcp/provider/Home/tabid/135/Default.aspx'  # Replace with the actual URL containing multiple tables
driver.get(url)
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



#     print("selector not found")

# click eligibility
element = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"a#dnn_DropDownMenu_PrimaryMenuRepeater_PrimaryItemCmnHyperlink_1"))
)
element.click()

# Read input
df = pd.read_excel("Ent.xlsx")
for index,row in df.iterrows():
    print()
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
    time.sleep(3)

#   fill User Id
    UserId = driver.find_element(By.XPATH, "//input[@type='text']")
    UserId.send_keys("Abhi$2611")
    # Clic On Login Button
    login = driver.find_element(By.XPATH,"//input[@value='Log In']")
    login.click()
    time.sleep(1)

#      getting Challenge Question:
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





