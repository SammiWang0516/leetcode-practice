# 977 Squares of a Sorted Array
'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''
def sortedSquares(nums):
    # extract the list with negative values
    # extract the list with postive values, which is already sorted

    square_list = []
    for value in nums:
        square_value = value ** 2
        square_list.append(square_value)

    point = 0
    n = len(nums)
    for i in range(n):
        if nums[i] < 0:
            point += 1
    neg_list = []
    pos_list = []
    neg_list = square_list[:point][::-1]
    pos_list = square_list[point:]

    j = 0  # pointer for negative list
    k = 0  # pointer for positive list
    if len(neg_list) == 0:
        return pos_list
    elif len(pos_list) == 0:
        return neg_list
    else:
        result = []
        while True:  # traverse all elements in negative list
            min_value = min(neg_list[j], pos_list[k])
            result.append(min_value)
            if neg_list[j] > pos_list[k]:
                k += 1
                if k == len(pos_list):
                    return result + neg_list[j:]
            else:
                j += 1
                if j == len(neg_list):
                    return result + pos_list[k:]
nums = [-7, -3, 2, 3, 11]
print(sortedSquares(nums))
