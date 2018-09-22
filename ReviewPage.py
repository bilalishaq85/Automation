from Selunium_Automation.Lib.LogConfig import Logger
from Selunium_Automation.Lib.PageElements import PageElements


class ReviewPage(object):
    @classmethod
    def IsReviewPageDisplayed(cls):
        reviewPage = PageElements.IsElementPresent("ReviewPage", "ReviewPageHeader")
        if not reviewPage:
            Logger.logr.error("Review order page is not displayed")
            return False
        else:
            Logger.logr.info("Review order page is displayed")
            return True