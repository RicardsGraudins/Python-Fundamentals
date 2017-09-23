#Importing random library https://docs.python.org/3/library/random.html
import random

#Creating 2 hardcoded lists
myList = [1, 3, 5]
myList2 = [2, 4, 6]

#This function takes in 2 lists as parameters
def mergeLists(list1, list2):
	#Print the contents of the two lists
	print("\nPassed in the following lists:")
	print("List one: {}".format(list1))
	print("List two: {}".format(list2))
	#Concat the two lists into a new list
	list3 = list1 + list2
	#Sort the new list
	list3.sort()
	#Print the new list
	print("New sorted list: {}".format(list3))
	
#Passing in the two hardcoded lists into mergeLists()
mergeLists(myList, myList2)

#Using the random library - 2 lists are created with 5 randomly generated integers between
#1 and 100 in each list and then passed into mergeLists()
mergeLists([random.randint(1, 101) for i in range(5)], [random.randint(1, 101) for i in range(5)] )