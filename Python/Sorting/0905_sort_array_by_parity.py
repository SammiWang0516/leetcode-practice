# 905 Sort Array by Parity
'''
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:
Input: nums = [0]
Output: [0]
'''
def sortArrayByParity(nums):
    even_element = []
    odd_element = []
    for element in nums:
        if element % 2 != 0:        # odd number
            odd_element.append(element)
        else:
            even_element.append(element)
    return even_element + odd_element
nums = [0]
print(sortArrayByParity(nums))
# output = [2, 4, 3, 1]