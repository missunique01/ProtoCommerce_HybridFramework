# Setup method for browser invocation
import os
from datetime import datetime
import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver
driver_obj = None
# Special Hook for checking additional command in the command prompt
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action = "store", default = "chrome"
    )
#Special Fixture and it will retrieve the data from the command prompt & return the Browser value to setup
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
# Pass browser to the setup method
@pytest.fixture(scope="class")
def setup(request):
    global driver_obj
    browser = request.config.getoption("--browser")
    if browser.startswith("chrome"):
        from selenium.webdriver.chrome.options import Options
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        # if browser == "chrome--headless":
        #     options.add_argument("--headless=new")
        driver_obj = webdriver.Chrome(options=options)
    elif browser.startswith("edge"):
        from selenium.webdriver.edge.options import Options
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach",True)
        if browser == "edge--headless":
            options.add_argument("--headless=new")
        driver_obj = webdriver.Edge(options=options)
    elif browser == "firefox":
        from webdriver_manager import Firefox
        from webdriver_manager.firefox import GeckoDriverManager
        driver_obj = webdriver.Firefox(GeckoDriverManager.install())
    # Opening the webpage
    driver_obj.implicitly_wait(10)
    driver_obj.get("https://rahulshettyacademy.com/angularpractice/")
    driver_obj.maximize_window()
    # request is the instance variable of setup method using this we are accessing
    # the Test class's driver and assigning it to driver
    # Assigning our local driver of this fixture to the class driver
    request.cls.driver_obj = driver_obj  # return driver_obj
    yield
    driver_obj.close()

## Specifying report folder location and save report with timestamp
# For generating the HTML Report we need to add fixtures and HOOKS
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config.option.htmlpath = (os.path.abspath(os.curdir) + "\\reports\\"
                                  + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + "_report.html")
    config.stash[metadata_key]["Project Name"] = "Proto E-Commerce Application"
    config.stash[metadata_key]["Module Name"] = "Shop Module"
    config.stash[metadata_key]["Tester Name"] = "Nazma"
# It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


