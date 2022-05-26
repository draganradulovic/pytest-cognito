from selenium import webdriver


def WebDriverFactory(browser):
    browser.lower()
    if browser=='chrome':
        driver = webdriver.Chrome(executable_path=r"C:\Program Files\Chromedriver\chromedriver.exe")
    elif browser=='firefox':
        driver = webdriver.Firefox(executable_path=r"C:\Program Files\Mozilladriver\geckodriver.exe")
    else:
        driver = webdriver.Chrome(executable_path=r"C:\Program Files\Chromedriver\chromedriver.exe")

    return driver