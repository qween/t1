name = input("What's your name? ")
# the input str for the above prompt should be in single or double quotes from the user
# otherwise there's error.
# name = raw_input("What's your name? ")
# instead if you use the raw_input command, it take the user's input asis. 
# raw_input takes every input as a string
print ("Nice to meet you " + name + "!") # str addition
age = input("Your age? ")
print("So, you are already " + str(age) + " years old, " + name + "!")
print(age, type(age))
# input interprets the input. That's the reason, why we had to cast the variable "age" into a string.
# when the user enters a number for age, it has to be converted to a string by the str() fn
# so that it can be added with other strings in the print statement.