#Ask the user for input
word = raw_input("Enter a word to reverse:")

#Simplest way to reverse a string:
#Function takes in string as parameter and outputs reverse string
def reverseString(string):
	reversed = string[::-1]
	print("The reverse of %s is %s" % (string, reversed))
	
#Passing in user input into reverseString()
reverseString(word)

#Alternatively the recursive way:
#Ref. https://stackoverflow.com/questions/18686860/reverse-a-string-without-using-reversed-or-1
def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]
	
#Passing in user input into reverse()
print("\nRecursive function output: %s" % reverse(word))