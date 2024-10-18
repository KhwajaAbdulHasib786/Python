from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
options = webdriver.ChromeOptions()
# Add any desired options here

# Initialize the Chrome driver
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

# Open a webpage
driver.get("http://www.example.com")

# Close the browser
driver.quit()
