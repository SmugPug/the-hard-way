from sys import argv

script, filename = argv

openfile = open(filename)

print openfile.read()

openfile.close()