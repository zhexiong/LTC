# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.nodes = []
        self._push(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.nodes != []

    # @return an integer, the next smallest number
    def next(self):
        node = self.nodes.pop()
        self._push(node.right)
        return node.val
        
    def _push(self, node):
        if node:
            self.nodes.append(node)
            self._push(node.left)

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())