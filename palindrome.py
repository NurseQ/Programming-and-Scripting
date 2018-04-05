# James Quintin, 21/03/2018
# Problems: Python Fundamentals no. 2
#Adapted from Ian McLoughlin


def ispalindrome(word):
    
    ans = True #starts with an assumption that you have a palindrome
    #this loops through the range of the length of the string,  
    for i in range(len(word)):
        # the range loop produces the index (0,1,2...) but to get to the character of the index, use i as index or subscript of string 
        if word[i] != word[len(word)-1-i]:
            #if word[i] means if the current character  is not equal to the 
            #word[len(word)-1-i] this works out last character
            ans = False

    return ans

print(ispalindrome("radar"))
print(ispalindrome("radars"))