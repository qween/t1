print "How old are you?", 
# the comma shows the prompt for the user in the same line as the question asked
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
print "So, you're %r old, %s tall and %r heavy." % (age, height, weight)

# we put a comma after every print line so that 'print' doesn't end the line 
# with a newline character (or carriage return) and go to a new line