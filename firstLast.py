#James Quintin 28/02/18
#Adapted from Ian McLoughlin from https://github.com/ianmcloughlin/python-fib/blob/master/fibname.py
#Exercise 1 and 2

"""This function returns the nth Fibonacci number."""
def fib(n):
  
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    # Fibonacci sequence, start from 0 and 1, every number after the first two is the sum of the two preceding ones
    n = n - 1
    # counter and reduce n by 1 until 0.
  return i

name = "Quintin"
first = name[0]
#assigns first with index 0 or first letter of name
last = name[-1]
#assigns last to last letter of name
firstno = ord(first)
#ord function to assign integer of the unicode point of that character
lastno = ord(last)
x = firstno + lastno
#adds int of first and last letter of name then assigns to x 
ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

#Exercise 1
#My name is James, so the first and last letter of my name (J + S = 10 + 19) give the number  29. The 29th Fibonacci number is 514229. 

#Exercise 2
# My last name is Quintin. 
# The first letter Q is number 81. 
# The last letter n is number 110. 110 + 81 = 191
# Fibonacci number 191 is 3691087032412706639440686994833808526209
""" ord() is a built in function in Python where when given a string representing one Unicode character it returns an integer representing the Unicode code point of that character. 
For example, ord('Q') returns the integer 81 and ord('n') returns 110. 
This is the inverse of chr()"""
