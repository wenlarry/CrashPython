#  Writing to a file

#  Writing to an empty file
#  The arg'w' tells Python that we want to open file in write mode
#     ('r'=read, 'a'=append,'r+'=read n write)
#  Open the file 'program.txt'; see the output
#  Including new lines in write() statement amke each string appears
#     on its own line
filename = 'program.txt'

with open(filename, 'w') as file_object:
    file_object.write("We luv programs\n")
    file_object.write("We luv python_charts\n")

#  appending to a file
filename = 'program.txt'

with open(filename, 'a') as file_object:
        file_object.write("We also luv datasets\n")
        file_object.write("We also luv apps on browsers\n")

       