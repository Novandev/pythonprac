'''
Program will take input and
'''
def divisors(div):
    div = int(sys.argv[1])
    x =range(2, div)
    for elem in x:
        if div % elem == 0:
            print("{} is an divisor of {}".format(elem,div))


if __name__ =="__main__" :
    import sys
    divisors(sys.argv[1:])
