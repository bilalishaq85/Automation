import xml.etree.ElementTree as ET
from Selunium_Automation.Lib.LogConfig import Logger

tree = ET.parse("../Utilities/SiteElement.xml")
root = tree.getroot()


class SiteElement(object):
    @classmethod
    def getSearchValue(cls, pgnameattr, elekeystr):
        xpathstring = "./pages/page[@name='" + pgnameattr + "']/element[@Key='" + elekeystr + "']"
        for element in root.findall(xpathstring):
            locator = element.find('value').text
            if locator is None:
                Logger.logr.error("Please provide value for element: " + elekeystr)
                return False
            else:
                return locator

    @classmethod
    def getSearchBy(cls, pgnameattr, elekeystr):
        xpathstring = "./pages/page[@name='" + pgnameattr + "']/element[@Key='" + elekeystr + "']"
        for element in root.findall(xpathstring):
            searchby = element.find('searchby').text
            return searchby

