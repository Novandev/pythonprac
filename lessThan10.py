'''
Program that will print all the numvers less than ten
'''
ten_or_less=[]
def lessThan10():
    list_10=[1,2,3,4,5,6,7,8,9,10]
    for element in list_10:
        if element < 10:
            ten_or_less.append(element)
    print (ten_or_less)

lessThan10()
