# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        head = root
        while head:
            dummy = current = TreeNode(0)
            dummy.next = None
            while head:
                if head.left:
                    current.next = head.left
                    current = current.next
                if head.right:
                    current.next = head.right
                    current = current.next
                head = head.next
            head = dummy.next