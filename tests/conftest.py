from selenium import webdriver
import unittest
import pytest
from config.webdriverfactory import WebDriverFactory

@pytest.fixture(scope='class')
def oneTimeSetUp(browser,request):
    print("Once before class")
    global driver
    driver = WebDriverFactory(browser)
    driver.maximize_window()
    driver.implicitly_wait(10)

    if request.cls is not None:
        request.cls.driver=driver


    yield driver
    print("Once after class")
    driver.close()

@pytest.fixture()
def setUp7():
    print("Before every test")
    driver.get("https://www.cognitoforms.com/Tina8/CreateNew")
    yield
    print("After every test")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

