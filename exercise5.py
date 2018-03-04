# James Quintin 03/03/18
# Exercise 5 

with open("datum/iris.csv") as f:
    print("petal length " "petal width " "sepal length " "sepal width "" Iris Name")
    for line in f:
        
        line = line.split(',')
        
        print('{:^12}{:^16}{:^8}{:^15}{:15}'.format(line[0],line[1],line[2],line[3],line[4]),  )
        
