################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/balanced-binary-tree/
################################################################



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = True

        def dfs(root):
            nonlocal balance

            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            # Check balance
            if not (left == right or 
                    left == right + 1 or 
                    left == right - 1):
                balance = False

            return 1 + max(left, right)
        
        dfs(root)
        return balance