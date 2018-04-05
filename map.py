#James Quintin
# this example show how to use the map function

def times2(x):
    return x * 2

print(times2(5))

seq = [2, 3, 4, 5, 6]

# if you want to use funtion times2 to a list
print(list(map(times2, seq)))

#the use of lambda expression eliminates the need for defining a function
print(list(map(lambda num: num * 3, seq)))