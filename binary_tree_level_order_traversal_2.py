# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        res = []
        if not root:
            return res
        current = collections.deque([root])
        res.append([root.val])
        while current:
            next = collections.deque()
            temp = []
            while current:
                node = current.popleft()
                if node.left:
                    next.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    next.append(node.right)
                    temp.append(node.right.val)
            current = next
            if temp:
                res.append(temp)
        return res[-1::-1]
                