# 704 Binary Search
'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''
''' (simplest and the most straightforward thought)
def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
'''
def search(nums, target):
    # use binary search to find the value
    # much faster than a for loop, which takes O(n)
    # using binary search only take O(logn)
    def binary_search(array, start, end, target):
        # if the size of array is even number, then take the left side of element
        middle = (start + end) // 2
        # base case (only one element left or cannot find the target value)
        # if start > end, that means the target value is not in array
        if start > end:
            return -1
        if array[middle] == target:
            return middle
        elif array[middle] > target:
            return binary_search(array, start, middle-1, target)
        else:
            return binary_search(array, middle+1, end, target)
    return binary_search(nums, 0, len(nums)-1, target)
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search(nums, target))
# output = 4