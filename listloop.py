#James Quintin 02/03/18
#adapted from week 4 lecture of Ian McLoughlin

squares = [1, 4, 9, 16, 25]

i = 0
while i < len(squares):
    print(i, squares[i]) #print i and whatever i is in the list
    i = i + 1

words = ["cat", "mouse", "rabbit"]
for w in words:  # w is a special variable in for loops that represent whateverthe current word you are on in the list
    print(w, len(w))  

#to get a similar outcome as the while loop
for i in range(len(words)):
    print(i, words[i], len(words[i]))