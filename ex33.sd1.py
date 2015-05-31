def wangfunk(numberwang, increment):
	i = 0
	numbers = []

	while i < numberwang:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i = i + increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
		
	print "The numbers: "

	for num in numbers:
		print num
		
for i in range(1,6):
	numberwang = 10
	increment = i
	wangfunk(numberwang, increment)