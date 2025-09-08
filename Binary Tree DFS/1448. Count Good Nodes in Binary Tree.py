################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
################################################################




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        if root is None:
            return 0

        def dfs(node, carry):
            nonlocal good

            if node is None:
                return

            # Check if the node is good or bad
            if node.val >= carry:
                good += 1
                # Update carry max_so_far
                carry = max(node.val, carry)

            if node.left:
                left = dfs(node.left, carry)
            if node.right:
                right = dfs(node.right, carry)
            
            return

        dfs(root, root.val)
        return good