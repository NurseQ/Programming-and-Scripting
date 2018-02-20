# The fizzbuzz game

j = 1

while j <= 30:
    if (j % 3 ==0) and (j % 5 == 0):
        print("fizzbuzz")
    elif j % 3 == 0:
        print("fizz")
    elif j % 5 ==0:
        print("buzz")
    
    else:
        print(j)
    j = j+1
