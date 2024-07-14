'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        realRows = []
        realCols = []
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    realRows.append(row)
                    realCols.append(col)
        for row in realRows:
            for col in range(cols):
                matrix[row][col] = 0
        for col in realCols:
            for row in range(rows):
                matrix[row][col] = 0
        return matrix