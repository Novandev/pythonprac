def checkPrime(num):
    num= int(sys.argv[1])
    x =range(2, num)
    def isPrime(x):
        for elem in x:
            if num % elem == 0:
                return False

    check = isPrime(x)
    if check == False:
        print (False)
    else:
        print (True)

if __name__== "__main__":
    import sys
    checkPrime(sys.argv[1:])
