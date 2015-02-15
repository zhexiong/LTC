# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        root = UndirectedGraphNode(node.label)
        queue = collections.deque([node])
        map = {node:root}
        while queue:
            node = queue.popleft()
            copy = map[node]
            for n in node.neighbors:
                if n in map:
                    copy.neighbors.append(map[n])
                else:
                    temp = UndirectedGraphNode(n.label)
                    map[n] = temp
                    copy.neighbors.append(temp)
                    queue.append(n)
        return root