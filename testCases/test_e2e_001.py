import os
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
class TestE2E(BaseClass):
    def test_e2e(self):
        log = self.getlogger()
        hp_obj = HomePage(self.driver_obj)
        # We just skipped creating the productdisplay page object as we created & returned it in Homepage itself
        log.info("Clicking on Shop")
        pdp_obj = hp_obj.clickShop()
        log.info("Adding Products to cart")
        pdp_obj.AddingProducts()
        log.info("Clicking on checkout Button to go the ConfirmPage")
        CP_obj = pdp_obj.clickCheckout()
        CP_obj.OC_Checkout().click()
        log.info("Sending the Country as Ind")
        CP_obj.getCountry().send_keys("Ind")
        country_name = CP_obj.getCountryName()
        log.info("Veryfying the link presence")
        self.VerifyLinkPresence(country_name).click()
        CP_obj.clickCheckBox_Agree().click()
        CP_obj.click_Purchase_BTN().click()

        successmsg_text = CP_obj.getSuccessMSG().text
        print(successmsg_text)
        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in successmsg_text
        # if successmsg_text == "Success! Thank you! ":
        #     log.info("Order Success")
        #     assert True
        # else:
        #     self.driver_obj.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_e2e_OrderUnsuccessful.png")
        #     log.info("Order Failed")
        #     assert False

