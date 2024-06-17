# Making user to enter 'n' number of elements in the list.
num = int (input('How many elements you want in a list : '))
print ('Enter ', num, ' elemenets ')
numLst = []

for i in range (0, num):
    data = int (input())
    numLst.append(data)

# Create the iterator.
iterator = iter (numLst)

#Iteate in the lop and display the elments of the list.
for i in iterator:
    print (i)
