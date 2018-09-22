from Selunium_Automation.Lib.LogConfig import Logger
from Selunium_Automation.Lib.PageElements import PageElements


class CartPage(object):
    @classmethod
    def IsCartPageDisplayed(cls):
        cartPage = PageElements.IsElementPresent("CartPage", "CartPageHeader")
        if not cartPage:
            Logger.logr.error("Cart detail page is not displayed")
            return False
        else:
            Logger.logr.info("Cart detail page is displayed")
            return True