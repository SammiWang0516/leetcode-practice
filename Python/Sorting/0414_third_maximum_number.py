# 414 Third Maximum Number
'''
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
'''
''' (using sorted method,which is Big O (nlogn)
def thirdMax(nums):
    sorted_nums = sorted(nums, reverse = True)
    unique_sorted = []
    for value in sorted_nums:
        if value not in unique_sorted:
            unique_sorted.append(value)
    if len(unique_sorted) >= 3:
        return unique_sorted[2]
    else:
        return unique_sorted[0]
'''
''' (find the max and second large value first)
def thirdMax(nums):
    # identify max value and second max value
    max_value = second_max_value = third_max_value = float('-inf')
    n = len(nums)
    # find the max value
    for i in range(n):
        max_value = max(max_value, nums[i])
    # if there is only 2 or less values, return the max one
    if n <= 2:
        return max_value
    # if more than 2 values, find the second maximum
    for j in range(n):
        if nums[j] == max_value:
            continue
        second_max_value = max(second_max_value, nums[j])
    for k in range(n):
        if nums[k] == max_value or nums[k] == second_max_value:
            continue
        third_max_value = max(third_max_value, nums[k])
    if third_max_value == float('-inf'):
        return max_value
    else:
        return third_max_value
'''
def thirdMax(nums):
    # first use set() to get the unique value
    unique_value = set(nums)
    # make it a list so that we can slice them
    list_unique_value = list(unique_value)
    first = second = third = float('-inf')
    n = len(list_unique_value)
    for i in range(n):
        # if current value is greater than maximum value
        if list_unique_value[i] > first:
            first, second, third = list_unique_value[i], first, second
        # if current value is less than first but greater than second max value
        elif list_unique_value[i] > second:
            second, third = list_unique_value[i], second
        # if current value is less than both maximum and second max value but greater than third value
        # assign such value to third variable
        elif list_unique_value[i] > third:
            third = list_unique_value[i]
    if n >= 3:
        return third
    else:
        return first
nums = [2, 2, 3, 1, 4]
print(thirdMax(nums))