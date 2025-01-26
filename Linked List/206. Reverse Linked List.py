################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/reverse-linked-list/
################################################################



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nextNode = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = nextNode
            nextNode = cur
            cur = temp

        return nextNode