################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
################################################################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        cur = root
        pval = p.val
        qval = q.val

        while cur:
            cur_val = cur.val
            if (cur_val >= pval) and (cur_val >= qval):
                if (cur_val == pval) or (cur_val == qval):
                    return cur
                else:
                    cur = cur.left
            elif (cur_val <= pval) and (cur_val <= qval):
                if (cur_val == pval) or (cur_val == qval):
                    return cur
                else:
                    cur = cur.right
            else:
                return cur
        

# Simplified
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         while True:
#             if root.val > p.val and root.val > q.val:
#                 root = root.left
#             elif root.val < p.val and root.val < q.val:
#                 root = root.right
#             else:
#                 return root
