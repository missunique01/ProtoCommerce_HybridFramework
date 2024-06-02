import inspect
import os
import pytest
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup")

class BaseClass:
    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        current_log_path = os.path.join(os.getcwd(), "logs", "automationLogs.log")
        filehandlers_obj = logging.FileHandler(current_log_path)
        formatters = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandlers_obj.setFormatter(formatters)
        logger.addHandler(filehandlers_obj)
        logger.setLevel(logging.INFO)
        logger.debug("A debug statement is executed")
        logger.info("Information statement")
        logger.warning("Something is in warning mode")
        logger.error("A Major error has happened")
        logger.critical("Critical")
        return logger
    def VerifyLinkPresence(self, text):
        element = WebDriverWait(self.driver_obj, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))
        return element
    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)


