# 136 Single Number
'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
'''
def singleNumber(nums):
    # use dictionary to store every element and see the value (frequency)
    # if the value == 1, then the key is the answer
    from collections import defaultdict
    dict = defaultdict(int)
    for value in nums:
        dict[value] += 1
    for key, value in dict.items():
        if value == 1:
            return key
nums = [1]
print(singleNumber(nums))