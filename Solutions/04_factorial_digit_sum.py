# Simplest way to calculate the factorial using the math library https://docs.python.org/2/library/math.html
# Requires Python version 2.6 and higher
import math
print("Using the math library to calculate the factorial of 7: %d" % math.factorial(7))

# The standard factorial function using recursion https://stackoverflow.com/questions/5136447/function-for-factorial-in-python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
		
print("Recursive function, factorial of 7: %d" % factorial(7))

# Calls the factorial function for 100
factorialNum = factorial(100)
# Getting the sum of all digits in 100
print("Factorial digit sum of 100: %d" % sum([int(i) for i in str(factorialNum)]))