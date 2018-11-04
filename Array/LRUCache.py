# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = self.DoublyLL(-1)
        self.tail = self.DoublyLL(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache_map = {}

    def DoublyLL(self,val):
        self.val = val
        self.next = None
        self.prev = None




    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cache_map.has_key(key):
            self.cache_map[key].prev.next = self.cache_map[key].next
            self.cache_map[key].next.prev = self.cache_map[key].prev
            self.cache_map[key].next = self.tail
            self.cache_map[key].prev = self.tail.prev
            self.tail.prev.next = self.cache_map[key]

        elif len(self.cache_map)<= self.capacity:
            node = self.DoublyLL(value)
            self.cache_map[key] = node
            self.cache_map[key].next = self.tail
            self.cache_map[key].prev = self.tail.prev
            self.tail.prev.next = self.cache_map[key]
        else:





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

            # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache = LRUCache(2)

print cache.put(1, 1)
print cache.put(2, 2)
print cache.get(1)    #   // returns 1
print cache.put(3, 3) #   // evicts key 2
print cache.get(2)   #    // returns -1 (not found)
print cache.put(4, 4)   # // evicts key 1
print cache.get(1)      # // returns -1 (not found)
print cache.get(3)      # // returns 3
print cache.get(4)      # // returns 4


class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dct = {}
        self.capacity = capacity

    def addTail(self, node):

        tmpnd = self.tail.prev
        tmpnd.next = node
        node.prev = tmpnd
        node.next = self.tail
        self.tail.prev = node
        # print "AddingTail"+str(node.value)

    def remNode(self, node):

        node.prev.next = node.next
        node.next.prev = node.prev

        tmpnd = self.tail.prev
        tmpnd.next = node
        node.prev = tmpnd
        node.next = self.tail
        self.tail.prev = node
        # print "REAddingTail"+str(node.value)
        return node

    def removeHead(self):
        hd = self.head.next.key
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return hd

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dct:  # .keys():
            node = self.dct[key]
            self.remNode(node)
            return self.dct[key].value

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dct:  # .keys():
            node = self.dct[key]
            nd = self.remNode(node)
            nd.value = value
            self.dct[key] = nd

        else:
            nd = Node(key, value)
            self.addTail(nd)
            self.dct[key] = nd

            if len(self.dct) > self.capacity:
                # print self.head.next.value
                # print self.dct.keys()
                key = self.removeHead()
                del self.dct[key]
                # print "deleting"+str(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

