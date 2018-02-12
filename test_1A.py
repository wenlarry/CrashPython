#  Failing Test

#  Testing on a new version of get_formatted-name() that requires a middle
#     name
#  Outputs example:
#  E tells us one unit test in the test case resulted in an error
#  ERROR: test_first_last_name(_main_.NamesTestCase) - Knowing which test
#     failed is critical when our test case contains many unit tests
#  Traceback - reports that the function 'get_formatted_names('qi', 'ni')
#      no longer works because it's missing one required positional arg
#  Ran i test in 0.000s
#  FAILED (errors=1) - Overall test case failed and that one error occurred

#  Responding to a Failed Test

#  When a test fails, don't change the test> Instead, fix the code that caused
#    the test to fail. Eg: get-formatted name in test_1.py required two para:
#    a first name and a last name. Now it requires a first, middle and last name
#    The addition of that mandatory middle name para broke the desired behavior 
#    of get_formatted_name(). Make the middle name para optional.
#  Modify 'get_formatted-name() in file_1.py. Move the para middle to the end of
#     of the para list in the function definition and give it an empty default 
#     value. Add an if test that builds the name properly depending on whether
#     or not a middle name is provided
#  Modification in file_1A.py and testing it in file_3.py 
def get_formatted_name(first, last, middle=''):
	"""Get a formatted full name"""
	if middle:
		full_name = first + ' ' + middle + ' ' + last
	else:
		full_name = first + ' ' + last
	return full_name.title()

