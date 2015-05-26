# Single variable set to a format string utilizing the decimal format.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"

# Single variable set to a format string utilizing two string formats.
y = "Those who know %s and those who %s." % (binary, do_not)

# Prints the two format strings
print x
print y

# Prints the previous strings through a format, showing that you can chain together format strings
# Also the first use of the Repr() module
print "I said: %r." % x
print "I also said: '%s'." % y

# Stupid joke using Boolean
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints said stupid joke
print joke_evaluation % hilarious

# Sets two strings
w = "This is the left side of..."
e = "a string with a right side."

# Concatenate two previous strings
print w + e