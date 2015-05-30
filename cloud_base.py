print "Cloud base calculator\n"

temp = int(raw_input("Enter temperature in Fahrenheit\n>>>"))

dew = int(raw_input("Enter dewpoint in Fahrenheit\n>>>"))

cloud_base = ((temp - dew) / 4.4) * 1000

print "Cloud base is at %d feet." % cloud_base