#Using the range function we create a list of numbers from 0 to 99 https://docs.python.org/2/library/functions.html#range
#Each number in the list is FizzBuzz tested
#If the number is a multiple of 3 and a multiple of 5 - print "FizzBuzz"
#If the number is only a multiple of 3 				  - print "Fizz"
#If the number is only a multiple of 5				  - print "Buzz"
#If the number is not a multiple of 3 or 5            - print the number

for i in range (100):
	if i % 3 == 0 and i % 5 == 0:
		print("FizzBuzz")
	elif i % 3 == 0:
		print("Fizz")
	elif i % 5 == 0:
		print("Buzz")
	else:
		print(i)