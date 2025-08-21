# 14 Longest Common Prefix
'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
'''
def longestCommonPrefix(strs):
    # take the first string as the comparison
    prefix = strs[0]
    if len(strs) == 1:
        return strs[0]
    else:
        for string in strs[1:]:
            temp = ''
            for i in range(len(string)):
                if i < len(prefix):
                    if string[i] == prefix[i]:
                        temp += prefix[i]
                    else:
                        break
            prefix = temp
    return prefix
'''
def longestCommonPrefix(strs):
    # find the shortest string in strs
    if len(strs) == 1:
        return strs[0]
    sorted_strs = sorted(strs)
    prefix = ''
    min_length = min(len(sorted_strs[0]), len(sorted_strs[-1]))
    for i in range(min_length):
        if sorted_strs[0][i] == sorted_strs[-1][i]:
            prefix += sorted_strs[0][i]
        else:
            break
    return prefix
strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))