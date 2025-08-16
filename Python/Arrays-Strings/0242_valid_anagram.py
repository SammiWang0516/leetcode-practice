# 242 valid anagram
'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''
def isAnagram(s, t):
    dict = {}
    for char in s:
        if char in dict:
            dict[char][0] += 1
        else:
            dict[char] = [1, 0]
    for char in t:
        if char in dict:
            dict[char][1] += 1
        else:
            dict[char] = [0, 1]
    for key, value in dict.items():
        if value[0] != value[1]:
            return False
    return True
s = 'rat'
t = 'car'
print(isAnagram(s, t))