'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, word, index):
            if index == len(word):
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols or word[index] != board[row][col]:
                return False
            else:
                temp = board[row][col]
                board[row][col] = "$"

                toReturn = dfs(row + 1, col, word, index + 1) or dfs(row - 1, col, word, index + 1) or dfs(row, col + 1, word, index + 1) or dfs(row, col - 1, word, index + 1)

                board[row][col] = temp
                return toReturn

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, word, 0):
                    return True
        return False