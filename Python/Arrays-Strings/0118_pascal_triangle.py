# 118 Pascal's Triangle
'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
'''
def generate(numRows):
    result = []
    for i in range(numRows):
        # list is the list currently counting
        if i < 2:
            result.append([1] * (i+1))
        else:
            temp = []
            for j in range(i-1):
                temp.append(result[i-1][j] + result[i-1][j+1])
            result.append([1] + temp + [1])
    return result
numRows = 8
print(generate(numRows))