def fib(n):
    n = int(sys.argv[1])
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
        print(a)
if __name__== "__main__":
    import sys
    fib(sys.argv[1:])
