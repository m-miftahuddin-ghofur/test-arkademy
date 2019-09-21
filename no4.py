def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def fibo(f,g):
    for i in range(g):
        l = list(fib(f))
        print(l)
        f = f + g + 1
    
fibo(4,3)

