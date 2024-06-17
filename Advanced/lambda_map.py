"""
  With regular function, which takes a number and multiply with itself and returns the data.
"""
def numMultiply (data):
     result = data * data
     return result

#Defining a list of numbers
numLst = [1,2,3,4,5]

#Calling a map function with the data and the result is returned to sqr_lst
sqr_lst = list(map(numMultiply, numLst))
print ('Original List : ',numLst)
print ("Square list   : ", sqr_lst) #Result is printed.

# The same using lambda function...
sqrLst2 = list(map(lambda data : data*data, numLst))
print ("\nSame functionality with Lambda : ", sqrLst2)
