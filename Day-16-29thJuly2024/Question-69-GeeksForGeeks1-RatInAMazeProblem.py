'''
Rat in a Maze Problem - I
Difficulty: MediumAccuracy: 35.75%Submissions: 263K+Points: 4
Consider a rat placed at (0, 0) in a square matrix mat of order n* n. It has to reach the destination at (n - 1, n - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell. In case of no path, return an empty list. The driver will output "-1" automatically.

Examples:

Input: mat[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1}, 
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output:
DDRDRR DRDDRR
Explanation:
The rat can reach the destination at 
(3, 3) from (0, 0) by two paths - DRDDRR 
and DDRDRR, when printed in sorted order 
we get DDRDRR DRDDRR.
Input: mat[][] = {{1, 0},
         {1, 0}}
Output:
-1
Explanation:
No path exists and destination cell is 
blocked.
Expected Time Complexity: O((3N^2)).
Expected Auxiliary Space: O(L * X), L = length of the path, X = number of paths.

Constraints:
2 ≤ n ≤ 5
0 ≤ mat[i][j] ≤ 1
'''

class Solution:
    def findPath(self, mat):
        n = len(mat)
        ans = []
        if mat[0][0] == 0 or mat[n-1][n-1] == 0:
            return ans
        def dfs(row, col, path):
            if row == n - 1 and col == n - 1:
                ans.append("".join(path))
                return
            if not(0 <= row < n) or not(0 <= col < n) or mat[row][col] == 0:
                return
            temp = mat[row][col]
            mat[row][col] = "$"
            if row + 1 < n and mat[row + 1][col] != "$":
                path.append("D")
                dfs(row + 1, col, path)
                path.pop()
            if col + 1 < n and mat[row][col + 1] != "$":
                path.append("R")
                dfs(row, col + 1, path)
                path.pop()
            if row - 1 >= 0 and mat[row - 1][col] != "$":
                path.append("U")
                dfs(row - 1, col, path)
                path.pop()
            if col - 1 >= 0 and mat[row][col - 1] != "$":
                path.append("L")
                dfs(row, col - 1, path)
                path.pop()
            mat[row][col] = temp
        dfs(0, 0, [])
        return ans