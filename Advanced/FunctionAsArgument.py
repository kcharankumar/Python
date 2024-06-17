""""
A unction add is defined with 2 arguments in it (x and y).  THsi function will add x and y and will return the result
Another function maths is defined which takes func as the function name and x and y as the argument.  Func is
the functionname here.  whatever the result of func(x,y) that is stored in a variable and it is return.
THe calling portiong of maths() is displaying the result.
"""

def add(x,y):
    return x + y

def maths(func, x, y):
    result = func(x,y)
    return result

result = maths (add, 10,20)
print ('Result is : ',result)
