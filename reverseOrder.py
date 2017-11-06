def reverse(listo):
    listo =list(sys.argv[1:])
    print(listo)
    print(" ".join(listo[::-1]))


if __name__=="__main__":
    import sys
    reverse(sys.argv[1:])
