'''
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
'''
from typing import List
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        iddict = dict()
        def islandIDdfs(i, j, id):
            grid[i][j] = id
            iddict[id] += 1
            dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in dir:
                nr, nc = dr + i, dc + j
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    islandIDdfs(nr, nc, id)
        def area(i, j):
            area = 1
            ids = set()
            if i + 1 < rows:
                id = grid[i + 1][j]
                if id != 0 and id not in ids:
                    area += iddict[id]
                    ids.add(id)
            if j + 1 < cols:
                id = grid[i][j + 1]
                if id != 0 and id not in ids:
                    area += iddict[id]
                    ids.add(id)
            if i - 1 >= 0:
                id = grid[i - 1][j]
                if id != 0 and id not in ids:
                    area += iddict[id]
                    ids.add(id)
            if j - 1 >= 0:
                id = grid[i][j - 1]
                if id != 0 and id not in ids:
                    area += iddict[id]
                    ids.add(id)
            return area
        curr = -1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    iddict[curr] = 0
                    islandIDdfs(i, j, curr)
                    curr -= 1
        if not iddict:
            return 1
        ans = max(iddict.values())
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    ans = max(area(r, c), ans)
        return ans