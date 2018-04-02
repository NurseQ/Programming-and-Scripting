#James Quintin 02/04/18
#python code for project euler problem no. 5
#adapted from https://gist.github.com/PEZ/47534 


def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

def lcm(a, b):
  return (a * b) / gcd(a, b)

llcm = lcm(11, 12)
for n in range(12, 20):
  llcm = lcm(n, llcm)

print (llcm)
    
