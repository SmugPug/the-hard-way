from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	choice = raw_input("> ")
	if int(choice) == True:
		how_much = choice
	else:
		dead("Man, learn to type a number.")
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy cock towel!")
	
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		choice = raw_input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews through your leg.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I have no idea what that means."
			
def cthulhu_room():
	print "Here you see the great evil Cthulhu. It stares at you, it's cold black pupils rapidly expand to fill your entire vision."
	print "Your gaze into the infinite abyss and the see the sea of the multiverse, frothing against the shores of reality. You understand. You go insane."
	print "Do you green sideways or lamp smithing space candles?"
	
	choice = raw_input("> ")
	
	if "green" in choice:
		start()
	elif "lamp" in choice:
		dead("Cthulhu consumes your eternal soul.")
	else:
		cthulu_room()

def dead(why):
	print why, "Bingo bango bongo!"
	exit(0)
	
def start():
	print "You are in a dark musty room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You are paralysed by indecision, you slowly starve to death.")
		
start()