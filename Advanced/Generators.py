def fibonacci(n):
    #Initialize the data
    fib1=0; fib2=1; result = 0;

    #Send initial values to the calling method.
    yield fib1
    yield fib2

    #Iteate and generate fibonacci numbers and send one by one
    for i in range (0,n-2):
        result = fib1 + fib2

        yield result

        fib1 = fib2;
        fib2=result

num = int (input ('How Many nubmer of fibinacci numbers to be generated : '))

#Generator returng iterator
fib_iterator = fibonacci(num)
for i in fib_iterator:
    print (i)


