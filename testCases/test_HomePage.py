import pytest

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from testData.HomePageData import HomePageData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getlogger()
        hp_obj = HomePage(self.driver_obj)
        log.info("Passing name")
        hp_obj.getName().send_keys(getData["Name"])
        log.info("Passing Email")
        hp_obj.getEmail().send_keys(getData["Email"])
        log.info("Passing Password")
        hp_obj.getPassword().send_keys(getData["Password"])
        log.info("Clicking Checbox")
        hp_obj.clickCheckBox().click()
        log.info("Selecting Gender")
        self.selectOptionByText(hp_obj.selectGender(), getData["Gender"])
        log.info("Selecting Employee status")
        hp_obj.getEmpStatus().click()
        log.info("Submitting the Form")
        hp_obj.SubmitForm().click()
        success_msg_text = hp_obj.getSuccess_message().text
        print(success_msg_text)
        log.info("Checking the Success message")
        assert "Success" in success_msg_text
        log.info("Refreshing the Webpage for passing new data ")
        self.driver_obj.refresh()
    # Data Driven Testing
    @pytest.fixture(params=HomePageData.getTestData("TestCase2"))
    def getData(self, request):
        return request.param
