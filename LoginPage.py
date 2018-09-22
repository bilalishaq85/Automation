from Selunium_Automation.Lib.LogConfig import Logger
from Selunium_Automation.Lib.PageElements import PageElements
from Selunium_Automation.Lib.Functions import *


class User(object):
    def __init__(self):
        self.EmailAddress, self.Password = User.loginCredentials()

    @staticmethod
    def loginCredentials():
        return ReadMapSection('Constants', 'Constants')["email"], \
               ReadMapSection('Constants', 'Constants')["pwd"]


class LoginPage(object):
    @staticmethod
    def Login():
        if PageElements.SetElementValue(User().EmailAddress, "LoginPage", "LoginUserName") and \
                PageElements.SetElementValue(User().Password, "LoginPage", "LoginPassword"):
            return True
        else:
            return False

    @staticmethod
    def isLoginSucessful():
        if not PageElements.IsElementPresent("HomePage", "LogOff"):
            Logger.logr.error(" Not able to log in")
            return False
        else:
            Logger.logr.info(" Login Successful")
            return True

    @staticmethod
    def isLogoutSuccessful():
        if not PageElements.IsElementPresent("HomePage", "SignIn"):
            Logger.logr.error("Not able to log out")
            return False
        else:
            Logger.logr.info("Logout Successful")
            return True



            # classlist = Web.driver.find_elements_by_xpath(
            #   '//form[@id="loginForm"]//div[@class="signInForm"]/*[@class]')
            # for i in classlist:
            #   if len(i) == 2:
            #      Logger.logr.error()


            # print(i.get_attribute('class'))
