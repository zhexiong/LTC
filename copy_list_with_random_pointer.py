# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        nodeMap = {}
        current = head
        copy = dummy = RandomListNode(0)
        while current:
            copy.next = RandomListNode(current.label)
            nodeMap[current] = copy.next
            current = current.next
            copy = copy.next
        
        current = head
        copy = dummy.next
        while current:
            copy.random = nodeMap[current.random] if current.random else None
            current = current.next
            copy = copy.next
            
        return dummy.next