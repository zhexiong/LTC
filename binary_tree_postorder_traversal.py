# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        nodes = []
        def postorderTraversalHelper(root, nodes):
            if root:
                postorderTraversalHelper(root.left, nodes)
                postorderTraversalHelper(root.right, nodes)
                nodes.append(root.val)
        postorderTraversalHelper(root, nodes)
        return nodes

class Solution2:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        nodes = []
        if not root:
            return nodes
        stack = [root]
        while stack:
            node = stack.pop()
            nodes.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return nodes[-1::-1]