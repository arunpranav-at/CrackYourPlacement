'''
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.nodes = []
        if root:
            self.nodes.append(root.val)
        def helper(node):
            if not node:
                return
            if node.left:
                self.nodes.append(node.left.val)
                helper(node.left)
            if node.right:
                self.nodes.append(node.right.val)
                helper(node.right)        
        helper(root)
        self.nodes.sort()
        self.ans = float("inf")
        for i in range(1, len(self.nodes)):
            self.ans = min(self.ans, self.nodes[i] - self.nodes[i - 1])
        return self.ans