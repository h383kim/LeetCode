################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
################################################################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Empty Tree
        if not root:
            return 0
        
        def goDown(count, cur):
            if not cur.left and not cur.right:
                return count
            elif not cur.left:
                count += 1
                return goDown(count, cur.right)
            elif not cur.right:
                count += 1
                return goDown(count, cur.left)
            else:
                count += 1
                return max(goDown(count, cur.left), goDown(count, cur.right))

        count = goDown(1, root)
        return count


## GPT Recommendation below:
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         # Base case: If the tree is empty, the depth is 0
#         if not root:
#             return 0
        
#         # Recursively calculate the depth of the left and right subtrees
#         left_depth = self.maxDepth(root.left)
#         right_depth = self.maxDepth(root.right)
        
#         # The depth of the current tree is the maximum depth of its subtrees + 1 (for the current root)
#         return max(left_depth, right_depth) + 1
