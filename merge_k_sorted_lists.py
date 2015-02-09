# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        heap = [(x.val, x) for x in lists if x]
        heapq.heapify(heap)
        dummy = current = ListNode(0)
        while heap:
            current.next = heapq.heappop(heap)[1]
            current = current.next
            if current.next:
                heapq.heappush(heap, (current.next.val, current.next))
        return dummy.next

class Solution2:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        count = len(lists)
        if count == 0:
            return None
        if count == 1:
            return lists[0]
        l1 = self.mergeKLists(lists[:count/2])
        l2 = self.mergeKLists(lists[count/2:])
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next