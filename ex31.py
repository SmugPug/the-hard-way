print "You stand before two paths, one into a dark forest(1), and one into a sunlit meadow(2), which do you choose? (Type 1 or 2)"

path = raw_input("> ")

if path == "2":
	print "You gaze out over the beautiful meadow and realize life is worthless, what do you decide to do about it?"
	print "1. Take out your pocket knife and fix the world."
	print "2. Frolic happily through the meadow."
	print "3. Withdraw inside yourself to your safe place."
	
	decision = raw_input("> ")
	
	if decision == "1":
		print "You quickly slide the blade into your neck, smiling as the warmth spreads down your shirt."
	elif decision == "2":	
		print "You frolic happily ever after."
	else:
		print "You die in your sleep."
		
elif path == "1":
	print "You casually stroll into the dark woods. You come around a bend, fall into a hole and break your leg."
	
else:
	print "Your indecision pays off. A pot of gold falls at your feet. Then a bear mauls you from behind."