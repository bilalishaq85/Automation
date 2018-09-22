from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Selunium_Automation.Lib.LogConfig import Logger
from Selunium_Automation.Lib.WebDriverSetup import Web
from Selunium_Automation.Lib.SiteElement import SiteElement


class PageElements(object):
    # ******************************************************************************************************************
    #                         Checking if the element is present & then setting the element value
    # ******************************************************************************************************************

    @staticmethod
    def FindElementByLocator(pgnameattr, elekeystr):
        locatorType = SiteElement.getSearchBy(pgnameattr, elekeystr)
        locatorValue = SiteElement.getSearchValue(pgnameattr, elekeystr)

        if locatorType == 'id':
            return Web.driver.find_element_by_id(locatorValue)

        elif locatorType == 'class':
            return Web.driver.find_element_by_class_name(locatorValue)

        elif locatorType == 'plink':
            return Web.driver.find_element_by_partial_link_text(locatorValue)

        elif locatorType == 'xpath':
            return Web.driver.find_elements_by_xpath(locatorValue)

        elif locatorType == 'link':
            return Web.driver.find_element_by_link_text(locatorValue)

    @staticmethod
    def IsElementPresent(pgnameattr, elekeystr):
        try:
            return WebDriverWait(Web.driver, 2).until(
                lambda driver: PageElements.FindElementByLocator(pgnameattr, elekeystr))
        except TimeoutException as E:
            Logger.logr.info("Element " + elekeystr + " is not present on the " + pgnameattr)
            return False

    @classmethod
    def SetElementValue(cls, value, pgnameattr, elekeystr):
        cls.element_present = cls.IsElementPresent(pgnameattr, elekeystr)
        if cls.element_present:
            cls.element_present.clear()
            cls.element_present.send_keys(value)
            return True
        else:
            return False

    @staticmethod
    def SetFormElementsValue(elementid, value):
        elementid.clear()
        elementid.send_keys(value)

    @staticmethod
    def IsFeedBackWindowPopup():
        try:
            WebDriverWait(Web.driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "fsrFloatingMid")))
        except TimeoutException:
            pass
        else:
            try:
                element = WebDriverWait(Web.driver, 1).until(
                    lambda driver: PageElements.IsElementPresent("FeedBackModel", "FeedbackCancelBtn"))
                element.click()
            except TimeoutException as e:
                Logger.logr.info("Element No, thanks does not exist on feedback Model window")

    # ******************************************************************************************************************
    #                   Embed provided value into a provided string at a particular position
    # ******************************************************************************************************************

    @classmethod
    def InsertVariableInString(cls, string, index, variable):
        return string[:index] + variable + string[index:]


class PageLocators(object):
    """ This class is to handle all page locators  """
    @staticmethod
    def ClickLocator(pgnameattr, elekeystr):
        PageElements.IsFeedBackWindowPopup()
        locator = PageElements.IsElementPresent(pgnameattr, elekeystr)
        if locator:
            locator.click()
            return True
        else:
            return False
