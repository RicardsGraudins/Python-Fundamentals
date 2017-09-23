#Importing math library https://docs.python.org/2/library/math.html
import math
#Importing decimal library https://docs.python.org/2/library/decimal.html
from decimal import *

#If the user enters invalid input, inform the user of the exception https://docs.python.org/2/tutorial/errors.html
try:
	#Ask the user for input
	x = Decimal(input("Enter a number: "))
	z = Decimal(input("Enter squared guess: "))

	#Newton's method for square roots
	approx = z - ((z*z - x) / (2 * z))
	difference = 1

	#Loop until close to the real square root
	while difference > 0.00000000001:
		z = approx
		approx = z - ((z*z - x) / (2 * z))
		difference = z - approx
	
	#Print Newton's method
	print("\nUsing Newton's method:     " + str(approx))
	#Print accurate square root using math.sqrt(x)
	print("Using math.sqrt(x) method: " + str(Decimal(math.sqrt(x))))
except Exception:
	print("Invalid input, only integers permitted.")