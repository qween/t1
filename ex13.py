from sys import argv
# argv stands for argument variables
# the first line stands for importing arguments - modules or libraries
# specified while executing the script

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

print argv
print len(argv) # no. of features or modules

print len(first), len(second)

