#James Quintin 09/02/18
#Python code for Collatz conjecture
#Week 3 exercise

# asks user to input a number character that python converts into int
j = int(input("Enter a number: "))

# 1 is eventual end number of Collatz conjecture
while j > 1:
    #prints first number
    print (j)
    
    # conditional to test if int is divisble without remainder, hence even
    if j % 2 == 0:
        #// - division that results into whole number (condition for even int)
        j = j // 2
    else:
        ## multiply by 3 add 1 (condition for odd int)
        j = (j * 3) + 1
        
    
