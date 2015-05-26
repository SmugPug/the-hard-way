from sys import argv

script_name, color, movie, cloud_type, food = argv

reason = raw_input("I hate the color " + color + " why do you like it?")
reason2 = raw_input("I hate the movie " + movie + " why do you like it?")
reason3 = raw_input("I hate the cloud type " + cloud_type + " why do you like it?")
reason4 = raw_input("I hate the food " + food + " why do you like it?")

print "Translation: ", reason, reason2, reason3, reason4, "\n= You suck."