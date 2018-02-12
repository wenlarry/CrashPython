#  setUp Method

#  When we include a setUp() method in a TestCase class, Python runs the
#     setUp() method before running each method starting with test_. any objects
#     created in the setUp() method are then available in each test method
#  The method setUp() creates a survey instance and a list of responses. Each is
#      prefixed by self, so that they can be used anywhere in the class
#  The method test_store__single_response() verifies that the first response in
#      self.responses-self.responses[0]-can be stored correctly and test_store_
#      -single_response() verifies that all three responses in self.responses can
#      be stored correctly
#  These tests are useful when trying to expand AnonymousSurvey to handle multiple
#      responses for each person
#   When testing our own classes, the setUp() method can make our test method easier
#      to write. We make one set of instances and attributes in in setUp() and then
#      use these instances in all our test methods. 
import unittest
from test_4 import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for class AnonymousSurvey"""

    def setUp(self):
        """ Create a survey and responses for all test methods"""
        question = "What lang you first spoke?"
        self.our_survey = AnonymousSurvey(question) 
        self.responses = ['English', 'Mandarin', 'Malay']
    
    def test_store_single_response(self):
    	self.our_survey.store_response(self.responses[0])
    	self.assertIn(self.responses[0], self.our_survey.responses)

    def test_store_three_responses(self):
    	for response in self.responses:
    		self.our_survey.store_response(response)
    	for response in self.responses:
    		self.assertIn(response, self.our_survey.responses)

unittest.main()



