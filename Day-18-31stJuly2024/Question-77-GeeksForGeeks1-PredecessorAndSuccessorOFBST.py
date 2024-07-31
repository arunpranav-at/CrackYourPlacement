'''
Predecessor and Successor
Difficulty: MediumAccuracy: 47.36%Submissions: 116K+Points: 4
There is BST given with the root node with the key part as an integer only. You need to find the in-order successor and predecessor of a given key. If either predecessor or successor is not found, then set it to NULL.

Note:- In an inorder traversal the number just smaller than the target is the predecessor and the number just greater than the target is the successor. 

Example 1:

Input:
      8
    /   \
   1     9
    \     \
     4    10
    /
   3
key = 8 
Output: 4 9
Explanation: 
In the given BST the inorder predecessor of 8 is 4 and inorder successor of 8 is 9.
Example 2:

Input:
        10
      /   \
     2    11
   /  \ 
  1    5
      /  \
     3    6
      \
       4
key = 11
Output: 10 -1
Explanation:In given BST, the inorder predecessor of 11 is 10 whereas it does not have any inorder successor.
Your Task: You don't need to print anything. You need to update pre with the predecessor of the key or NULL if the predecessor doesn't exist and succ to the successor of the key or NULL if the successor doesn't exist. pre and succ are passed as an argument to the function findPreSuc(). Please note, The key may be located either inside or outside the tree.

Expected Time Complexity: O(Height of the BST).
Expected Auxiliary Space: O(Height of the BST).

Constraints: 
1 <= Number of nodes <= 104
1 <= key of node <= 107
1 <= key <= 107
'''

'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''
def copy_node(a, b):
    a.key = b.key
    a.left = b.left
    a.right = b.right
    
class Solution:
    def findPreSuc(self, root, pre, suc, key):
        while root:
            if root.key == key:
                if root.left:
                    tmp = root.left
                    while tmp.right:
                        tmp = tmp.right
                    copy_node(pre,tmp)
                if root.right:
                    tmp = root.right
                    while tmp.left:
                        tmp = tmp.left
                    copy_node(suc, tmp)
                return pre, suc
            if root.key > key:
                copy_node(suc, root)
                root = root.left
            else:
                copy_node(pre, root)
                root = root.right