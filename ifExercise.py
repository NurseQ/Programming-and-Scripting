#if statement practice 
#adapted from https://docs.python.org/3/tutorial/controlflow.html

x = int(input("Please enter your age: "))

if x <= 20:
    x = 0
    print("You are young!")
elif x <= 30:
    print("You are getting old!")
elif x <= 40:
    print("You are old!")
else:
    print("You are very old!")
