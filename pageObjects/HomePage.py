from selenium.webdriver.common.by import By
from pageObjects.ProductDisplayPage import ProductDisplayPage
from selenium.webdriver.support.select import Select

class HomePage:
    # Locators
    lnk_shop_css = (By.CSS_SELECTOR, "a[href*='shop']")
    txtbox_name_css = (By.CSS_SELECTOR, "[name='name']")
    txtbox_email_name = (By.NAME, "email")
    txtbox_password_id = (By.ID, "exampleInputPassword1")
    checkbox_id = (By.ID,"exampleCheck1")
    gender_id = (By.ID, "exampleFormControlSelect1")
    radio_btn_css = (By.CSS_SELECTOR, "#inlineRadio1")
    dob_xpath = (By.XPATH, "//input[@name='bday']")
    submit_btn_xpath = (By.XPATH, "//input[@type='submit']")
    msg_classname = (By.CLASS_NAME, "alert-success")

    # Constructors
    def __init__(self,driver_obj):
        self.driver_obj = driver_obj
    # Action Methods
    def clickShop(self):
        self.driver_obj.find_element(*HomePage.lnk_shop_css).click()
        pdp_obj = ProductDisplayPage(self.driver_obj)
        return pdp_obj
    def getName(self):
        return self.driver_obj.find_element(*HomePage.txtbox_name_css)
    def getEmail(self):
        return self.driver_obj.find_element(*HomePage.txtbox_email_name)
    def getPassword(self):
        return self.driver_obj.find_element(*HomePage.txtbox_password_id)
    def clickCheckBox(self):
        return self.driver_obj.find_element(*HomePage.checkbox_id)
    def selectGender(self):
        return self.driver_obj.find_element(*HomePage.gender_id)
    def getEmpStatus(self):
        return self.driver_obj.find_element(*HomePage.radio_btn_css)

    def getDOB(self):
        return self.driver_obj.find_element(*HomePage.dob_xpath)

    def SubmitForm(self):
        return self.driver_obj.find_element(*HomePage.submit_btn_xpath)

    def getSuccess_message(self):
        return self.driver_obj.find_element(*HomePage.msg_classname)