#  Testing a class

#  Six common assert methods that we can verify that returned
#     values equal or don't equal expected values, that values
#     are True or False, and that values are in or not in a list
#  We can use these methods only in a class that inherits from 
#     unittest.TestCase
#
#  assertEqual(a, b)       Verify that a == b
#  assertNotEqual(a, b)    Verify that a != b
#  assertTrue(x)           Verify that x is True
#  assertFalse(x)          Verify that x is False
#  assertIn(item, list)    Verify that item is in list
#  assertNotIn(item, list)  Verify that item is not in list

from test_4 import AnonymousSurvey

#  Define a q; make a survey
question = "What language first spoken ?"
our_survey = AnonymousSurvey 

#  Show the q and store responses to the q
our_survey.show_question 
print("Enter 'q' to quit.\n" )
while True:
    response = input("language: ")
    if response == 'q':
        break
    our_survey.store_response(response)

#  Show the survey results:
print("\nTks to All who participated!")
our_survey.show_results()

