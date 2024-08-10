'''
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

 

Example 1:


Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:


Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
'''
from collections import deque
from typing import List
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append([i, j])
        if len(queue) == 0 or len(queue) == n * n:
            return -1
        res = 0
        dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dir:
                    if 0 <= r + dr < n and 0 <= c + dc < n and grid[r + dr][c + dc] == 0:
                        grid[r + dr][c + dc] = 1
                        queue.append([r + dr, c + dc])
            res += 1
        return res - 1