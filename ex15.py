# Import module to allow for CLI argument
from sys import argv

# Set argv parameters
script, filename = argv

# Open the file that is provided by user and save to txt
txt = open(filename)

# Prints file contents to screen
print "Here's your file %r:" % filename
print txt.read()

# Pulls file name from user via raw_input
print "Type the filename again:"
file_again = raw_input("> ")

# Open the file
txt_again = open(file_again)

# Prints file contents to screen
print txt_again.read()

# Closes files
txt.close()
txt_again.close()