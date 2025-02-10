################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
################################################################



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.Min = 100000000

        # In-order traversal can effectively scan the tree in a sorted order
        # We only need to compare each consectuive difference
        def inOrder(node):
            if not node:
                return
            
            inOrder(node.left)

            # Prev is not defined yet. i.e. node is the leftmost node of the tree
            if self.prev is not None:
                self.Min = min(self.Min, node.val - self.prev.val)
            self.prev = node

            inOrder(node.right)
        
        inOrder(root)
        
        return self.Min
