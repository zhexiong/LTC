# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = current = head
        pre = dummy
        while current and current.next:
            post = current.next.next
            next = current.next
            next.next = current
            current.next = post
            pre.next = next
            pre = current
            current = post
        return dummy.next