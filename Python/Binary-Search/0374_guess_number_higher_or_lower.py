# 374 Guess Number Higher or Lower
'''
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns three possible results:
-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

Example 1:
Input: n = 10, pick = 6
Output: 6

Example 2:
Input: n = 1, pick = 1
Output: 1

Example 3:
Input: n = 2, pick = 1
Output: 1
'''
def guessNumber(n):
    # this question is packed like a game
    # but it is actually the concept of binary search
    # given a n, which is the integer range
    # target number is from API call
    # if, else if condition can compare with the result of api
    def binary_search(start, end):
        # since the picked number can be found, no need for base case
        middle = (start + end) // 2
        if guess(middle) == 0:
            return middle
        elif guess(middle) == -1:
            return binary_search(start, middle-1)
        else:
            return binary_search(middle+1, end)
    return binary_search(1, n)
n = 10
# pick = 6
print(guessNumber(n))
# output = 6g