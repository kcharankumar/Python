"""
  Program to add two numbers using lambda.
"""
num1 = int (input ("Enter a number "))
num2 = int (input ("Enter a number "))

# Here x and y are arguments.  THey are added and returned to a function name sum1.
sum1 = lambda x,y:x+y

#Sum1() is called with the input data and result is printed.
print(sum1(num1,num2))

