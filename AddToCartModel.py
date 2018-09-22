from Selunium_Automation.Lib.LogConfig import Logger
from Selunium_Automation.Lib.PageElements import PageElements


class AddToCartModel(object):
    @classmethod
    def isModelPopup(cls):
        modelPopup = PageElements.IsElementPresent("AddToCartModel", "CartModel")
        if not modelPopup:
            Logger.logr.error("Add to Cart Model did not pop up")
            return False
        else:
            Logger.logr.info("Add to Cart Model pops up")
            return True

