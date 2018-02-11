#  Handling the FileNotFond Error Exception

#  Python can't read from a missing file, so it raises an exception
#filename = 'al.txt'

#with open(filename) as f_obj:
#	contents = f_obj.read()

#  Handling the error ; the code in the try block produces an error,
#     so Python looks for an except block that matches that error -
#      result - a friendly error msg
filename = 'Al.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()

except FileNotFoundError:
	msg = "Sorry, the file  " + filename + " doesn't exist"
	print(msg)

#  Analyzing Text

#  Pulling in a text of 'Al' and count the numbers
#    of words in the text. Use the string method split(), that can
#    build a list of words from a string
#  Create a txt file 'al.txt'
#  We take the string contents that now contain the entire text of 'al.txt'
#    and use the split() method to produce a list of all the words in 'al.txt'
#  We use len() on the list to examine its length and get an approx of the
#    number of words in the original string
#  Code is in the else block because it will work only if the code in the try
#    block is executed successfully

# >>> title = "Al"
# >>>title.split()
#['Al']


filename = 'Al.txt'

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



