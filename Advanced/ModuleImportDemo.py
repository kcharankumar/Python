# A python file named Maths.py is imported and named as MathsModule in here.
#All the functions of Maths modules is used in here.
import Maths as MathsModule

x = int(input('Enter a number..'))
y = int(input('Enter a number..'))

#Add and Multiply are the Maths module functions which are used in here.
result_add = MathsModule.add(x, y)
result_mul = MathsModule.multiply(x, y)

print('Result of additio is ', result_add)
print('Result of multiplation is : ', result_mul)




