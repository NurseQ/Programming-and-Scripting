#James Quintin 02/04/18
#python code for project euler problem no. 5
#adapted from https://gist.github.com/PEZ/47534 

# This script first defines a function to return gcd, then calculate lcm

# function to calculate greatest common divisor
def gcd(a, b):
  #this while loop uses less lines rather than with if statement
  while b > 0:
    a, b = b, a % b
  return a

#this function calculates the lowest common multiple of two ints
def lcm(a, b):
  return (a * b) / gcd(a, b)

#calculates lcm of range of numbers
ans = lcm(11, 12)
for n in range(12, 20):
  ans = lcm(n, ans)

print (ans)
    
