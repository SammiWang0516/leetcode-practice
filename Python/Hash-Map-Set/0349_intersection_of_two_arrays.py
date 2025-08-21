# 349 Intersection of Two Arrays
'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
'''
'''
def intersection(nums1, nums2):
    nums1_set = list(set(nums1))
    len_nums1 = len(nums1_set)
    nums2_set = list(set(nums2))
    len_nums2 = len(nums2_set)
    result = []
    # start from the shortest one
    if len_nums1 <= len_nums2:
        for i in range(len_nums1):
            if nums1_set[i] in nums2_set:
                result.append(nums1_set[i])
    else:
        for j in range(len_nums2):
            if nums2_set[j] in nums1_set:
                result.append(nums2_set[j])
    return result
'''
''' ** reduce space complexity **
def intersection(nums1, nums2):
    len_nums1 = len(nums1)
    len_nums2 = len(nums2)
    result = []
    if len_nums1 <= len_nums2:
        nums1_set = set(nums1)
        for value in nums1_set:
            if value in nums2:
                result.append(value)
    else:
        nums2_set = set(nums2)
        for value in nums2_set:
            if value in nums1:
                result.append(value)
    return result
'''
def intersection(nums1, nums2):
    nums1_set = set(nums1)
    nums2_set = set(nums2)
    result = []
    if len(nums1_set) <= len(nums2_set):
        for value in nums1_set:
            if value in nums2_set:
                result.append(value)
    else:
        for value in nums2_set:
            if value in nums1_set:
                result.append(value)
    return result
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))
a = {3, 4, 5, 6, 7}
c = {3, 8, 7, 2}
print(list(a & c))