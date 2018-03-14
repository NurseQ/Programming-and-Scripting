# how to use function
def sumall(upto):
    sumupto = 0
    for i in range(1, upto +1):
        sumupto = sumupto + i
    return sumupto


print("The sum of the values in the range is: ", sumall(50) )

# code below is to find the greatest common divisor
def gcd(x, y):
    while x != y:
        if x > y:
            x = x - y
        else: 
            y = y - x
    return x

print("The gcd of 6 and 15: ", gcd(6, 15))
z = gcd(221, 323)
print("gcd of 221 and 323 is : ", z)

# code below is a more efficient way to find the greatest common divisor

def GCD(x, y):
    while x != 0 and y!= 0:
        if x > y:
            x = x % y
        else: 
            y = y % x
    if x ==0:
        return y
    else: 
        return x

print("The gcd of 6 and 15: ", GCD(6, 15))
z = GCD(36, 96)
print("gcd of 36 and 96 is : ", z)



