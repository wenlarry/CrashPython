#  Unit Test

#  'unittest' module from Python std lib provide tools for code tests
#  A unit test verifies that one specific aspect of a function's behavior
#  is correct . A test case is a collection of unit tests that together
#  prove that a function behaves. A good test case considers all the 
#  possible inputs a function could receive and includes tests to represent
#  each of these situations.
#  A test case with full coverage includes a full range of unit tests 
#  covering all the possible ways we can use the function. Good enough to
#  test codes' critical behaviours and then aim for full coverage if the 
#  project begins with widespread use

#  A Passing Test
#  
#  Import the unittest module and the function to be tested. Then create a
#  class that inherits from unittest.TestCase and write a series of methods
#     to test different aspects of the function
#  Class must inherit from the class uniitest.TestCase so Python knows
#     how to run the tests
#  We call get_formatted name with the args 'qi' and 'ni' and store the 
#     results in formatted_name
#  Using unittest's most useful features:an assert method
#  Assert methods verify that a result received matches the result expected
#  The line unittest.main() tells Python to run the tests in this file

#  Here's a test case with one method that verifies that the function
#  get_formatted_name() works correctly when given the first and last name
#  Note: Ran 1 test; FAILED (Failures =1)

import unittest
from test_1 import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Tests for test_1.py"""
	def test_first_last_name(self):
	 	"""Do names like 'qi ni' work ?"""
	 	formatted_name = get_formatted_name('qi', 'ni')
	 	self.assertEqual(formatted_name, 'Qi Ni')

unittest.main() 

#  Testing with function in test_1A file
#  Now it shoud work
from test_1A import get_formatted_name

class NamesTestCase(inittest.TestCase):
	"""Tests for test_1A.py"""
	def test_first_last_name(self):
		"""Do names like 'qi ni' work?"""
		formatted_name = get_formatted_name('qi', 'ni')
		self.assertEqual(formatted_name, 'Qi Ni')

unittest.main()

#  Adding new test
#
#  A test including the middle name. Adding another method
#     to the class NamesTestCase

from test_1A import get_formatted_name
class NamesTestCase(inittest.TestCase):
	"""Tests for test_1A.py"""
	def test_first_last_name(self):
	    """Do names like 'qi ni' work?"""
	    formatted_name = get_formatted_name('qi', 'ni')
	    self.assertEqual(formatted_name, 'Qi Ni')

	def test_first_last_middle_name(self):
		"""Do names like 'qi an ni' work?"""
		formatted_name = get_formatted_name('qi', 'an', 'ni')
		self.assertEqual(formatted_name, 'Qi An Ni')

unittest.main()


