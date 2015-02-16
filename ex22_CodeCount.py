from sys import argv
script, filename = argv

def code_count(code_file):
	total_lines = 0
	empty_lines = 0
	comment_lines = 0
	
	file_object = open(code_file, 'r')
	
	for line in file_object:
		character_list = line.split()
		
		if character_list == []:
			empty_lines += 1
		elif character_list == '#':
			comment_lines += 1
		total_lines += 1
		
	file_object.close()
	print "Total Lines = %d, Empty Lines = %d, Comment Lines = %d" % (
		total_lines, empty_lines, comment_lines)
	return total_lines, empty_lines, comment_lines
	
t,e,c = code_count(filename)

