"""
Given an array of integers, find the first missing positive integer in linear 
time and constant space. In other words, find the lowest positive integer that does 
not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
#test_list = [3, 4, -1, 1]
test_list = [1, 2, 0]

# without linear time constant and actually pretty ugly
def first_missing_pos(input_list):
    pos_list = [x for x in input_list if x >= 0]
    pos_list.sort()
    num = pos_list[0]
    for i in pos_list:
        if i == pos_list[-1]:
            return (num + 1)
            break
        if i != num:
            return num
            break
        if i == num: 
            num += 1
            next

# Solution in N time and no additional space
def first_missing_positive(nums):
    if not nums:
        return 1
    for i, num in enumerate(nums):
        while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
            v = nums[i]
            nums[i], nums[v - 1] = nums[v - 1], nums[i]
            nums[v - 1] = v
            if nums[i] == nums[v - 1]:
                break
    for i, num in enumerate(nums, 1):
        if num != i:
            return i
    return len(nums) + 1   

# Solution using set and counter
def first_missing_positive2(nums):
    s = set(nums)
    i = 1
    while i in s:
        i += 1
    return i  

print(first_missing_pos(test_list))   
print(first_missing_positive(test_list))  
print(first_missing_positive2(test_list))  