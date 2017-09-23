# Python-Fundamentals
This repository contains solutions to the [Python fundamentals problem sheet](https://emerging-technologies.github.io/problems/python-fundamentals.html) completed as part of my course work for the module [Emerging Technologies](https://emerging-technologies.github.io/).
The module is taught to undergraduate students at [GMIT](http://www.gmit.ie/) in the Department of Computer Science and Applied Physics for the course [B.S.c. (Hons) in Software Developement.](https://www.gmit.ie/software-development/bachelor-science-honours-software-development) The lecturer is  [Dr. Ian McLoughlin](https://ianmcloughlin.github.io/).

The aim of this problem sheet is to give you a good understanding of Python. There are a variety of training exercises that are optimal for either learning Python from the ground up or refreshing your memory of the language.

## How this repository is organized:
Each solution to each problem on the problem sheet is in its own file. The files are named in the format `##-title.py`.

## How to run:
Download the repository and using the command console CD into the directory then launch the desired solution by typing `##-title.py` e.g. `01_hello_world.py`  

**Note:** Python version 2.6 or higher must be installed. Recommended [Python 3.6.1](https://www.python.org/downloads/release/python-361/)

## Exercises:
## 01. Hello, World!
Write a program that prints “Hello, world!” to the screen.
## 02. Current time
Write a program that prints the current time and date to the console.
## 03. FizzBuzz
Source: [http://wiki.c2.com/?FizzBuzzTest](http://wiki.c2.com/?FizzBuzzTest)

Write a program that prints the numbers from 1 to 100, except for the following conditions. For multiples of three print “Fizz” instead of the number, and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
## 04. Factorial digit sum
Write a function that calculates the sum of the digits of the factorial of a number. n! means n x (n − 1) … x 3 x 2 x 1. For example, 10! = 10 x 9 x … x 3 x 2 x 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. Find the sum of the digits in the number 100!
## 05. Guessing game
Source: [https://adriann.github.io/programming_problems.html](https://adriann.github.io/programming_problems.html)

Write a guessing game where the user must guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. It counts only as one try if they input the same number multiple times consecutively.
## 06. Largest and smallest in list
Source: [https://adriann.github.io/programming_problems.html](https://adriann.github.io/programming_problems.html)

Write a function that returns the largest and smallest elements in a list.
## 07. Palindrome test
Source: [https://adriann.github.io/programming_problems.html](https://adriann.github.io/programming_problems.html)

Write a function that tests whether a string is a palindrome.
## 08. Merge list and sort
Source: [https://adriann.github.io/programming_problems.html](https://adriann.github.io/programming_problems.html)

Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6].
## 09. Newton’s method for square roots
Source: [https://tour.golang.org/flowcontrol/8](https://tour.golang.org/flowcontrol/8)

Implement the square root function using Newton’s method. In this case, Newton’s method is to approximate sqrt(x) by picking a starting point z and then repeating:

`z_next = z - ((z*z - x) / (2 * z))`

To begin with, just repeat that calculation 10 times and see how close you get to the answer for various values (1, 2, 3, …). Next, change the loop condition to stop once the value has stopped changing (or only changes by a very small delta). How close are you to the math.sqrt value?
## 10. Reverse string
Write a function to reverse a string.
