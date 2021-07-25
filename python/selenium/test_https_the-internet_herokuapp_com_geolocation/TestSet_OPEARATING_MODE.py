
import unittest
from selenium import webdriver

from test_config import pg
from test_config import button
from test_config import pq_lat
from test_config import pq_long
from test_config import google_map_link
from test_config import expected_link_str
from test_config import KPT
from test_config import Codahead
from test_config import negative_cordinates
from test_config import globe_boundary_cordinates

# Group of example tests designed to verify page functionality
class TestSet_OPEARATING_MODE(unittest.TestCase):

    def setUp(self):    # "Hook method for setting up the test fixture before exercising it."
        self.driver = webdriver.Chrome()
        self.addCleanup(self.driver.quit)
        self.driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
            "latitude": KPT.latitude,
            "longitude": KPT.longitude,
            "accuracy": KPT.accuracy
        })
        self.driver.get(pg)

    def tearDown(self): # "Hook method for deconstructing the test fixture after testing it."
        pass

    def testCheckGeo(self):
        self.driver.find_element_by_xpath(button).click()
        self.assertEqual(KPT.latitude, float(self.driver.find_element_by_xpath(pq_lat).get_attribute('innerHTML')))
        self.assertEqual(KPT.longitude, float(self.driver.find_element_by_xpath(pq_long).get_attribute('innerHTML')))

    def testCheckGeoUpdate(self):
        self.driver.find_element_by_xpath(button).click()
        self.driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
            "latitude": Codahead.latitude,
            "longitude": Codahead.longitude,
            "accuracy": Codahead.accuracy
        })
        self.driver.find_element_by_xpath(button).click()
        self.assertEqual(Codahead.latitude, float(self.driver.find_element_by_xpath(pq_lat).get_attribute('innerHTML')))
        self.assertEqual(Codahead.longitude, float(self.driver.find_element_by_xpath(pq_long).get_attribute('innerHTML')))

    def testNegativeCoordinates(self):
        self.driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
            "latitude": negative_cordinates.latitude,
            "longitude": negative_cordinates.longitude,
            "accuracy": negative_cordinates.accuracy
        })
        self.driver.find_element_by_xpath(button).click()
        self.assertEqual(negative_cordinates.latitude, float(self.driver.find_element_by_xpath(pq_lat).get_attribute('innerHTML')))
        self.assertEqual(negative_cordinates.longitude, float(self.driver.find_element_by_xpath(pq_long).get_attribute('innerHTML')))

    def testBoundaryCoordinates(self):
        self.driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
            "latitude": globe_boundary_cordinates.latitude,
            "longitude": globe_boundary_cordinates.longitude,
            "accuracy": globe_boundary_cordinates.accuracy
        })
        self.driver.find_element_by_xpath(button).click()
        self.assertEqual(globe_boundary_cordinates.latitude, float(self.driver.find_element_by_xpath(pq_lat).get_attribute('innerHTML')))
        self.assertEqual(globe_boundary_cordinates.longitude, float(self.driver.find_element_by_xpath(pq_long).get_attribute('innerHTML')))

    def testCheckGoogleMapsLink(self):
        self.driver.find_element_by_xpath(button).click()
        self.assertIn(expected_link_str + str(KPT.latitude) + ',' + str(KPT.longitude),
                         self.driver.find_element_by_xpath(google_map_link).get_attribute("href"))

    def testCheckGoogleMapsLinkIsUpdated(self):
        self.driver.find_element_by_xpath(button).click()
        self.driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
            "latitude": Codahead.latitude,
            "longitude": Codahead.longitude,
            "accuracy": Codahead.accuracy
        })
        self.driver.find_element_by_xpath(button).click()
        self.assertIn(expected_link_str + str(Codahead.latitude) + ',' + str(Codahead.longitude),
                         self.driver.find_element_by_xpath(google_map_link).get_attribute("href"))

