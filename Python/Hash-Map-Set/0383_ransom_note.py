# 383 Ransom Note
'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
'''
def canConstruct(ransomNote, magazine):
    dict_note = {}
    dict_magazine = {}
    for char in ransomNote:
        if char not in dict_note:
            dict_note[char] = 1
        else:
            dict_note[char] += 1
    for char in magazine:
        if char not in dict_magazine:
            dict_magazine[char] = 1
        else:
            dict_magazine[char] += 1
    for key, value in dict_note.items():
        if key not in dict_magazine:
            return False
        else:
            if value > dict_magazine[key]:
                return False
    return True
def canConstruct_2(ransomNote, magazine):
    from collections import defaultdict
    dict_note = defaultdict(int)
    dict_magazine = defaultdict(int)
    for char in ransomNote:
        dict_note[char] += 1
    for char in magazine:
        dict_magazine[char] += 1
    for key, value in dict_note.items():
        if key not in dict_magazine:
            return False
        else:
            if value > dict_magazine[key]:
                return False
    return True
ransomNote = 'aa'
magazine = 'aab'
print(canConstruct_2(ransomNote, magazine))