'''
Given an array of increasing numbers (range function in python)

find out how many bribes everone had to take to get to thier positions, note that a single person cannot bribe fore than 2 people in from of them

the input n is the number of people in line in sorted order

'''




def minimum_swaps(n,new_order):
    num_swaps = 0
    orig = list(range(1,n+1))
    new_order_dict = {}
    [new_order_dict.update({item:pos}) for pos,item in enumerate(new_order)]

    print(orig)
    print(new_order_dict)
    for i in range(n):
        # print(i)
        num_swaps += new_order[i] - orig[i]
        print(f'position {i} in new_order holds the value {new_order[i]}')
        print(f'the original list at this position had the value {orig[i]}')
        if new_order[i] - orig[i] >2:
            # print(num_swaps)
            print('INVALID')
            break
        else:
            num_swaps += new_order[i] - orig[i]
    
    print(num_swaps)


minimum_swaps(5,[1,5,4,2,3])