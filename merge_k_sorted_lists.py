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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __lt__(self, n):
        return self.val < n.val

class Solution3:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        heap = [x for x in lists if x]
        heapq.heapify(heap)
        dummy = current = ListNode(0)
        while heap:
            current.next = heapq.heappop(heap)
            current = current.next
            if current.next:
                heapq.heappush(heap, current.next)
        return dummy.next

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l2 = ListNode(1)
    l2.next = ListNode(1)
    l2.next.next = ListNode(2)
    s = Solution3()
    l = s.mergeKLists([l1, l2])
    while l:
        print l.val
        l = l.next