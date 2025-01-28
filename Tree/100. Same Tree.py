################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/same-tree/
################################################################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: If both nodes are None (empty trees or reached leaf nodes), they are the same
        if not p and not q:
            return True
        elif not p:
            return False
        elif not q:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                # Recursive case: Check if both the left subtrees and the right subtrees are the same
                # The function returns True only if BOTH left and right subtrees are identical
                return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))

