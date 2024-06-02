from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage

class ProductDisplayPage:
    # Locators
    products_xpath = (By.XPATH, "//div[@class='card h-100']")
    title_xpath = (By.XPATH, "div/h4/a")
    prod_add_btn_xpath = (By.XPATH,"div/button")
    btn_checkout_css = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    # Constructor
    def __init__(self, driver_obj):
        self.driver_obj = driver_obj

    # Action Methods
    def AddingProducts(self):
        products = self.driver_obj.find_elements(ProductDisplayPage.products_xpath)
        for product in products:
            product_title = product.find_element(ProductDisplayPage.title_xpath)
            if product_title.text == "Blackberry":
                product.find_element(ProductDisplayPage.prod_add_btn_xpath).click()
    def clickCheckout(self):
        self.driver_obj.find_element(ProductDisplayPage.btn_checkout_css).click()
        CP_obj = ConfirmPage(self.driver_obj)
        return CP_obj