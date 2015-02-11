# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if not root:
            return []
        paths = []
        self.pathSumHelper(root, sum, [], paths)
        return paths
        
    def pathSumHelper(self, root, sum, path, paths):
        if not root.left and not root.right:
            if sum == root.val:
                paths.append(path[:] + [root.val])
            return
        if root.left:
            path.append(root.val)
            self.pathSumHelper(root.left, sum - root.val, path, paths)
            path.pop()
        if root.right:
            path.append(root.val)
            self.pathSumHelper(root.right, sum - root.val, path, paths)
            path.pop()

"""
This solution got TLE!!!
"""
class Solution2:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if not root:
            return []
        paths = []
        self.pathSumHelper(root, sum, [], paths)
        return paths
        
    def pathSumHelper(self, root, sum, path, paths):
        path.append(root.val)
        sum -= root.val
        if not root.left and not root.right:
            if sum == 0:
                paths.append(path[:])
            return
        if root.left:
            self.pathSumHelper(root.left, sum, path, paths)
        if root.right:
            self.pathSumHelper(root.right, sum, path, paths)