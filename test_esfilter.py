import pytest
from selenium import webdriver
import time

driver=None
@pytest.fixture()
def setup():

    print("launching the browser")
    global driver
    #driver=webdriver.Chrome("C:\Users\ypalanis\PycharmProjects\elasticg42\searchg42\drivers\chromedriver.exe")
    driver = webdriver.Chrome("searchg42/drivers/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    print("produce the resultant output")

@pytest.mark.g42search
def test_login(setup):
    driver.get("https://www.linkedin.com/company/g42ai/")
    time.sleep(10)
    print("g42 elastic search login")


def test_search(setup):
    print("g42 elastic search action")


def test_logout(setup):
    print("g42 elastic search logout")
