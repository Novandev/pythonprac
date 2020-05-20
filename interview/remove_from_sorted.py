


def remove_duplicated(nums):
    '''
    Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

    Given nums = [0,0,1,1,1,2,2,3,3,4],

    Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

    It doesn't matter what values are set beyond the returned length.
    

    Algorithm

Since the array is already sorted, we can keep two pointers i and j, where i is the slow-runner while j is the fast-runner. As long as nums[i] = nums[j]nums[i]=nums[j], we increment jj to skip the duplicate.

When we encounter nums[j] != nums[i], the duplicate run has ended so we must copy its value to nums[i + 1].
 i is then incremented and we repeat the same process again until j reaches the end of array.
    '''
    if (len(nums) == 0):
         return 0
    i = 0
    for j in range(1,len(nums)-1):
        if nums[j] != nums[i]:
            i+=1
            nums[i] = nums[j]
 
    return i + 1

num_list = [1,1,2,3,4,5,5]
answer = remove_duplicated(num_list)

print(answer)
for i in range(answer):
    print(num_list[i])