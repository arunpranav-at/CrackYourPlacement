'''
Given a square chessboard, the initial position of Knight and position of a target. Find out the minimum steps a Knight will take to reach the target position.

Note:
The initial and the target position coordinates of Knight have been given according to 1-base indexing.

 

Example 1:

Input:
N=6
knightPos[ ] = {4, 5}
targetPos[ ] = {1, 1}
Output:
3
Explanation:

Knight takes 3 step to reach from 
(4, 5) to (1, 1):
(4, 5) -> (5, 3) -> (3, 2) -> (1, 1).
 

 

Your Task:
You don't need to read input or print anything. Your task is to complete the function minStepToReachTarget() which takes the initial position of Knight (KnightPos), the target position of Knight (TargetPos), and the size of the chessboard (N) as input parameters and returns the minimum number of steps required by the knight to reach from its current position to the given target position or return -1 if its not possible.

 

Expected Time Complexity: O(N2).
Expected Auxiliary Space: O(N2).
'''

from collections import deque
class Solution:

	#Function to find out minimum steps Knight needs to reach target position.
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
		
		start = (KnightPos[0] - 1, KnightPos[1] - 1)
		target = (TargetPos[0] - 1, TargetPos[1] - 1)
		
		directions = [(-2, -1), (-2, 1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
		visited = set()
		
		queue = deque()
		queue.append(start)
		visited.add(start)
		steps = 0
		
		while queue:
		    for i in range(len(queue)):
    		    curr = queue.popleft()
    		    if curr == target:
    		        return steps
    		        
    	        for di, dj in directions:
    	            if 0 <= curr[0] + di < N and 0 <= curr[1] + dj < N and (curr[0] + di, curr[1] + dj) not in visited:
    	                queue.append((curr[0] + di, curr[1] + dj))
    	                visited.add((curr[0] + di, curr[1] + dj))
            steps += 1
            
        return -1