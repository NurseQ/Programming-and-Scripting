# James Quintin 03/02/18
# Using split() to separate string component

with open("datum/iris.csv") as f:
    for line in f: 
        print(line.split(',')[0]) # prints to the terminal the first column of data


