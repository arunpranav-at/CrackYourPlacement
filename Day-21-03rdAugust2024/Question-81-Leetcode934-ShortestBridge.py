'''
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
'''

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def isValid(i, j):
            return 0 <= i < n and 0 <= j < n
        visited = set()
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        def dfs(i, j):
            if not isValid(i, j) or (i, j) in visited or not grid[i][j]:
                return
            visited.add((i, j))
            for dr, dc in directions:
                dfs(dr + i, dc + j)            
        def bfs():
            q = deque(visited)
            ans = 0
            while q:
                for i in range(len(q)):
                    cr, cc = q.popleft()
                    for dr, dc in directions:
                        nr = dr + cr
                        nc = dc + cc
                        if not isValid(nr, nc) or (nr, nc) in visited:
                            continue
                        if grid[nr][nc]:
                            return ans
                        q.append((nr, nc))
                        visited.add((nr, nc))
                ans += 1                            
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return bfs()
