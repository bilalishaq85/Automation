from Selunium_Automation.Lib.BaseClass import *
from Selunium_Automation.WebPages.PageFactory import PageFactory


class SmokeTest(BaseClass):
    def test_aCanGoToHomePage(self):
        result = PageFactory.CanGoToHomePage()
        self.assertTrue(result)

    def test_bCanLogIn(self):
        result = PageFactory.GoToLoginPage()
        if result:
            result = PageFactory.LoginAsRegisteredUser()
            if result:
                PageFactory.ClickLogOffBtn()
        self.assertTrue(result)

    def test_cCanBulkOrderPad(self):
        result = PageFactory.GoToLoginPage()
        if result:
            result = PageFactory.LoginAsRegisteredUser()
            if result:
                result = PageFactory.GoToBulkOrderPad()
                if result:
                    PageFactory.ClickLogOffBtn()
        self.assertTrue(result)

    def test_dAnnonymousBulkOrderPad(self):
        result = PageFactory.GoToAnnonymousBulkOrderPad()
        if result:
            result = PageFactory.LoginAsRegisteredUser()
            if result:
                result = PageFactory.ProcessOrder()
                if result:
                    PageFactory.ClickLogOffBtn()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()