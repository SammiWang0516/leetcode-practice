# 350 Intersection of Two Arrays II
'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
'''
def intersect(nums1, nums2):
    # store the value and its frequency from longer list
    from collections import defaultdict
    dict_nums1 = defaultdict(int)
    dict_nums2 = defaultdict(int)
    # list of result
    result = []
    for element in nums1:
        dict_nums1[element] += 1
    for element in nums2:
        dict_nums2[element] += 1
    for key, value in dict_nums1.items():
        if key in dict_nums2.keys():
            if dict_nums1[key] <= dict_nums2[key]:
                result.extend([key] * dict_nums1[key])
            else:
                result.extend([key] * dict_nums2[key])
    return result

nums1 = [54,93,21,73,84,60,18,62,59,89,83,89,25,39,41,55,
         78,27,65,82,94,61,12,38,76,5,35,6,51,48,61,0,47,
         60,84,9,13,28,38,21,55,37,4,67,64,86,45,33,41]
nums2 = [17,17,87,98,18,53,2,69,74,73,20,85,59,89,84,91,
         84,34,44,48,20,42,68,84,8,54,66,62,69,52,67,27,
         87,49,92,14,92,53,22,90,60,14,8,71,0,61,94,1,22,
         84,10,55,55,60,98,76,27,35,84,28,4,2,9,44,86,12,
         17,89,35,68,17,41,21,65,59,86,42,53,0,33,80,20]

print(intersect(nums1, nums2))
# output = [2, 2]

a = [54,21,73,84,60,18,62,59,89,89,41,55,27,65,94,61,12,76,35,48,0,60,84,9,28,55,4,67,86,33]
print(sorted(a))