# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        nodes = []
        def helper(root, nodes):
            if root:
                nodes.append(root.val)
                helper(root.left, nodes)
                helper(root.right, nodes)
        helper(root, nodes)
        return nodes

class Solution2:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        nodes = []
        if not root:
            return nodes
        stack = [root]
        while stack:
            node = stack.pop()
            nodes.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return nodes