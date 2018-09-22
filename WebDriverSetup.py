from Selunium_Automation.Lib.Functions import *
from Selunium_Automation.Lib.LogConfig import Logger
from Selunium_Automation.Lib.LogConfig import singleton
from WebDriverFactory import WebDriverFactory


@singleton
class Web:
    @classmethod
    def InitializeDriver(cls):
        cls.driver = WebDriverFactory.getWebdriver()
        if cls.driver is not False:
            cls.driver.maximize_window()
            cls.URL = ReadMapSection('Constants', 'Constants')['url']
            if cls.URL is not False:
                cls.driver.get(cls.URL)
        else:
            Logger.logr.error("Not able to initialize web driver")
            return False

    @classmethod
    def CloseDriver(cls):
        if cls.driver is not False:
            cls.driver.implicitly_wait(2)
            cls.driver.quit()
