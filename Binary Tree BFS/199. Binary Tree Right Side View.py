################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/binary-tree-right-side-view/
################################################################



 from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        rightView = []
        deq = deque([root])
        while deq:
            lenDeque = len(deq)
            rightView.append(deq[lenDeque - 1].val)
            for _ in range(lenDeque):
                cur = deq.popleft()
                if cur.left:
                    deq.append(cur.left)
                if cur.right:
                    deq.append(cur.right)
            
        return rightView
