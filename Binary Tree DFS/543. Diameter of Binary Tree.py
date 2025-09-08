################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/diameter-of-binary-tree/
################################################################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(root):
            nonlocal diameter

            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            # Update global max diameter
            diameter = max(diameter, left + right)
            
            return 1 + max(left, right)

        dfs(root)
        return diameter