# python code problems and solutions
# Question 4 in http://www.practicepython.org/exercise/2014/02/26/04-divisors.html

x = int(input("Please input a number: "))
y = []

for i in range(2, x):
    if i % 2 == 0:
        y.append(i)
    
print(y)
