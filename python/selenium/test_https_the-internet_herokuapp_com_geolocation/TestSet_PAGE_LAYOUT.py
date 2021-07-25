
import unittest
from selenium import webdriver

from test_config import pg
from test_config import title
from test_config import button


# Group of example tests designed to verify page composition
class TestSet_PAGE_LAYOUT(unittest.TestCase):

    def setUp(self):    # "Hook method for setting up the test fixture before exercising it."
        self.driver = webdriver.Chrome()
        self.addCleanup(self.driver.quit)
        self.driver.get(pg)

    def tearDown(self): # "Hook method for deconstructing the test fixture after testing it."
        pass

    def testPageTitle(self):
        self.assertIn(title, self.driver.title)

    def testPageTitleAfterScriptRun(self):
        self.driver.find_element_by_xpath(button).click()
        self.assertIn(title, self.driver.title)

