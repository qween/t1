x = "There are %d types of people." % 10 # assigning a string with a variable
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # assigning string inside string

print x
print y

print "I said: %r." % x # assigning string inside string r - displays the raw data of a variable
print "I also said: '%s'." % y # assigning string inside string

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" # assigning string inside string

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
 
print w + e # string concatenation


hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r" # assigning string inside string

print joke_evaluation % hilarious