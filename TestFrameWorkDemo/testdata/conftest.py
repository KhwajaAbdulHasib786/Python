import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
@pytest.fixture(scope="class")
def setup(request):
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver,10)
    driver.get("https://portal.indianamedicaid.com/hcp/provider/Home/tabid/135/Default.aspx")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait

    yield
    driver.close()
