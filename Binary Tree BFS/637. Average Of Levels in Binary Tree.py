################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/
################################################################



from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        deq = deque([root])
        averages = []
        while deq:
            lenDeque = len(deq)
            Sum = 0
            for _ in range(lenDeque):
                cur = deq.popleft()
                Sum += cur.val
                if cur.left:
                    deq.append(cur.left)
                if cur.right:
                    deq.append(cur.right)

            averages.append(Sum / lenDeque)
        
        return averages