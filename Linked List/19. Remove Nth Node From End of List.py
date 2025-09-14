################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
################################################################




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first, second = head, head

        for _ in range(n):
            first = first.next
        
        # Edge case: When you remove the first node
        if first is None:
            return head.next
        
        while first.next is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return head
    