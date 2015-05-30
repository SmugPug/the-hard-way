def add2(num1, num2):
	charlie(num1, num2)
	
def charlie(num1, num2):
	write = str(num1 + num2)
	file = raw_input("What is your least favourite number?") + ".txt"
	open(file, 'w').write(write)
	

num1 = int(raw_input("Give me a number: "))
num2 = int(raw_input("Give me another number:"))

add2(num1, num2)


