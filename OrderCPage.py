from Selunium_Automation.Lib.LogConfig import Logger
from Selunium_Automation.Lib.PageElements import PageElements


class OrderCPage(object):
    @classmethod
    def IsOrderCPageDisplayed(cls):
        reviewPage = PageElements.IsElementPresent("OrderCPage", "OrderCPageHeader")
        if not reviewPage:
            Logger.logr.error("Order confirmation page is not displayed")
            return False
        else:
            Logger.logr.info("Order confirmation page is displayed")
            return True