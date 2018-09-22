from Selunium_Automation.Lib.Functions import *
from Selunium_Automation.Lib.PageElements import PageElements
from Selunium_Automation.Lib.WebDriverSetup import Web


class HomePage(object):
    @staticmethod
    def isHome():
        title = Web.driver.title
        if '503' in title:
            Logger.logr.error("WebSite is not reachable, down for maintenance")
            return False
        else:
            Logger.logr.info("WebSite is loaded successfully")
            return True

    # ************************************ Bulk Order Pad **************************************************************
    @staticmethod
    def TypeBulkOrderPadItems():
        formIds_1 = PageElements.IsElementPresent('HomePage', 'BulkOrderPadElementsPath')
        if not formIds_1:
            Logger.logr.error("Item Id's cannot be found for BulkOrderPad Form")
            return False
        else:
            formIds_2 = PageElements.IsElementPresent('HomePage', 'BulkOrderPadElementsQtyPath')
            if not formIds_2:
                Logger.logr.error("Qty Id's cannot be found for BulkOrderPad Form")
                return False
            else:
    # ************************************ Fetching Product Item #s ****************************************************
                items = ReadMapSection('Constants', 'Constants')['items']
                itemsqty = ReadMapSection('Constants', 'Constants')['itemqtys']
                if items and itemsqty is not False:
                    itemsList = items.split(',')
                    itemsqtyList = itemsqty.split(',')
                for index in range(len(formIds_1)):
                    PageElements.SetFormElementsValue(formIds_1[index], itemsList[index])
                    PageElements.SetFormElementsValue(formIds_2[index], itemsqtyList[index])
                Logger.logr.info("Items/qtys load in order pad is successful")
                return True
