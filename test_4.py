#  Testing a Class

#  This class starts with a survey Q; includes an empty list
#     to store responses. The class has method to print the
#     survey q, add a response to the response list and print
#     all the responses stored in the list. To create an instance
#     from this class, we have to provide a question. Once we have
#     an instance representing a survey, we can display the survey
#     question with show_question(), store a response using 
#     store_response() and show results with show_results()
#
#  Program that use this class in test_5.py
class AnonymousSurvey():
    """Collect anonymous answers to a survey"""
    def _init_(self, question):
        """Store a q, and store responses"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey q"""
        print(question)

    def store_response(self, new_response):
    	"""Store a single response to survey"""
    	self.responses.append(new_response)

    def show_results(self):
    	"""show all responses given"""
    	print("Survey results:")
    	for response in responses:
    		print('_ ' + response)
