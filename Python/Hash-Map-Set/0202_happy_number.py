# 202 Happy Number
'''
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false
'''
def isHappy(n):
    # since the greatest number is 2**31-1, that means the digit would be ranged from 1 ~ 1 * 10^10
    # at most there is 10 digit number, and the least would be 1 digit
    # my idea is that eventually the number would hit a cycle if it is 'not happy'
    # thus, give it a loop and if it does not reach to 1, then it must be false
    i = 0
    while i < 10:
        numbers = []
        while n // 10 >= 1:
            numbers.append(n % 10)
            n = n // 10
        numbers.append(n)
        # square every value in the list and sum up
        sum = 0
        for value in numbers:
            sum += value ** 2
        if sum == 1:
            return True
        else:
            n = sum
            i += 1
    return False
def isHappy_2(n):
    # after I looked through other ppl's code, i realized that i can use set() to store the visit value
    # if the value is already in set(), that means the function now enter a cycle and it must be false
    visit = set()
    def generate_new_number(num):
        output = 0
        while num:
            output += (num % 10) ** 2
            num = num // 10
        return output
    new_number = generate_new_number(n)
    while new_number not in visit:
        if new_number == 1:
            return True
        visit.add(new_number)
        new_number = generate_new_number(new_number)
    return False
n = 19
print(isHappy_2(n))
