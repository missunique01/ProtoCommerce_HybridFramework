from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass

class ConfirmPage:
    # Locators
    checkout_btn_css = (By.CSS_SELECTOR, "button[class='btn btn-success']")
    txt_country_id = (By.ID, "country")
    txt_country_india_lnktxt = "India"
    box_checkbox_xpath = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    btn_purchase_css = (By.CSS_SELECTOR, "input[class*='btn-success']")
    success_msg_css = (By.CSS_SELECTOR, "div[class*='alert-success']")

    # Constructor
    def __init__(self, driver_obj):
        self.driver_obj = driver_obj

    # Action Methods
    def OC_Checkout(self):
        return self.driver_obj.find_element(*ConfirmPage.checkout_btn_css)

    def getCountry(self):
        return self.driver_obj.find_element(*ConfirmPage.txt_country_id)
    def getCountryName(self):
        return ConfirmPage.txt_country_india_lnktxt

    def clickCheckBox_Agree(self):
        return self.driver_obj.find_element(*ConfirmPage.box_checkbox_xpath)

    def click_Purchase_BTN(self):
        return self.driver_obj.find_element(*ConfirmPage.btn_purchase_css)

    def getSuccessMSG(self):
        return self.driver_obj.find_element(*ConfirmPage.success_msg_css)