# 169 Majority Element
'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''
'''
def majorityElement(nums):
    from collections import defaultdict
    dict = defaultdict(int)
    for element in nums:
        dict[element] += 1
        if dict[element] > (len(nums) / 2):
            return element
'''
def majorityElement(nums):
    unique_element = list(set(nums))
    total = 0
    for element in nums:
        total += element
    n = len(nums)
nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))