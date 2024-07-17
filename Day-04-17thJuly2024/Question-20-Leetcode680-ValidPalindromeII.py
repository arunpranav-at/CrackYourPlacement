'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        if i == j:
            return True
        else:
            st1 = s[:i] + s[i + 1:]
            st2 = s[:j] + s[j + 1:]
            if st1 == st1[::-1] or st2 == st2[::-1]:
                return True
        return False