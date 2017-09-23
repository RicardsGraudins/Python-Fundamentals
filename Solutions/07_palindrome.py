#Palindrome - a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam
#Ask the user for input
word = raw_input("Enter a word, phrase or sequence: ");

#Check if the parameter passed is a palindrome
#Note that the function is case sensitive, madam is not the same as Madam
def palindromeTest(string):
	if(str(string) == str(string)[::-1]):
		return True
	else:
		return False
		
#Preform palindromeTest() on the user input to check if it's a palindrome
print(palindromeTest(word))

#Adapted from https://stackoverflow.com/questions/17331290/how-to-check-for-palindrome-using-python-logic