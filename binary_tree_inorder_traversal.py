# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        nodes = []
        def helper(root, nodes):
            if root:
                helper(root.left, nodes)
                nodes.append(root.val)
                helper(root.right, nodes)
        helper(root, nodes)
        return nodes

class Solution2:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        nodes = []
        if not root:
            return nodes
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                nodes.append(root.val)
                root = root.right
        return nodes