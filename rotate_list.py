# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head:
            return head
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        k = k % count
        if k == 0:
            return head
        slow = fast = head
        while k > 0:
            k -= 1
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        new_head = slow.next
        fast.next = head
        slow.next = None
        return new_head