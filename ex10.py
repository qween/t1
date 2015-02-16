tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \/ a \\ cat." # backslash escape, '\/' - doesn't work

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

fat_cat2 = """
I'll do a list:
\t* Cat food\n\t* Fishies\n\t* Catnip\n\t* Grass
"""
print fat_cat2

fat_cat3 = '''
I'll do a list:
\t* Cat food\n\t* Fishies\n\t* Catnip\n\t* Grass
'''
print fat_cat3 # Both single and double quoted strings give same output

print "I am 6'2\" tall." # escape double-quote in a double-quoted string
print 'I am 6\'2" tall.' # escape single-quote in a single-quoted string

# infinite loop example
#while True:
#	for i in ["/","-","|","\\","|"]:
#		print "%s\r" % i,



