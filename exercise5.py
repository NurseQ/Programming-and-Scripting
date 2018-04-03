# James Quintin 03/03/18
# Exercise 5 

# code to open a file, without need for closing the file
with open("datum/iris.csv") as f:
    # print as a header for the values
    print("petal length " "petal width " "sepal length " "sepal width "" Iris Name")
    
    # loops thru the contents of the file
    for line in f:
        # splits the content into a list
        line = line.split(',')
        
        print('{:^12}{:^16}{:^8}{:^15}{:15}'.format(line[0],line[1],line[2],line[3],line[4])  )
        
