#  Testing a function

#  This is a function that is called in test_2.py and test_3.py

def get_formatted_name(first, last):
    """Get a formatted full name"""
    full_name = first + ' ' + last
    return full_name.title()
