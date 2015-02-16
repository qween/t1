from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')# the file has to be opened in write mode
# the default mode is 'read'
#target = open(filename, 'a')# the file has to be opened in append mode
# to add to the existing info

print "Truncating the file. Goodbye!"
target.truncate() # cannot use truncate command without opening the file
# in write mode during the open command
# Even without using truncate command we're able to delete the existing
# contents, if we open the file in w mode.
# truncate is necessary if we open the file in append mode so that
# the original contents will be erased first.

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line2 : ")
line3 = raw_input("line3 : ")

# putting all the three lines of string variables in one string variable
# which is more efficient than using 6 target commands
#newstr = ("%s" + "\n" + "%s" + "\n" + "%s" + "\n") % ( line1, line2, line3)
# the above line works too but the below one is the easiest
newstr = line1 + "\n" + line2 + "\n" + line3
print newstr
print "I'm going to write these to the file."
target.write(newstr)

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally we, close it."
target.close()




