################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/add-two-numbers/
################################################################



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = ListNode() # Init sum LinkedList
        carryOn = 0
        cur = s
        while l1 or l2: # Loop until both operands run out
            if l1 and l2:
                Sum = l1.val + l2.val + carryOn
                l1 = l1.next
                l2 = l2.next
            elif l1:
                Sum = l1.val + carryOn
                l1 = l1.next
            else:
                Sum = l2.val + carryOn
                l2 = l2.next

            cur.val = Sum % 10 # Store the sum digit to current sum digit
            cur.next = ListNode() # Extend the sum LinkedList
            cur = cur.next

            if Sum >= 10:
                carryOn = 1
            else:
                carryOn = 0

        # In case of carryOn remains at the end
        if carryOn == 1:
            cur.val = carryOn
        else:
            # Extra node delete
            cur = s
            while cur.next.next:
                cur = cur.next
            cur.next = None
            
        return s


