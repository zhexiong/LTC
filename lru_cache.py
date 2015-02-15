class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.pool = collections.OrderedDict()

    # @return an integer
    def get(self, key):
        if key in self.pool:
        	val = self.pool.pop(key)
        	self.pool[key] = val
        	return val
        else:
        	return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
    	if self.capacity == 0:
    		return
    	if key in self.pool:
    		self.pool.pop(key)
    	elif len(self.pool) == self.capacity:
    		self.pool.popitem(last=False)
    	self.pool[key] = value


"""
This implement OrderedDict, with double linked list and dictionary.
"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.first = None #oldest
        self.last = None
        
    def __pop(self):
        node = self.first
        if self.first == self.last:
            self.first = self.last = None
        elif self.first:
            self.first = self.first.next
            self.first.prev = None
        return node
        
    def __remove(self, node):
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
        elif node.next:
            self.first = node.next
            self.first.prev = None
        elif node.prev:
            self.last = node.prev
            self.last.next = None
        else:
            self.first = self.last = None
            
    def __append(self, node):
        if self.last:
            self.last.next = node
            node.prev = self.last
            node.next = None
            self.last = node
        else:
            self.first = self.last = node

    # @return an integer
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.__remove(node)
            self.__append(node)
            return node.val
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.__remove(node)
            self.__append(node)
        else:
            if len(self.cache) == self.capacity:
                node = self.__pop()
                if node:
                    self.cache.pop(node.key)
            node = Node(key, value)
            self.cache[key] = node
            self.__append(node)