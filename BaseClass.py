import unittest
from Selunium_Automation.Lib.WebDriverSetup import Web
from Selunium_Automation.Lib.Functions import *
from Selunium_Automation.Lib.LogConfig import Logger


class BaseClass(unittest.TestCase):
    Web.InitializeDriver()

    def setUp(self):
        if ReadMapSection('ResultSet', 'ResultLog')['lasttestresult'] in ('Failed', 'Skipped'):
            Logger.logr.info(self._testMethodName + " Skipped, Reason:Dependent Test Failed")
            WriteMapSection(self._testMethodName, 'Skipped')
            self.skipTest()
        else:
            Logger.logr.info(" ***** Initializing testcase: " + self._testMethodName + " *****")

    def run(self, result):
        # Store the result on the class so tearDown can behave appropriately
        self.result = result.result if hasattr(result, 'result') else result
        self._feedErrorsToResultEarly = self._feedErrorsToResult
        self._feedErrorsToResult = lambda *args, **kwargs: None  # no-op
        super(BaseClass, self).run(result)

    @property
    def Errored(self):
        return self.id() in [case.id() for case, _ in self.result.errors]

    @property
    def Failed(self):
        return self.id() in [case.id() for case, _ in self.result.failures]

    @property
    def Passed(self):
        return not (self.errored or self.failed)

    def tearDown(self):
        Logger.logr.info(" ***** Finished " + self._testMethodName + " Execution *****")
        self._feedErrorsToResultEarly(self.result, self._outcome.errors)
        if self.Errored:
            WriteMapSection(self._testMethodName, 'Errored')
        elif self.Failed:
            WriteMapSection(self._testMethodName, 'Failed')
        else:
            WriteMapSection(self._testMethodName, 'Passed')
        Logger.logr.info(" ******* TestCase Status: " + ReadMapSection('ResultSet', 'ResultLog')['lasttestresult'] + " ******* ")

