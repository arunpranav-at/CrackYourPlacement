'''
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
'''
from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i + 1, j) if i + 1 < rows and val > matrix[i + 1][j] else 0,
                    dfs(i, j + 1) if j + 1 < cols and val > matrix[i][j + 1] else 0,
                    dfs(i - 1, j) if i - 1 >= 0 and val > matrix[i - 1][j] else 0,
                    dfs(i, j - 1) if j - 1 >= 0 and val > matrix[i][j - 1] else 0                    
                )
            return dp[i][j]            
        for i in range(rows):
            for j in range(cols):
                dfs(i, j)
        return max(max(i) for i in dp)