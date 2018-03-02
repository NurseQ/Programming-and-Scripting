#James Quintin 02/03/18
#Week 4 tutorial by Ian McLoughlin

for i in range(5):
    print(i)

#the above for loop is same as below but using range.

myrange = [0,1,2,3,4]
for j in myrange:
    print(j)

# This code loops thru a range from 6 to 11
for t in range (6, 12):
    print(t)


# This code loops thru a range from 4 to 20 in increments of 2's
for s in range (4, 20, 2):
    print (s)

#  Creates a list of 0-4 and print out whatever element is in the index
a = ["Mary", "had", "a", "little", "lamb"]
for i in range(len(a)):
    print(i, a[i])

# You don't need range if you want to just print out the elements of the list

for s in a:
    print(s)