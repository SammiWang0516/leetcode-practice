# 976 Larget Perimeter Triangle
'''
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Example 1:
Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.

Example 2:
Input: nums = [1,2,1,10]
Output: 0
Explanation:
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
'''
''' use 2 pointers with one sort (Big O(nlogn))
def largestPerimeter(nums):

    # sort the array first so that the shortest length comes first
    sort_nums = sorted(nums)

    # store the maximum perimeter from the array
    max_perimeter = float('-inf')

    # use 2 pointers and count the last combination
    i = 0                       # left pointer
    j = i + 2                   # right pointer

    # simplest case: if the nums has only three element, check again is fine
    if len(nums) == 3:
        if sort_nums[i] + sort_nums[i+1] > sort_nums[j]:
            return sort_nums[i] + sort_nums[i+1] + sort_nums[j]

    # other cases
    while i <= len(nums)-1-2:
        if sort_nums[i] + sort_nums[i+1] > sort_nums[j]:
            max_perimeter = max(max_perimeter, sort_nums[i] + sort_nums[i+1] + sort_nums[j])
        else:
            i += 1
            j = i + 2
            continue
        if j == len(nums)-1:
            i += 1
            j = i + 2
        else:
            j += 1
    if max_perimeter < 0:
        return 0
    else:
        return max_perimeter
'''
def largestPerimeter(nums):
    # sort the nums
    # search from the every end
    sort_nums = sorted(nums)
    i = len(nums)-1                 # pointer pointing at the last element
    while i-2 >= 0:
        if sort_nums[i-2] + sort_nums[i-1] > sort_nums[i]:
            return sort_nums[i-2] + sort_nums[i-1] + sort_nums[i]
        else:
            i -= 1
    return 0
nums1 = [2, 1, 2]                   # [1, 2, 2]
print(largestPerimeter(nums1))
# output = 5
nums2 = [1, 2, 1, 10]               # [1, 1, 2, 10]
print(largestPerimeter(nums2))
# output = 0
nums3 = [3, 2, 3, 4]                 # [2, 3, 3, 4]
print(largestPerimeter(nums3))
# output = 10