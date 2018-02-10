#James Quintin 09/02/18
#Python code for Collatz conjecture

j = int(input("Enter a number: "))

while j > 1:
    print (j)
    
    if j % 2 == 0:
        j = j // 2
    else:
        j = (j * 3) + 1
        
    
