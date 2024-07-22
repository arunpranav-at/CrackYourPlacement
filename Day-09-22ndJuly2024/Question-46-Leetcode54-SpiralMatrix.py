'''
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])
        while top < bottom and right > left:
            for col in range(left, right):
                result.append(matrix[top][col])
            top += 1
            for row in range(top, bottom):
                result.append(matrix[row][right - 1])
            right -= 1
            if top < bottom:
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[bottom - 1][col])
                bottom -= 1
            if left < right:
                for row in range(bottom - 1, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        return result