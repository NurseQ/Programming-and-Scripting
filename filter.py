#James Quintin
#this code uses the expression filter

seq = [2,3,4,5,6]

#prints out the variables in the list that are even. 
print(list(filter(lambda num: num % 2==0, seq)))