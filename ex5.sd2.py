name = 'Nathan'
age = 24
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
weight_kg = round(weight * 0.4536)
height_cm = round(height * 2.54)

print "Let's talk about %s." % name
print "He's %d inches tall, which is %d centimetres" % (height, height_cm)
print "He's %d pounds heavy, which is %d kilograms." % (weight, weight_kg)
print "Actually that's not too heavy."
print "He's got %s eyes %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)