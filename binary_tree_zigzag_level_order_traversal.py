# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        results = []
        current = [root]
        leftToRight = True
        while current:
            next = []
            result = []
            while current:
                node = current.pop()
                result.append(node.val)
                if leftToRight:
                    if node.left:
                        next.append(node.left)
                    if node.right:
                        next.append(node.right)
                else:
                    if node.right:
                        next.append(node.right)
                    if node.left:
                        next.append(node.left)
            results.append(result)
            current = next
            leftToRight = not leftToRight
        return results