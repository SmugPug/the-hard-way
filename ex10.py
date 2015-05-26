# Ex of escape char for a tab
tabby_cat = "\tI'm a tabbed in."
# Ex of an escape char for a new line
persian_cat = "I'm a split\non a line."
# Ex of an escape char for a backslash char
backslash_cat = "I'm \\ a \\ cat."

# Ex of triple quote displaying multiple new lines
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "This is an ASCII \abell"
print "This is an ASCII \bbackspace"
print "This is an ASCII \fformfeed"
print "This is an ASCII \vverticle tab"
print "This is a character with octal value ooo \ooo"

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,