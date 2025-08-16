# 28 Find the Index of the First Occurence in a String
'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''
'''
def strStr(haystack, needle):
    dict = {}
    n = len(haystack)
    for i in range(n):
        dict[i] = []
        for j in range(i, n):
            dict[i].append(haystack[i:j+1])
    for key, value in dict.items():
        if needle in value:
            return key
    return -1
'''
def strStr(haystack, needle):
    len_nee = len(needle)
    len_hay = len(haystack)
    dict = {}
    for i in range(len_hay - len_nee + 1):
        dict[i] = haystack[i:i+len_nee]
    for key, value in dict.items():
        if needle in value:
            return key
    return -1
haystack = 'sadbutsad'
needle = 'sad'
print(strStr(haystack, needle))

