'''
Print all the duplicate characters in a string
Last Updated : 30 Apr, 2024
Given a string S, the task is to print all the duplicate characters with their occurrences in the given string.

Example:

Input: S = “geeksforgeeks”
Output:

e, count = 4
g, count = 2
k, count = 2
s, count = 2

Explanation: e,g,k,and s are characters which are occured in string in more than one times.
'''
import collections
class Solution:
    def printDuplicates(self, s: str) -> None:
        freq = collections.Counter(s)
        for i in freq:
            if freq[i] > 1:
                print(i, ", count = ", freq[i])