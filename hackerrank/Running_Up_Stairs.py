def fibonacci(x):
    fib = [0 for i in range(22001)]
    fib[0] = 1
    fib[1] = 1
    for i in range(2, x+1):
        fib[i] = fib[i - 2] + fib[i - 1]
    return fib[x]

t = int(input())
for i in range(t):
    stairs = int(input())
    print(fibonacci(stairs))