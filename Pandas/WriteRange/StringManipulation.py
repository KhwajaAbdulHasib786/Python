#
# import re
# import  pandas as pd
# df = pd.read_excel("Ent.xlsx")
# for index,row in df.iterrows():
#     policyN = row['Policy Number']
#     print(policyN)
#     LastName = re.split('\s',row['Patient Name'])[0].replace(",","")
#     print(LastName)
#     FirstName = re.split('\s',row['Patient Name'])[1].replace(",","")
#     print(FirstName)
#     # lastName = re.split('\s',PatientName)
#     # print(lastName[0].replace(",",""))
#     # FirstName = lastName[1].replace(",","")
#     # print(FirstName)
#     DateOfBirth = re.split('\s',row['DOB (Age)'])[0]
#     from datetime import datetime
#
#
#     AppintmentDate = re.split('\s', row['Appointment Date'])[0]
#     print(AppintmentDate)
#     date_obj =datetime.strptime(AppintmentDate,"%m/%d/%y")
#     format_date = date_obj.strftime("%m/%d/%Y")

    # print(format_date)

# from datetime import datetime
#
# # Original date string
# date_str = "9/27/24"
#
# # Convert the string to a datetime object
# date_obj = datetime.strptime(date_str, "%m/%d/%y")
#
# # Format the datetime object to the desired string format
# formatted_date = date_obj.strftime("%m/%d/%Y")
#
# # Print the result

# print(formatted_date)  # Output: 09/27/2024

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import re
from datetime import datetime
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://portal.indianamedicaid.com/hcp/provider/Home/tabid/135/Default.aspx")
driver.maximize_window()
time.sleep(3)