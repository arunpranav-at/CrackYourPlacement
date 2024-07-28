'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: Optional[TreeNode], left: List[int], right: List[int]) -> Optional[TreeNode]:
        if len(left) <= 1 and len(right) <= 1:
            if left!=[] and right!=[]:
                root.left = TreeNode(left[0])
                root.right = TreeNode(right[0])
            elif left==[] and right!=[]:
                root.right = TreeNode(right[0])
            elif left!=[] and right==[]:
                root.left = TreeNode(left[0])
            return root
        else:
            midl = len(left)//2
            leftl = left[:midl]
            leftr = left[midl + 1:]
            root.left = self.helper(TreeNode(left[midl]), leftl, leftr)

            midr = len(right)//2
            rightl = right[:midr]
            rightr = right[midr + 1:]
            root.right = self.helper(TreeNode(right[midr]), rightl, rightr)
            return root
            
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = len(nums)//2
        left = nums[:mid]
        root = TreeNode(nums[mid])
        right = nums[mid + 1:]
        return self.helper(root, left, right)