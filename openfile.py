#f = open("datum/iris.csv")
#print (f.read())
#f.close() 

#closing file is good practice


#Using ff code will make closing file unnecessary
with open("datum/iris.csv") as f:
    contents = (f.read())
    print(contents)