
import unittest
from selenium import webdriver

from test_config import pg
from test_config import pg_backendPerformance_max
from test_config import pg_frontendPerformance_max


# Group of example tests designed to verify response timings, ability to work close to defined limits and so on ...
class TestSet_PERFORMANCE(unittest.TestCase):

    def setUp(self):    # "Hook method for setting up the test fixture before exercising it."
        self.driver = webdriver.Chrome()
        self.addCleanup(self.driver.quit)
        self.driver.get(pg)

    def tearDown(self): # "Hook method for deconstructing the test fixture after testing it."
        pass

    def testTimings(self):
        navigationStart = self.driver.execute_script("return window.performance.timing.navigationStart")
        responseStart = self.driver.execute_script("return window.performance.timing.responseStart")
        domComplete = self.driver.execute_script("return window.performance.timing.domComplete")

        backendPerformance_calc = responseStart - navigationStart
        frontendPerformance_calc = domComplete - responseStart

        self.assertGreaterEqual(pg_backendPerformance_max, backendPerformance_calc)
        self.assertGreaterEqual(pg_frontendPerformance_max, frontendPerformance_calc)

    def testResponseUnderLoad(self):
        #TODO
        pass