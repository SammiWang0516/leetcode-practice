# 81 Search in Rotated Sorted Array II
'''
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
'''
def search(nums, target):

    # the nums should be sorted
    # however, it got rotated. Thus, we need to find the original sorted array
    # does not fit for list contains only 2 elements
    sorted_nums = []
    i = 0                                   # pointer for rotation check
    while i+1 <= len(nums)-1:
        if nums[i] > nums[i+1]:
            sorted_nums = nums[i+1:]
            sorted_nums.extend(nums[:i+1])
            break
        else:
            i += 1

    def binary_search(array, start, end, target):
        # find the middle point
        middle = (start + end) // 2
        # base case
        if start > end:
            return False
        if array[middle] == target:
            return True
        elif array[middle] > target:
            return binary_search(array, start, middle-1, target)
        else:
            return binary_search(array, middle+1, end, target)

    if len(sorted_nums) == 0:
        return binary_search(nums, 0, len(nums)-1, target)
    else:
        return binary_search(sorted_nums, 0, len(sorted_nums)-1, target)

nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
print(search(nums, target))
# output = true