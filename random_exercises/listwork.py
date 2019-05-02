'''
takes all even elements and puts them into another list
'''
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def geteven():
    b = []
    for even in a:
        if even % 2 == 0:
            b.append(even)
    print(b)

geteven()
