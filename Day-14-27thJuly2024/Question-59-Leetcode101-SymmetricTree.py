'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, root1, root2) -> bool:
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        return root1.val == root2.val and self.isSameTree(root1.left, root2.right) and self.isSameTree(root1.right, root2.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTree(root, root)        