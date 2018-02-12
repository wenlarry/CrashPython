#  Testing the AnonymousSurvey Class

#  The first test method  verify that when we store a response 
#    to a survey question, the response ends up in the survey's
#    list of responses i.e. test_store_single_response()
#  if  this test fails, than there is a problem storing a single
#     response to the survey
#  We create an instance of the class 'our-survey' with the question
#     "What lang...?" and store a single response 'English'
#  We then verify that the response was stored correctly by asserting
#    that English is in the list 'our_survey.responses'
import unittest
from test_4 import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""Tests for class AnonymousSurvey"""
def test_store_single_response(self):
	"""test that a single response is stored"""
	question = "What lang you first spoke ?"
	our_survey = AnonymousSurvey(question)
	our_survey.store_response('English')

	self.assertIn('English', our_survey.responses)

#  Verify that 3 responses can be stored correctly
def test_store_three_responses(self):
	"""test that 3 responses are stored"""
	question = "What lang you first spoke?"
	our_survey = AnonymousSurvey(question)
	responses = ['English', 'Mandarin', 'Malay']
	for response in responses:
		our_survey.store_response(response)

	for response in responses:
		self.assertIn(response, our_survey.responses)

unittest.main()
 