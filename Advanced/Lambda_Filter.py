from functools import reduce
# Define a function which takes data and returns whether the number
# is even or odd.
def evenOrOdd(data):
    return data % 2 == 0

#Taking n number of inputs into a list.
n = int (input ('How many number of elements you want to enter in the list : '))
print ('Enter ', n ,' Elements')
numLst = []
for i in range (0,n):
    data = int (input ())
    numLst.append (data)

#Printing the original List.
print ("Entered list is : ", numLst)

#Filtering for even numbers in the list and printing it
filteredLst = list(filter(evenOrOdd, numLst))
print ('Filtered List is : ', filteredLst)

#Filtering for even numbers using lambda.
filteredLstWithLambda = list(filter(lambda x: x%2 ==0, numLst))
print ('Filtered List with Lambda is : ', filteredLstWithLambda)

#reduce operations.
total =   reduce(lambda x,y: x+y, numLst)
print ('Sum of all the lements are : ', total)
