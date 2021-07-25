
import unittest

import TestSet_PAGE_LAYOUT
import TestSet_OPEARATING_MODE
import TestSet_FAILURES_HANDLING
import TestSet_PERFORMANCE

import random

    # PAGE LAYOUT
        # Test_Scenario_1 testPageTitle
        # Test_Scenario_2 testPageTitleAfterScriptRun

    # OPEARATING MODE
        # Test_Scenario_1 testCheckGeo
        # Test_Scenario_2 testCheckGeoUpdate
        # Test_Scenario_3 testNegativeCoordinates
        # Test_Scenario_4 testBoundaryCoordinates
        # Test_Scenario_5 testCheckGoogleMapsLink
        # Test_Scenario_6 testCheckGoogleMapsLinkUpdate

    # FAILURES HANDLING
        # Test_Scenario_1 testOffGlobeCoordinates

    # PERFORMANCE
        # Test_Scenario_1 testTimings
        # Test_Scenario_2 testResponseUnderLoad


suite = []

suite.append(unittest.TestLoader().loadTestsFromModule(TestSet_PAGE_LAYOUT))
suite.append(unittest.TestLoader().loadTestsFromModule(TestSet_OPEARATING_MODE))
#suite.append(unittest.TestLoader().loadTestsFromModule(TestSet_FAILURES_HANDLING))
suite.append(unittest.TestLoader().loadTestsFromModule(TestSet_PERFORMANCE))

for st in suite:
    unittest.TextTestRunner(verbosity=2).run(st)

