# Adapted from Ian McLoughlin

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Quintin"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

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
# ord() is a built in function in Python where when given a string representing one Unicode character it returns an integer representing the Unicode code point of that character. 
# For example, ord('Q') returns the integer 81 and ord('n') returns 110. 
# This is the inverse of chr() 
