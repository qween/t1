print "I will now count my chickens:"

print "Hens", 25 + 30 / 6

print "Roosters", 100 - 25 * 3 % 4
# Using the PEMDAS order 100 - 75%4 = 100 - 3 = 97

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
# ans = 7
# 4%2 = 0 and 1/4 = 0. division considers only quotient,
# % considers only remainder 

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False"

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

print " 7/4 =", 7/4
print " 7.0/4.0 = ", 7.0/4.0
print " Round(7.0/4.0) = ", round(7.0/4.0)
print " Float(7.0/4.0) = ", float(7.0/4.0)
print " Int(7.0/4.0)   = ", int(7.0/4.0), "\n"


float_ans = 7.0/4.0
print " 7.0/4.0 = %f " % float_ans
print " 7.0/4.0 = %f " % int(float_ans)
print " 7.0/4.0 = %d " % int(float_ans)

float_int = float(7/4)
print " 7.0/4.0 = %f " % float_int