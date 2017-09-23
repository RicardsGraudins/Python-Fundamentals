#Importing random library https://docs.python.org/3/library/random.html
import random

#Answer variable is a random int between 0-10 and can also be either 0 or 10
answer = random.randint(0,10)
correctGuess = False
tries = 0
prevGuess = None

#The while loop runs endlessly until the user inputs the correct answer
while(correctGuess is False):
	#If the user enters invalid input, inform the user of the exception https://docs.python.org/2/tutorial/errors.html
	try:
		guess = int(input("Guess the number: "))
		print("You entered %d" % guess)
		
		#If the user guesses correctly, add 1 to tries and set correctGuess to True which exits the while loop
		if (guess == answer):
			print("You guessed correct, the number is %d!" % guess)
			tries = tries + 1
			print("It took you %d tries." % tries)
			correctGuess = True;
		
		#Else, if the user answers incorrectly:
		#Add 1 to tries if the previous guess wasn't the same number, in other words,
		#if the user enters the same guess n number of times consecutively, it will only count as 1 try
		else:
			print("You guessed incorrectly, try again!")
			if(prevGuess != guess):
				tries = tries + 1
				prevGuess = guess
			
		#If the guess is lower or higher than the answer, give the user a hint
			if (guess < answer):
				print("Your guess is too low.")
			elif (guess > answer):
				print("Your guess is too high.")
	except Exception:
		print("Invalid input, only integers permitted.")