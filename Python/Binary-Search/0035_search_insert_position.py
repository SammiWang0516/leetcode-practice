# 35 Search Insert Position
'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
'''
def searchInsert(nums, target):
    # first it is almost the same as binary search
    # however, if the value is not found, try to find its correct index
    def binary_search(nums, start, end, target):
        # middle index
        middle = (start + end) // 2
        # base case: start > end means the target value is not found
        # if there is only one element and it is not the target value, start would add 1
        if start > end:
            return end + 1
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            return binary_search(nums, start, middle-1, target)
        else:
            return binary_search(nums, middle+1, end, target)
    return binary_search(nums, 0, len(nums)-1, target)
nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))
# output = 1