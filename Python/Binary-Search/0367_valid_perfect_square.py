# 367 Valid Perfect Square
'''
Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.

Example 1:
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:
Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
'''
def isPerfectSquare(num):
    # cannot use the built in function
    # thus, i can only find the integer smaller num
    # if i can find the value ** 2 that is equal to num, return true
    # if value ** 2 is smaller than num, find greater value
    # else, find smaller value
    def binary_search(num, start, end):
        # find middle value from 1 to num
        middle = (start + end) // 2
        if start > end:
            return False
        if middle ** 2 == num:
            return True
        elif middle ** 2 > num:
            return binary_search(num, start, middle-1)
        elif middle ** 2 < num:
            return binary_search(num, middle+1, end)
    return binary_search(num, 1, num)

num = 16
print(isPerfectSquare(num))
# output = true