def Fibonacci(n):
    f = 0
    f = ((1.618034) ** n-(1-1.618034) ** n) // (5 ** 0.5)
    print(f)
Fibonacci(19)