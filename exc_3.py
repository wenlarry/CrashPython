#  Working with multiple files

#  Move the bulk of the program to a function 'count_words'. Easier than to
#     run the analysis of many books
def count_words(filename):
    """Count the approx number of words in the file"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()

    except FileNotFoundError:
	        msg = "Sorry, the file  " + filename + " doesn't exist"
	        print(msg)

    else:
	    # count approx number of words in the file
	    words = contents.split()
	    num_words = len(words)
	    print("File " + filename + " has abt " + str(num_words) + " words")

filename = 'Al.txt'
count_words(filename)

#  We can then write a simple loop to count the words in an text
#  Store the names of the file in a list
#  Intentionally, omit 'sid.txt' from the dir; the output is that 'sid.txt'
#     doesn't exist
def count_words(filename):
    """Count the approx number of words in the file"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()

    except FileNotFoundError:
	        msg = "Sorry, the file  " + filename + " doesn't exist"
	        print(msg)

    else:
	    # count approx number of words in the file
	    words = contents.split()
	    num_words = len(words)
	    print("File " + filename + " has abt " + str(num_words) + " words")

filenames = ['Al.txt', 'moby_dick.txt','sid.txt']
for filename in filenames:
	count_words(filename) 

#  Failing silently

#  We want the program to fail silently when an exception occurs. Use the pass
#     statement 
#  We decide how much to share with users when things go wrong
def count_words(filename):
    """Count the approx number of words in the file"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()

    except FileNotFoundError:
	    pass

    else:
	    # count approx number of words in the file
	    words = contents.split()
	    num_words = len(words)
	    print("File " + filename + " has abt " + str(num_words) + " words")

filenames = ['Al.txt', 'moby_dick.txt','sid.txt']
for filename in filenames:
	count_words(filename) 
