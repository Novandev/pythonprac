"""
this function should compute the nth fibonocci number

"""

def fib(num):
    if num == 1:
        return 1
    if num < 1:
        return 0
    return num * fib(num -1)


if __name__ == "__main__":
    print(fib(5))