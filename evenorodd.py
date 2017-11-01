#program takes a number fomr the command line and depending on wether it is even or odd returns a message

def evenOrOdd(num):
    num = int(sys.argv[1])
    if num % 2 == 0:
        print("Bih, its even")
    else:
        print("Bih, its odd")

if __name__ == "__main__":
    import sys
evenOrOdd(sys.argv[1:])
