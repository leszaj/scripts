
import unittest
from selenium import webdriver

from test_config import pg
from test_config import button
from test_config import out_of_globe


# Group of example tests designed to verify page reaction for potential input faults
class TestSet_FAILURES_HANDLING(unittest.TestCase):

    def setUp(self):    # "Hook method for setting up the test fixture before exercising it."
        self.driver = webdriver.Chrome()
        self.addCleanup(self.driver.quit)
        self.driver.get(pg)

    def tearDown(self): # "Hook method for deconstructing the test fixture after testing it."
        pass

    def testOffGlobeCoordinates(self):
        # GEOLOCATION BLOCKS INVALID COORDINATES SETTING
        # {"code":-32000,"message":"Invalid geolocation"}
        # TEST IS INVALID

        """
        self.driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
            "latitude": out_of_globe.latitude,
            "longitude": out_of_globe.longitude,
            "accuracy": out_of_globe.accuracy
        })
        try:
            self.driver.find_element_by_xpath(button).click()
        catch:
            ...
        """