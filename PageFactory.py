from Selunium_Automation.Lib.PageElements import PageLocators
from Selunium_Automation.WebPages.AddToCartModel import *
from Selunium_Automation.WebPages.CartPage import *
from Selunium_Automation.WebPages.HomePage import *
from Selunium_Automation.WebPages.LoginPage import *
from Selunium_Automation.WebPages.OrderCPage import *
from Selunium_Automation.WebPages.ReviewPage import *


class PageFactory(object):
    @staticmethod
    def CanGoToHomePage():
        return HomePage.isHome()

    # ****************************************** LogIn & Logout ********************************************************
    @staticmethod
    def GoToLoginPage():
        return PageLocators.ClickLocator("HomePage", "SignIn")

    @staticmethod
    def LoginAsRegisteredUser():
        if LoginPage.Login():
            result = PageLocators.ClickLocator("LoginPage", "LoginButton")
            if result:
                return LoginPage.isLoginSucessful()

    @staticmethod
    def ClickLogOffBtn():
        if PageLocators.ClickLocator("HomePage", "LogOff"):
            return LoginPage.isLogoutSuccessful()

# ****************************************** Bulk Order Pad ************************************************************
    @staticmethod
    def GoToBulkOrderPad():
        if PageLocators.ClickLocator("HomePage", "BulkOrderPad"):
            if HomePage.TypeBulkOrderPadItems():
                if PageLocators.ClickLocator("HomePage", "BulkPadAddToCart"):
                    if AddToCartModel.isModelPopup():
                        if PageLocators.ClickLocator("AddToCartModel", "ViewCart"):
                            if CartPage.IsCartPageDisplayed():
                                if PageLocators.ClickLocator("CartPage", "CheckOut"):
                                    if ReviewPage.IsReviewPageDisplayed():
                                        if PageLocators.ClickLocator("ReviewPage", "SubmitOrder"):
                                            return OrderCPage.IsOrderCPageDisplayed()

# ************************************** Annonymous Bulk Order Pad *****************************************************
    @staticmethod
    def GoToAnnonymousBulkOrderPad():
        if PageLocators.ClickLocator("HomePage", "BulkOrderPad"):
            if HomePage.TypeBulkOrderPadItems():
                if PageLocators.ClickLocator("HomePage", "BulkPadAddToCart"):
                    if AddToCartModel.isModelPopup():
                        return PageLocators.ClickLocator("AddToCartModel", "ViewCart")

    @staticmethod
    def ProcessOrder():
        if CartPage.IsCartPageDisplayed():
            if PageLocators.ClickLocator("CartPage", "CheckOut"):
                if ReviewPage.IsReviewPageDisplayed():
                    if PageLocators.ClickLocator("ReviewPage", "SubmitOrder"):
                        return OrderCPage.IsOrderCPageDisplayed()