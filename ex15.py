from sys import argv

script, filename = argv

# Open the file that is provided by user and save to txt
txt = open(filename)

# Read the file
print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()