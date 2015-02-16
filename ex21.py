def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	

print "Let's do some math with just functions!"

age = add(30, 5) # the value returned by the function is assigned to a variable
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
what2 = add(30+5, subtract(78-4, multiply(90*2, divide(100/2, 2))))
what3 = divide(10000, multiply(10, subtract(100, add(1, 1))))
what4 = divide(10000.0, multiply(10.0, subtract(100.0, add(1.0, 1.0))))

print "That becomes: %r" % what, "Can you do it by hand?\n"
print "That becomes: ", what2, "\n"
print "That becomes: ", what3, "\n"
print "That becomes: ", what4, "\n"
