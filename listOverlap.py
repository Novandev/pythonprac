'''
this will check for elements in a list that overlap
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common =[]
#for each of the elements in b
for item in b:
    #if the element is in a but not already in common
    if item in a and item not in common:
        common.append(item)
for elem in common:
    print (elem)
