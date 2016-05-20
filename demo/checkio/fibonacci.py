import sys

def Fibonacci(n):
    if n <= 1: 
        return 1
    else: 
        return Fibonacci(n-1) + Fibonacci(n-2)
    

sumf = 0
for i in sys.argv[1]:
    sumf = sumf + Fibonacci(int(i))

print Fibonacci(int(sys.argv[1])), sumf
