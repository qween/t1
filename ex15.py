from sys import argv

script,filename = argv # ref: ex15_sample.txt

txt = open(filename) # 'txt' is a variable of type 'file'
# The fn open returns a file object.
print type(txt)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()

# tried opening and reading files from the python shell prompt
# inside powershell
# txt = open("ex15_sample.txt")
# print txt.read()
# txt.close()

a = 3
print type(a)
