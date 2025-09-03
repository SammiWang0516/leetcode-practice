# 1051 Height Checker
'''
A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.
You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).
Return the number of indices where heights[i] != expected[i].

Example 1:
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation:
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.

Example 2:
Input: heights = [5,1,2,3,4]
Output: 5
Explanation:
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.

Example 3:
Input: heights = [1,2,3,4,5]
Output: 0
Explanation:
heights:  [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match.
'''
def heightChecker(height):
    # use merge sort to comapre 2 arrays and find the answer
    def mergesort(array):
        # base case
        if len(array) <= 1:
            return array
        middle = len(array) // 2
        left_array = mergesort(array[:middle])
        right_array = mergesort(array[middle:])
        return merge(left_array, right_array)
    def merge(left, right):
        result = []
        i = 0                   # left pointer for left array
        j = 0                   # right pointer for right array
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    sorted_height = mergesort(height)
    count = 0
    for k in range(len(height)):
        if height[k] != sorted_height[k]:
            count += 1
    return count
heights = [5, 1, 2, 3, 4]
print(heightChecker(heights))
# output = 3