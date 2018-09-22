from webdriverplus import WebDriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from Functions import *
from Selunium_Automation.Lib.LogConfig import Logger


class WebDriverFactory:
    @staticmethod
    def getWebdriver():
        InitializeMapSection('ResultSet', 'ResultLog')
        browserName = ReadMapSection('Constants', 'Constants')['browser']
        if browserName != '':
            if browserName == 'Firefox':
                binary = FirefoxBinary('C:\\Users\\bilal\\workspace\\Projects\\Selenium\\FirFox\\firefox.exe')
                webDriver = WebDriver('firefox', firefox_binary=binary, reuse_browser=True)
            elif browserName == 'Chrome':
                webDriver = WebDriver('chrome', reuse_browser=True)
            elif browserName == 'IE':
                webDriver = WebDriver('Ie', reuse_browser=True)
            else:
                Logger.logr.error("WebDriver in not configured for browser " + browserName)
                WriteMapSection("WebDriver", "Failed")
                return False
            Logger.logr.info("Initiating web driver for browser: " + browserName)
            WriteMapSection("WebDriver", "Passed")
            return webDriver
        else:
            Logger.logr.error("Please provide browser name")
            WriteMapSection("WebDriver", "Failed")
            return False
