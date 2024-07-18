'''
Find Pair Given Difference
Difficulty: EasyAccuracy: 27.25%Submissions: 241K+Points: 2
Given an array arr[] of size n and an integer x, return 1 if there exists a pair of elements in the array whose absolute difference is x, otherwise, return -1.

Example 1:

Input:
n = 6
x = 78
arr[] = {5, 20, 3, 2, 5, 80}
Output:
1
Explanation:
Pair (2, 80) have absolute difference of 78.
Example 2:

Input:
n = 5
x = 45
arr[] = {90, 70, 20, 80, 50}
Output:
-1
Explanation:
There is no pair with absolute difference of 45.
Your Task:
You need not take input or print anything. Your task is to complete the function findPair() which takes integers n, x, and an array arr[] as input parameters and returns 1 if the required pair exists, return -1 otherwise.
'''

from typing import List
import collections

class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        freq = collections.Counter(arr)
        for i in arr:
            val = i - x
            if val in freq and (val != i or freq[val] > 1):
                return 1
        return -1