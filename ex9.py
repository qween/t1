# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" # \n for newlines
months2 = "\tSep\tOct\tNov\tDec"


print "Here are the days: ", days
print "Here are the months: ", months
print "Here are the months: %r " % months
print "Here are the months: %s " % months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

print "%r" % months2
print "%s\r" % months2