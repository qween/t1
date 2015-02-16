dividend = 0
divisor_3 = 3
divisor_5 = 5
sum = 0

while dividend < 1000
	dividend += 1
	if dividend % divisor_3 == 0 OR dividend % divisor_5 == 0
	then sum += dividend
	end
	
print "Sum of multiples of 3 and 5 under 1000 is %d", % int(sum)

