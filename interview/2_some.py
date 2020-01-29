"""
S spme interview questions
with in an array,  count up 2 numbers that add up to  the target value
sample input 

[1,2,2,4,7,5,6],4

the unique solution would be 2 + 2
"""


def two_sum(arr,target):

    if len(arr) < 2 or target ==0:
        return None
    seen ={}
    seen[arr[0]] = True
    for item in arr:
        for value in seen:
            if item + value == target:
                return f"{target}, {item}, {value}"
        seen[item] =True
        # print(seen)
    return None

if __name__=="__main__":

    print(two_sum([1,2,2,4,7,5,6],4))
    print(two_sum([1,1,2,4,7,5,6],4))
    print(two_sum([0],4))
    print(two_sum([1,1,2,4,7,5,6],0))
        