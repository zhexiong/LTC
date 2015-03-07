# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
    	dummy = current = ListNode(0)
        carry = 0
        while l1 or l2 or carry > 0:
        	sum = carry
        	if l1:
        		sum += l1.val
        		l1 = l1.next
        	if l2:
        		sum += l2.val
        		l2 = l2.next
        	current.next = ListNode(sum % 10)
        	current = current.next
        	carry = sum / 10
        return dummy.next