#James Quintin 01/04/18
#Exercise 6 
#function to output the factorial of a positive integer

# define function
def myfactorial (x):
    ans = 1
    #loop, start with number 1 and add one to end variable
    for i in range(1, x+1):
        #calculate factorial
        ans = ans * i
    
    return ans
#test factorial
print("the factorial of 10: ", myfactorial(10))
print("the factorial of 7: ", myfactorial(7))
print("the factorial of 5: ", myfactorial(5))

