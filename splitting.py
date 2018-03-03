# James Quintin 03/02/18
# Using split() to separate string component

with open("datum/iris.csv") as f:
    for line in f: 
        print(line) #adds another new line 


# adding print(line, end='') removes the new line in code above

# adding print(line.split(','), end='') places each line into a python list

# adding print(line.split(',')[0]) prints to the terminal the first column of data