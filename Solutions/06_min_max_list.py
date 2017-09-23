#Importing random library https://docs.python.org/3/library/random.html
import random

#Hardcoded list of numbers
myList = [16,6,2,4,7,9,1,12,15]

#Function that takes in list as parameter and returns the min and max values
def minMax(list):
	return("The min value is: %d \nThe max value is: %d" % (min(list), max(list)))
	
#Passing myList into minMax()
print(minMax(myList))

#Function that creates a list of 10 random numbers in the (inclusive) range from 1 to 100,
#Prints the values generated as well as the min and max values
def minMax2():
	myRandomList = random.sample(xrange(1, 101), 10)
	print("\nRandomly generated list of numbers: {}".format(myRandomList))
	print("The min value is: %d \nThe max value is: %d" % (min(myRandomList), max(myRandomList)))

#Calling minMax2()
minMax2()